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
    "film": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M7 3v18M17 3v18M3 8h4M3 16h4M17 8h4M17 16h4M3 12h18"/>',
    "mic": '<rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v4M8 22h8"/>',
    "phone": '<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>',
    "send": '<path d="M12 16V4M7 9l5-5 5 5"/><path d="M4 16v2a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-2"/>',
    "tag": '<path d="M20.6 13.4 13.4 20.6a2 2 0 0 1-2.8 0L3 13V3h10l7.6 7.6a2 2 0 0 1 0 2.8z"/><circle cx="7.5" cy="7.5" r="1.5"/>',
    "repeat": '<path d="M17 2l4 4-4 4"/><path d="M3 11V9a3 3 0 0 1 3-3h15M7 22l-4-4 4-4"/><path d="M21 13v2a3 3 0 0 1-3 3H3"/>',
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


def svc_nav(active, cta_href, cta_text):
    clip = ' aria-current="page"' if active == "clip" else ""
    edit = ' aria-current="page"' if active == "edit" else ""
    return (f'<span class="navr"><span class="svc" role="navigation" aria-label="Services">'
            f'<a href="/"{clip}><span class="s-long">Clipping</span><span class="s-short">Clips</span></a>'
            f'<a href="/video-editing/"{edit}><span class="s-long">Video editing</span><span class="s-short">Editing</span></a></span>'
            f'<a class="cta ghost" href="{cta_href}">{cta_text}</a></span>')


def head(title, desc, canonical, noindex=False, ld=None, active="clip", cta_href="#trial", cta_text="Get 5 free clips"):
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
  {svc_nav(active, cta_href, cta_text)}
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
    links += '<a class="cta ghost" href="/video-editing/">Video editing</a>'
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
    page = head("Page not found · Clipline Studio", "This page doesn't exist.", f"{SITE}/404.html", noindex=True, active=None, cta_href="/#trial") + body
    (ROOT / "404.html").write_text(page)
    print("wrote 404.html")


# ---------------------------------------------------------------------------
# Video editing page (added 2026-10-14). Not a clipping niche: own hero, services,
# process and FAQ; reuses the home contact form with editing wording; no pricing
# table (every project gets a quote).
# ---------------------------------------------------------------------------
EDIT = {
    "slug": "video-editing",
    "title": "Video Editing for YouTubers & Podcasts · Clipline Studio",
    "desc": "Video editing for YouTube videos, podcasts and short-form. Cuts, pacing, captions, sound and colour, delivered ready to upload. Get a free quote within 24 hours.",
    "services": [
        ("film", "YouTube videos", "Your raw footage turned into a finished long-form video: tight cuts, pacing that holds attention, zooms, on-screen text, b-roll, music and sound."),
        ("mic", "Podcast episodes", "Full episodes edited for YouTube and Spotify: camera switching, cleaned and levelled audio, intro and outro, and chapters."),
        ("phone", "Short-form from raw footage", "TikToks, Reels and Shorts edited from your own clips or footage, with captions, a hook in the first second and fast pacing."),
    ],
    "included": [
        "Cuts that remove pauses, mistakes and dead air",
        "Pacing, zooms and on-screen text that keep people watching",
        "Captions or subtitles, burned in or as a file",
        "Audio cleanup and levelling so every voice is clear",
        "Colour correction for a consistent look",
        "Royalty-free music and sound effects",
        "Revision rounds included in every quote",
        "You own the finished video. Files are yours to keep.",
    ],
    "steps": [
        ("send", "Step 1", "Send your footage", "Share a Drive, Dropbox or WeTransfer link and tell us what you need: length, style and an example you like."),
        ("tag", "Step 2", "Get a fixed quote", "Within 24 hours you get a fixed price and delivery date. Nothing starts until you say yes."),
        ("repeat", "Step 3", "Review and revise", "You get the finished edit, ready to upload. Ask for changes until it's right, within the revision rounds in your quote."),
    ],
    "faq": [
        ("How much does editing cost?", "It depends on the length of the footage and the style you want, so every project gets a fixed quote within 24 hours. You know the full price before any work starts."),
        ("How do I send my footage?", "Upload it to Google Drive, Dropbox or WeTransfer and paste the link in the form. Large files are fine."),
        ("How long does an edit take?", "It depends on the project. Your quote includes a delivery date, and we stick to it."),
        ("Can you match my channel's style?", "Yes. Send a link to a video you like, yours or someone else's, and we'll edit to that style."),
        ("Which languages can you caption?", "English, German, Serbian, Croatian, Bosnian, Macedonian and Russian."),
        ("Who owns the edited video?", "You do. It's your footage and your video, delivered to you to publish wherever you want."),
    ],
}

