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
      .map(function (r) { return r.c; });
  }

  function entry(b) {
    var e = el('div', 'entry'), unv = b.status !== 'confirmed';
    e.appendChild(el('span', 'status' + (unv ? ' unv' : ''), unv ? 'Unverified report' : 'Confirmed'));
    e.appendChild(el('h4', 0, b.title));
    var dl = el('dl', 'facts');
    function row(label, node) { var d = el('div'); d.appendChild(el('dt', 0, label)); var dd = el('dd'); if (typeof node === 'string') dd.textContent = node; else dd.appendChild(node); d.appendChild(dd); dl.appendChild(d); }
    row('When it happened', fmt(b.date));
    if (b.affected) row('How many people', b.affected);
    var ul = el('ul', 'tags'); b.categories.forEach(function (x) { ul.appendChild(el('li', 0, x)); });
    row('What was exposed', ul);
    e.appendChild(dl);
    if (unv) e.appendChild(el('p', 'plain', 'This comes from a report that has not been confirmed. Treat it with care.'));
    e.appendChild(el('p', 'plain', b.description));
    var s = el('p', 'src', 'Source: ');
    if (/^https:\/\//.test(b.source_url)) { var l = el('a', 0, b.source_name || b.source_url); l.href = b.source_url; l.target = '_blank'; l.rel = 'noopener noreferrer'; s.appendChild(l); }
    e.appendChild(s);
    return e;
  }

  function card(c, banner) {
    var a = el('article', 'result');
    a.setAttribute('aria-label', 'Breach history for ' + c.name);
    a.appendChild(el('div', 'banner', banner || 'Based on public sources. Not a complete record.'));
    var b = el('div', 'result-body');
    b.appendChild(el('h3', 0, c.name));
    if (c.aliases.length) b.appendChild(el('p', 'aka', 'Also known as: ' + c.aliases.join(', ')));
    if (!c.breaches.length) b.appendChild(el('p', 'plain', 'No breach records for this company in our database. That does not mean it has never had one.'));
    c.breaches.forEach(function (x) { b.appendChild(entry(x)); });
    var fix = el('p', 'src'); var fl = el('a', 0, 'Report a mistake in this record'); fl.href = 'contact.html'; fix.appendChild(fl); b.appendChild(fix);
    a.appendChild(b);
    return a;
  }

  function setUrl(term) {
    try { var u = new URL(location.href); if (term) u.searchParams.set('q', term); else u.searchParams.delete('q'); history.replaceState(null, '', u); } catch (e) {}
  }

  function run(term, scroll) {
    ready.then(function () {
      out.replaceChildren();
      var r = find(term);
      setUrl(term);
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
    if (count) count.textContent = DB.companies.length + ' companies · last updated ' + d.updated;
    if (browse) DB.companies.forEach(function (c) {
      var li = el('li'), btn = el('button'); btn.type = 'button';
      btn.appendChild(el('b', 0, c.name));
      btn.appendChild(el('small', 0, c.breaches.length + (c.breaches.length === 1 ? ' record' : ' records') + ' · ' + c.website));
      btn.addEventListener('click', function () { q.value = c.name; run(c.name, true); });
      li.appendChild(btn); browse.appendChild(li);
    });
  });

  form.addEventListener('submit', function (e) { e.preventDefault(); var t = q.value.trim(); if (t.length > 1) run(t, window.innerWidth < 900); });
  document.querySelectorAll('[data-try]').forEach(function (b) { b.addEventListener('click', function () { q.value = b.dataset.try; run(b.dataset.try, window.innerWidth < 900); }); });

  var start = new URLSearchParams(location.search).get('q');
  if (start) { q.value = start; run(start); }
  else ready.then(function () {
    var ex = DB.companies.filter(function (c) { return c.name === 'British Airways'; })[0] || DB.companies[0];
    out.appendChild(card(ex, 'Example from the database'));
  }).catch(function () { msg('The database couldn’t be loaded. Please refresh the page and try again.'); });
})();
