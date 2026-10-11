#!/usr/bin/env python3
"""Build the niche landing pages and 404 page from index.html.

Run from the repo root after changing index.html:
    python3 tools/build_pages.py

Each page reuses the home page's styles, proof stats, pricing, contact form,
footer and script, and adds its own title, hero, "why it works" cards and FAQ.
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://cliplinestudio.com"
src = (ROOT / "index.html").read_text()


def grab(pattern):
    m = re.search(pattern, src, flags=re.S)
    if not m:
        raise SystemExit(f"pattern not found: {pattern[:60]}")
    return m.group(0)


STYLE = grab(r"<style>.*?</style>")
FONTS = grab(r'<link rel="preload" href="/fonts/bricolage-grotesque.woff2"[^>]*>\n<link rel="preload" href="/fonts/figtree.woff2"[^>]*>')
ICON = grab(r'<link rel="icon"[^>]*>')
PROOF = grab(r'  <section id="proof">.*?\n  </section>\n')
PRICING = grab(r'  <section id="pricing">.*?\n  </section>\n')
TRIAL = grab(r'  <section id="trial".*?\n  </section>\n')
FOOTER = grab(r"  <footer>.*?</footer>")
SCRIPT = grab(r"<script>\n\(function\(\)\{.*?\}\)\(\);\n</script>")
TICK = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" '
        'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>')

ICONS = {
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M21.5 20a6.5 6.5 0 0 0-4-6"/>',
    "calendar": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18M9 16l2 2 4-4"/>',
    "play": '<rect x="3" y="5" width="18" height="14" rx="3"/><path d="m10 9 5 3-5 3z"/>',
    "door": '<path d="M14 3h5a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-5"/><path d="M10 17l5-5-5-5M15 12H3"/>',
    "archive": '<rect x="3" y="4" width="18" height="5" rx="1"/><path d="M5 9v10a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V9M10 13h4"/>',
    "bolt": '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
}


def icon(name):
    return ('<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


def absolutize(fragment):
    """Make media paths work from sub-folders."""
    return fragment.replace('"media/', '"/media/').replace("'media/", "'/media/").replace("(media/", "(/media/")


PAGES = [
    {
        "slug": "podcast-clipping",
        "title": "Podcast Clipping Service · Clipline Studio",
        "desc": "Podcast clipping for video podcasts. We cut every episode into captioned vertical clips for TikTok, Reels and Shorts. Get 5 free clips from your latest episode.",
        "eyebrow": "Podcast clipping service",
        "h1_pre": "Every episode, cut into",
        "h1_em": "clips that grow",
        "h1_post": "your podcast.",
        "sub": "We watch the full episode and pull the moments that stand on their own: the hot take, the story, the guest's best line. Each one is reframed to 9:16 on whoever is talking, captioned word by word and posted for you, or sent as ready-to-post files.",
        "cta": "Get 5 free clips from your latest episode",
        "videos": ["d1v", "d2v", "d3v"],
        "why_h": "Why clips work for podcasts",
        "why_lead": "A full episode asks for an hour. A clip asks for 30 seconds, then sends the people who liked it to the full show.",
        "why": [
            ("clock", "The best part is buried at minute 52", "Most people will never press play on a 90-minute episode. A clip puts the best moment in front of them first."),
            ("users", "Guest moments travel", "Every strong guest moment is a clip your guest can share with their own audience, which puts your show in front of new listeners."),
            ("calendar", "One episode, a week of posts", "A long conversation has plenty of standalone moments, so one recording can keep you posting daily until the next episode is out."),
        ],
        "faq": [
            ("Do you clip audio-only podcasts?", "We work from video. If your show is audio-only, email us first and we'll tell you honestly whether clips will work for it."),
            ("How long are the clips?", "Usually 20 to 60 seconds. Each clip is as long as the moment needs to make sense to someone who has never heard your show."),
            ("Can you clip older episodes?", "Yes. Plans count clips, not episodes, so we can pull moments from your back catalogue as well as new episodes."),
            ("Do you post to my accounts, or do I?", "Either. On Growth and Scale we post for you with scheduling access you grant. On Starter we deliver finished files and captions, and you post."),
            ("Who owns the clips?", "You do. They're cut from your episodes and delivered to you. We never post your clips anywhere except the accounts you choose."),
        ],
    },
    {
        "slug": "stream-clipping",
        "title": "Stream Clipping Service for Twitch, Kick and YouTube Live · Clipline Studio",
        "desc": "Clipping service for streamers. We cut your Twitch, Kick or YouTube Live VODs into captioned vertical clips and post them to TikTok, Reels and Shorts. Get 5 free clips.",
        "eyebrow": "Clipping for Twitch, Kick & YouTube Live",
        "h1_pre": "Your stream's best moments,",
        "h1_em": "clipped and posted",
        "h1_post": "for you.",
        "sub": "We go through your VOD and cut the reactions, fails, clutches and chat moments, reframe them to vertical with captions, and post them to TikTok, Reels and Shorts. You stream. We keep you in the feed between streams.",
        "cta": "Get 5 free clips from your last stream",
        "videos": ["v2", "v1", "v3"],
        "why_h": "Why streamers need clips",
        "why_lead": "Hardly anyone finds a streamer by opening a six-hour VOD. They find a 30-second clip first.",
        "why": [
            ("play", "Nobody rewatches the VOD", "Your best moments happen live and then disappear into hours of footage. Clips give them a second life."),
            ("door", "Clips are how new viewers find you", "A clip reaches people who have never heard of you and gives them a reason to show up next stream."),
            ("bolt", "Daily posts without the editing", "Consistent clips keep your name in the feed on days you don't stream, and you don't have to touch an editor."),
        ],
        "faq": [
            ("Which platforms do you clip from?", "Twitch, Kick and YouTube Live. If your VOD has a link we can open, we can clip it."),
            ("Do you clip gameplay and IRL streams?", "Both. Send us the stream and we'll pick the moments that work on their own for people who weren't watching live."),
            ("How long are the clips?", "Usually 20 to 60 seconds, long enough for the moment to land and short enough to keep people watching."),
            ("Do you post to my accounts, or do I?", "Either. On Growth and Scale we post for you with scheduling access you grant. On Starter we deliver finished files and captions, and you post."),
            ("Who owns the clips?", "You do. They're cut from your streams and delivered to you. We never post your clips anywhere except the accounts you choose."),
        ],
    },
    {
        "slug": "youtube-clipping",
        "title": "YouTube Shorts Clipping Service · Clipline Studio",
        "desc": "Turn your long YouTube videos into Shorts, TikToks and Reels. Vertical clips with captions and hooks, posted daily. Get 5 free clips from your latest video.",
        "eyebrow": "YouTube Shorts clipping service",
        "h1_pre": "Turn your long videos into",
        "h1_em": "Shorts that send viewers back",
        "h1_post": "to your channel.",
        "sub": "We find the strongest moments in every upload, cut them vertical with a hook title and word-by-word captions, and post them to YouTube Shorts, TikTok and Reels on a schedule. You keep making long videos. We keep your channel in the feed.",
        "cta": "Get 5 free clips from your latest video",
        "videos": ["v1", "v3", "v2"],
        "why_h": "Why Shorts work for long-form creators",
        "why_lead": "Shorts are where new viewers sample your channel before they commit to a 20-minute video.",
        "why": [
            ("door", "A front door to your channel", "A good Short shows what your channel is about in seconds and gives people a reason to watch the full video."),
            ("archive", "Your back catalogue is full of clips", "Videos you published months ago still have moments that work as Shorts today."),
            ("calendar", "Daily posts without filming more", "One long video can fill a week of Shorts, so you post every day without adding shoots."),
        ],
        "faq": [
            ("Do you upload Shorts to my channel?", "On Growth and Scale, yes, with access you grant. On Starter we deliver finished files and captions, and you post."),
            ("Can you clip videos that are already out?", "Yes. Plans count clips, not videos, so we can pull moments from older uploads as well as new ones."),
            ("How long are the clips?", "Usually 20 to 60 seconds. Each clip has to make sense to someone who has never seen your channel."),
            ("Who owns the clips?", "You do. They're cut from your videos and delivered to you. We never post your clips anywhere except the accounts you choose."),
            ("Can I cancel?", "Yes, any time. Plans are month to month."),
        ],
    },
]


def head(title, desc, canonical, noindex=False, ld=None):
    t, d = html.escape(title), html.escape(desc)
    robots = '<meta name="robots" content="noindex">\n' if noindex else ""
    ld_block = f'<script type="application/ld+json">{ld}</script>\n' if ld else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="{d}">
{robots}<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="Clipline Studio">
<meta property="og:image" content="{SITE}/media/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#f7f8fa" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0a0b0f" media="(prefers-color-scheme: dark)">
{ICON}
<title>{t}</title>
{ld_block}<script>document.documentElement.classList.add('js')</script>
{FONTS}
<!-- Generated by tools/build_pages.py from index.html. Edit the script, not this file. -->
{STYLE}
</head>
<body>
<div class="progress" aria-hidden="true"></div>
<div class="backdrop" aria-hidden="true"><div class="dots"></div><div class="blob b1"></div><div class="blob b2"></div></div>

<nav class="wrap">
  <a class="logo" href="/" aria-label="Clipline Studio home"><i></i>Clipline Studio</a>
  <a class="cta ghost" href="#trial">Get 5 free clips</a>
</nav>
"""


