// Lights up the toolbar icon when the site in the current tab is in the database.
// The page address is only compared with the company list stored in the browser; it is never sent anywhere.
import { getDB, findByHost, worstSev } from './data.js';

const COLOR = { high: '#D7263D', med: '#C77700', low: '#5B6275' };
const LABEL = { high: 'high-risk', med: 'medium-risk', low: 'lower-risk' };

async function update(tabId, url) {
  let host = '';
  try { const u = new URL(url); if (u.protocol === 'http:' || u.protocol === 'https:') host = u.hostname; } catch (e) {}
  const db = await getDB();
  const c = host ? findByHost(db, host) : null;
  if (!c || !c.breaches.length) {
    await chrome.action.setBadgeText({ tabId, text: '' });
    await chrome.action.setTitle({ tabId, title: 'Has it been Breached?' + (host ? ' – nothing on record for ' + host.replace(/^www\./, '') : '') });
    return;
  }
  const n = c.breaches.length, w = worstSev(c);
  await chrome.action.setBadgeText({ tabId, text: String(n) });
  await chrome.action.setBadgeBackgroundColor({ tabId, color: COLOR[w] });
  if (chrome.action.setBadgeTextColor) await chrome.action.setBadgeTextColor({ tabId, color: '#FFFFFF' });
  await chrome.action.setTitle({ tabId, title: c.name + ': ' + n + (n === 1 ? ' breach' : ' breaches') + ' on record, ' + LABEL[w] + ' data exposed. Click for details.' });
}

chrome.tabs.onUpdated.addListener((tabId, info, tab) => { if (info.url || info.status === 'complete') update(tabId, tab.url); });
chrome.tabs.onActivated.addListener(async ({ tabId }) => { try { const t = await chrome.tabs.get(tabId); update(tabId, t.url); } catch (e) {} });

// Refresh the company list once a day, and on install.
chrome.runtime.onInstalled.addListener(() => { chrome.alarms.create('refresh', { periodInMinutes: 24 * 60 }); getDB(true); });
chrome.alarms.onAlarm.addListener(a => { if (a.name === 'refresh') getDB(true); });
