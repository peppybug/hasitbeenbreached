"""Batch 7 (November 2026): airlines, UK, retail and payments.

Run from the repository root:  python3 tools/batches/2026-11-batch-7.py
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
 {"name": "Air Canada", "aliases": ["Aeroplan"], "website": "aircanada.com", "breaches": [B(
  title="2018 break-in to app accounts", date="2018-08", status="confirmed", affected="About 20,000 app profiles",
  categories=["Names", "Email addresses", "Phone numbers", "Aeroplan numbers", "Passport details (if saved in the app)", "Dates of birth"],
  description="Between 22 and 24 August 2018 Air Canada detected unusual logins to its mobile app, and about 20,000 of 1.7 million profiles may have been accessed. Profiles could include saved passport details. Air Canada locked all app accounts and made every user reset their password.",
  source_name="Air Canada", source_url="https://www.aircanada.com/it/en/aco/home/book/travel-news-and-updates/2018/notice-air-canada-mobile-app-users.html",
  statement=own("Notice to Air Canada mobile App users", "https://www.aircanada.com/it/en/aco/home/book/travel-news-and-updates/2018/notice-air-canada-mobile-app-users.html"),
  disclosed="2018-08", outcomes=[])]},

 {"name": "Advance Auto Parts", "aliases": [], "website": "advanceautoparts.com", "breaches": [B(
  title="2024 theft from a cloud database", date="2024-04", status="confirmed", timing_unclear=True,
  affected="About 2.3 million people, mostly job applicants and employees",
  categories=["Names", "Social Security numbers", "Government ID numbers", "Dates of birth"],
  description="In 2024 attackers took data from a cloud database used by Advance Auto Parts, a US car parts retailer, part of a wave of attacks on companies’ Snowflake cloud accounts. Files held Social Security and other ID numbers of current and former job applicants and employees.",
  source_name="Advance Auto Parts filing (US Securities and Exchange Commission)",
  source_url="https://www.sec.gov/Archives/edgar/data/1158449/000115844924000162/aap-20240523.htm",
  statement=None, disclosed="2024-06", outcomes=[])]},

 {"name": "Conduent", "aliases": [], "website": "conduent.com", "breaches": [B(
  title="Theft of data handled for government and health clients", date="2024-10", status="confirmed", timing_unclear=True,
  affected="About 10.5 million people",
  categories=["Names", "Social Security numbers", "Health insurance details", "Medical information"],
  description="Conduent processes payments and records for US state governments and health insurers. In January 2025 it found an attacker had been in part of its network and had taken files with personal information of people served by its clients. Filings with US states put the number affected at about 10.5 million.",
  source_name="Conduent filing (US Securities and Exchange Commission)",
  source_url="https://www.sec.gov/Archives/edgar/data/1677703/000167770325000067/cndt-20250409.htm",
  statement=None, disclosed="2025-01", outcomes=[])]},

 {"name": "Krispy Kreme", "aliases": [], "website": "krispykreme.com", "breaches": [B(
  title="2024 cyber attack", date="2024-11", status="confirmed", affected="About 160,000 people, mostly employees and their families",
  categories=["Names", "Social Security numbers", "Dates of birth", "Driver’s licence numbers", "Bank account details"],
  description="In late 2024 a cyber attack on Krispy Kreme disrupted online ordering in parts of the US. Personal data was taken, mostly of current and former employees and their families.",
  source_name="Krispy Kreme filing (US Securities and Exchange Commission)",
  source_url="https://www.sec.gov/Archives/edgar/data/1857154/000185715424000123/dnut-20241211.htm",
  statement=None, disclosed="2024-12", outcomes=[])]},

 {"name": "Morrisons", "aliases": ["WM Morrison Supermarkets"], "website": "morrisons.com", "breaches": [B(
  title="Employee leaked staff payroll data", date="2014-01", status="confirmed", affected="About 100,000 employees",
  categories=["Names", "Home addresses", "Bank account details", "Salary details", "National Insurance numbers"],
  description="In 2014 a Morrisons employee with a grudge copied payroll data for the UK supermarket’s whole workforce and posted details of nearly 100,000 staff online. He was jailed. Employees sued Morrisons, but in 2020 the UK Supreme Court ruled the company was not responsible for what he did.",
  source_name="UK Supreme Court", source_url="https://www.supremecourt.uk/cases/uksc-2018-0213",
  statement=None, disclosed="2014-03",
  outcomes=[{"kind": "court", "text": "UK Supreme Court ruled Morrisons was not liable for the employee’s leak", "year": 2020}])]},

 {"name": "Synnovis", "aliases": [], "website": "synnovis.co.uk", "breaches": [B(
  title="2024 ransomware attack on NHS pathology services", date="2024-06", status="confirmed",
  affected="Patients of London NHS hospitals; Synnovis did not give a total",
  categories=["Names", "NHS numbers", "Blood test results and other pathology data"],
  description="On 3 June 2024 a ransomware attack hit Synnovis, which runs blood testing for several London NHS hospitals. Operations and blood transfusions were cancelled or delayed for weeks. The attackers later published stolen data, including patient test information.",
  source_name="Synnovis", source_url="https://www.synnovis.co.uk/news-and-press/synnovis-cyberattack",
  statement=own("Synnovis’ statement on this week’s cyberattack", "https://www.synnovis.co.uk/news-and-press/synnovis-cyberattack"),
  disclosed="2024-06", outcomes=[])]},

 {"name": "Wendy’s", "aliases": ["Wendys", "Wendy's"], "website": "wendys.com", "breaches": [B(
  title="2015–2016 payment card malware", date="2015-10", status="confirmed",
  affected="Cards used at about 1,000 franchised US restaurants",
  categories=["Cardholder names", "Payment card numbers", "Card expiry dates", "Card security codes"],
  description="From autumn 2015 attackers used a supplier’s stolen login to put malware on payment systems at Wendy’s franchised restaurants in the US. It first said fewer than 300 restaurants were affected, then found a second type of malware at many more. Wendy’s said its own company-run restaurants were not affected.",
  source_name="Wendy’s", source_url="https://www.wendys.com/payment-card-incident",
  statement=own("Payment Card Incident", "https://www.wendys.com/payment-card-incident"),
  disclosed="2016-01", outcomes=[])]},

 {"name": "Heartland Payment Systems", "aliases": ["Heartland"], "website": "heartlandpaymentsystems.com", "breaches": [B(
  title="2008 card data theft from a payment processor", date="2008", status="confirmed", timing_unclear=True,
  affected="Tens of millions of payment cards; no exact total given",
  categories=["Payment card numbers", "Card expiry dates", "Cardholder names (some cards)"],
  description="In 2008 malware in the network of Heartland, a large US card payment processor, captured card data as it passed through unencrypted. It was announced in January 2009 and was one of the largest card breaches of its time. Heartland paid card companies and cardholders to settle claims, and spent about $148 million on the breach in total.",
  source_name="Heartland filing (US Securities and Exchange Commission)",
  source_url="https://www.sec.gov/Archives/edgar/data/0001144354/000136231009000509/c79618exv99w1.htm",
  statement=own("Heartland Payment Systems press release (January 2009)", "https://www.sec.gov/Archives/edgar/data/0001144354/000136231009000509/c79618exv99w1.htm"),
  disclosed="2009-01",
  outcomes=[{"kind": "settlement", "text": "Settled with American Express ($3.6 million) and later other card companies", "year": 2009}])]},

 {"name": "Virgin Media", "aliases": ["Virgin Media O2"], "website": "virginmedia.com", "breaches": [B(
  title="Marketing database left open online", date="2019-04", status="confirmed", affected="About 900,000 people",
  categories=["Names", "Home addresses", "Email addresses", "Phone numbers", "Dates of birth (very few people)"],
  description="A Virgin Media marketing database was set up wrongly and could be accessed from the internet for about ten months until researchers reported it in 2020. It held contact details of about 900,000 people, customers and non-customers. Virgin Media said there were no passwords or financial details, and UK regulators closed the matter without action.",
  source_name="Virgin Media", source_url="https://www.virginmedia.com/corporate/media-centre/press-releases/virgin-medias-data-incident",
  statement=own("Virgin Media’s data incident", "https://www.virginmedia.com/corporate/media-centre/press-releases/virgin-medias-data-incident"),
  disclosed="2020-03", outcomes=[])]},

 {"name": "Delta Air Lines", "aliases": ["Delta"], "website": "delta.com", "breaches": [B(
  title="Card data theft through a chat supplier", date="2017-09", status="confirmed",
  affected="Several hundred thousand customers (estimate)",
  categories=["Names", "Home addresses", "Payment card numbers", "Card security codes", "Card expiry dates"],
  description="From 26 September to 12 October 2017 malware at [24]7.ai, a chat software supplier, could capture card details that customers typed on Delta’s desktop website. Delta said it couldn’t tell for sure whether anyone’s details were actually taken, offered free credit monitoring and said customers would not pay for any fraud.",
  source_name="Delta Air Lines", source_url="https://www.delta.com/content/www/en_US/response.html",
  statement=own("Information on [24]7.ai cyber incident", "https://www.delta.com/content/www/en_US/response.html"),
  disclosed="2018-04", outcomes=[])]},
]

have = {c["name"].lower() for c in d["companies"]}
for c in new:
    assert c["name"].lower() not in have, "already in the database: " + c["name"]
d["companies"] += new
d["updated"] = "2026-11-18"
DATA.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("added %d companies, now %d" % (len(new), len(d["companies"])))
