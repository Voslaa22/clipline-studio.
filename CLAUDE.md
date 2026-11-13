# Working on this repo

Website for Clipline Studio. Read `README.md` for how the site is built and published.

## Rules

- Read `DESIGN.md` before changing anything visual. Use its tokens and rules. A new visual choice gets one line in its decision log in the same commit; a past decision is replaced by a new line, never edited.
- Copy is written as "I", never "we". No invented testimonials, clients or results. Proof is from the studio's own accounts and labelled with its month.
- Prices, plan contents and turnaround live in `tools/clipsite/content.py`. Change them only when asked.
- Edit `tools/clipsite/content.py` and `tools/clipsite/css.py`, then run `python3 tools/build_site.py` and commit the regenerated pages with the source. Never hand-edit the generated HTML.

## Plan, build, check

1. Plan: say the goal and how it will be checked. For anything touching more than one section, the form or the publish step, consult the advisor on the plan first.
2. Build on a branch. Smallest change that reaches the goal.
3. Check before saying done: build, serve the repo root, run `node tools/qa/qa.js`, and look at the changed section in light and dark and at phone width. Consult the advisor before declaring done on anything that will be published.
4. The same error twice means stop and consult the advisor, not a third variation.

## Publishing

`main` is not the live site. The live site is the `gh-pages` branch. Merge `main` into `gh-pages` and push only after the owner has seen a preview and said to go live.
