# DESIGN.md · Clipline Studio

Single source for every visual decision in this project. Last updated 2026-11-13.

**How to use this file (for Claude or any agent):**
1. Read this file before producing anything visual: a clip, a frame, a thumbnail, a page, a deck, a PDF.
2. Use the tokens and rules below. Do not introduce a colour, font, size or layout that is not in here.
3. If the work needs something this file does not cover, pick it, then add one line to the decision log at the bottom in the same change. Never change a past decision silently: add a new line that replaces it.
4. Order of authority: the owner's stated rules, then this brand's colours and fonts, then reference sites for layout and feel only.

## What Clipline is

Clipline Studio is a one-person clipping and video-editing studio: long videos, podcasts and streams cut into vertical clips for TikTok, Reels and Shorts. Everything it publishes should look like a sheet from a careful editor's binder: paper, ink, one blue, numbered figures.

## Voice and copy

- Write as **I**. Never "we", "our team" or "the agency". The footer line is the tone: "One person, not an agency. You email me, I answer."
- Plain, concrete sentences. A number beats an adjective: clips per day, hours to delivery, price per month.
- Proof comes from Clipline's own clip accounts and is labelled that way, with the month it was read. It is never presented as a client result and never as a promise.
- No invented testimonials, clients, reviews or logos. If there is no proof for a claim, cut the claim.
- Sentence case everywhere except `label`, which is uppercase.
- Prices, plan contents and turnaround are read from cliplinestudio.com at the time of writing, never restated from memory. As read on 2026-11-13: Starter 299, Growth 499, Scale 1,099 per month (USD or EUR, same figure), plus Custom; free trial of 5 clips within 48 hours.

## Colour

- Ground is `paper`, raised sheets are `card`, text is `ink`, then `ink-2`, then `ink-3`.
- `accent` is the only colour that means "Clipline". One accent element per view is the target: the primary button, or the highlighted plan, or a link. Not all three fighting.
- `mark` is a highlighter stroke behind a few `ink` words. `tape` holds photos to the sheet. Neither is ever text.
- `good` and `rec` are states and always come with a word or an icon.
- No gradients, glows, shimmer or marquee. If a surface needs emphasis, give it a border, not a colour wash.
- Both themes exist. Build light first, then check dark: `accent` gets lighter in dark, so text on an accent fill is `paper` in dark, white in light.

## Type

- Headings in `serif` (Instrument Serif, regular and italic only): `display`, `title`, `subtitle`, all with -0.01em tracking. Italic is for one emphasised word in a heading, not whole lines.
- Body in `body` (Figtree): `body` at 17px/1.6. Button labels use `button`.
- `label` in `mono` (JetBrains Mono 500, uppercase, 0.14em): kickers, sheet numbers, the cut-line, stamps.
- `caption` in `mono`: the "Fig." line under every illustration, in `ink-3`.
- `note` in `hand` (Caveat 700, `ink-2`): handwritten margin notes pointing at a figure. Two or three per page at most.

## Layout and surfaces

- Content column up to `wrap`, side padding `pad`.
- Sections are numbered like sheets in a binder ("Sheet 02 of 5", "01 See it work"). Every figure has a caption in `label` or `ink-3`.
- Borders are drawn, not cast: a `line`-wide `ink` border with an uneven radius. The two radii used are `255px 15px 225px 15px / 15px 225px 15px 255px` and its mirror `15px 225px 15px 255px / 255px 15px 225px 15px`.
- The primary button is an `ink` fill with `paper` text, a `line` `ink` border and the first uneven radius, padding 13px 20px. On hover it moves 2px up and left and gets a hard `accent` shadow offset by `lift`, no blur.
- Cards sit very slightly rotated (under half a degree). A scissors cut-line with a `label` separates numbered sections.
- A fine paper grain sits over the whole page: 8% multiplied in light, 6% screened in dark.
- Photos and clip stills are fixed with `tape` strips, slightly rotated.

## Motion

- One easing family: `cubic-bezier(.2,.7,.2,1)` for moves, `cubic-bezier(.16,1,.3,1)` for reveals.
- Three durations: 150 ms for feedback, 400 ms for section reveals, 900 ms for the few large moves. Stagger 70 ms.
- Decorative loops run only while on screen. Everything switches off under reduced motion, and every number and section reads without JavaScript.
- The only gradients on the site are two moving highlights: the beam around the recommended plan and the beam along the workflow connectors. Do not add others.

## Logo

Two slanted strokes, the first in `ink`, the second in `accent`, followed by the words "Clipline Studio" in `body`. The mark, exactly as the site draws it:

