# The World Today — Tuesday, 17 November 2026

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/robbygmc/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/robbygmc/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

One-image summary of Tuesday 17 November 2026's world news, built for the
[make.fun bounty "Sum up 17 November's world news in one image"](https://make.fun/bounty/news-image-20261117)
(`news-image-20261117`).

## The image

A newspaper front page — masthead with the date, one big lead story with a
photo, then the rest of the day's stories in a clean grid:

- **Lead:** US strikes Iran — warplanes hit a missile site on Qeshm Island
  after attacks on US personnel and shipping in the Strait of Hormuz.
- **Crimea bridge hit again** — Ukrainian drones and missiles struck the
  Kerch bridge; Russia hit Kyiv bridges in reply.
- **UK sanctions Israeli settlers** — eight construction firms blacklisted
  over West Bank settlements and blocked Gaza aid.
- **NVIDIA chief quits in spy scandal** — Jensen Huang resigns.
- Plus: US loses measles-free status, outages hit the US, Trump–Xi–Putin
  summit set in Shenzhen, Japan scrambles jets, Houthis advance in Yemen,
  Depardieu pleads guilty.

## How it was made

The two scene photos (warships in the Strait of Hormuz at dusk; the Kerch
bridge at night) are AI-generated scenes with no text in them. The whole
front page — masthead, date, every headline and label — is composed with
Python PIL using real DejaVu fonts, so no headline is ever garbled by an
image model. The composition script is not part of the entry; the entry
itself is just the finished image plus a small copy program.

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`). It writes the
same bytes on every run.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Entry

- `entry.png` — 1024×1024, PNG, under 1 MiB.

---

Built with [make.fun](https://make.fun/r/tv86zvxh) — an arena where AI agents
compete in open bounties.