EDIT_CSS = """<style>
.ed-mock{border:1px solid var(--line);border-radius:20px;padding:14px;background:linear-gradient(180deg,var(--surface),color-mix(in srgb,var(--surface) 60%,var(--bg)));box-shadow:0 30px 70px -50px color-mix(in srgb,var(--accent) 80%,transparent)}
.ed-mock .scr{position:relative;border-radius:12px;overflow:hidden;aspect-ratio:16/9;background:#05070c}
.ed-mock .scr video{width:100%;height:100%;object-fit:cover;display:block}
.ed-mock .ed-frame{position:absolute;inset:0;display:grid;place-items:center;background:radial-gradient(120% 90% at 30% 20%,color-mix(in srgb,var(--accent) 55%,#05070c),#05070c 70%),#05070c}
.ed-mock .ed-frame::before{content:"";position:absolute;inset:0;background:repeating-linear-gradient(90deg,rgba(255,255,255,.04) 0 1px,transparent 1px 64px);pointer-events:none}
.ed-mock .ed-play{width:64px;height:64px;border-radius:50%;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.3);-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px);position:relative}
.ed-mock .ed-play::after{content:"";position:absolute;left:26px;top:20px;border-left:18px solid #fff;border-top:12px solid transparent;border-bottom:12px solid transparent}
.ed-mock .ed-cap{position:absolute;bottom:14px;left:50%;transform:translateX(-50%);font:800 clamp(14px,1.6vw,18px)/1 var(--display);color:#fff;text-shadow:0 2px 8px rgba(0,0,0,.6);white-space:nowrap}
.ed-mock .ed-cap b{color:#ffd23f}
.ed-mock .ed-tc{z-index:2;white-space:nowrap;position:absolute;left:10px;top:10px;font:500 11px/1 var(--mono);color:#fff;background:rgba(5,7,12,.6);padding:6px 8px;border-radius:6px;letter-spacing:.04em}
.ed-mock .tracks{margin-top:12px;display:grid;gap:6px;position:relative}
.ed-mock .trk{display:flex;gap:4px;height:22px}
.ed-mock .trk i{display:block;height:100%;border-radius:5px;flex:none}
.ed-mock .v i{background:color-mix(in srgb,var(--accent) 75%,transparent)}
.ed-mock .t i{background:color-mix(in srgb,var(--violet) 70%,transparent);height:60%;align-self:center}
.ed-mock .a i{background:color-mix(in srgb,var(--cyan) 55%,transparent)}
.ed-mock .ph{position:absolute;top:-4px;bottom:-4px;width:2px;background:#ef4444;left:8%;border-radius:2px;box-shadow:0 0 10px #ef4444;animation:edph 8s linear infinite}
@keyframes edph{to{left:96%}}
@media (prefers-reduced-motion:reduce){.ed-mock .ph{animation:none;left:42%}}
.ed-mock .lbl{display:flex;justify-content:space-between;margin-top:8px;font:500 11px/1 var(--mono);color:var(--ink-3)}
.quote-note{margin-top:18px;padding:16px 18px;border:1px dashed var(--line);border-radius:14px;color:var(--ink-2);max-width:62ch}
.quote-note b{color:var(--ink)}
</style>"""


