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
  var HIGH = /social security|insurance number|citizen service|bsn|passport|licen[cs]e|id number|id document|government id|payment card|card number|security code|cvv|bank account|brokerage account|password|passcode|puk code|authentication key|session token|private key|certificate key|security question|health|medicare|medical|claims|test result|genetic|ancestry|ethnicity|income|credit/i;
  var MED = /date of birth|dates of birth|home address|billing address|shipping address|phone|location|family tree|expiry|booking|stay|order|contact details|ip address|household|demographic|employment|call and text|emails and attachments|customer service|support messages|account balance|transaction|portfolio|payout|sim card/i;
  var PARTIAL = /masked|partial|last four/i;
  function sev(cat) { if ((PARTIAL.test(cat) && !/social security/i.test(cat)) || /sim card number/i.test(cat)) return 'med'; return HIGH.test(cat) ? 'high' : MED.test(cat) ? 'med' : 'low'; }
  var SEV_LABEL = { high: 'High risk', med: 'Medium risk', low: 'Lower risk' };
  var SEV_ORDER = { high: 0, med: 1, low: 2 };

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
    if (unv) e.appendChild(el('p', 'caveat', 'This comes from a report that has not been confirmed. Treat it with care.'));
    e.appendChild(el('p', 'plain', b.description));
    var leg = el('p', 'legend'); leg.setAttribute('aria-hidden', 'true');
    ['high', 'med', 'low'].forEach(function (k) { leg.appendChild(el('span', 'lg-' + k, SEV_LABEL[k])); });
    e.appendChild(leg);
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
