// Loads the company list and matches websites against it. Everything here runs inside the browser:
// the only network request is downloading the public company list from hasitbeenbreached.com.
import { sev, SEV_ORDER } from './sev.js';

export const SITE = 'https://hasitbeenbreached.com/';
const REMOTE = SITE + 'data/breaches.json';
const MAX_AGE = 24 * 60 * 60 * 1000; // refresh the list once a day

// Returns the company list: the cached copy if it is fresh, otherwise a new download,
// otherwise the copy bundled with the extension (so it also works offline or if the site is down).
export async function getDB(force = false) {
  let cached = null;
  try { cached = (await chrome.storage.local.get('db')).db; } catch (e) {}
  if (!force && cached && Date.now() - cached.fetched < MAX_AGE) return cached.data;
  try {
    const r = await fetch(REMOTE, { cache: 'no-cache' });
    if (!r.ok) throw new Error('HTTP ' + r.status);
    const data = await r.json();
    if (!Array.isArray(data.companies)) throw new Error('bad data');
    await chrome.storage.local.set({ db: { fetched: Date.now(), data } });
    return data;
  } catch (e) {
    if (cached) return cached.data;
    const r = await fetch(chrome.runtime.getURL('data/breaches.json'));
    return r.json();
  }
}

// "www.booking.com" or "secure.booking.com" both match a company whose website is "booking.com".
export function findByHost(db, host) {
  host = String(host || '').toLowerCase().replace(/^www\./, '');
  if (!host) return null;
  let best = null;
  let bestLen = 0;
  for (const c of db.companies) {
    for (const d of [c.website].concat(c.domains || [])) {
      const w = String(d || '').toLowerCase().replace(/^www\./, '');
      if (w && (host === w || host.endsWith('.' + w)) && w.length > bestLen) { best = c; bestLen = w.length; }
    }
  }
  return best;
}

export function worstSev(company) {
  let w = 'low';
  for (const b of company.breaches) for (const cat of b.categories) { const s = sev(cat); if (SEV_ORDER[s] < SEV_ORDER[w]) w = s; }
  return w;
}

export function breachWorst(b) {
  return b.categories.reduce((w, x) => (SEV_ORDER[sev(x)] < SEV_ORDER[w] ? sev(x) : w), 'low');
}

// Same rule as slug() in assets/search.js and tools/build_pages.py, which build company/<slug>.html.
export function slug(s) {
  return String(s).normalize('NFKD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');
}

// Search by name, alias or website, like the search box on the site.
function norm(s) {
  return String(s || '').toLowerCase().normalize('NFKD').replace(/[̀-ͯ]/g, '')
    .replace(/^https?:\/\//, '').replace(/^www\./, '').replace(/[^a-z0-9]+/g, ' ').trim();
}
export function search(db, term) {
  const t = norm(term); if (t.length < 2) return [];
  const tight = t.replace(/ /g, '');
  return db.companies.map(c => {
    const keys = [c.name, c.website, String(c.website || '').replace(/\.[a-z.]+$/, '')].concat(c.aliases || [], c.domains || []).map(norm);
    let s = 0;
    for (const k of keys) {
      const kt = k.replace(/ /g, '');
      if (k === t || kt === tight) s = Math.max(s, 3);
      else if (k.startsWith(t) || kt.startsWith(tight)) s = Math.max(s, 2);
      else if (tight.length > 2 && (k.includes(t) || kt.includes(tight))) s = Math.max(s, 1);
    }
    return { c, s };
  }).filter(r => r.s > 0).sort((a, b) => b.s - a.s || a.c.name.localeCompare(b.c.name)).slice(0, 8).map(r => r.c);
}