def editing_trial():
    t = absolutize(TRIAL)
    reps = [
        ("<h2>5 free clips from your latest video</h2>", "<h2>Get a free quote for your edit</h2>"),
        ("No call, no card. Send us your channel link and you'll have 5 finished clips within 48 hours. Keep them and post them either way.",
         "No call needed. Send a link to your footage and a few words about what you need. You'll get a fixed price and delivery date within 24 hours."),
        ("<li><b>1</b>Send your channel link</li>", "<li><b>1</b>Send your footage link</li>"),
        ("<li><b>2</b>Get 5 clips in 48 hours</li>", "<li><b>2</b>Get a quote in 24 hours</li>"),
        ("<li><b>3</b>Like them? Pick a plan.</li>", "<li><b>3</b>Say yes, get your edit</li>"),
        ('<label for="channel">Your channel link</label>', '<label for="channel">Link to your footage or channel</label>'),
        ('placeholder="youtube.com/@yourchannel"', 'placeholder="drive.google.com/… or youtube.com/@yourchannel"'),
        ('<label for="message">Anything we should know? <small>optional</small></label>', '<label for="message">What do you need edited? <small>optional</small></label>'),
        ('placeholder="Which video to clip, your style, platforms you post on…"', 'placeholder="Type of video, length, style, deadline, an example you like…"'),
        ('<span class="lbl">Get my 5 free clips</span>', '<span class="lbl">Get my free quote</span>'),
        ("We only use your details to reply and send your clips. No newsletter, no spam.", "We only use your details to reply with your quote. No newsletter, no spam."),
        ('<p id="doneText">Your 5 free clips are on the way. We\'ll email them to you within 48 hours.</p>', '<p id="doneText">We\'ll reply with your quote within 24 hours.</p>'),
        ('Send another channel', 'Send another project'),
    ]
    for a, b in reps:
        if a not in t:
            raise SystemExit(f"editing trial: text not found: {a[:50]}")
        t = t.replace(a, b, 1)
    return t


def editing_script():
    sc = absolutize(SCRIPT)
    reps = [
        ("_subject:'New free-clips request'", "_subject:'New video-editing request'"),
        ("lbl.textContent='Get my 5 free clips'", "lbl.textContent='Get my free quote'"),
        ("'Add your channel link so we know what to clip.'", "'Add a link to your footage or channel.'"),
        ("'Add your email so we can send the clips.'", "'Add your email so we can send your quote.'"),
        ("'Your 5 free clips are on the way. We’ll send them to '+(em||'your email')+' within 48 hours.'",
         "'We’ll reply to '+(em||'your email')+' with a fixed quote within 24 hours.'"),
    ]
    for a, b in reps:
        if a not in sc:
            raise SystemExit(f"editing script: text not found: {a[:50]}")
        sc = sc.replace(a, b, 1)
    return sc


