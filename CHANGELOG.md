# Changelog

## 23 November 2026: no named owner; contact by form only

- The colophon, the page's own metadata, the citation file, the licence and the catalogue entry no longer name a
  person or give a role, directorate or ORCID iD. The colophon's Owner row is now a Contact row with the public
  contact form. The licence and citation credit the portal's contributors.
- New check C10 keeps personal details out of every file of the repository, and C3 now covers every file too. Both
  compare hashed words and phrases, so the checker never spells out what it keeps out; a planted canary proves each.
- The build no longer quotes the mailbox address it used to replace: the artifact carries the fix, and the build
  confirms it.

## 22 November 2026: source fixes carried back into the artifact

- The fixes that belong in the artifact too (contact by form, the Young Person 360º link, grid caps) were carried back
  into it (now its version 1795362921-1cc3; self-assessment 100, axe clean in light and dark at 1280, 390 and 320).
  `tools/publish.py` confirms them instead of reapplying them, and has a `--source` mode. The public page built from
  the new export is byte-identical to the one it replaces.

## 22 November 2026: grid minimums capped

- New checks C8 and C9 (every YAML and CFF file parses), found while publishing Young Person 360º: an auto-fit grid with an uncapped minimum can force
  sideways scrolling when text is enlarged. One rule here (`.forpro .stats-in`) was uncapped; the build now caps
  every such minimum at the container width.

## 22 November 2026: published as a public site

- First public release, from release 33 of the private artifact. Renamed from *Earning or learning* to *Earning,
  learning and training*.
- Two new routes: *Start your own business* (Start Up Loans from 18, The King's Trust, Big Ideas Wales, the Universal
  Credit start-up period) and *If you are 25 or over, or coming back after time away*. Both link to
  [Starting out, or starting again](https://cyberdudeuk.github.io/start-a-business-uk/starting-out-or-again/).
- The parts *Before the label* and *The whole young person* are renamed *Spotting risk early* and *Records that follow
  a young person*, and point to Young Person 360º for what it owns. Measured against Young Person 360º, they hold
  16 to 24 content found nowhere else, so they were kept and scoped, not cut.
- Health: the page's own self-check scores 100/100 (was 56). One main heading; glossary terms and the welcome link
  work without in-page fragment links; the QR code and barcode have a title and description; every source in the
  register is cited.
- The colophon shows no email address; feedback goes through the public
  contact form.
