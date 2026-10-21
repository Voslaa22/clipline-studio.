"""Stylesheet for the handmade redesign (2026-10-21).

Design rules, in short:
  * paper, ink, one accent (Clipline blue). No gradients, glows, shimmer or marquee.
  * Instrument Serif for headings, Figtree for body, JetBrains Mono for labels,
    Caveat for the handwritten margin notes.
  * borders are drawn, not cast: a 1.5 px ink line with an uneven ("wobbly")
    radius, a hard 3 px offset shadow on hover, tape strips on photos.
  * every figure has a caption. Sections are numbered like a sheet in a binder.
"""

GRAIN = ("url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E"
         "%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/%3E"
         "%3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .6 0'/%3E%3C/filter%3E"
         "%3Crect width='300' height='300' filter='url(%23n)'/%3E%3C/svg%3E\")")

DARK = ("--paper:#0a0b0f;--card:#13151b;--ink:#f3f5f9;--ink-2:#b8bfcc;--ink-3:#8a92a2;"
        "--rule:rgba(243,245,249,.34);--rule-soft:rgba(243,245,249,.14);--rule-faint:rgba(243,245,249,.07);"
        "--accent:#4d8dff;--accent-soft:#16213a;--good:#4cc27a;--tape:rgba(255,210,63,.32);color-scheme:dark")

