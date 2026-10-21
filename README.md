# Clipline Studio

Website for Clipline Studio: short-form clipping and video editing for YouTubers, podcasts and streamers.
Live at https://cliplinestudio.com (GitHub Pages, branch `gh-pages`).

## How the site is built

Plain HTML, no framework, no build tools beyond Python 3.

```
tools/build_site.py        # generates every page
tools/clipsite/content.py  # all the copy (titles, hero text, plans, FAQ…)
tools/clipsite/css.py      # the stylesheet
```

Edit the copy or the CSS, then run

```
python3 tools/build_site.py
```

and commit the regenerated `index.html`, `404.html` and the four `*/index.html` subpages.
`--preview DIR` also writes a flat copy with relative links, handy for previews that aren't served from a domain root.

## Design (October 2026 redesign)

Paper, ink and one blue accent (`#1d5cff`, the Clipline colour). Instrument Serif for headings, Figtree for body text,
JetBrains Mono for labels and figure captions, Caveat for the handwritten margin notes. Borders are drawn, not cast:
uneven "wobbly" radii, tape strips on photos, a scissors cut-line between numbered sections, "Fig." captions under every
illustration, and a "Sheet n of 5" footer. No gradients, glows or shimmer.

The editorial-diagram style follows the `diagram-design` skill (MIT, by Cathryn Lavery), copied into
`.claude/skills/diagram-design/` so it can be used for future diagrams on the site.

## Fonts

Self-hosted in `fonts/` (Fontsource latin subsets, SIL OFL; see `fonts/LICENSE.txt`).

## Form

The contact form posts to FormSubmit (AJAX) and lands in the studio inbox. Field ids and the payload are in
`tools/build_site.py` (`trial()` and the script at the bottom).

## Publishing

Work on a branch, preview, then merge into `main` and publish by merging `main` into `gh-pages` and pushing.
