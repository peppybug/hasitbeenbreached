/* Search runs entirely in the browser over data/breaches.json. Nothing typed here is sent anywhere. */
(function () {
  var $ = function (id) { return document.getElementById(id); };
  var form = $('search'), q = $('q'), note = $('searched'), out = $('results'), browse = $('browse'), count = $('count');
  var M = ['January','February','March','April','May','June','July','August','September','October','November','December'];
  var DB = null, ready;

  function el(t, c, x) { var e = document.createElement(t); if (c) e.className = c; if (x != null) e.textContent = x; return e; }
  function msg(t) { note.hidden = !t; note.textContent = t || ''; }
  function fmt(d) { var p = String(d).split('-'); return p.length === 1 ? p[0] : M[+p[1] - 1] + ' ' + p[0]; }
  function norm(s) {
    return String(s || '').toLowerCase().normalize('NFKD').replace(/[̀-ͯ]/g, '')
      .replace(/^https?:\/\//, '').replace(/^www\./, '').replace(/[^a-z0-9]+/g, ' ').trim();
  }
  /* Same rule as slug() in tools/build_pages.py, which builds company/<slug>.html. */
  function slug(s) { return String(s).normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, ''); }
  function keys(c) { return [c.name, c.website, c.website.replace(/\.[a-z.]+$/, '')].concat(c.aliases).map(norm); }

  function find(term) {
    var t = norm(term); if (t.length < 2) return [];
    var tight = t.replace(/ /g, '');
    return DB.companies.map(function (c) {
      var best = 0;
      keys(c).forEach(function (k) {
        var kt = k.replace(/ /g, '');
        if (k === t || kt === tight) best = Math.max(best, 3);
        else if (k.indexOf(t) === 0 || kt.indexOf(tight) === 0) best = Math.max(best, 2);
        else if (tight.length > 2 && (k.indexOf(t) > -1 || kt.indexOf(tight) > -1)) best = Math.max(best, 1);
      });
      return { c: c, s: best };
    }).filter(function (r) { return r.s > 0; })
      .sort(function (a, b) { return b.s - a.s || a.c.name.localeCompare(b.c.name); })
      /* keep only the best tier: an exact match hides partial ones, a prefix match hides mid-word ones */
      .filter(function (r, i, all) { return r.s === all[0].s; })
      .map(function (r) { return r.c; });
  }

  /* How risky each type of exposed data is for the people affected. Not colour alone: tags are sorted, labelled and explained in a legend. */
  var HIGH = /social security|insurance number|citizen service|bsn|passport|licen[cs]e|id number|id document|government id|payment card|card number|security code|cvv|bank account|brokerage account|password|passcode|puk code|authentication key|session token|private key|certificate key|security question|health|medicare|medical|claims|test result|genetic|ancestry|ethnicity|income|credit|criminal|sexual|camera video|camera stream|login|salary|home access|resident registration|clinical|payment information/i;
  var MED = /date of birth|dates of birth|home address|billing address|shipping address|phone|location|family tree|expiry|booking|stay|order|contact details|ip address|household|demographic|employment|call and text|emails and attachments|customer service|support messages|account balance|transaction|portfolio|payout|sim card|banking|delivery address|direct message|private message|mortgage/i;
  var PARTIAL = /masked|partial|last four/i;
  function sev(cat) { if ((PARTIAL.test(cat) && !/social security/i.test(cat)) || /sim card number/i.test(cat)) return 'med'; return HIGH.test(cat) ? 'high' : MED.test(cat) ? 'med' : 'low'; }
  var SEV_LABEL = { high: 'High risk', med: 'Medium risk', low: 'Lower risk' };
  var SEV_ORDER = { high: 0, med: 1, low: 2 };

  /* ---------- track record helpers ---------- */
  function ym(s) { var p = String(s || '').split('-'); return { y: +p[0], m: p[1] ? +p[1] : null }; }
  /* How long between the breach and the company making it known. Precision follows the data: months when both dates have them, otherwise years. */
  function lag(b) {
    if (!b.disclosed || !b.date || b.timing_unclear) return null;
    var a = ym(b.date), z = ym(b.disclosed), months, text;
    if (a.m && z.m) {
      months = (z.y - a.y) * 12 + (z.m - a.m);
      if (months <= 0) text = 'the same month';
      else if (months === 1) text = 'about 1 month later';
      else if (months < 12) text = 'about ' + months + ' months later';
      else if (months < 18) text = 'over a year later';
      else text = 'about ' + Math.round(months / 12) + ' years later';
    } else {
      var years = z.y - a.y; months = years * 12;
      text = years <= 0 ? 'the same year' : years === 1 ? 'about a year later' : 'about ' + years + ' years later';
    }
    return { months: months, text: text, yearly: !(a.m && z.m), bucket: months <= 2 ? 'fast' : months < 12 ? 'mid' : 'slow' };
  }
  function lagShort(l) { return l.months <= 0 ? (l.yearly ? 'Same year' : 'Same month') : l.months < 12 ? (l.months === 1 ? '1 month' : l.months + ' months') : (Math.round(l.months / 12) === 1 ? 'About a year' : 'About ' + Math.round(l.months / 12) + ' years'); }
  var KIND = { fine: 'fine', settlement: 'settlement', court: 'court case', investigation: 'investigation', order: 'regulator order' };

  function track(c) {
    var box = el('section', 'track');
    box.setAttribute('aria-label', 'Track record for ' + c.name);
    var head = el('div', 'track-head');
    head.appendChild(el('h4', 0, 'Track record'));
    head.appendChild(el('p', 'track-note', 'A summary of the records below. Not a security rating.'));
    box.appendChild(head);
    var grid = el('div', 'track-grid');
    function stat(label, value, sub, cls) {
      var s = el('div', 'tstat' + (cls ? ' ' + cls : '')); s.appendChild(el('p', 'tl', label));
      s.appendChild(el('p', 'tv', value)); if (sub) s.appendChild(el('p', 'ts', sub)); grid.appendChild(s);
    }
    var n = c.breaches.length, years = c.breaches.map(function (b) { return ym(b.date).y; }).sort();
    stat('Breaches on record', String(n), n ? (years[0] === years[n - 1] ? 'In ' + years[0] : years[0] + ' to ' + years[n - 1]) : '');
    var lags = c.breaches.map(lag).filter(Boolean).sort(function (x, y) { return y.months - x.months; });
    if (lags.length) {
      var worst = lags[0];
      stat(n > 1 ? 'Longest time to make it known' : 'Time to make it known', lagShort(worst), 'after the breach began', 'lag-' + worst.bucket);
    } else stat('Time to make it known', 'Unknown', '');
    var outs = []; c.breaches.forEach(function (b) { (b.outcomes || []).forEach(function (o) { outs.push(o); }); });
    if (outs.length) {
      var counts = {}; outs.forEach(function (o) { counts[o.kind] = (counts[o.kind] || 0) + 1; });
      var parts = Object.keys(counts).map(function (k) { return counts[k] + ' ' + KIND[k] + (counts[k] > 1 ? (k === 'fine' ? 's' : k === 'court' ? 's' : 's') : ''); });
      stat('Regulator or court action', parts.join(', '), 'See details below', 'has-action');
    } else stat('Regulator or court action', 'None recorded', 'That we know of');
    var worstSev = 'low';
    c.breaches.forEach(function (b) { b.categories.forEach(function (x) { var s = sev(x); if (SEV_ORDER[s] < SEV_ORDER[worstSev]) worstSev = s; }); });
    stat('Most sensitive data exposed', SEV_LABEL[worstSev], '', 'risk-' + worstSev);
    var st = c.breaches.filter(function (b) { return b.statement; }).length;
    stat('Official statements', st + ' of ' + n, st === n ? 'Company spoke publicly every time' : st ? 'Not for every breach' : 'None found', '');
    box.appendChild(grid);
    return box;
  }

  function entry(b) {
    var e = el('div', 'entry'), unv = b.status !== 'confirmed';
    var top = el('div', 'entry-top');
    top.appendChild(el('h4', 0, b.title));
    top.appendChild(el('span', 'status' + (unv ? ' unv' : ''), unv ? 'Unverified report' : 'Confirmed'));
    e.appendChild(top);
    var dl = el('dl', 'facts');
    function row(label, node, wide) { var d = el('div', wide ? 'wide' : ''); d.appendChild(el('dt', 0, label)); var dd = el('dd'); if (typeof node === 'string') dd.textContent = node; else dd.appendChild(node); d.appendChild(dd); dl.appendChild(d); }
    row('When', fmt(b.date));
    if (b.affected) row('Affected', b.affected);
    var lg = lag(b);
    if (b.disclosed) { var mp = el('span'); mp.appendChild(document.createTextNode(fmt(b.disclosed))); if (lg) { var tag = el('span', 'lagtag lag-' + lg.bucket, lg.text); mp.appendChild(tag); } row('Made known', mp); }
    row('Source', b.source_name || 'Public source');
    var ul = el('ul', 'tags sev-tags');
    b.categories.slice().sort(function (x, y) { return SEV_ORDER[sev(x)] - SEV_ORDER[sev(y)]; }).forEach(function (x) {
      var s = sev(x), li = el('li', 'sev-' + s); li.title = SEV_LABEL[s];
      li.appendChild(el('span', 'sr', SEV_LABEL[s] + ': ')); li.appendChild(document.createTextNode(x)); ul.appendChild(li);
    });
    var worst = b.categories.reduce(function (w, x) { var s = sev(x); return SEV_ORDER[s] < SEV_ORDER[w] ? s : w; }, 'low');
    top.appendChild(el('span', 'risk risk-' + worst, worst === 'high' ? 'High-risk data exposed' : worst === 'med' ? 'Medium-risk data exposed' : 'Lower-risk data exposed'));
    row('Exposed', ul, true);
    e.appendChild(dl);
    var leg = el('p', 'legend'); leg.setAttribute('aria-hidden', 'true');
    ['high', 'med', 'low'].forEach(function (k) { leg.appendChild(el('span', 'lg-' + k, SEV_LABEL[k])); });
    e.appendChild(leg);
    if (unv) e.appendChild(el('p', 'caveat', 'This comes from a report that has not been confirmed. Treat it with care.'));
    e.appendChild(el('p', 'plain', b.description));
    if (b.outcomes && b.outcomes.length) {
      var ob = el('div', 'outcomes'); ob.appendChild(el('p', 'ol', 'What happened next'));
      var ul2 = el('ul');
      b.outcomes.forEach(function (o) {
        var li = el('li', 'oc-' + o.kind); li.appendChild(el('span', 'okind', KIND[o.kind] + ' · ' + o.year));
        var tx = el('span', 'otext', o.text); li.appendChild(tx);
        if (o.url) { var ol = el('a', 0, 'Decision'); ol.href = o.url; ol.target = '_blank'; ol.rel = 'noopener noreferrer'; li.appendChild(document.createTextNode(' ')); li.appendChild(ol); }
        ul2.appendChild(li);
      });
      ob.appendChild(ul2); e.appendChild(ob);
    }
    function link(text, url) { var l = el('a', 0, text); l.href = url; l.target = '_blank'; l.rel = 'noopener noreferrer'; return l; }
    var st = b.statement, same = st && st.url === b.source_url;
    var box = el('div', 'statement' + (st ? '' : ' none'));
    if (st) {
      box.appendChild(el('p', 'st-label', 'Official statement from ' + (CUR || 'the company')));
      var sp = el('p', 'st-link'); sp.appendChild(link(st.title, st.url)); box.appendChild(sp);
    } else {
      box.appendChild(el('p', 'st-label', 'No official company statement found'));
      box.appendChild(el('p', 'st-none', 'We couldn’t find a public statement from the company about this breach. The record is based on the source below.'));
    }
    e.appendChild(box);
    if (!same && /^https:\/\//.test(b.source_url)) { var s = el('p', 'src', 'Source: '); s.appendChild(link(b.source_name || b.source_url, b.source_url)); e.appendChild(s); }
    return e;
  }

  var CUR = '';
  function card(c, banner) {
    CUR = c.name;
    var a = el('article', 'result');
    a.setAttribute('aria-label', 'Breach history for ' + c.name);
    var h = el('div', 'result-head');
    if (banner) h.appendChild(el('p', 'result-label', banner));
    h.appendChild(el('h3', 0, c.name));
    if (c.aliases.length) h.appendChild(el('p', 'aka', 'Also known as ' + c.aliases.join(', ')));
    var pl = el('p', 'permalink'), pa = el('a', 0, 'Open the full page for ' + c.name + ' →'); pa.href = 'company/' + slug(c.name); pl.appendChild(pa); h.appendChild(pl);
    if (c.breaches.length) h.appendChild(track(c));
    a.appendChild(h);
    var b = el('div', 'result-body');
    if (!c.breaches.length) b.appendChild(el('p', 'plain', 'No breach records for this company in our database. That does not mean it has never had one.'));
    c.breaches.forEach(function (x) { b.appendChild(entry(x)); });
    var fix = el('p', 'fix'); var fl = el('a', 0, 'Report a mistake in this record'); fl.href = 'contact.html'; fix.appendChild(fl); b.appendChild(fix);
    a.appendChild(b);
    return a;
  }

  function mark(names) {
    if (!browse) return;
    browse.querySelectorAll('button').forEach(function (b) { b.setAttribute('aria-pressed', names.indexOf(b.dataset.name) > -1 ? 'true' : 'false'); });
  }

  function setUrl(term) {
    try { var u = new URL(location.href); if (term) u.searchParams.set('q', term); else u.searchParams.delete('q'); history.replaceState(null, '', u); } catch (e) {}
  }

  function run(term, scroll) {
    ready.then(function () {
      out.replaceChildren();
      var r = find(term);
      setUrl(term);
      mark(r.map(function (c) { return c.name; }));
      if (!r.length) {
        msg('No matches for “' + term + '”. That doesn’t mean the company has never had a breach. Our database is small and doesn’t cover every company.');
        /* Opens the visitor's own email app. Nothing is sent unless they choose to send it. */
        var rq = el('div', 'request'); rq.appendChild(el('p', 'rq-title', 'Want “' + term + '” added?'));
        rq.appendChild(el('p', 'rq-text', 'Send a request and the company will be researched from official public sources. Requests decide what gets added next.'));
        var ra = el('a', 'btn sm', 'Request this company'); ra.href = 'mailto:contact@hasitbeenbreached.com?subject=' + encodeURIComponent('Please add: ' + term) + '&body=' + encodeURIComponent('Hi, please add ' + term + ' to Has it been Breached?\n\nIf you know of a breach, a link to a public source helps:\n');
        rq.appendChild(ra); out.appendChild(rq);
      } else {
        msg(r.length + (r.length > 1 ? ' matches' : ' match') + ' for “' + term + '”.');
        r.forEach(function (c) { out.appendChild(card(c)); });
      }
      if (scroll) $('sample').scrollIntoView({ behavior: 'smooth', block: 'start' });
    }).catch(function () { msg('The database couldn’t be loaded. Please refresh the page and try again.'); });
  }

  ready = fetch('data/breaches.json', { cache: 'no-cache' }).then(function (r) { if (!r.ok) throw new Error('load'); return r.json(); }).then(function (d) {
    DB = d;
    DB.companies.sort(function (a, b) { return a.name.localeCompare(b.name); });
    if (count) count.textContent = DB.companies.length + ' companies · updated ' + d.updated;
    if (browse) DB.companies.forEach(function (c) {
      var li = el('li'), btn = el('button'); btn.type = 'button'; btn.dataset.name = c.name; btn.setAttribute('aria-pressed', 'false');
      btn.appendChild(el('b', 0, c.name));
      btn.appendChild(el('small', 0, c.breaches.length + (c.breaches.length === 1 ? ' record' : ' records') + ' · ' + c.website));
      btn.addEventListener('click', function () { q.value = c.name; run(c.name, window.innerWidth < 820); });
      li.appendChild(btn); browse.appendChild(li);
    });
  });

  form.addEventListener('submit', function (e) { e.preventDefault(); var t = q.value.trim(); if (t.length > 1) run(t, true); });
  document.querySelectorAll('[data-try]').forEach(function (b) { b.addEventListener('click', function () { q.value = b.dataset.try; run(b.dataset.try, true); }); });

  var start = new URLSearchParams(location.search).get('q');
  if (start) { q.value = start; run(start); }
  else ready.then(function () {
    var ex = DB.companies.filter(function (c) { return c.name === 'British Airways'; })[0] || DB.companies[0];
    out.appendChild(card(ex, 'Example from the database'));
    mark([ex.name]);
  }).catch(function () { msg('The database couldn’t be loaded. Please refresh the page and try again.'); });
})();