CSS = r"""
@font-face{font-family:"Instrument Serif";src:url(/fonts/instrument-serif.woff2) format("woff2");font-weight:400;font-style:normal;font-display:swap}
@font-face{font-family:"Instrument Serif";src:url(/fonts/instrument-serif-italic.woff2) format("woff2");font-weight:400;font-style:italic;font-display:swap}
@font-face{font-family:"Figtree";src:url(/fonts/figtree.woff2) format("woff2");font-weight:300 900;font-display:swap}
@font-face{font-family:"JetBrains Mono";src:url(/fonts/jetbrains-mono-400.woff2) format("woff2");font-weight:400;font-display:swap}
@font-face{font-family:"JetBrains Mono";src:url(/fonts/jetbrains-mono-500.woff2) format("woff2");font-weight:500;font-display:swap}
@font-face{font-family:"Caveat";src:url(/fonts/caveat.woff2) format("woff2");font-weight:700;font-display:swap}

:root{
  --paper:#f7f8fa;--card:#ffffff;--ink:#0b0d12;--ink-2:#4a5160;--ink-3:#646b7b;
  --rule:rgba(11,13,18,.32);--rule-soft:rgba(11,13,18,.12);--rule-faint:rgba(11,13,18,.07);
  --accent:#1d5cff;--accent-soft:#eef3ff;--good:#16a34a;--rec:#ef4444;--mark:#ffd23f;
  --tape:rgba(255,210,63,.5);--shadow:var(--ink);
  --serif:"Instrument Serif",Georgia,"Times New Roman",serif;
  --body:"Figtree",system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono:"JetBrains Mono",ui-monospace,Menlo,Consolas,monospace;
  --hand:"Caveat","Segoe Print","Bradley Hand",cursive;
  --wob:255px 15px 225px 15px / 15px 225px 15px 255px;
  --wob2:15px 225px 15px 255px / 255px 15px 225px 15px;
  --wrap:1120px;--pad:clamp(18px,4vw,40px);
  /* motion system: one easing family, three durations, one stagger */
  --ease:cubic-bezier(.2,.7,.2,1);--ease-out:cubic-bezier(.16,1,.3,1);--t-fast:.15s;--t-med:.4s;--t-slow:.9s;--stagger:70ms;
  color-scheme:light dark;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){DARK}}
:root[data-theme="dark"]{DARK}
*{box-sizing:border-box}
[hidden]{display:none!important}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth;scroll-padding-top:16px}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--paper);color:var(--ink);font:400 17px/1.6 var(--body);overflow-x:hidden;-webkit-font-smoothing:antialiased}
body::before{content:"";position:fixed;inset:0;z-index:50;pointer-events:none;opacity:.08;background-image:GRAIN;mix-blend-mode:multiply}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) body::before{opacity:.06;mix-blend-mode:screen}}
:root[data-theme="dark"] body::before{opacity:.06;mix-blend-mode:screen}
a{color:inherit}
img,video,svg{max-width:100%;display:block}
figure{margin:0}
::selection{background:var(--mark);color:#0b0d12}
.wrap{max-width:var(--wrap);margin:0 auto;padding:0 var(--pad)}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.skip{position:absolute;left:-999px;top:8px;background:var(--ink);color:var(--paper);padding:8px 12px;z-index:100}
.skip:focus{left:8px}

/* ---- type ---- */
h1,h2,h3{font-family:var(--serif);font-weight:400;letter-spacing:-.01em;margin:0}
h1{font-size:clamp(42px,6.2vw,76px);line-height:.98;text-wrap:balance}
h2{font-size:clamp(32px,4vw,50px);line-height:1.02;text-wrap:balance}
h3{font-size:26px;line-height:1.1}
h1 em,h2 em{font-style:italic;position:relative;white-space:nowrap}
h1.kin{font-family:var(--body);font-weight:440;font-size:clamp(38px,5.2vw,64px);letter-spacing:-.03em;line-height:1;display:flex;flex-wrap:wrap;column-gap:.24em;row-gap:.06em;--hp:calc(1em/16);--sw:calc(1em*125/6000)}
.kin .w{display:inline-flex;white-space:nowrap}
.kin .c{display:inline-block;-webkit-text-stroke:var(--sw) transparent;transition:font-weight var(--t-med) var(--ease),-webkit-text-stroke-color var(--t-med) var(--ease),padding var(--t-med) var(--ease),opacity .7s var(--ease-out) var(--dl,0s)}
@media (hover:hover){
  .kin .c:hover{font-weight:860;padding-inline:var(--hp);-webkit-text-stroke-color:var(--accent)}
  .kin .c:hover+.c,.kin .c:has(+.c:hover){font-weight:660;padding-inline:calc(var(--hp)/2)}
  .kin .c:hover+.c+.c,.kin .c:has(+.c+.c:hover){font-weight:540}
}
.kin em.ul{font-style:normal;color:var(--accent);display:inline-flex;flex-wrap:wrap;column-gap:.24em}
.kin em.ul path{stroke:var(--ink)}
.js:not(.loaded) .kin .c{opacity:0;font-weight:300}
@media (prefers-reduced-motion:reduce){.js:not(.loaded) .kin .c{opacity:1;font-weight:440}.kin .c{transition:none}}
@media (max-width:700px){h1 em,h2 em,em.ul{white-space:normal}}
em.ul{font-style:italic;position:relative;display:inline-block}
em.ul svg{position:absolute;left:-2%;right:-2%;bottom:-.08em;width:104%;height:.32em;overflow:visible;pointer-events:none}
em.ul path{fill:none;stroke:var(--accent);stroke-width:3.2;stroke-linecap:round;stroke-linejoin:round}
p{margin:0}
.lead{font-size:clamp(18px,1.6vw,21px);color:var(--ink-2);max-width:60ch;margin-top:14px}
.kicker{display:inline-flex;flex-wrap:wrap;align-items:center;gap:4px 10px;font:500 12px/1.6 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--ink-3)}
.kicker b{font-weight:500;color:var(--accent)}
.hand{font:700 clamp(19px,1.9vw,24px)/1.15 var(--hand);color:var(--ink-2)}
.hand.ac{color:var(--accent)}
.mono{font-family:var(--mono)}
.fig{font:400 12.5px/1.5 var(--mono);color:var(--ink-3);margin-top:12px;max-width:72ch}
.fig b{font-weight:500;color:var(--ink-2)}

/* ---- rules ---- */
.cut{display:flex;align-items:center;gap:14px;margin:clamp(56px,8vw,104px) 0 34px;color:var(--ink-3);font:500 12px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase}
.cut svg{width:18px;height:18px;flex:none;stroke:var(--ink-3);fill:none;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round;transform:rotate(-90deg)}
.cut::after{content:"";flex:1;border-top:2px dashed var(--rule)}
.cut i{font-style:normal;color:var(--ink)}
.wob{border:1.5px solid var(--ink);border-radius:var(--wob);background:var(--card)}
.wob2{border:1.5px solid var(--ink);border-radius:var(--wob2);background:var(--card)}

/* ---- buttons ---- */
.btn{display:inline-flex;align-items:center;gap:9px;padding:13px 20px;background:var(--ink);color:var(--paper);font:600 15.5px/1 var(--body);border:1.5px solid var(--ink);border-radius:var(--wob);text-decoration:none;cursor:pointer;transition:transform .15s,box-shadow .15s;white-space:nowrap}
.btn:hover{transform:translate(-2px,-2px);box-shadow:3px 3px 0 var(--accent)}
.btn:active{transform:none;box-shadow:none}
.btn.alt{background:transparent;color:var(--ink)}
.btn.sm{padding:9px 14px;font-size:14px}
.btn:focus-visible,a:focus-visible,button:focus-visible,summary:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.btn .arr{font-family:var(--hand);font-size:22px;line-height:0;margin-left:2px}

/* ---- nav ---- */
nav.top{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:22px 0 10px}
.logo{display:inline-flex;align-items:center;gap:10px;text-decoration:none;font:400 24px/1 var(--serif)}
.logo svg{width:28px;height:28px;stroke:var(--ink);fill:none;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.logo .ac{stroke:var(--accent)}
.navr{display:flex;align-items:center;gap:22px}
.svc{display:flex;gap:18px;font:500 15px/1 var(--body)}
.svc a{text-decoration:none;color:var(--ink-2);position:relative;padding:6px 0}
.svc a[aria-current]{color:var(--ink)}
.svc a[aria-current]::after{content:"";position:absolute;left:-2px;right:-2px;bottom:-1px;height:7px;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 8' preserveAspectRatio='none'%3E%3Cpath d='M2 5c20-4 40-3 60-1s25 1 36-2' fill='none' stroke='%231d5cff' stroke-width='2.6' stroke-linecap='round'/%3E%3C/svg%3E") no-repeat center/100% 100%}
.svc a.sep{margin-left:6px;padding-left:16px;border-left:1px dashed var(--rule)}
.menu-btn{display:none;width:42px;height:42px;border:1.5px solid var(--ink);border-radius:var(--wob);background:transparent;color:var(--ink);cursor:pointer;place-items:center}
.menu-btn svg{width:22px;height:22px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round}
.menu-btn .x{display:none}
.menu-btn[aria-expanded="true"] .bars{display:none}.menu-btn[aria-expanded="true"] .x{display:block}
@media (max-width:720px){
  .menu-btn{display:grid}
  .navr{gap:10px}
  .btn.top{padding:10px 13px;font-size:14px}
  .svc{display:none;position:absolute;left:0;right:0;top:100%;z-index:40;flex-direction:column;gap:0;background:var(--card);border:1.5px solid var(--ink);border-radius:var(--wob2);padding:8px 6px;box-shadow:4px 4px 0 var(--accent);font-size:17px}
  .svc.open{display:flex;animation:menu var(--t-med) var(--ease-out)}
  @keyframes menu{from{opacity:0;transform:translateY(-6px)}to{opacity:1;transform:none}}
  .svc a{padding:12px 14px;border-bottom:1px dashed var(--rule-soft)}
  .svc a:last-child{border-bottom:0}
  .svc a.sep{margin:0;padding-left:14px;border-left:0}
  .svc a[aria-current]::after{left:14px;right:auto;width:70px}
  nav.top{position:relative}
}

/* ---- hero ---- */
.hero{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:clamp(24px,5vw,64px);align-items:center;padding:clamp(28px,5vw,64px) 0 10px;position:relative}
@media (max-width:860px){.hero{grid-template-columns:1fr}}
.hero .kicker{margin-bottom:14px}
.hero .sub{font-size:clamp(17px,1.5vw,20px);color:var(--ink-2);max-width:56ch;margin-top:22px}
.hero .actions{display:flex;flex-wrap:wrap;gap:12px;margin-top:28px;align-items:center}
@media (max-width:420px){.hero .actions .btn,.plan .btn,.send{white-space:normal;text-align:left;line-height:1.25}.hero .actions .btn{width:100%}}
.trust{display:flex;flex-wrap:wrap;gap:6px 22px;margin-top:22px;font:700 20px/1.1 var(--hand);color:var(--ink-2)}
.trust span{display:inline-flex;align-items:center;gap:7px}
.trust svg{width:18px;height:18px;stroke:var(--good);fill:none;stroke-width:3;stroke-linecap:round;stroke-linejoin:round}
.stamp{display:inline-block;transform:rotate(-6deg);border:3px double var(--accent);color:var(--accent);padding:9px 13px 8px;font:500 12px/1.25 var(--mono);letter-spacing:.14em;text-transform:uppercase;border-radius:var(--wob);background:transparent;opacity:.92;white-space:nowrap}
.pols .stamp{position:absolute;right:0;top:0;z-index:5}
@media (max-width:860px){.pols .stamp{top:0;right:4px;transform:rotate(-4deg)}}

/* polaroids */
.pols{display:flex;justify-content:center;align-items:flex-end;gap:0;padding:64px 0 10px;min-height:380px;position:relative}
@media (min-width:1300px){.pols{min-height:440px}}
.pol{--r:0deg;position:relative;background:var(--card);padding:9px 9px 32px;border:1px solid var(--rule-soft);box-shadow:3px 4px 0 var(--rule-soft);transform:rotate(var(--r));width:clamp(118px,13vw,196px);flex:none;transition:transform .35s cubic-bezier(.3,1.3,.5,1),z-index 0s}
.pol:nth-of-type(1){--r:-6deg;margin-right:4px;z-index:1}
.pol:nth-of-type(2){--r:2deg;z-index:3;width:clamp(132px,14.5vw,220px);margin-bottom:22px}
.pol:nth-of-type(3){--r:5deg;margin-left:4px;z-index:2}
.scene{position:relative}
.scene .pol{--z:1;transform:rotate(var(--r)) translate(calc(var(--mx,0px)*var(--z)),calc(var(--my,0px)*var(--z)))}
.scene .pol:nth-of-type(2){--z:1.6}.scene .pol:nth-of-type(3){--z:.7}
.js:not(.loaded) .scene .pol{opacity:0;transform:rotate(0deg) translateY(22px)}
.js .scene .pol{transition:transform var(--t-slow) var(--ease-out) var(--pd,0s),opacity .6s var(--ease-out) var(--pd,0s)}
.js .settled .scene .pol{transition:transform .35s cubic-bezier(.3,1.3,.5,1)}
.scene .pol:hover{transform:rotate(0deg) translateY(-8px);z-index:4}
.pol:hover{transform:rotate(0deg) translateY(-8px);z-index:4}
.pol::before{content:"";position:absolute;top:-12px;left:50%;width:84px;height:24px;background:var(--tape);transform:translateX(-50%) rotate(-4deg);z-index:2;box-shadow:0 1px 1px rgba(0,0,0,.06)}
.pol:nth-of-type(3)::before{transform:translateX(-50%) rotate(5deg)}
.pol .scr{aspect-ratio:9/16;overflow:hidden;background:#0b0d12}
.pol video{width:100%;height:100%;object-fit:cover}
.pol .cap{position:absolute;left:12px;right:8px;bottom:6px;font:700 16px/1 var(--hand);color:var(--ink-2);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
@media (max-width:860px){.pols{min-height:0;padding-top:64px}.pol{width:clamp(100px,26vw,150px)}.pol:nth-of-type(2){width:clamp(112px,29vw,168px)}}
@media (max-width:400px){.pol{width:26vw}.pol:nth-of-type(2){width:28vw}.pol:nth-of-type(1){margin-right:0}.pol:nth-of-type(3){margin-left:0}}

/* hero editing deck: three tracks, a playhead, caption segments that light up as it passes */
.deck{position:relative;margin:4px 8px 0;padding:10px 10px 12px 36px;border:1.5px solid var(--ink);border-radius:var(--wob2);background:var(--card);--cycle:9s}
.deck .tc{display:flex;justify-content:space-between;font:400 10px/1 var(--mono);color:var(--ink-3);margin-bottom:6px}
.deck .trk{position:relative;height:12px;margin-top:5px;background:var(--rule-faint);border-radius:2px}
.deck .trk i{position:absolute;top:0;bottom:0;left:calc(var(--l)*100%);width:calc(var(--w)*100%);border-radius:2px;background:var(--ink);opacity:.85}
.deck .trk.v i{background:var(--ink-2)}
.deck .trk.v i::after{content:"";position:absolute;right:0;top:0;bottom:0;width:2px;background:var(--paper)}
.deck .trk.c i{background:var(--accent);opacity:.3;animation:deckcap var(--cycle) linear infinite;animation-delay:calc((var(--l) - 1)*var(--cycle))}
@keyframes deckcap{0%,1%{opacity:.3}2%,16%{opacity:1}17%,100%{opacity:.3}}
.deck .trk.a{display:flex;align-items:flex-end;gap:2px;background:transparent;height:14px}
.deck .trk.a b{flex:1;height:var(--h);background:var(--rule);border-radius:1px}
.deck .lab{position:absolute;left:-26px;top:2px;font:500 8px/1 var(--mono);color:var(--ink-3);letter-spacing:.1em}
.deck .ph{position:absolute;top:22px;bottom:10px;left:36px;width:2px;background:var(--rec);animation:deckph var(--cycle) linear infinite;z-index:2}
.deck .ph::before{content:"";position:absolute;top:-6px;left:-4px;width:10px;height:6px;background:var(--rec);clip-path:polygon(0 0,100% 0,50% 100%)}
@keyframes deckph{from{left:36px}to{left:calc(100% - 10px)}}
.js .deck{opacity:0;transform:translateY(10px);transition:opacity .6s var(--ease-out) .55s,transform .6s var(--ease-out) .55s}
.js.loaded .deck{opacity:1;transform:none}
.deck .ph,.deck .trk.c i{animation-play-state:paused}
.loaded .deck.live .ph,.loaded .deck.live .trk.c i{animation-play-state:running}
@media (prefers-reduced-motion:reduce){.deck .ph{animation:none;left:46%}.deck .trk.c i{animation:none;opacity:.8}.js .deck{opacity:1;transform:none;transition:none}}
@media (max-width:860px){.deck{margin:10px 0 0}}

/* ---- contents line ---- */
.contents{margin-top:clamp(34px,5vw,56px);padding:18px 0;border-top:2px dashed var(--rule);border-bottom:2px dashed var(--rule);display:flex;flex-wrap:wrap;gap:8px 28px;align-items:baseline;font:500 13px/1.5 var(--mono);color:var(--ink-2)}
.contents b{font-weight:500;color:var(--ink-3);letter-spacing:.12em;text-transform:uppercase;font-size:11px;margin-right:4px}
.contents span::before{content:"✓";color:var(--good);margin-right:7px;font-family:var(--hand);font-size:18px;font-weight:700;line-height:0}

/* ---- sections ---- */
section{scroll-margin-top:24px}
.sec-head{max-width:70ch}
.sec-head .hand{margin-top:10px;display:block}

/* ---- demo / storyboard ---- */
.board{display:grid;grid-template-columns:minmax(0,1.25fr) auto minmax(0,.95fr);gap:clamp(14px,2.4vw,30px);align-items:center;margin-top:30px}
@media (max-width:860px){.board{grid-template-columns:1fr}.board .arrow{transform:rotate(90deg);margin:-6px auto;width:60px}}
.ep{padding:14px;position:relative;transform:rotate(-.6deg)}
.ep .top{display:flex;justify-content:space-between;gap:10px;font:500 12px/1 var(--mono);color:var(--ink-3);margin-bottom:10px}
.ep .top b{font-weight:500;color:var(--ink)}
.ep .top .rec{display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--rec);margin-right:7px;vertical-align:1px}
.ep .frame{position:relative;aspect-ratio:16/9;overflow:hidden;border:1.5px solid var(--ink);background:#0b0d12}
.ep .frame video{width:100%;height:100%;object-fit:cover}
.ep .crop{position:absolute;top:4%;bottom:4%;left:35%;width:30%;border:2px dashed var(--mark);border-radius:4px}
.ep .crop span{position:absolute;left:0;right:0;bottom:-24px;text-align:center;font:700 15px/1 var(--hand);color:#fff;text-shadow:0 1px 2px #000}
.ep .scan{position:absolute;top:0;bottom:0;width:2px;background:var(--accent);left:5%;animation:scan 9s linear infinite;opacity:.9}
@keyframes scan{to{left:95%}}
.tl{position:relative;height:38px;margin:22px 4px 0;border-bottom:2px solid var(--ink)}
.tl .pin{position:absolute;left:var(--x);bottom:-7px;width:12px;height:12px;border-radius:50%;background:var(--accent);border:2px solid var(--paper);transform:translateX(-50%)}
.tl .lab{position:absolute;left:var(--x);bottom:10px;transform:translateX(-50%) rotate(-3deg);font:700 17px/1 var(--hand);color:var(--ink-2);white-space:nowrap}
.tl .lab em{font-style:normal;color:var(--ink-3);font-size:14px}
.tl .t0,.tl .t1{position:absolute;bottom:-22px;font:400 11px/1 var(--mono);color:var(--ink-3)}
.tl .t0{left:0}.tl .t1{right:0}
.ep .log{margin-top:30px;font:700 19px/1.1 var(--hand);color:var(--ink-2)}
.board .arrow{width:84px;color:var(--ink);stroke:currentColor;fill:none;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}
.outs{display:flex;justify-content:center;gap:0;padding:18px 0 8px}
.outs .pol{width:clamp(96px,10.5vw,132px)}
.outs .pol:nth-of-type(1){--r:-5deg;margin-right:-12px}
.outs .pol:nth-of-type(2){--r:1deg;margin-bottom:14px;width:clamp(104px,11.5vw,144px)}
.outs .pol:nth-of-type(3){--r:5deg;margin-left:-12px}
@media (prefers-reduced-motion:reduce){.ep .scan{animation:none;left:47%}.pol{transition:none}}
.stages{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:clamp(10px,1.6vw,18px);margin-top:34px;align-items:start}
@media (max-width:980px){.stages{grid-template-columns:repeat(3,minmax(0,1fr))}}
@media (max-width:600px){.stages{grid-template-columns:repeat(2,minmax(0,1fr))}}
.stage{padding:10px 10px 12px;transform:rotate(var(--r,0deg));min-width:0}
.stage:nth-child(2n){--r:.5deg}.stage:nth-child(3n){--r:-.5deg}
.stage .n{font:500 11px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--accent)}
.stage .pic{position:relative;margin-top:8px;overflow:hidden;background:#0b0d12;border:1.5px solid var(--ink)}
.stage .pic.wide{aspect-ratio:16/9}.stage .pic.tall{aspect-ratio:9/16;max-height:240px;margin-inline:auto}
.stage .pic img,.stage .pic video{width:100%;height:100%;object-fit:cover;transition:transform .5s var(--ease)}
@media (hover:hover){.stage:hover .pic img,.stage:hover .pic video{transform:scale(1.04)}}
.stage .pic .box{position:absolute;top:4%;bottom:4%;left:35%;width:30%;border:2px dashed var(--mark)}
.stage .pic .mk{position:absolute;left:0;right:0;bottom:0;height:8px;background:rgba(255,255,255,.18)}
.stage .pic .mk i{position:absolute;left:18%;width:3%;top:0;bottom:0;background:var(--mark)}
.stage .pic .tag{position:absolute;left:6px;top:6px;background:var(--mark);color:#0b0d12;font:700 13px/1 var(--hand);padding:4px 7px}
.stage h3{font-size:19px;margin-top:10px}
.stage p{font-size:13.5px;color:var(--ink-2);margin-top:4px;line-height:1.45}
.stage video{display:block}
.player{display:grid;grid-template-columns:auto minmax(0,1fr);gap:22px;align-items:center;margin-top:30px;padding:16px;max-width:720px}
@media (max-width:560px){.player{grid-template-columns:1fr}}
.player video{width:200px;max-width:100%;aspect-ratio:9/16;background:#0b0d12;border:1.5px solid var(--ink)}
.player h3{font-size:24px}.player p{color:var(--ink-2);font-size:15.5px;margin-top:6px}
.player .hand{margin-top:10px;display:block}

/* ---- Section A: scroll-driven source -> vertical clip (desktop; the stage strip is the static/mobile version) ---- */
.morph{display:none}
@media (min-width:861px) and (prefers-reduced-motion:no-preference){
  .morph{display:block;height:230vh;margin-top:30px;view-timeline-name:--morph;view-timeline-axis:block}
  .stages{display:none}
  .morph{--sw:min(640px,54vw,70vh)}
  .morph .pin{position:sticky;top:max(2vh,calc((100vh - var(--sw)*1.14 - 80px)/2));height:auto;display:grid;grid-template-rows:auto auto;gap:14px}
  .morph .stage{position:relative;height:calc(var(--sw)*1.14);display:grid;place-items:center;overflow:hidden}
  .morph .src{position:relative;width:var(--sw);aspect-ratio:16/9;z-index:2;border:1.5px solid var(--ink);background:#0b0d12;transform-origin:50% 50%;will-change:transform,clip-path}
  .morph .src video{width:100%;height:100%;object-fit:cover}
  .morph .box{position:absolute;top:0;bottom:0;left:35%;width:30%;border:2px dashed var(--mark);box-shadow:0 0 0 999px rgba(0,0,0,0);opacity:0}
  .morph .box span{position:absolute;left:50%;top:8px;transform:translateX(-50%);font:700 15px/1 var(--hand);color:var(--mark)}
  .morph .fin{position:absolute;left:50%;top:50%;height:calc(var(--sw)*1.08);aspect-ratio:9/16;transform:translate(-50%,-50%);border:1.5px solid var(--ink);background:#0b0d12;opacity:0;overflow:hidden;z-index:3}
  .morph .fin video{width:100%;height:100%;object-fit:cover}
  .morph .out{position:absolute;top:50%;width:calc(var(--sw)*.27);transform:translateY(-50%);opacity:0;--r:0deg;z-index:4}
  .morph .out.l{left:calc(50% - var(--sw)*.56)}.morph .out.r{right:calc(50% - var(--sw)*.56)}
  .morph .side{position:absolute;top:50%;width:calc(var(--sw)*.42);aspect-ratio:16/9;border:1.5px solid var(--ink);background:#0b0d12;transform:translateY(-50%) rotate(var(--r));z-index:1;opacity:.9}
  .morph .side video{width:100%;height:100%;object-fit:cover}
  .morph .side.l{left:calc(50% - var(--sw)*.78);--r:-3deg}.morph .side.r{right:calc(50% - var(--sw)*.78);--r:3deg}
  .morph .side .cap{position:absolute;left:8px;bottom:-26px;font:700 16px/1 var(--hand);color:var(--ink-2);white-space:nowrap}
  .morph .side::before{content:"";position:absolute;top:-10px;left:50%;width:64px;height:20px;background:var(--tape);transform:translateX(-50%) rotate(-3deg)}
  .morph .out .pol{margin:0;display:block}
  .morph .tl2{position:relative;height:46px;border:1.5px solid var(--ink);border-radius:var(--wob);background:var(--card);padding:0 14px}
  .morph .tl2 .bar{position:absolute;left:14px;right:14px;top:22px;height:2px;background:var(--rule-soft)}
  .morph .tl2 .fill{position:absolute;left:14px;top:22px;height:2px;width:0;background:var(--accent)}
  .morph .tl2 .mk{position:absolute;top:18px;left:calc(14px + var(--x)*(100% - 28px));width:10px;height:10px;border-radius:50%;background:var(--accent);border:2px solid var(--paper);transform:translateX(-50%)}
  .morph .tl2 .ph{position:absolute;top:8px;bottom:8px;left:14px;width:2px;background:var(--rec)}
  .morph .tl2 .lab{position:absolute;left:14px;top:30px;font:500 10.5px/1 var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--ink-3);opacity:0}
  .morph .tl2 .lab:first-of-type{opacity:1}
  .morph .tl2 .t{position:absolute;right:14px;top:6px;font:400 10px/1 var(--mono);color:var(--ink-3)}
  .morph [data-a]{animation:1s linear both paused;animation-delay:calc(var(--p,0)*-1s)}
  .morph .src{animation-name:m-src}.morph .box{animation-name:m-box}.morph .fin{animation-name:m-fin}
  .morph .out.l{animation-name:m-outl}.morph .out.r{animation-name:m-outr}.morph .side{animation-name:m-side}.morph .fill{animation-name:m-fill}.morph .tl2 .ph{animation-name:m-ph}
  .morph .lab.l1{animation-name:m-l1}.morph .lab.l2{animation-name:m-l2}.morph .lab.l3{animation-name:m-l3}.morph .lab.l4{animation-name:m-l4}.morph .lab.l5{animation-name:m-l5}
  @supports (animation-timeline:view()){
    .morph [data-a]{animation-timeline:--morph;animation-range:cover 27% cover 68%;animation-delay:0s;animation-play-state:running}
  }
}
@keyframes m-src{0%,38%{clip-path:inset(0 0 0 0);transform:scale(1)}58%,100%{clip-path:inset(0 35% 0 35%);transform:scale(1.92)}}
@keyframes m-box{0%{opacity:0;box-shadow:0 0 0 999px rgba(0,0,0,0)}14%{opacity:1;box-shadow:0 0 0 999px rgba(0,0,0,0)}36%{opacity:1;box-shadow:0 0 0 999px rgba(0,0,0,.55)}58%,100%{opacity:0;box-shadow:0 0 0 999px rgba(0,0,0,.55)}}
@keyframes m-fin{0%,58%{opacity:0}72%,100%{opacity:1}}
@keyframes m-side{0%,30%{opacity:.9}46%,100%{opacity:0}}
@keyframes m-outl{0%,76%{opacity:0;transform:translateY(-50%) translateX(60px) rotate(0deg)}100%{opacity:1;transform:translateY(-50%) translateX(0) rotate(-6deg)}}
@keyframes m-outr{0%,80%{opacity:0;transform:translateY(-50%) translateX(-60px) rotate(0deg)}100%{opacity:1;transform:translateY(-50%) translateX(0) rotate(6deg)}}
@keyframes m-fill{from{width:0}to{width:calc(100% - 28px)}}
@keyframes m-ph{from{left:14px}to{left:calc(100% - 14px)}}
@keyframes m-l1{0%,16%{opacity:1}22%,100%{opacity:0}}
@keyframes m-l2{0%,20%{opacity:0}24%,38%{opacity:1}44%,100%{opacity:0}}
@keyframes m-l3{0%,42%{opacity:0}46%,60%{opacity:1}66%,100%{opacity:0}}
@keyframes m-l4{0%,64%{opacity:0}68%,78%{opacity:1}84%,100%{opacity:0}}
@keyframes m-l5{0%,82%{opacity:0}88%,100%{opacity:1}}

/* ---- Section B: moment selection ---- */
.moments{display:grid;grid-template-columns:minmax(0,1.3fr) auto;gap:clamp(18px,3vw,40px);align-items:center;margin-top:34px;padding:22px 24px}
@media (max-width:760px){.moments{grid-template-columns:1fr}}
.moments h3{font-size:24px}
.moments .lead2{color:var(--ink-2);font-size:15.5px;margin-top:6px}
.mtl{position:relative;margin-top:28px;padding:36px 0 26px}
.mtl .track{position:relative;height:2px;background:var(--ink)}
.mtl .mk{position:absolute;left:var(--x);top:50%;transform:translate(-50%,-50%)}
.js .mtl .mk,.js .mtl .dot{opacity:0;transition:opacity var(--t-med) var(--ease-out) var(--d,0s)}
.js .moments.in .mtl .mk,.js .moments.in .mtl .dot{opacity:1}
@media (prefers-reduced-motion:reduce){.js .mtl .mk,.js .mtl .dot{opacity:1;transition:none}}
.mtl .mk button{font:700 16px/1 var(--hand);color:var(--ink-2);background:var(--card);border:1.5px solid var(--rule);border-radius:var(--wob);padding:6px 10px;cursor:pointer;white-space:nowrap;transition:color var(--t-fast),border-color var(--t-fast),transform var(--t-fast) var(--ease)}
.mtl .mk button em{font-style:normal;font:400 11px/1 var(--mono);color:var(--ink-3);margin-left:6px}
.mtl .mk button[aria-pressed="true"]{color:var(--accent);border-color:var(--accent);transform:translateY(-2px)}
.mtl .mk button:hover{border-color:var(--ink)}
.mtl .dot{position:absolute;left:var(--x);top:50%;width:10px;height:10px;border-radius:50%;background:var(--accent);border:2px solid var(--paper);transform:translate(-50%,-50%)}
.mtl .mph{position:absolute;left:var(--x);top:22px;bottom:14px;width:2px;background:var(--rec);transform:translateX(-50%);transition:left var(--t-slow) var(--ease)}
.mtl .tc{display:flex;justify-content:space-between;margin-top:24px;font:400 11px/1 var(--mono);color:var(--ink-3)}
.mprev .pol{--r:2deg;width:168px;margin:0 auto;display:block}
.mprev .pol video{transition:opacity .35s var(--ease)}
.mprev .pol.sw video{opacity:0}
@media (max-width:760px){.mtl .mk button{font-size:14px;padding:5px 7px}.mtl .mk button em{display:none}}
@media (prefers-reduced-motion:reduce){.mtl .mph{transition:none}.mprev .pol video{transition:none}}

/* ---- Section C: before / after ---- */
.cmp{position:relative;width:300px;max-width:100%;aspect-ratio:9/16;margin:30px auto 0;border:1.5px solid var(--ink);overflow:hidden;background:#0b0d12;--c:50%;user-select:none}
.cmp video,.cmp img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.cmp .before{position:absolute;inset:0;clip-path:inset(0 calc(100% - var(--c)) 0 0);background:#0b0d12}
.cmp .before video{width:333.3%;height:auto;max-width:none;left:-116.7%;top:0;right:auto;bottom:auto;aspect-ratio:16/9;filter:brightness(.85)}
.cmp .line{position:absolute;top:0;bottom:0;left:var(--c);width:2px;background:var(--mark);transform:translateX(-50%);pointer-events:none}
.cmp .knob{position:absolute;top:50%;left:var(--c);width:36px;height:36px;border-radius:50%;background:var(--mark);border:1.5px solid #0b0d12;transform:translate(-50%,-50%);display:grid;place-items:center;pointer-events:none;font:700 15px/1 var(--hand);color:#0b0d12}
.cmp input{position:absolute;inset:0;width:100%;height:100%;margin:0;opacity:0;cursor:ew-resize}
.cmp input:focus-visible~.knob{outline:3px solid var(--accent);outline-offset:3px}
.cmp .tag{position:absolute;top:8px;font:500 10px/1 var(--mono);letter-spacing:.12em;text-transform:uppercase;padding:5px 7px;background:rgba(11,13,18,.7);color:#fff;pointer-events:none}
.cmp .tag.l{left:8px}.cmp .tag.r{right:8px}
.cmpwrap{display:grid;grid-template-columns:minmax(0,300px) minmax(0,1fr);gap:clamp(18px,3vw,44px);align-items:center;margin-top:30px}
@media (max-width:640px){.cmpwrap{grid-template-columns:1fr}}
.cmpwrap h3{font-size:24px}.cmpwrap p{color:var(--ink-2);font-size:15.5px;margin-top:8px}
.cmpwrap .hand{display:block;margin-top:12px}

/* ---- Section D: one clip, three feeds ---- */
.dist{display:grid;grid-template-columns:minmax(0,250px) minmax(0,1fr);gap:clamp(20px,4vw,56px);align-items:center;margin-top:30px}
@media (max-width:700px){.dist{grid-template-columns:1fr;justify-items:center}}
.phone{position:relative;width:250px;max-width:100%;aspect-ratio:9/19;border:2px solid var(--ink);border-radius:28px;background:#0b0d12;overflow:hidden;box-shadow:5px 5px 0 var(--rule-soft)}
.phone video{position:absolute;inset:0;width:100%;height:100%;object-fit:contain}
.phone .ui{position:absolute;inset:0;opacity:0;transition:opacity .35s var(--ease);pointer-events:none;color:#fff;font:600 10px/1.3 var(--body)}
.phone[data-p="tiktok"] .ui.tiktok,.phone[data-p="reels"] .ui.reels,.phone[data-p="shorts"] .ui.shorts{opacity:1}
.phone .rail{position:absolute;right:8px;bottom:70px;display:grid;gap:12px;justify-items:center}
.phone .rail i{width:22px;height:22px;border-radius:50%;background:rgba(255,255,255,.85)}
.phone .rail i.sq{border-radius:6px}
.phone .meta{position:absolute;left:10px;right:44px;bottom:16px;text-shadow:0 1px 2px rgba(0,0,0,.7)}
.phone .meta b{display:block;font-weight:800;margin-bottom:4px}
.phone .meta .pill{display:inline-block;margin-left:6px;padding:2px 7px;border:1px solid #fff;border-radius:4px;font-weight:700;font-size:9px}
.phone .top{position:absolute;left:0;right:0;top:12px;text-align:center;font-weight:700;letter-spacing:.04em;opacity:.9}
.phone .ui.shorts .top{text-align:left;left:12px}
.phone .ui.tiktok .top span{margin:0 8px;opacity:.6}.phone .ui.tiktok .top span.on{opacity:1;border-bottom:2px solid #fff;padding-bottom:3px}
.phone .ui.reels .meta b::before{content:"";display:inline-block;width:18px;height:18px;border-radius:50%;background:#fff;vertical-align:middle;margin-right:6px}
.phone .ui.shorts .meta .pill{background:#fff;color:#0b0d12;border-color:#fff}
.dist .tabs{display:inline-flex;gap:6px;border:1.5px solid var(--ink);border-radius:var(--wob);padding:4px;margin-top:18px}
.dist .tabs button{font:600 14px/1 var(--body);padding:8px 14px;border:0;background:transparent;color:var(--ink-2);cursor:pointer;border-radius:var(--wob);transition:background-color var(--t-fast),color var(--t-fast)}
.dist .tabs button[aria-selected="true"]{background:var(--ink);color:var(--paper)}
.dist h3{font-size:26px}.dist p{color:var(--ink-2);font-size:16px;margin-top:8px;max-width:48ch}
.dist .hand{display:block;margin-top:14px}

/* ---- process diagram ---- */
.proc{margin-top:30px}
.proc svg{width:100%;height:auto;display:block}
@media (max-width:700px){.proc svg{display:none}}
.proc .n{fill:var(--card);stroke:var(--ink);stroke-width:1.6}
.proc .n.ac{fill:var(--accent-soft);stroke:var(--accent)}
.proc .ar{fill:none;stroke:var(--ink);stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.proc .ar.ac{stroke:var(--accent)}
.proc .bm{fill:none;stroke-width:3;stroke-linecap:round}
@media (prefers-reduced-motion:reduce){.proc .bm{display:none}}
.proc .t{font:400 22px var(--serif);fill:var(--ink)}
.proc .t.i{font-style:italic}
.proc .m{font:500 11px var(--mono);fill:var(--ink-3);letter-spacing:.1em}
.proc .h{font:700 18px var(--hand);fill:var(--ink-2)}
.proc .h.ac{fill:var(--accent)}
.steps{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(14px,2.4vw,28px);margin-top:22px}
@media (max-width:760px){.steps{grid-template-columns:1fr}}
.step{padding:18px 20px 20px;position:relative;transform:rotate(var(--r,0deg))}
.step:nth-child(2){--r:.5deg}.step:nth-child(3){--r:-.4deg}
.step .n{font:500 11px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--accent)}
.step h3{margin-top:8px}
.step p{color:var(--ink-2);margin-top:8px;font-size:16px}

/* ---- proof ---- */
.proof{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(14px,2.4vw,28px);margin-top:26px}
@media (max-width:760px){.proof{grid-template-columns:1fr}}
.stat{padding:22px 22px 20px;transform:rotate(var(--r,0deg))}
.stat:nth-child(1){--r:-.7deg}.stat:nth-child(3){--r:.6deg}
.stat .v{font:400 clamp(52px,6vw,74px)/1 var(--serif);letter-spacing:-.02em;font-variant-numeric:tabular-nums}
.stat .v small{font-size:.5em;font-style:italic}
.stat .l{margin-top:10px;color:var(--ink-2);font-size:15.5px}
.best{margin-top:22px;padding:22px 24px;display:grid;grid-template-columns:minmax(0,1fr) auto;gap:18px 32px;align-items:center;position:relative;background:var(--accent-soft);border-color:var(--accent)}
@media (max-width:640px){.best{grid-template-columns:1fr}}
.best .k{font:500 11px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--accent)}
.best p{margin-top:8px;font-size:17px}
.best .nums{display:flex;gap:28px}
.best .nums .v{font:400 clamp(40px,4.4vw,58px)/1 var(--serif)}
.best .nums .l{font:500 12px/1.4 var(--mono);color:var(--ink-3);margin-top:6px}
.best .note{position:absolute;right:18px;top:-18px;transform:rotate(3deg)}

/* ---- checklist ---- */
.list{list-style:none;margin:22px 0 0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px 28px;max-width:960px}
@media (max-width:700px){.list{grid-template-columns:1fr}}
.list li{display:flex;gap:12px;align-items:flex-start;padding:10px 0;border-bottom:1px dashed var(--rule-soft);font-size:16.5px}
.list li svg{flex:none;width:22px;height:22px;margin-top:2px;stroke:var(--good);fill:none;stroke-width:3;stroke-linecap:round;stroke-linejoin:round}
.inc{display:grid;grid-template-columns:minmax(0,1fr) 380px;gap:clamp(20px,4vw,56px);align-items:start}
@media (max-width:900px){.inc{grid-template-columns:1fr}}
.inc .list{grid-template-columns:1fr;max-width:none;margin-top:22px}
.anat{position:relative;margin:30px auto 0;width:min(100%,380px);padding:14px 0 0}
.anat .pol{--r:1.5deg;width:170px;margin:0 auto;display:block}
.anat .pol .scr img{width:100%;height:100%;object-fit:cover}
.anat .call{position:absolute;z-index:2;font:700 17px/1.1 var(--hand);color:var(--accent);max-width:104px;white-space:normal}
.anat .call svg{position:absolute;width:40px;height:28px;stroke:var(--accent);fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.anat .c1{left:0;top:30px}.anat .c1 svg{left:100%;top:2px}
.anat .c2{right:0;top:44%;text-align:right}.anat .c2 svg{right:100%;top:-6px;transform:scaleX(-1)}
.anat .c3{left:0;bottom:70px}.anat .c3 svg{left:100%;top:-20px}
.anat .fig{text-align:center;max-width:none}
@media (max-width:400px){.anat .call{font-size:15px;max-width:84px}.anat .pol{width:150px}}

/* ---- pricing ---- */
.plans{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:clamp(12px,2vw,22px);margin-top:28px;align-items:start}
@media (max-width:980px){.plans{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:560px){.plans{grid-template-columns:1fr}}
.plan{padding:20px 20px 22px;position:relative;transform:rotate(var(--r,0deg));display:flex;flex-direction:column;min-height:100%}
.plan:nth-child(1){--r:-.5deg}.plan:nth-child(3){--r:.6deg}
.plan h3{font-size:30px;position:relative;display:inline-block;align-self:flex-start}
.plan .price{font:400 34px/1 var(--serif);margin-top:12px;letter-spacing:-.01em}
.plan .price small{display:block;font:400 13px/1.5 var(--mono);color:var(--ink-3);margin-top:6px}
.plan ul{list-style:none;padding:0;margin:16px 0 20px;color:var(--ink-2);font-size:15px;flex:1}
.plan li{padding:7px 0;border-top:1px dashed var(--rule-soft)}
.plan li::before{content:"—";color:var(--ink-3);margin-right:8px}
.plan .btn{align-self:flex-start;width:100%;justify-content:center;white-space:normal;text-align:center}
.plan{transition:transform var(--t-fast) var(--ease),box-shadow var(--t-fast) var(--ease)}
@media (hover:hover){.plan:hover{transform:translate(-2px,-2px) rotate(0deg);box-shadow:4px 4px 0 var(--rule)}.plan.pick:hover{box-shadow:6px 6px 0 var(--accent)}}
.plan.pick{border-color:var(--accent);box-shadow:4px 4px 0 var(--accent)}
.beam{position:absolute;inset:-1.5px;border-radius:inherit;pointer-events:none;border:1.5px solid transparent;display:none;overflow:hidden;
  -webkit-mask:linear-gradient(transparent,transparent),linear-gradient(#000,#000);mask:linear-gradient(transparent,transparent),linear-gradient(#000,#000);
  -webkit-mask-clip:padding-box,border-box;mask-clip:padding-box,border-box;-webkit-mask-composite:xor;mask-composite:intersect}
.beam i{position:absolute;width:90px;aspect-ratio:1;background:linear-gradient(to left,var(--accent),var(--mark),transparent);offset-path:rect(0 auto auto 0 round 90px);offset-anchor:50% 50%;animation:beam 7s linear infinite}
@keyframes beam{from{offset-distance:0%}to{offset-distance:100%}}
@supports (offset-path:rect(0 auto auto 0 round 90px)){.beam{display:block}}
@media (prefers-reduced-motion:reduce){.beam{display:none}}
.plan .tag{position:absolute;right:14px;top:-14px;transform:rotate(3deg);background:var(--mark);color:#0b0d12;font:700 17px/1 var(--hand);padding:7px 12px;border-radius:var(--wob2);border:1.5px solid #0b0d12}
.plan.custom{background:var(--mark);color:#0b0d12;border-color:#0b0d12;transform:rotate(1.2deg)}
.plan.custom .price,.plan.custom ul,.plan.custom li::before,.plan.custom .price small{color:#0b0d12}
.plan.custom .btn{background:#0b0d12;color:#fff;border-color:#0b0d12}
.plan.custom .btn:hover{box-shadow:3px 3px 0 #0b0d12}
.plan.custom::before{content:"";position:absolute;top:-11px;left:50%;width:78px;height:22px;background:rgba(11,13,18,.12);transform:translateX(-50%) rotate(-2deg)}

/* month calendar */
.month{margin-top:30px;padding:22px 22px 20px}
.month-head{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;gap:14px}
.month-head h3{font-size:30px}
.month-head p{color:var(--ink-2);margin-top:6px;font-size:15.5px}
.seg{display:inline-flex;gap:6px;border:1.5px solid var(--ink);border-radius:var(--wob);padding:4px}
.seg button{font:600 14px/1 var(--body);padding:8px 14px;border:0;background:transparent;color:var(--ink-2);cursor:pointer;border-radius:var(--wob);transition:background-color .2s,color .2s}
.seg button[aria-pressed="true"]{background:var(--ink);color:var(--paper)}
.days{display:grid;grid-template-columns:repeat(10,minmax(0,1fr));gap:6px;margin-top:20px}
@media (max-width:560px){.days{grid-template-columns:repeat(6,minmax(0,1fr))}}
.days i{display:grid;place-items:center;aspect-ratio:1.45;border:1px solid var(--rule);font:700 18px/1 var(--hand);color:var(--accent);font-style:normal;position:relative;background:var(--card)}
.days i::before{content:attr(data-d);position:absolute;left:4px;top:2px;font:400 9px/1 var(--mono);color:var(--ink-3)}
.days.files i{color:var(--ink-2);border-style:dashed}
.month-foot{display:flex;flex-wrap:wrap;justify-content:space-between;gap:14px;align-items:flex-end;margin-top:18px}
.month-foot .total{font:400 44px/1 var(--serif)}
.month-foot .tl2{font:500 12px/1.4 var(--mono);color:var(--ink-3);margin-top:4px}
.month-foot .key{display:flex;gap:18px;font:500 12px/1.4 var(--mono);color:var(--ink-3)}
.month-foot .key i{display:inline-block;width:14px;height:14px;border:1px solid var(--rule);vertical-align:-2px;margin-right:6px;background:var(--card)}
.month-foot .key i.o{border-style:dashed}
.founding{margin-top:18px;display:inline-block;transform:rotate(-1deg)}

/* ---- trial / form ---- */
.trial{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:clamp(22px,4vw,56px);align-items:start;margin-top:10px}
@media (max-width:860px){.trial{grid-template-columns:1fr}}
.trial h2{font-size:clamp(34px,4.4vw,54px)}
.trial .lead{margin-top:16px}
.mini{list-style:none;padding:0;margin:22px 0 0;display:grid;gap:10px;font-size:16.5px}
.mini li{display:flex;gap:12px;align-items:baseline}
.mini b{font:700 22px/1 var(--hand);color:var(--accent);min-width:22px}
.altc{margin-top:22px;display:flex;flex-wrap:wrap;gap:10px 14px;align-items:center;color:var(--ink-2);font-size:15px}
.card{padding:clamp(18px,2.6vw,28px);position:relative;transform:rotate(.4deg);background:var(--card)}
.card::before{content:"";position:absolute;top:-12px;left:34px;width:92px;height:26px;background:var(--tape);transform:rotate(-3deg)}
.card::after{content:"";position:absolute;top:-12px;right:40px;width:70px;height:26px;background:var(--tape);transform:rotate(4deg)}
.card.flash{animation:flash .7s}
@keyframes flash{0%{box-shadow:0 0 0 0 var(--accent)}100%{box-shadow:0 0 0 12px transparent}}
.fld{margin-top:14px}
.fld label{display:block;font:700 19px/1.2 var(--hand);color:var(--ink);margin-bottom:6px}
.fld label small{font:400 12.5px/1.4 var(--mono);color:var(--ink-3);margin-left:8px}
.fld input,.fld textarea{width:100%;font:400 16px/1.4 var(--body);color:var(--ink);background:transparent;border:0;border-bottom:1.5px solid var(--ink);padding:8px 2px;border-radius:0;outline:0;transition:border-color .2s}
.fld textarea{resize:vertical;min-height:84px;border:1.5px solid var(--ink);border-radius:var(--wob2);padding:10px 12px}
.fld input:focus,.fld textarea:focus{border-color:var(--accent);box-shadow:0 2px 0 var(--accent)}
.fld textarea:focus{box-shadow:none}
.fld.bad input,.fld.bad textarea{border-color:var(--rec)}
.fld .err{display:block;font:700 15px/1.3 var(--hand);color:var(--rec);min-height:0;margin-top:4px}
.row{display:grid;grid-template-columns:1fr 1fr;gap:0 18px}
@media (max-width:520px){.row{grid-template-columns:1fr}}
.plan-chip{display:inline-flex;align-items:center;gap:8px;margin-top:14px;font:500 12.5px/1 var(--mono);color:var(--accent);background:var(--accent-soft);border:1px solid var(--accent);padding:7px 10px;border-radius:var(--wob)}
.plan-chip button{border:0;background:transparent;color:inherit;font:inherit;font-size:16px;cursor:pointer;padding:0 2px;line-height:1}
.hp{position:absolute;left:-9999px;top:auto;width:1px;height:1px;overflow:hidden}
.status{font:700 16px/1.3 var(--hand);color:var(--rec);margin-top:12px;min-height:0}
.send{margin-top:18px;width:100%;justify-content:center;position:relative}
.sending .send{opacity:.65;pointer-events:none}
.fine{margin-top:12px;font:400 12.5px/1.5 var(--mono);color:var(--ink-3)}
.done{text-align:left;padding:12px 4px}
.done .tick{width:54px;height:54px;border:1.5px solid var(--good);border-radius:var(--wob);display:grid;place-items:center;color:var(--good);transform:rotate(-4deg)}
.done .tick svg{width:28px;height:28px;stroke:currentColor;fill:none;stroke-width:3;stroke-linecap:round;stroke-linejoin:round}
.done h3{margin-top:16px;font-size:32px}
.done p{color:var(--ink-2);margin-top:8px}
.done .btn{margin-top:18px}

/* ---- faq ---- */
.faq{margin-top:20px;max-width:820px}
.faq details{border-top:1.5px solid var(--rule-soft);padding:4px 0}
.faq details:last-child{border-bottom:1.5px solid var(--rule-soft)}
.faq summary{cursor:pointer;list-style:none;display:flex;gap:14px;align-items:baseline;padding:14px 0;font:400 22px/1.25 var(--serif)}
.faq summary::-webkit-details-marker{display:none}
.faq summary::before{content:"+";font:700 26px/1 var(--hand);color:var(--accent);flex:none;width:18px;transition:transform .2s}
.faq details[open] summary::before{content:"–"}
.faq p{padding:0 0 18px 32px;color:var(--ink-2);max-width:66ch}
.faq details[open] p{animation:dfade var(--t-med) var(--ease-out)}
@keyframes dfade{from{opacity:0;transform:translateY(-4px)}to{opacity:1;transform:none}}

/* ---- why cards (niche pages) ---- */
.why{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(14px,2.4vw,28px);margin-top:26px}
@media (max-width:760px){.why{grid-template-columns:1fr}}
.why .wcard{padding:20px 20px 22px;transform:rotate(var(--r,0deg));position:relative}
.why .wcard:nth-child(1){--r:-.6deg}.why .wcard:nth-child(3){--r:.7deg}
.why .wcard .n{font:700 24px/1 var(--hand);color:var(--accent)}
.why .wcard h3{margin-top:10px;font-size:25px}
.why .wcard p{margin-top:8px;color:var(--ink-2);font-size:16px}

/* ---- editing example ---- */
.edit-ex{padding:14px;transform:rotate(-.5deg)}
.edit-ex .frame{position:relative;aspect-ratio:16/9;overflow:hidden;border:1.5px solid var(--ink);background:#0b0d12}
.edit-ex video{width:100%;height:100%;object-fit:cover;filter:grayscale(.9) brightness(.72) contrast(.8);transition:filter .9s}
.edit-ex[data-step="grade"] video{filter:none}
.edit-ex .hook{position:absolute;top:8%;left:50%;transform:translateX(-50%);background:#fff;color:#0b0d12;font:800 clamp(11px,1.4vw,15px)/1.15 var(--body);padding:7px 11px;border-radius:6px;opacity:0;transition:opacity .4s;white-space:normal;width:max-content;max-width:78%;text-align:center;text-wrap:balance}
.edit-ex .words{position:absolute;left:0;right:0;bottom:7%;text-align:center;font:800 clamp(13px,1.6vw,20px)/1.15 var(--body);color:#fff;text-shadow:0 2px 0 #000,0 0 14px rgba(0,0,0,.7);padding:0 8%;opacity:0;transition:opacity .3s}
.edit-ex .words .k{color:var(--mark)}
.edit-ex[data-step="cap"] .hook,.edit-ex[data-step="grade"] .hook,.edit-ex[data-step="cap"] .words,.edit-ex[data-step="grade"] .words{opacity:1}
.edit-ex .tape-l{position:absolute;left:4%;top:-12px;width:80px;height:24px;background:var(--tape);transform:rotate(-5deg)}
.edit-ex .foot{display:flex;flex-wrap:wrap;justify-content:space-between;gap:10px;align-items:center;margin-top:12px}
.edit-ex .st{display:flex;gap:6px;flex-wrap:wrap}
.edit-ex .st button{font:600 13px/1 var(--body);padding:8px 11px;border:1.5px solid var(--ink);background:transparent;color:var(--ink-2);cursor:pointer;border-radius:var(--wob)}
.edit-ex .st button[aria-pressed="true"]{background:var(--ink);color:var(--paper)}
.edit-ex .rt{font:500 12px/1 var(--mono);color:var(--ink-3)}
.edit-ex .rt b{color:var(--ink);font-weight:500}
.quote-note{margin-top:18px;padding:16px 18px;color:var(--ink-2);max-width:62ch;transform:rotate(-.4deg)}
.quote-note b{color:var(--ink)}
.svcs{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(14px,2.4vw,28px);margin-top:26px}
@media (max-width:760px){.svcs{grid-template-columns:1fr}}

/* ---- footer ---- */
footer{margin-top:clamp(64px,9vw,120px);padding:28px 0 40px;border-top:2px dashed var(--rule);display:grid;gap:14px;font-size:14.5px;color:var(--ink-2)}
footer .sheet{font:500 12px/1 var(--mono);letter-spacing:.12em;text-transform:uppercase;color:var(--ink-3)}
footer .flinks{display:flex;flex-wrap:wrap;gap:6px 18px}
footer .flinks a{color:var(--ink-2);text-decoration:none;border-bottom:1.5px solid var(--rule)}
footer .flinks a:hover{color:var(--ink);border-color:var(--accent)}
footer .by{font:700 20px/1.1 var(--hand);color:var(--ink-2)}
footer .fnote{font-size:13px;color:var(--ink-3);max-width:80ch;line-height:1.55}

/* ---- reveal ---- */
.js .rv{opacity:0;transform:translateY(6px);filter:blur(6px);transition:opacity var(--t-med) var(--ease-out) var(--d,0s),transform var(--t-med) var(--ease-out) var(--d,0s),filter var(--t-med) var(--ease-out) var(--d,0s)}
.js .rv.x{transform:translateX(-10px)}.js .rv.x.in{transform:none}
.js .rv.in{opacity:1;transform:none;filter:none}
.js.loaded .hero .rv{transition-duration:.6s}
@media (prefers-reduced-motion:reduce){.js .rv{opacity:1;transform:none;filter:none;transition:none}}
/* hand-drawn underline draws itself on load */
.js em.ul path{stroke-dasharray:420;stroke-dashoffset:420;transition:stroke-dashoffset 1s cubic-bezier(.3,.9,.3,1) .5s}
.js.loaded em.ul path{stroke-dashoffset:0}
@media (prefers-reduced-motion:reduce){.js em.ul path{stroke-dashoffset:0;transition:none}}

@media (prefers-reduced-motion:reduce){.faq details[open] p,.svc.open{animation:none}.plan,.stage .pic img,.stage .pic video,.phone .ui{transition:none}}

/* ---- 404 ---- */
.nf{padding:clamp(40px,8vw,100px) 0}
.nf .links{display:flex;flex-wrap:wrap;gap:10px;margin-top:24px}
""".replace("GRAIN", GRAIN).replace("DARK", DARK)
