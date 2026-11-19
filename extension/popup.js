// Popup: shows the record for the site in the current tab, plus a company search.
// All matching happens here, in the browser. Text from the data is inserted with textContent only.
import { getDB, findByHost, worstSev, breachWorst, slug, search, SITE } from './data.js';

const $ = id => document.getElementById(id);
const M = ['January','February','March','April','May','June','July','August','September','October','November','December'];
const RISK = { high: 'High-risk data exposed', med: 'Medium-risk data exposed', low: 'Lower-risk data exposed' };
function el(tag, cls, text) { const e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }
function fmt(d) { const p = String(d).split('-'); return p.length === 1 ? p[0] : M[+p[1] - 1] + ' ' + p[0]; }

let DB = null, HOST = '';

function showCompany(c, fromSearch) {
  const box = $('current'); box.replaceChildren();
  const card = el('div', 'card');
  if (fromSearch) {
    const back = el('button', 'back', '← Back'); back.type = 'button';
    back.addEventListener('click', () => { $('q').value = ''; $('results').hidden = true; showCurrent(); });
    card.appendChild(back);
  } else card.appendChild(el('p', 'site', 'You’re on ' + HOST));
  card.appendChild(el('h1', null, c.name));
  const n = c.breaches.length;
  const sum = el('div', 'sum');
  sum.appendChild(el('span', 'pill', n + (n === 1 ? ' breach' : ' breaches') + ' on record'));
  if (n) { const w = worstSev(c); sum.appendChild(el('span', 'pill risk-' + w, RISK[w])); }
  card.appendChild(sum);
  const ul = el('ul', 'breaches');
  c.breaches.slice().sort((a, b) => String(b.date).localeCompare(String(a.date))).forEach(b => {
    const li = el('li', 'b-' + breachWorst(b));
    li.appendChild(el('div', 'bt', b.title));
    li.appendChild(el('div', 'bm', fmt(b.date) + (b.affected ? ' · ' + b.affected : '') + (b.status !== 'confirmed' ? ' · Unverified report' : '')));
    ul.appendChild(li);
  });
  card.appendChild(ul);
  const a = el('a', 'btn', 'See full history and sources'); a.href = SITE + 'company/' + slug(c.name); a.target = '_blank'; a.rel = 'noopener';
  card.appendChild(a);
  box.appendChild(card);
}

function showNone() {
  const box = $('current'); box.replaceChildren();
  const card = el('div', 'card none');
  if (HOST) {
    card.appendChild(el('p', 'site', 'You’re on ' + HOST));
    card.appendChild(el('h1', null, 'No breaches on record'));
    const p = el('p', null, 'Our database is still growing, so this doesn’t mean the site has never had a breach. ');
    const a = el('a', null, 'Request it');
    a.href = 'mailto:contact@hasitbeenbreached.com?subject=' + encodeURIComponent('Please add: ' + HOST);
    p.appendChild(a); card.appendChild(p);
  } else {
    card.appendChild(el('h1', null, 'Check a company’s history'));
    card.appendChild(el('p', null, 'Visit a website or search below to see its data breaches on public record.'));
  }
  box.appendChild(card);
}

function showCurrent() { const c = HOST ? findByHost(DB, HOST) : null; c ? showCompany(c, false) : showNone(); }

function showResults(term) {
  const out = $('results'); out.replaceChildren();
  if (term.trim().length < 2) { out.hidden = true; return; }
  const r = search(DB, term);
  if (!r.length) { out.appendChild(el('li', 'empty', 'Not in the database yet.')); }
  r.forEach(c => {
    const li = el('li'), btn = el('button'); btn.type = 'button';
    btn.appendChild(document.createTextNode(c.name));
    btn.appendChild(el('small', null, c.breaches.length + (c.breaches.length === 1 ? ' record' : ' records') + ' · ' + c.website));
    btn.addEventListener('click', () => { out.hidden = true; showCompany(c, true); });
    li.appendChild(btn); out.appendChild(li);
  });
  out.hidden = false;
}

(async () => {
  DB = await getDB();
  // ?url= lets the popup be previewed in a normal tab during development.
  let url = new URLSearchParams(location.search).get('url');
  if (!url) { try { const [t] = await chrome.tabs.query({ active: true, currentWindow: true }); url = t && t.url; } catch (e) {} }
  try { const u = new URL(url); if (u.protocol === 'http:' || u.protocol === 'https:') HOST = u.hostname.replace(/^www\./, ''); } catch (e) {}
  showCurrent();
  $('q').addEventListener('input', e => showResults(e.target.value));
  $('search').addEventListener('submit', e => { e.preventDefault(); const r = search(DB, $('q').value); if (r[0]) { $('results').hidden = true; showCompany(r[0], true); } });
})();
