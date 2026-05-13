# ZENYTH feed

Static JSON feed of EURUSD OHLC + pre-computed ZENYTH context. Built so Claude can `web_fetch` your latest market state on demand.

## What it does

1. You drop TradingView CSV exports into `./data/`
2. `scripts/process.py` parses them, computes ATR(14), Asia range H/L, prior day H/L
3. `scripts/deploy.sh` commits + pushes; Vercel auto-redeploys
4. Claude fetches `https://your-feed.vercel.app/context.json` (or any TF file)

## Setup (one time)

1. **Create GitHub repo**, push this folder
2. **Vercel:** import the repo. Build settings:
   - Framework: Other
   - Root directory: `public`
   - Build command: *(blank)*
   - Output directory: `.`
3. **Get TradingView CSVs:** on TV chart → ⋯ menu → Export chart data → CSV. Do this for M5, M15, H1, H4, D1. Save as `EURUSD_M5.csv` etc. into `./data/`

## Daily use

```bash
# after dumping fresh CSVs into ./data/
bash scripts/deploy.sh
```

That's it. Live in ~30s.

## Files Claude can fetch

- `/context.json` — small summary (Asia range, prior day, last close, ATR). Cheap.
- `/eurusd_m5.json` — last 500 M5 candles + ATR
- `/eurusd_m15.json` — last 500 M15 candles + ATR
- `/eurusd_h1.json`, `/eurusd_h4.json`, `/eurusd_d1.json` — same

## Notes

- Update cadence is manual (you run deploy.sh when you want fresh data). Easy to add GitHub Actions cron later.
- TradingView CSV time format: handles both unix-seconds and ISO. If your export uses something weird, edit `parse_tv_csv`.
- Asia range = 00:00–07:00 UTC. Change `ASIA_START_HOUR_UTC` / `ASIA_END_HOUR_UTC` if your definition differs.
