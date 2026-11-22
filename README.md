# Earning, learning and training

For young people aged 16 to 24 who are not in work, learning or training, and everyone around them: what helps, what
government is doing about it, and how to get into work, learning, training or your own business. Every claim cites its
source.

**Open it:** https://cyberdudeuk.github.io/earning-learning-training/

A prototype and independent analysis, not an official government service. Formerly called *Earning or learning*.

## What is in it

One page in 38 parts, including:

- **Your plan and the route finder:** 17 routes into work, learning, training and self-employment, filtered by age,
  nation and situation.
- **The Milburn Review** and every UK government strategy, programme, duty and target that bears on it, across the
  four nations.
- **Spotting risk early:** signals, risk-of-NEET tools, council tracking and where it stops.
- **Records that follow a young person:** who holds each record, which number identifies it, and where the trail
  breaks.
- **A source register:** every source, when it was checked, and what it supports.

## How it fits with the other 360º portals

Each topic lives in one place, and the others link to it
([shared glossary and routing](https://cyberdudeuk.github.io/data/shared-glossary.json)):

| Portal | Owns |
|---|---|
| **Earning, learning and training** (this one) | How a 16 to 24 year old gets into work, learning or training |
| [Young Person 360º: before the label](https://cyberdudeuk.github.io/young-person-360/) | Children and young people held, lost or unseen by the system, from birth |
| [Starting a business in the UK](https://cyberdudeuk.github.io/start-a-business-uk/) | Starting a business at any age, including starting safely and starting again |
| Whole-life 360º (not yet published) | Adults, including learning, retraining and going back to work |

## How it is built and run

The portal is edited as a private Claude artifact. `tools/publish.py` turns its export into `index.html`, fit to
publish: its own address and QR code become the public ones, links to private artifacts become public addresses or
plain text, and feedback goes to the [contact form](https://github.com/cyberdudeuk/earning-learning-training/issues/new/choose).
Every replacement is asserted, so a change in the export stops the build rather than publishing something half-done.

The page checks itself in your browser (a score out of 100 at the foot of the page), with no network access.
`tools/check.py` runs 10 checks in CI, each proved by a deliberate break (`--negative`).

```
python3 tools/publish.py path/to/export.html   # after editing the artifact
python3 tools/check.py                          # 10 checks
python3 tools/check.py --negative               # prove each check fails when it should
```

GitHub Pages serves the `main` branch as it is: there is no build step.

## Keeping it running

| Task | When | Effort |
|---|---|---|
| Recheck the sources and the in-page currency warning | Each quarter | Two to three hours |
| Republish after editing the artifact | After each change | Minutes |
| Answer contact-form issues | As they come | Minutes each |

## Contact and licence

Contact is by the [contact form](https://github.com/cyberdudeuk/earning-learning-training/issues/new/choose) only; it
is public, so leave out personal details. Security problems: see [SECURITY.md](SECURITY.md).

Code: MIT. Written content: Open Government Licence v3.0. Quoted content stays under its owners' terms. See
[LICENSE](LICENSE).
