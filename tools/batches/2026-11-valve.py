"""Adds Valve Corporation (Steam) to data/breaches.json. Safe to run once; refuses duplicates.

Run from the repository root:  python3 tools/batches/2026-11-valve.py
Then rebuild the pages:        python3 tools/build_pages.py
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "breaches.json"
d = json.loads(DATA.read_text(encoding="utf-8"))

valve = {"name": "Valve Corporation", "aliases": ["Valve", "Steam", "Steam Community"], "website": "valvesoftware.com", "breaches": [
 {"title": "2011 break-in to the Steam forums and a Steam database", "date": "2011-11", "status": "confirmed",
  "affected": "Steam users; Valve gave no total",
  "categories": ["Usernames", "Hashed passwords", "Email addresses", "Billing addresses", "Encrypted payment card details", "Game purchase history"],
  "description": "In November 2011 attackers defaced the Steam forums and got into a Steam database holding usernames, scrambled (salted and hashed) passwords, purchase history, email and billing addresses and encrypted card details. Valve made forum users reset their passwords. In February 2012 it said the attackers had probably copied a backup of Steam transactions from 2004 to 2008, without Steam passwords, and that it had no evidence card details were misused.",
  "source_name": "Valve (Steam news)", "source_url": "https://store.steampowered.com/oldnews/6761",
  "statement": {"title": "Message from Gabe to Steam Community", "url": "https://store.steampowered.com/oldnews/6761"},
  "disclosed": "2011-11", "outcomes": []},
 {"title": "2015 Steam Store caching error", "date": "2015-12", "status": "confirmed",
  "affected": "About 34,000 users",
  "categories": ["Billing addresses", "Email addresses", "Purchase history", "Last four digits of Steam Guard phone numbers", "Partial payment card numbers (last two digits)"],
  "description": "On 25 December 2015, during a cyber attack on Steam, a configuration mistake made the Steam Store show some users’ account pages to other users for about 90 minutes. Pages of about 34,000 users may have been seen. Valve said full card numbers and passwords were not shown and nobody could make changes to other accounts.",
  "source_name": "Valve (Steam news)", "source_url": "https://store.steampowered.com/oldnews/19852",
  "statement": {"title": "Update on Christmas Issues", "url": "https://store.steampowered.com/oldnews/19852"},
  "disclosed": "2015-12", "outcomes": []},
]}

assert valve["name"].lower() not in {c["name"].lower() for c in d["companies"]}
d["companies"].append(valve)
d["updated"] = "2026-11-19"
DATA.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("added Valve Corporation, now %d companies" % len(d["companies"]))