```html
<svg viewBox="0 0 32 32" aria-hidden="true">
  <path d="M9 6h7l-5 20H4z" fill="#0b0d12"/>
  <path d="M21 6h7l-5 20h-7z" fill="#1d5cff"/>
</svg>
```

Use it as given. Do not redraw, recolour beyond the two tokens, or add effects.

## Clips (the product)

- Every clip is `clip-w` by `clip-h`, 9:16, reframed so faces stay in frame.
- Word-by-word captions, a hook title inside the first second, branding kept subtle.
- Captions and the hook title stay inside the safe area: `clip-text-max` wide, starting 60px from the left edge, with the top `clip-top-clear` and the bottom `clip-bottom-clear` left free. Text shrinks before it touches an edge.
- Each clip must make sense to someone who never saw the long video. No "as I said earlier".
- Quality over quantity: pick and shape clips after the recent posts that performed best. Never post near-duplicates.
- Only original footage or footage with the right to use it. Client clips are credited the way the client asks.
- Caption fonts, colours, graphics and the cut style of the clips themselves are defined in the clip pipeline's own DESIGN.md and style config, not here.
- Framing and graphics follow what is said: changes at cuts and sentence starts, never on a timer.

## Never

- "We", fake social proof, or results presented as guaranteed.
- A second accent colour, gradients, glows, drop shadows with blur, emoji as decoration.
- Text that leaves the 9:16 frame or sits under the app buttons.

## Tokens

### Colour

| Token | Light | Dark | Use |
|---|---|---|---|
| `paper` | `#f7f8fa` | `#0a0b0f` | Page ground. Every page, PDF and slide starts on paper. |
| `card` | `#ffffff` | `#13151b` | Raised sheets on paper: pricing cards, form, figures. |
| `ink` | `#0b0d12` | `#f3f5f9` | Headings and body copy on paper and card. Also the drawn 1.5px border and the hard hover shadow. |
| `ink-2` | `#4a5160` | `#b8bfcc` | Secondary copy on paper and card. |
| `ink-3` | `#646b7b` | `#8a92a2` | Labels, captions under figures, sheet numbers, on paper and card. |
| `rule` | `rgba(11,13,18,.32)` | `rgba(243,245,249,.34)` | Strong hairline between sections. |
| `rule-soft` | `rgba(11,13,18,.12)` | `rgba(243,245,249,.14)` | Dividers inside a card or table. |
| `rule-faint` | `rgba(11,13,18,.07)` | `rgba(243,245,249,.07)` | Background grid and the faintest separators. |
| `accent` | `#1d5cff` | `#4d8dff` | Clipline blue, the only accent: links, the primary button, the second stroke of the logo, the highlighted plan. Text on paper and card. |
| `accent-soft` | `#eef3ff` | `#16213a` | Tint behind an accent label or the selected plan. |
| `good` | `#16a34a` | `#4cc27a` | Success state, always with a word or a check mark. Not for body text in light theme (about 3.1:1 on paper). |
| `rec` | `#ef4444` | `#ef4444` | The recording dot in demo frames and form errors with a word. A mark, not text. |
| `mark` | `#ffd23f` | `#ffd23f` | Highlighter behind a few ink words. Never text colour. |
| `tape` | `rgba(255,210,63,.5)` | `rgba(255,210,63,.32)` | Tape strips that hold photos and clip stills to the sheet. |

### Type

| Family key | Stack |
|---|---|
| `serif` | "Instrument Serif", Georgia, "Times New Roman", serif |
| `body` | "Figtree", system-ui, -apple-system, "Segoe UI", sans-serif |
| `mono` | "JetBrains Mono", ui-monospace, Menlo, Consolas, monospace |
| `hand` | "Caveat", "Segoe Print", "Bradley Hand", cursive |

| Style | Family | Size / line | Weight | Use |
|---|---|---|---|---|
| `display` | serif | 76px / 0.98, tracking -0.01em | 400 | The page headline, one per page or slide. On the site it scales: clamp(42px,6.2vw,76px). |
| `title` | serif | 50px / 1.02, tracking -0.01em | 400 | Section headings. On the site: clamp(32px,4vw,50px). |
| `subtitle` | serif | 26px / 1.1, tracking -0.01em | 400 | Card and figure headings. |
| `body` | body | 17px / 1.6 | 400 | Body copy. |
| `button` | body | 15.5px / 1 | 600 | Button labels. |
| `label` | mono | 12px / 1.6, tracking 0.14em | 500 | Uppercase kickers, sheet numbers, the cut-line between sections, stamps. |
| `caption` | mono | 12.5px / 1.5 | 400 | The 'Fig.' caption under every illustration, in ink-3. |
| `note` | hand | 24px / 1.15 | 700 | Handwritten margin notes in ink-2, a few words at most. On the site: clamp(19px,1.9vw,24px). |

