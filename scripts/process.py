"""
ZENYTH feed processor.

Takes TradingView CSV exports from ./data/ and produces JSON files in ./public/
with OHLCV + pre-computed context (Asia range, prior day H/L, ATR).

Expected input filenames (drop in ./data/):
  EURUSD_M5.csv
  EURUSD_M15.csv
  EURUSD_H1.csv
  EURUSD_H4.csv
  EURUSD_D1.csv

Run:  python scripts/process.py
"""

import csv
import json
import os
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
OUT_DIR = ROOT / "public"
HISTORY = 500  # candles to keep per timeframe

TIMEFRAMES = ["M5", "M15", "H1", "H4", "D1"]

# Asia session in UTC (approximation: Tokyo open 00:00 UTC -> London open 07:00 UTC)
# ZENYTH uses Asia range = 00:00 UTC -> 07:00 UTC
ASIA_START_HOUR_UTC = 0
ASIA_END_HOUR_UTC = 7


def parse_tv_csv(path: Path):
    """TradingView CSV columns: time, open, high, low, close, Volume (case can vary)."""
    rows = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        # normalize headers
        reader.fieldnames = [h.strip().lower() for h in reader.fieldnames]
        for r in reader:
            r = {k.strip().lower(): v for k, v in r.items()}
            t = r.get("time") or r.get("date") or r.get("timestamp")
            # TV exports time as unix seconds OR ISO. handle both.
            try:
                ts = datetime.fromtimestamp(int(t), tz=timezone.utc)
            except (ValueError, TypeError):
                ts = datetime.fromisoformat(t.replace("Z", "+00:00"))
                if ts.tzinfo is None:
                    ts = ts.replace(tzinfo=timezone.utc)
            rows.append({
                "t": ts.isoformat(),
                "ts": int(ts.timestamp()),
                "o": float(r["open"]),
                "h": float(r["high"]),
                "l": float(r["low"]),
                "c": float(r["close"]),
                "v": float(r.get("volume", 0) or 0),
            })
    rows.sort(key=lambda x: x["ts"])
    return rows


def atr(candles, period=14):
    """Wilder ATR, returns list aligned to candles (None for warmup)."""
    if len(candles) < period + 1:
        return [None] * len(candles)
    trs = [None]
    for i in range(1, len(candles)):
        h, l = candles[i]["h"], candles[i]["l"]
        pc = candles[i - 1]["c"]
        tr = max(h - l, abs(h - pc), abs(l - pc))
        trs.append(tr)
    out = [None] * len(candles)
    # seed
    seed = sum(trs[1:period + 1]) / period
    out[period] = seed
    for i in range(period + 1, len(candles)):
        out[i] = (out[i - 1] * (period - 1) + trs[i]) / period
    return out


def compute_asia_range(m5_or_m15_candles):
    """Return Asia range H/L for the most recent completed Asia session."""
    # group by UTC date
    by_date = {}
    for c in m5_or_m15_candles:
        ts = datetime.fromisoformat(c["t"])
        if ASIA_START_HOUR_UTC <= ts.hour < ASIA_END_HOUR_UTC:
            key = ts.date().isoformat()
            by_date.setdefault(key, []).append(c)
    if not by_date:
        return None
    latest = max(by_date.keys())
    session = by_date[latest]
    return {
        "date": latest,
        "high": max(c["h"] for c in session),
        "low": min(c["l"] for c in session),
        "candle_count": len(session),
    }


def prior_day_hl(d1_candles):
    if len(d1_candles) < 2:
        return None
    pd = d1_candles[-2]
    return {"date": pd["t"][:10], "high": pd["h"], "low": pd["l"], "close": pd["c"]}


def process_timeframe(tf: str):
    src = DATA_DIR / f"EURUSD_{tf}.csv"
    if not src.exists():
        print(f"  skip {tf} (missing {src.name})")
        return None
    candles = parse_tv_csv(src)[-HISTORY:]
    atrs = atr(candles, 14)
    for c, a in zip(candles, atrs):
        c["atr14"] = round(a, 6) if a is not None else None
    return candles


def main():
    OUT_DIR.mkdir(exist_ok=True)
    all_tfs = {}
    print("Processing timeframes:")
    for tf in TIMEFRAMES:
        candles = process_timeframe(tf)
        if candles:
            all_tfs[tf] = candles
            out = OUT_DIR / f"eurusd_{tf.lower()}.json"
            with open(out, "w") as f:
                json.dump({
                    "pair": "EURUSD",
                    "timeframe": tf,
                    "updated_at": datetime.now(timezone.utc).isoformat(),
                    "count": len(candles),
                    "candles": candles,
                }, f, separators=(",", ":"))
            print(f"  wrote {out.name} ({len(candles)} candles)")

    # context file: the stuff ZENYTH actually cares about right now
    context = {
        "pair": "EURUSD",
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    if "M15" in all_tfs:
        context["asia_range"] = compute_asia_range(all_tfs["M15"])
        last = all_tfs["M15"][-1]
        context["last_m15"] = {
            "time": last["t"],
            "close": last["c"],
            "atr14": last["atr14"],
        }
    if "D1" in all_tfs:
        context["prior_day"] = prior_day_hl(all_tfs["D1"])

    with open(OUT_DIR / "context.json", "w") as f:
        json.dump(context, f, indent=2)
    print(f"  wrote context.json")

    # index page
    index_html = """<!DOCTYPE html>
<html><head><title>ZENYTH Feed</title>
<style>body{font-family:ui-monospace,monospace;max-width:640px;margin:40px auto;padding:0 20px;color:#ddd;background:#111}a{color:#9cf;display:block;padding:6px 0}h1{font-weight:400}code{background:#222;padding:2px 6px;border-radius:3px}</style>
</head><body>
<h1>ZENYTH feed · EURUSD</h1>
<p>Last updated: <code>""" + datetime.now(timezone.utc).isoformat() + """</code></p>
<a href="/context.json">/context.json</a>
"""
    for tf in TIMEFRAMES:
        if tf in all_tfs:
            index_html += f'<a href="/eurusd_{tf.lower()}.json">/eurusd_{tf.lower()}.json</a>\n'
    index_html += "</body></html>"
    with open(OUT_DIR / "index.html", "w") as f:
        f.write(index_html)

    print("\nDone. Files in ./public/ ready to deploy.")


if __name__ == "__main__":
    main()
