const { chromium } = require('playwright');
/* Browser QA for the generated site. Needs: npm i playwright (once), a local server on the repo root
   (python3 -m http.server 8765), then: node tools/qa/qa.js
   Checks every page at 7 widths for horizontal overflow, console errors, failed requests, heading order,
   dead anchors, unlabeled fields and nameless buttons; then the mobile menu (keyboard), the form
   (validation, mocked failure, mocked success), reduced motion, no-JS, dark mode and the number tickers. */
const BASE = process.env.BASE || 'http://127.0.0.1:8765/';
const pages = ['index.html','podcast-clipping/','stream-clipping/','youtube-clipping/','video-editing/','404.html'];
const widths = [320,375,430,768,1024,1440,1920];
(async () => {
  const b = await chromium.launch({ ...(process.env.CHROME ? { executablePath: process.env.CHROME } : {}) });
  let fails = 0;
  // 1. overflow + console errors + heading order, every page, every width
  for (const f of pages) for (const w of widths) {
    const p = await b.newPage({ viewport: { width: w, height: 900 } });
    const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type()==='error') errs.push(m.text()); });
    p.on('requestfailed', r => { if(!(/\.mp4$/.test(r.url()) && r.failure().errorText==='net::ERR_ABORTED')) errs.push('REQ ' + r.url()); });
    await p.goto(BASE + f);
    await p.evaluate(async()=>{document.querySelectorAll('.rv').forEach(e=>e.classList.add('in'));await document.fonts.ready});
    await p.waitForTimeout(400);
    const r = await p.evaluate(() => {
      const hs=[...document.querySelectorAll('h1,h2,h3')].map(h=>+h.tagName[1]); let bad=false; for(let i=1;i<hs.length;i++) if(hs[i]>hs[i-1]+1) bad=true;
      const links=[...document.querySelectorAll('a[href^="#"]')].map(a=>a.getAttribute('href')).filter(h=>h.length>1&&!document.querySelector(h));
      const unl=[...document.querySelectorAll('input,textarea')].filter(i=>i.type!=='hidden'&&!i.getAttribute('aria-label')&&!document.querySelector('label[for="'+i.id+'"]')).map(i=>i.id||i.type);
      const noname=[...document.querySelectorAll('button')].filter(b=>!b.textContent.trim()&&!b.getAttribute('aria-label')).length;
      return {sw:document.documentElement.scrollWidth, W:document.documentElement.clientWidth, h1:document.querySelectorAll('h1').length, badH:bad, deadAnchors:links, unlabeled:unl, noname};
    });
    const ok = r.sw<=r.W && !errs.length && r.h1===1 && !r.badH && !r.deadAnchors.length && !r.unlabeled.length && !r.noname;
    if(!ok){fails++; console.log('FAIL', f, w, JSON.stringify(r), errs.join('|'));}
    await p.close();
  }
  console.log('matrix done, failures:', fails);
  // 2. mobile menu keyboard
  {
    const p = await b.newPage({ viewport: { width: 375, height: 800 } });
    await p.goto('http://127.0.0.1:8765/index.html');
    const vis0 = await p.locator('#menu').isVisible();
    await p.locator('.menu-btn').click();
    const vis1 = await p.locator('#menu').isVisible();
    const exp = await p.locator('.menu-btn').getAttribute('aria-expanded');
    await p.keyboard.press('Escape');
    const vis2 = await p.locator('#menu').isVisible();
    const focused = await p.evaluate(()=>document.activeElement.className);
    await p.locator('.menu-btn').focus(); await p.keyboard.press('Enter'); await p.keyboard.press('Tab');
    const tabbed = await p.evaluate(()=>document.activeElement.textContent);
    console.log('menu: closed', !vis0, 'opens', vis1, exp, 'esc closes', !vis2, 'focus back', focused, 'tab into menu ->', tabbed);
    await p.close();
  }
  // 3. form: validation, mocked success, mocked failure, honeypot, double submit
  for (const [f,label] of [['index.html','clips'],['video-editing/','quote']]) {
    const p = await b.newPage({ viewport: { width: 1024, height: 900 } });
    let posts = 0, mode = 'ok';
    await p.route('https://formsubmit.co/**', route => { posts++; if (mode==='ok') route.fulfill({status:200, contentType:'application/json', body:'{"success":"true"}'}); else route.fulfill({status:500, body:'x'}); });
    await p.goto(BASE + f);
    await p.locator('#lf .send').click();
    const e1 = await p.locator('#f-channel .err').textContent(); const e2 = await p.locator('#f-email .err').textContent();
    await p.fill('#channel','not a link'); await p.fill('#email','bad'); await p.locator('#lf .send').click();
    const e3 = await p.locator('#f-channel .err').textContent(); const e4 = await p.locator('#f-email .err').textContent();
    await p.fill('#channel','youtube.com/@test'); await p.fill('#email','test@example.com'); await p.fill('#name','Test Person');
    mode='fail'; await p.locator('#lf .send').click(); await p.waitForTimeout(400);
    const failMsg = await p.locator('#lfStatus').textContent(); const doneHidden1 = await p.locator('#lfDone').isHidden();
    mode='ok'; await p.locator('#lf .send').click(); await p.locator('#lf .send').click({force:true}).catch(()=>{}); await p.waitForTimeout(500);
    const done = await p.locator('#doneTitle').textContent(); const doneText = await p.locator('#doneText').textContent();
    console.log(label, '| empty:', !!e1, !!e2, '| invalid:', !!e3, !!e4, '| failure shown:', failMsg.slice(0,40), 'done hidden', doneHidden1, '| success:', done, '/', doneText.slice(0,60), '| posts:', posts);
    await p.close();
  }
  // 3b. interactive demos: moments, compare, feeds, sticky scene end state
  {
    const p = await b.newPage({ viewport: { width: 1280, height: 800 } });
    await p.goto(BASE + 'index.html');
    await p.locator('#moments button[data-v="d3v"]').click(); await p.waitForTimeout(500);
    const mo = await p.evaluate(()=>({pressed:document.querySelector('#moments button[data-v="d3v"]').getAttribute('aria-pressed'), src:(document.querySelector('#moments .mprev source')||{}).getAttribute('src'), cap:document.querySelector('#moments .cap').textContent, ph:document.querySelector('#moments .mph').style.getPropertyValue('--x')}));
    await p.locator('#cmp input').focus(); await p.keyboard.press('ArrowRight'); await p.keyboard.press('ArrowRight');
    const cv = await p.evaluate(()=>document.getElementById('cmp').style.getPropertyValue('--c'));
    await p.locator('.dist [role=tab]').first().focus(); await p.keyboard.press('ArrowRight');
    const fd = await p.evaluate(()=>({p:document.querySelector('.phone').dataset.p, sel:[...document.querySelectorAll('.dist [role=tab]')].map(t=>t.getAttribute('aria-selected')).join(',')}));
    await p.evaluate(()=>{const m=document.querySelector('.morph');scrollTo(0,m.getBoundingClientRect().top+scrollY+m.offsetHeight-innerHeight-10)}); await p.waitForTimeout(400);
    const end = await p.evaluate(()=>({fin:getComputedStyle(document.querySelector('.morph .fin')).opacity, outl:getComputedStyle(document.querySelector('.morph .out.l')).opacity, label:getComputedStyle(document.querySelector('.morph .lab.l5')).opacity}));
    console.log('moments:', JSON.stringify(mo), '| compare --c:', cv, '| feeds:', JSON.stringify(fd), '| scene end:', JSON.stringify(end));
    await p.close();
  }
  // 4. reduced motion: content visible, no autoplay, counters final
  {
    const ctx = await b.newContext({ reducedMotion: 'reduce', viewport:{width:1280,height:900} });
    const p = await ctx.newPage(); await p.goto('http://127.0.0.1:8765/index.html'); await p.waitForTimeout(800);
    const r = await p.evaluate(()=>({hidden:[...document.querySelectorAll('.rv')].filter(e=>getComputedStyle(e).opacity!=='1').length, playing:[...document.querySelectorAll('video')].filter(v=>!v.paused).length, counter:document.querySelector('[data-count]').textContent}));
    console.log('reduced motion:', JSON.stringify(r));
    await ctx.close();
  }
  // 5. no-JS: everything visible
  {
    const ctx = await b.newContext({ javaScriptEnabled: false, viewport:{width:1280,height:900} });
    const p = await ctx.newPage(); await p.goto('http://127.0.0.1:8765/index.html');
    const r = await p.evaluate(()=>({hidden:[...document.querySelectorAll('.rv')].filter(e=>getComputedStyle(e).opacity!=='1').length, ticker:document.querySelector('[data-count]').textContent}));
    console.log('no-js:', JSON.stringify(r));
    await ctx.close();
  }
  // 6. ticker + dark mode sanity
  {
    const ctx = await b.newContext({ colorScheme:'dark', viewport:{width:1280,height:900} });
    const p = await ctx.newPage(); await p.goto('http://127.0.0.1:8765/index.html');
    await p.locator('#proof').scrollIntoViewIfNeeded(); await p.waitForTimeout(2200);
    const r = await p.evaluate(()=>({bg:getComputedStyle(document.body).backgroundColor, ink:getComputedStyle(document.body).color, counters:[...document.querySelectorAll('[data-count]')].map(c=>c.textContent).join(',')}));
    console.log('dark+ticker:', JSON.stringify(r));
    await ctx.close();
  }
  await b.close();
})();