### Layout

| Token | Value | Use |
|---|---|---|
| `wrap` | `1120px` | Maximum content width of a page (site value). |
| `pad` | `clamp(18px,4vw,40px)` | Side padding of the page (site value). |
| `line` | `1.5px` | Width of the drawn ink border on cards, buttons and figures. |
| `lift` | `3px` | Offset of the hard, unblurred shadow a card or button gets on hover. Accent on the primary button, ink elsewhere. |

### Frame

| Token | Value | Use |
|---|---|---|
| `clip-w` | `1080px` | Clip width. Every clip is 9:16. |
| `clip-h` | `1920px` | Clip height. |
| `clip-text-max` | `930px` | Width of the safe area for captions and graphics: x from 60 to 990. The hook title is capped at 940. |
| `clip-top-clear` | `150px` | Nothing above y 150, where the apps show their tabs. |
| `clip-bottom-clear` | `360px` | Nothing below y 1560, where the apps show their caption block. |

## Decision log

Newest at the bottom. A line is never edited or removed: a later line replaces it and says which one.

| # | Date | Decision | Why | From |
|---|---|---|---|---|
| 1 | 2026-10 | Copy is written as "I", never "we" or "our team". | Clipline is one person. | Owner |
| 2 | 2026-10 | Proof is shown as reach from Clipline's own clip accounts, with the month, never as client results. | Honest proof, no client yet to quote. | Owner |
| 3 | 2026-10 | Paper, ink and one accent (Clipline blue). No gradients, glows, shimmer or marquee. | The binder-sheet redesign of the site. | Site build rules |
| 4 | 2026-10 | Instrument Serif for headings, Figtree for body, JetBrains Mono for labels, Caveat for margin notes. | Same redesign. | Site build rules |
| 5 | 2026-10 | Borders are drawn: 1.5px ink line, uneven radius, hard 3px shadow on hover, tape on photos. Every figure has a caption, sections are numbered sheets. | Same redesign. | Site build rules |
| 6 | 2026-10 | Only original or properly licensed footage on the site and in client work. Example footage is disclosed in the footer. | Copyright and image rights. | Owner |
| 7 | 2026-10-20 | Quality over quantity: clips are chosen and shaped after the best recent posts. | Volume alone was not producing views. | Owner |
| 8 | 2026-10-21 | Captions and the hook title stay inside the 9:16 frame, never too big or too wide. | Captions had spilled past the edges. | Owner |
| 9 | 2026-11-13 | Decision 8 as numbers: text at most 900px wide on a 1080 frame, two lines at most, top 8% and bottom 18% free of text. | So a render can be checked automatically. Change the numbers if a platform's overlay proves different. | Claude, open |
| 10 | 2026-11-13 | Heading sizes for decks, PDFs and proposals: display 64, title 40, subtitle 28, note 22, small 14. | The site's own heading sizes were not readable in this session. Replace with the site values once the repo is connected. | Claude, open |
| 11 | 2026-11-13 | Test on talking-head clips: one visual change at least every 2 seconds (cut, punch-in, caption emphasis or an on-screen graphic). | Idea from a reference video. Unproven on these accounts, so it is a test against the current edit, judged on retention. | To test |
| 12 | 2026-11-13 | No outside design references merged yet. When some are added, they inform layout and feel only; colours and fonts stay as above. | Brand wins on colours and fonts. | Owner's rule for this file |
| 13 | 2026-11-13 | Replaces 10. Type sizes are the site's own: display 76 (scales from 42), title 50 (from 32), subtitle 26, body 17, button 15.5, label 12 at 0.14em, caption 12.5, note 24 (from 19). | Read from the site's stylesheet. | Site stylesheet |
| 14 | 2026-11-13 | Exception to 3: the moving beam on the recommended plan and on the workflow connectors stay. They are the only gradients. | Added with the motion work after the redesign and approved then. | Site README |
| 15 | 2026-11-13 | Motion uses one easing family, three durations (150, 400, 900 ms) and one 70 ms stagger. | Already the site's motion system; written down so new work matches. | Site stylesheet |
| 16 | 2026-11-13 | Replaces 9. The clip safe area is the pipeline's own: text between x 60 and 990 and between y 150 and 1560 on a 1080 by 1920 frame. | Read from the renderer's style config. | Clip pipeline |
| 17 | 2026-11-13 | Replaces 11. No timer-based visual changes. The pipeline's editorial style already ties graphics to spoken numbers and labels; whether to switch it on is the open question. | The renderer's own rule is "never on a timer". | Clip pipeline |
