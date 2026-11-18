"""Batch 5 (November 2026): companies' own breach announcements and securities filings.

Run from the repository root:  python3 tools/batches/2026-11-batch-5.py
Then rebuild the pages:        python3 tools/build_pages.py
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "breaches.json"
d = json.loads(DATA.read_text(encoding="utf-8"))

def B(**k):
    return k

def own(title, url):
    return {"title": title, "url": url}

new = [
 {"name": "Kickstarter", "aliases": [], "website": "kickstarter.com", "breaches": [B(
  title="2014 breach of user accounts", date="2014-02", status="confirmed", affected="Kickstarter users; the company gave no total",
  categories=["Usernames", "Email addresses", "Mailing addresses", "Phone numbers", "Hashed passwords"],
  description="In February 2014 hackers got into Kickstarter’s systems and took user account details, including scrambled (hashed) passwords. The crowdfunding site said no card data was taken, emailed all users and asked them to change their passwords, including on other sites where they used the same one.",
  source_name="Kickstarter", source_url="https://www.kickstarter.com/blog/important-kickstarter-security-notice",
  statement=own("Important Kickstarter Security Notice", "https://www.kickstarter.com/blog/important-kickstarter-security-notice"),
  disclosed="2014-02", outcomes=[])]},

 {"name": "Patreon", "aliases": [], "website": "patreon.com", "breaches": [B(
  title="2015 hack through a public test version of the site", date="2015-09", status="confirmed", affected="About 2.3 million accounts",
  categories=["Names", "Email addresses", "Posts and private messages", "Shipping addresses (some users)", "Billing addresses added before 2014", "Encrypted passwords"],
  description="In September 2015 attackers got in through a test version of Patreon’s website that had been left visible on the internet. Account data, including users’ posts and messages, was taken and later published online. Patreon said full card numbers were not exposed and passwords were strongly encrypted.",
  source_name="Patreon", source_url="https://patreon.com/posts/patreon-security-3530865",
  statement=own("Patreon security notice", "https://patreon.com/posts/patreon-security-3530865"),
  disclosed="2015-09", outcomes=[])]},

 {"name": "Disqus", "aliases": [], "website": "disqus.com", "breaches": [B(
  title="Leak of a 2012 user database", date="2012", status="confirmed", timing_unclear=True, affected="17.5 million users",
  categories=["Email addresses", "Usernames", "Sign-up and last login dates", "Hashed passwords (about a third of users)"],
  description="In October 2017 Disqus, the comment system used on many websites, was told that a copy of its user database from 2012 had leaked. It held email addresses and usernames of 17.5 million users, and scrambled passwords for about a third of them. Disqus reset the affected passwords.",
  source_name="Disqus", source_url="https://blog.disqus.com/security-alert-user-info-breach",
  statement=own("Security Alert: User Info Breach", "https://blog.disqus.com/security-alert-user-info-breach"),
  disclosed="2017-10", outcomes=[])]},

 {"name": "JPMorgan Chase", "aliases": ["Chase", "JP Morgan", "J.P. Morgan"], "website": "jpmorganchase.com", "breaches": [B(
  title="2014 cyber attack", date="2014-06", status="confirmed", affected="About 76 million households and 7 million small businesses",
  categories=["Names", "Home addresses", "Phone numbers", "Email addresses"],
  description="In 2014 attackers got into JPMorgan Chase’s systems and took contact details for about 76 million households and 7 million small businesses. The bank said account numbers, passwords, dates of birth and Social Security numbers were not taken, and it had seen no unusual fraud.",
  source_name="JPMorgan Chase filing (US Securities and Exchange Commission)",
  source_url="https://www.sec.gov/Archives/edgar/data/19617/000119312514362173/d799478d8k.htm",
  statement=own("JPMorgan Chase update on cybersecurity attack (Form 8-K)", "https://www.sec.gov/Archives/edgar/data/19617/000119312514362173/d799478d8k.htm"),
  disclosed="2014-10", outcomes=[])]},

 {"name": "Zomato", "aliases": ["Eternal"], "website": "zomato.com", "breaches": [B(
  title="2017 theft of user records", date="2017-05", status="confirmed", affected="About 17 million users",
  categories=["User IDs", "Names", "Usernames", "Email addresses", "Hashed passwords (6.6 million users)"],
  description="In May 2017 a hacker took about 17 million user records from Zomato, the Indian restaurant and food delivery app, through an employee’s compromised developer account, and offered them for sale. Zomato reset passwords. The hacker later agreed to take the data down after Zomato promised to start a bug bounty programme.",
  source_name="Zomato", source_url="https://www.zomato.com/blog/security-notice/",
  statement=own("Security Notice", "https://www.zomato.com/blog/security-notice/"),
  disclosed="2017-05", outcomes=[])]},

 {"name": "Frontier Communications", "aliases": ["Frontier"], "website": "frontier.com", "breaches": [B(
  title="2024 cyber attack", date="2024-04", status="confirmed", affected="About 750,000 people",
  categories=["Names", "Contact details", "Dates of birth", "Social Security numbers"],
  description="In April 2024 attackers got into parts of the network of Frontier, a US internet and phone company, and took personal information. Frontier shut down some systems to contain it. Notices filed with US states put the number of people affected at about 750,000.",
  source_name="Frontier filing (US Securities and Exchange Commission)",
  source_url="https://www.sec.gov/Archives/edgar/data/20520/000119312524100764/d784189d8k.htm",
  statement=None, disclosed="2024-04", outcomes=[])]},

 {"name": "Prudential Financial", "aliases": ["Prudential"], "website": "prudential.com", "breaches": [B(
  title="2024 cyber attack", date="2024-02", status="confirmed", affected="About 2.5 million people",
  categories=["Names", "Home addresses", "Driver’s licence numbers", "ID card numbers", "Social Security numbers"],
  description="On 4 February 2024 attackers got into some systems of Prudential, a large US insurer, and took customer data. About 2.5 million people were affected, and Social Security numbers were among the data exposed.",
  source_name="Prudential filing (US Securities and Exchange Commission)",
  source_url="https://www.sec.gov/Archives/edgar/data/1137774/000119312524033753/d770643d8k.htm",
  statement=None, disclosed="2024-02", outcomes=[])]},

 {"name": "Maximus", "aliases": [], "website": "maximus.com", "breaches": [B(
  title="2023 MOVEit file transfer breach", date="2023-05", status="confirmed", affected="8 to 11 million people (early estimate)",
  categories=["Social Security numbers", "Protected health information", "Other personal information"],
  description="Maximus runs services for US government programmes such as Medicare. In May 2023 attackers used a flaw in MOVEit file transfer software to take files that held personal information of an estimated 8 to 11 million people.",
  source_name="Maximus filing (US Securities and Exchange Commission)",
  source_url="https://www.sec.gov/Archives/edgar/data/1032220/000103222023000061/mms-20230726.htm",
  statement=None, disclosed="2023-07", outcomes=[])]},

 {"name": "Genworth", "aliases": ["Genworth Financial"], "website": "genworth.com", "breaches": [B(
  title="2023 MOVEit breach at a supplier", date="2023-05", status="confirmed", affected="About 2.5 to 2.7 million customers (early estimate)",
  categories=["Names", "Social Security numbers", "Dates of birth", "Policy details"],
  description="In May 2023 attackers used a flaw in MOVEit file transfer software at PBI Research Services, a supplier of Genworth, a US insurer. Personal information of an estimated 2.5 to 2.7 million Genworth customers was taken.",
  source_name="Genworth filing (US Securities and Exchange Commission)",
  source_url="https://www.sec.gov/Archives/edgar/data/1276520/000119312523172549/d463993d8k.htm",
  statement=None, disclosed="2023-06", outcomes=[])]},

 {"name": "KADOKAWA", "aliases": ["Kadokawa", "Niconico", "Dwango"], "website": "kadokawa.co.jp", "breaches": [B(
  title="2024 ransomware attack on Niconico", date="2024-06", status="confirmed", affected="254,241 people",
  categories=["Names", "Dates of birth", "Home addresses", "Phone numbers", "Email addresses", "Bank account details (some partners and creators)", "Student and family information (N High School)"],
  description="In June 2024 a ransomware attack hit the servers of Dwango, the KADOKAWA company that runs the Japanese video site Niconico, and the service was down for weeks. The attackers published stolen data. KADOKAWA said 254,241 people were affected, including employees, business partners, creators and students of its online schools. It said no customer card data was leaked.",
  source_name="KADOKAWA", source_url="https://group.kadokawa.co.jp/information/media-download/1355/9d3bd5d77ffe0c4d/",
  statement=own("Notice regarding information leak due to ransomware attack (August 2024)", "https://group.kadokawa.co.jp/information/media-download/1355/9d3bd5d77ffe0c4d/"),
  disclosed="2024-06", outcomes=[])]},

 {"name": "Capcom", "aliases": [], "website": "capcom.co.jp", "breaches": [B(
  title="2020 ransomware attack", date="2020-10", status="confirmed", affected="15,649 people confirmed, up to about 390,000 possibly affected",
  categories=["Names", "Home addresses", "Phone numbers", "Email addresses", "Employment and HR records"],
  description="In October 2020 attackers got into the Japanese video game company through an old backup VPN device at its US office, then spread to offices in the US and Japan and stole data. Capcom confirmed data of 15,649 people was taken and said up to about 390,000 could be affected. It said no card data was involved and it did not negotiate with the attackers.",
  source_name="Capcom", source_url="https://www.capcom.co.jp/ir/english/news/html/e210413.html",
  statement=own("4th Update Regarding Data Security Incident Due to Unauthorized Access: Investigation Results", "https://www.capcom.co.jp/ir/english/news/html/e210413.html"),
  disclosed="2020-11", outcomes=[])]},

 {"name": "WestJet", "aliases": [], "website": "westjet.com", "breaches": [B(
  title="2025 cyber attack", date="2025-06", status="confirmed", affected="WestJet did not give a total",
  categories=["Names", "Contact details", "Information and documents provided for bookings and travel"],
  description="On 13 June 2025 the Canadian airline found attackers in its systems, and some apps and websites were disrupted. Guest data was taken, varying by person. WestJet said payment card numbers and account passwords were not taken, and offered affected people fraud support.",
  source_name="WestJet", source_url="https://www.westjet.com/en-ca/news/2025/westjet-provides-further-update-on-june-13-2025-cybersecurity-incident",
  statement=own("WestJet provides further update on June 13, 2025 cybersecurity incident", "https://www.westjet.com/en-ca/news/2025/westjet-provides-further-update-on-june-13-2025-cybersecurity-incident"),
  disclosed="2025-06", outcomes=[])]},
]

have = {c["name"].lower() for c in d["companies"]}
for c in new:
    assert c["name"].lower() not in have, "already in the database: " + c["name"]
d["companies"] += new
d["updated"] = "2026-11-18"
DATA.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("added %d companies, now %d" % (len(new), len(d["companies"])))