def phones(videos):
    out = []
    for i, v in enumerate(videos):
        delay = ["-1s", "-3.5s", "-5.5s"][i]
        out.append(f'      <div class="phone beam" style="--beam-delay:{delay};--beam-speed:7s"><div class="screen">'
                   f'<video poster="/media/{v}.jpg" autoplay muted loop playsinline preload="metadata">'
                   f'<source src="/media/{v}.mp4" type="video/mp4"></video></div></div>')
    return "\n".join(out)


def h1_words(pre, em, post):
    parts, d = [], 0.08
    for w in pre.split():
        parts.append(f'<span class="w reveal" style="--d:{d:.2f}s">{html.escape(w)}</span>')
        d += 0.05
    parts.append(f'<em class="w reveal aurora" style="--d:{d:.2f}s">{html.escape(em)}</em>')
    d += 0.08
    for w in post.split():
        parts.append(f'<span class="w reveal" style="--d:{d:.2f}s">{html.escape(w)}</span>')
        d += 0.05
    return " ".join(parts)


def faq_ld(faq):
    import json
    return json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]})


def niche(p):
    canonical = f"{SITE}/{p['slug']}/"
    why_cards = "\n".join(
        f'      <div class="step spot reveal"><div class="ic">{icon(ic)}</div><h3>{html.escape(h)}</h3><p>{html.escape(t)}</p></div>'
        for ic, h, t in p["why"])
    faq = "\n".join(
        f'      <details class="reveal"><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>'
        for q, a in p["faq"])
    faq += ('\n      <details class="reveal"><summary>I have another question</summary><p>Send it through the '
            '<a href="#trial">form above</a> or email <a href="mailto:cliplines.studio@gmail.com" target="_blank" '
            'rel="noopener">cliplines.studio@gmail.com</a> and we\'ll get back to you within 24 hours.</p></details>')
    body = f"""
<div class="wrap">
  <header class="hero" id="top">
    <div>
      <span class="badge reveal" style="--d:.02s"><span class="live"></span><span class="eyebrow shiny">{html.escape(p['eyebrow'])}</span></span>
      <h1>{h1_words(p['h1_pre'], p['h1_em'], p['h1_post'])}</h1>
      <p class="sub reveal" style="--d:.66s">{html.escape(p['sub'])}</p>
      <div class="actions reveal" style="--d:.76s">
        <a class="cta shimmer" href="#trial"><span class="spark" aria-hidden="true"><span></span></span>{html.escape(p['cta'])} <span class="arrow" aria-hidden="true">→</span></a>
        <a class="cta ghost" href="#pricing">See pricing</a>
      </div>
      <div class="trust reveal" style="--d:.86s">
        <span>{TICK}No call, no card</span>
        <span>{TICK}Clips within 48 hours</span>
        <span>{TICK}Cancel anytime</span>
      </div>
    </div>
    <div class="phones reveal" style="--d:.4s" aria-hidden="true">
{phones(p['videos'])}
    </div>
  </header>

  <section>
    <span class="kicker reveal">Why it works</span>
    <h2 class="reveal">{html.escape(p['why_h'])}</h2>
    <p class="lead reveal">{html.escape(p['why_lead'])}</p>
    <div class="steps">
{why_cards}
    </div>
  </section>

  <section>
    <span class="kicker reveal">How it works</span>
    <h2 class="reveal">You create. We do the rest.</h2>
    <p class="lead reveal">Every clip is reframed to 9:16, captioned word by word, gets a hook title for the first second and your branding. <a href="/#demo">See the pipeline in action</a>.</p>
  </section>

{absolutize(PROOF)}
{absolutize(PRICING)}
{absolutize(TRIAL)}
  <section>
    <span class="kicker reveal">FAQ</span>
    <h2 class="reveal" style="margin-bottom:18px">Questions</h2>
    <div class="faq">
{faq}
    </div>
  </section>

{FOOTER}
</div>

{absolutize(SCRIPT)}
</body>
</html>
"""
    page = head(p["title"], p["desc"], canonical, ld=faq_ld(p["faq"])) + body
    out = ROOT / p["slug"] / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(page)
    print("wrote", out.relative_to(ROOT))