def editing():
    e = EDIT
    canonical = f"{SITE}/{e['slug']}/"
    services = "\n".join(
        f'      <div class="step spot reveal"><div class="ic">{icon(ic)}</div><h3>{html.escape(h)}</h3><p>{html.escape(t)}</p></div>'
        for ic, h, t in e["services"])
    steps = "\n".join(
        f'      <div class="step spot reveal"><div class="ic">{icon(ic)}</div><span class="n">{n}</span><h3>{html.escape(h)}</h3><p>{html.escape(t)}</p></div>'
        for ic, n, h, t in e["steps"])
    tick = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" '
            'stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>')
    included = "\n".join(f'      <li class="reveal">{tick}{html.escape(x)}</li>' for x in e["included"])
    faq = "\n".join(
        f'      <details class="reveal"><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>'
        for q, a in e["faq"])
    faq += ('\n      <details class="reveal"><summary>I have another question</summary><p>Send it through the '
            '<a href="#trial">form above</a> or email <a href="mailto:cliplines.studio@gmail.com" target="_blank" '
            'rel="noopener">cliplines.studio@gmail.com</a> and we\'ll get back to you within 24 hours.</p></details>')
    v = lambda w: [6, 14, 9, 18, 7, 12, 10, 8][w % 8]
    vtrack = "".join(f'<i style="width:{v(i)}%"></i>' for i in range(8))
    ttrack = "".join(f'<i style="width:{w}%;margin-left:{m}%"></i>' for w, m in [(10, 4), (14, 9), (8, 12), (12, 10)])
    atrack = '<i style="width:46%"></i><i style="width:52%"></i>'
    body = f"""
<div class="wrap">
  <header class="hero" id="top">
    <div>
      <span class="badge reveal" style="--d:.02s"><span class="live"></span><span class="eyebrow shiny">Video editing service</span></span>
      <h1>{h1_words("Your raw footage, edited into", "videos people finish", "watching.")}</h1>
      <p class="sub reveal" style="--d:.66s">Send us your recording and we send back a finished video, ready to upload: tight cuts, pacing that holds attention, captions, clean sound and colour. For YouTube videos, podcast episodes and short-form.</p>
      <div class="actions reveal" style="--d:.76s">
        <a class="cta shimmer" href="#trial"><span class="spark" aria-hidden="true"><span></span></span>Get a free quote <span class="arrow" aria-hidden="true">→</span></a>
        <a class="cta ghost" href="#included">See what's included</a>
      </div>
      <div class="trust reveal" style="--d:.86s">
        <span>{TICK}Quote within 24 hours</span>
        <span>{TICK}Fixed price up front</span>
        <span>{TICK}Revisions included</span>
      </div>
    </div>
    <div class="ed-mock reveal" style="--d:.4s" aria-hidden="true">
      <div class="scr"><div class="ed-frame"><span class="ed-play"></span><span class="ed-cap"><b>Your</b> footage, <b>edited</b></span></div><span class="ed-tc">EDIT · 00:14:32</span></div>
      <div class="tracks">
        <div class="trk v">{vtrack}</div>
        <div class="trk t">{ttrack}</div>
        <div class="trk a">{atrack}</div>
        <span class="ph"></span>
      </div>
      <div class="lbl"><span>V1 · cuts</span><span>T1 · text</span><span>A1 · audio</span></div>
    </div>
  </header>

  <section>
    <span class="kicker reveal">What we edit</span>
    <h2 class="reveal">Editing for creators who'd rather keep filming</h2>
    <p class="lead reveal">Editing takes hours you could spend making the next video. Hand it off and keep a steady upload schedule.</p>
    <div class="steps">
{services}
    </div>
  </section>

  <section id="included">
    <span class="kicker reveal">Included</span>
    <h2 class="reveal">Every edit includes</h2>
    <p class="lead reveal">Standard on every project.</p>
    <ul class="list">
{included}
    </ul>
  </section>

  <section>
    <span class="kicker reveal">How it works</span>
    <h2 class="reveal">From footage to finished video</h2>
    <p class="lead reveal">Three steps, and only the first one is yours.</p>
    <div class="steps">
{steps}
    </div>
    <p class="quote-note reveal"><b>Pricing:</b> every project is different, so instead of a price list you get a fixed quote within 24 hours. You know the full price and delivery date before any work starts.</p>
  </section>

{editing_trial()}
  <section>
    <span class="kicker reveal">FAQ</span>
    <h2 class="reveal" style="margin-bottom:18px">Questions</h2>
    <div class="faq">
{faq}
    </div>
  </section>

{FOOTER}
</div>

{editing_script()}
</body>
</html>
"""
    page = head(e["title"], e["desc"], canonical, ld=faq_ld(e["faq"]), active="edit", cta_text="Get a free quote")
    page = page.replace("</head>", EDIT_CSS + "\n</head>", 1)
    page += body
    out = ROOT / e["slug"] / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(page)
    print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    for p in PAGES:
        niche(p)
    editing()
    not_found()
