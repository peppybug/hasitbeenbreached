"""Batch 8 (November 2026): US retail and restaurant payment card breaches.

Run from the repository root:  python3 tools/batches/2026-11-batch-8.py
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

CARD = ["Cardholder names", "Payment card numbers", "Card expiry dates", "Card security codes"]

new = [
 {"name": "Michaels", "aliases": ["Michaels Stores", "Aaron Brothers"], "website": "michaels.com", "breaches": [B(
  title="2013–2014 payment card malware", date="2013-05", status="confirmed",
  affected="About 2.6 million cards at Michaels and 400,000 at Aaron Brothers",
  categories=["Payment card numbers", "Card expiry dates"],
  description="From May 2013 to January 2014 malware on payment systems at some Michaels and Aaron Brothers craft stores in the US captured card numbers and expiry dates. About 2.6 million Michaels cards and 400,000 Aaron Brothers cards may have been affected. The company said names, addresses and PINs were not at risk.",
  source_name="Michaels filing (US Securities and Exchange Commission)",
  source_url="https://www.sec.gov/Archives/edgar/data/740670/000110465914032010/a14-2849_110k.htm",
  statement=None, disclosed="2014-01", outcomes=[])]},

 {"name": "Chipotle", "aliases": ["Chipotle Mexican Grill", "Pizzeria Locale"], "website": "chipotle.com", "breaches": [B(
  title="2017 payment card malware", date="2017-03", status="confirmed",
  affected="Cards used at most Chipotle restaurants during the period; no total given",
  categories=CARD,
  description="Between 24 March and 18 April 2017 malware on payment devices at most Chipotle and Pizzeria Locale restaurants captured card details. Chipotle said no other customer information was affected and published a list of locations and dates.",
  source_name="Chipotle", source_url="https://newsroom.chipotle.com/2017-05-26-chipotle-mexican-grill-reports-findings-from-investigation-of-payment-card-security-incident",
  statement=own("Chipotle Mexican Grill Reports Findings from Investigation of Payment Card Security Incident", "https://newsroom.chipotle.com/2017-05-26-chipotle-mexican-grill-reports-findings-from-investigation-of-payment-card-security-incident"),
  disclosed="2017-04", outcomes=[])]},

 {"name": "Supervalu", "aliases": ["Cub Foods", "Shop 'n Save", "Shoppers Food & Pharmacy", "Farm Fresh", "Hornbacher's"], "website": "supervalu.com", "breaches": [B(
  title="Two 2014 payment card intrusions", date="2014-06", status="confirmed", affected="Cards used at some stores; no total given",
  categories=["Cardholder names", "Payment card numbers", "Card expiry dates"],
  description="In 2014 attackers got into the card payment network of Supervalu, a US grocery company, twice: first between June and July at stores such as Cub Foods, Farm Fresh and Shop ’n Save, and again later that year. Supervalu offered affected customers identity protection.",
  source_name="Supervalu filing (US Securities and Exchange Commission)",
  source_url="https://www.sec.gov/Archives/edgar/data/0000095521/000110465914061193/a14-19156_1ex99d1.htm",
  statement=own("Supervalu announcement of criminal intrusion (August 2014)", "https://www.sec.gov/Archives/edgar/data/0000095521/000110465914061193/a14-19156_1ex99d1.htm"),
  disclosed="2014-08", outcomes=[])]},

 {"name": "Sonic Drive-In", "aliases": ["Sonic"], "website": "sonicdrivein.com", "breaches": [B(
  title="2017 payment card malware", date="2017", status="confirmed", timing_unclear=True,
  affected="Cards used at certain drive-ins; no total given",
  categories=["Payment card numbers", "Card expiry dates", "Cardholder names"],
  description="In September 2017 Sonic’s card processor reported suspicious activity on cards used at some Sonic Drive-In restaurants, and malware was found. Sonic offered affected guests two years of free identity theft protection and faced several class actions.",
  source_name="Sonic filing (US Securities and Exchange Commission)",
  source_url="https://www.sec.gov/Archives/edgar/data/0000868611/000086861117000050/soncfy201710k.htm",
  statement=None, disclosed="2017-10", outcomes=[])]},

 {"name": "Saks Fifth Avenue", "aliases": ["Saks OFF 5TH", "Lord & Taylor", "Hudson's Bay Company", "HBC"], "website": "saksfifthavenue.com", "breaches": [B(
  title="Payment card theft at department stores", date="2017-05", status="confirmed", timing_unclear=True,
  affected="Cards used at certain North American stores; HBC did not give a total",
  categories=["Payment card numbers", "Card expiry dates"],
  description="In 2018 Hudson’s Bay Company said card data had been stolen at certain Saks Fifth Avenue, Saks OFF 5TH and Lord & Taylor stores in North America. It said online shopping, Saks credit cards and other personal details were not affected, and customers would not pay for fraudulent charges.",
  source_name="Hudson’s Bay Company", source_url="http://investor.hbc.com/news-releases/news-release-details/hbc-provides-update-previously-announced-data-security-issue",
  statement=own("HBC Provides Update on Previously-Announced Data Security Issue", "http://investor.hbc.com/news-releases/news-release-details/hbc-provides-update-previously-announced-data-security-issue"),
  disclosed="2018-04", outcomes=[])]},

 {"name": "DocuSign", "aliases": [], "website": "docusign.com", "breaches": [B(
  title="2017 theft of customer email addresses", date="2017-05", status="confirmed",
  affected="DocuSign account holders; no total given",
  categories=["Email addresses"],
  description="In May 2017 an attacker got into a DocuSign system used for service announcements and took a list of customer email addresses, which were then used for convincing fake DocuSign emails carrying malware. DocuSign said documents, names, passwords and payment data were not affected.",
  source_name="DocuSign", source_url="https://www.docusign.com/trust/alerts/update-5-15-2017-latest-update-on-malicious-email-campaign",
  statement=own("Latest update on malicious email campaign (May 2017)", "https://www.docusign.com/trust/alerts/update-5-15-2017-latest-update-on-malicious-email-campaign"),
  disclosed="2017-05", outcomes=[])]},

 {"name": "Staples", "aliases": [], "website": "staples.com", "breaches": [B(
  title="2014 payment card malware", date="2014-08", status="confirmed", affected="About 1.16 million payment cards at 115 US stores",
  categories=CARD,
  description="Between August and September 2014 malware on payment systems at 115 of Staples’ more than 1,400 US stores captured card details. About 1.16 million cards may have been affected. Staples offered free identity protection and added new encryption to its tills.",
  source_name="Staples", source_url="https://www.businesswire.com/news/home/20141219006077/en/Staples-Provides-Update-on-Data-Security-Incident",
  statement=own("Staples Provides Update on Data Security Incident", "https://www.businesswire.com/news/home/20141219006077/en/Staples-Provides-Update-on-Data-Security-Incident"),
  disclosed="2014-10", outcomes=[])]},

 {"name": "Whole Foods Market", "aliases": ["Whole Foods"], "website": "wholefoodsmarket.com", "breaches": [B(
  title="2017 card data theft at in-store bars and restaurants", date="2017-03", status="confirmed",
  affected="Cards used at taprooms and table-service restaurants in some stores",
  categories=CARD,
  description="Between March and September 2017 malware copied card details at taprooms and full table-service restaurants inside some Whole Foods stores, which used a separate payment system. Cards used at the main checkouts and on Amazon were not affected.",
  source_name="Whole Foods Market", source_url="https://media.wholefoodsmarket.com/whole-foods-market-payment-card-investigation-update/",
  statement=own("Whole Foods Market Payment Card Investigation Update", "https://media.wholefoodsmarket.com/whole-foods-market-payment-card-investigation-update/"),
  disclosed="2017-09", outcomes=[])]},

 {"name": "Forever 21", "aliases": [], "website": "forever21.com", "breaches": [B(
  title="2017 payment card malware", date="2017-04", status="confirmed", affected="Cards used at some US stores; no total given",
  categories=["Payment card data read from the card", "Cardholder names (sometimes)"],
  description="Between April and November 2017 encryption was switched off on some payment devices at Forever 21 stores in the US, and malware on them searched for card data. Cards used on the website were not affected.",
  source_name="Forever 21", source_url="https://newsroom.forever21.com/releases/forever-21-reports-findings-from-investigation-of-payment-card-security-incident",
  statement=own("Forever 21 Reports Findings from Investigation of Payment Card Security Incident", "https://newsroom.forever21.com/releases/forever-21-reports-findings-from-investigation-of-payment-card-security-incident"),
  disclosed="2017-11", outcomes=[])]},

 {"name": "Sally Beauty", "aliases": ["Sally Beauty Supply"], "website": "sallybeauty.com", "breaches": [B(
  title="2014 payment card malware", date="2014-02", status="confirmed", affected="Fewer than 25,000 payment card records",
  categories=["Payment card data read from the card"],
  description="In February 2014 malware on payment systems at Sally Beauty, a US beauty supply chain, captured card data from fewer than 25,000 transactions. The company removed the malware. It disclosed a second, separate incident a year later.",
  source_name="Sally Beauty filing (US Securities and Exchange Commission)",
  source_url="https://www.sec.gov/Archives/edgar/data/1368458/000110465914033026/a14-8385_110q.htm",
  statement=None, disclosed="2014-03", outcomes=[])]},
]

have = {c["name"].lower() for c in d["companies"]}
for c in new:
    assert c["name"].lower() not in have, "already in the database: " + c["name"]
d["companies"] += new
d["updated"] = "2026-11-18"
DATA.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("added %d companies, now %d" % (len(new), len(d["companies"])))