def not_found():
    links = "".join(f'<a class="cta ghost" href="/{p["slug"]}/">{html.escape(p["eyebrow"])}</a>' for p in PAGES)
    body = f"""
<div class="wrap">
  <header class="hero" id="top" style="grid-template-columns:minmax(0,1fr)">
    <div>
      <span class="eyebrow">404</span>
      <h1 style="margin-top:12px">This page doesn't exist.</h1>
      <p class="sub">The link may be old or mistyped. Here's where you can go instead.</p>
      <div class="actions">
        <a class="cta shimmer" href="/"><span class="spark" aria-hidden="true"><span></span></span>Go to the home page <span class="arrow" aria-hidden="true">→</span></a>
        <a class="cta ghost" href="/#trial">Get 5 free clips</a>
      </div>
      <div class="actions">{links}</div>
    </div>
  </header>
{FOOTER}
</div>
{absolutize(SCRIPT)}
</body>
</html>
"""
    page = head("Page not found · Clipline Studio", "This page doesn't exist.", f"{SITE}/404.html", noindex=True) + body
    page = page.replace('<a class="cta ghost" href="#trial">Get 5 free clips</a>', '<a class="cta ghost" href="/#trial">Get 5 free clips</a>', 1)
    (ROOT / "404.html").write_text(page)
    print("wrote 404.html")


if __name__ == "__main__":
    for p in PAGES:
        niche(p)
    not_found()
