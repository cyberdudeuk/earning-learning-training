#!/usr/bin/env python3
"""Turn the private artifact export of Earning, learning and training into the public page, index.html.

The portal is edited as a private Claude artifact. This step makes the exported page fit to publish:

  1. its own address, everywhere it appears, becomes the public address, and the colophon QR code is redrawn for it;
  2. links to private artifacts become public addresses, or plain text where nothing public exists;
  3. feedback points to this repository's public contact form (contact is by form only: no email address);
  4. the one email address quoted from a public domain register is described rather than printed.

Every replacement is asserted, so a change in the export stops the build instead of publishing something half-done.

Run:  python3 tools/publish.py path/to/artifact-export.html   writes index.html
"""
import re
import sys
from pathlib import Path

import segno

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = 'https://cyberdudeuk.github.io/earning-learning-training/'
REPO = 'https://github.com/cyberdudeuk/earning-learning-training'
SELF = 'https://claude.ai/artifact/CX1xhHpatCfvWAf9nPnRe3'
# Private artifact -> public address, or None for plain text.
PRIVATE = {
    'https://claude.ai/artifact/D5Z5M9w61vdEdVQU1sP587': 'https://cyberdudeuk.github.io/young-person-360/',
    'https://claude.ai/artifact/KtvH3k954KaATENz92AcdL': REPO + '#readme',
    'https://claude.ai/artifact/8qabj3EjNvkR42vgyk9bRf': None,
}
UNCAPPED = re.compile(r'(repeat\(auto-fi[lt],)minmax\((\d+(?:\.\d+)?rem),1fr\)')
PRIVATE_LINK = re.compile(r'https://claude\.ai/(?:artifact|code/artifact|chat|project)/[A-Za-z0-9-]+')


def qr_path(payload):
    """The QR code as the same path drawing the colophon uses: one 1x1 square per dark module, 4-module border."""
    q = segno.make(payload, error='m', boost_error=False)
    rows = list(q.matrix_iter(scale=1, border=4))
    d = ''.join(f'M{x},{y}h1v1h-1z' for y, row in enumerate(rows) for x, dark in enumerate(row) if dark)
    return len(rows), d


def swap(text, old, new, at_least=1):
    n = text.count(old)
    if n < at_least:
        raise SystemExit(f'publish: expected {old[:70]!r} in the export, found {n}')
    return text.replace(old, new)


def transform(s):
    # 1. the page's own address and its QR code
    m = re.search(r'(<svg[^>]*class="qr"[^>]*viewBox=")0 0 (\d+) \2("[^>]*>)(.*?)(<path d=")([^"]*)(")', s, re.DOTALL)
    if not m or SELF not in m.group(0):
        raise SystemExit('publish: colophon QR code not found where expected')
    size, d = qr_path(PUBLIC)
    new = (m.group(1) + f'0 0 {size} {size}' + m.group(3) + m.group(4) + m.group(5) + d + m.group(7))
    s = s[:m.start()] + new + s[m.end():]
    s = swap(s, SELF, PUBLIC, 3)
    # 2. links to private artifacts
    for old, new in PRIVATE.items():
        if new:
            s = swap(s, old, new)
    film = '"status": "available", "url": "https://claude.ai/artifact/8qabj3EjNvkR42vgyk9bRf", "what": "A short animated film about this portal.'
    s = swap(s, film, '"status": "private", "url": "", "what": "A short animated film about this portal, kept as a private artifact outside this repository.', 1)
    s = swap(s, "(av?'Available':'Placeholder')", "(av?'Available':(m.status===\"private\"?'Not published':'Placeholder'))", 1)
    s = swap(s, '"label": "the build and development hub"', '"label": "how this portal is built and run"', 1)
    # 3. feedback through the public contact form
    s = swap(s, '<p>Feedback on this portal: use the <b>Was this part useful?</b> form at the foot of any part. No email address is published.</p>',
             f'<p>Feedback on this portal: use the <a href="{REPO}/issues/new/choose">contact form</a>. It is public, so leave out personal details. No email address is published.</p>', 1)
    s = swap(s, "'<button type=\"button\" class=\"lnk\" id=\"ft-settings\">Display settings</button>', ",
             f"'<a href=\"{REPO}/issues/new/choose\">Contact</a>', '<button type=\"button\" class=\"lnk\" id=\"ft-settings\">Display settings</button>', ", 1)
    s = swap(s, 'If you leave feedback, it is sent to the owner.',
             'Feedback goes through a public contact form on GitHub, so leave out personal details.', 1)
    # 4. an address quoted from a public domain register
    s = swap(s, 'Infrastructure.Operations@education.gov.uk; ', 'a Department for Education operations mailbox; ', 1)
    # cap auto-fit grid minimums at the container width so large text cannot force sideways scrolling (check C8)
    s = UNCAPPED.sub(lambda m: f'{m.group(1)}minmax(min({m.group(2)},100%),1fr)', s)
    left = sorted(set(PRIVATE_LINK.findall(s)))
    if left:
        raise SystemExit(f'publish: links to private artifacts remain: {left}')
    return s


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    out = transform(Path(sys.argv[1]).read_text(encoding='utf-8'))
    (ROOT / 'index.html').write_text(out, encoding='utf-8')
    print(f'wrote index.html ({len(out):,} characters)')
