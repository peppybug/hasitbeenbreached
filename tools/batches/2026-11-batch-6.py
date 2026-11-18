"""Batch 6 (November 2026): European regulators, Australia, India and US hospitality and crypto.

Run from the repository root:  python3 tools/batches/2026-11-batch-6.py
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
 {"name": "Virgin Mobile Polska", "aliases": ["Virgin Mobile Poland", "P4"], "website": "virginmobile.pl", "breaches": [B(
  title="Theft of prepaid customer data", date="2019", status="confirmed", timing_unclear=True,
  affected="More than 114,000 prepaid customers",
  categories=["Names", "National ID numbers (PESEL)", "ID document numbers", "Phone numbers"],
  description="Attackers used a weakness in a system of Virgin Mobile Polska, a Polish mobile operator, to take data of more than 114,000 prepaid customers. Poland’s data protection authority found the company had not regularly tested its security and fined it almost 2 million złoty in 2020, later set at about 1.6 million złoty. Polish courts upheld the decision.",
  source_name="UODO (Polish Data Protection Authority)", source_url="https://uodo.gov.pl/pl/138/2869",
  statement=None,
  outcomes=[{"kind": "fine", "text": "Fined almost 2 million złoty by Poland’s data protection authority (later about 1.6 million)", "year": 2020},
            {"kind": "court", "text": "A Polish court upheld the fine", "year": 2023}])]},

 {"name": "Cosmote", "aliases": ["OTE", "OTE Group"], "website": "cosmote.gr", "breaches": [B(
  title="2020 leak of call records", date="2020-09", status="confirmed",
  affected="Millions of subscribers (estimates range from 4.8 million to over 10 million)",
  categories=["Call and text records (numbers and times)", "Phone numbers", "Cell tower location (some calls)"],
  description="In early September 2020 attackers took call records from a server of Cosmote, Greece’s largest mobile operator, covering millions of subscribers, including people on other networks they called. Greece’s data protection authority fined Cosmote €6 million and its parent OTE €3.25 million in 2022.",
  source_name="Hellenic Data Protection Authority", source_url="https://www.dpa.gr/en/enimerwtiko/news/fines-imposed-due-personal-data-breach-and-illegal-data-processing",
  statement=None,
  outcomes=[{"kind": "fine", "text": "Cosmote fined €6 million and OTE €3.25 million by Greece’s data protection authority", "year": 2022}])]},

 {"name": "South Staffordshire Water", "aliases": ["South Staffs Water", "South Staffordshire Plc", "Cambridge Water"], "website": "south-staffs-water.co.uk", "breaches": [B(
  title="Cyber attack on a water company", date="2020-09", status="confirmed", affected="633,887 people",
  categories=["Names", "Home addresses", "Customer account details", "Bank account details (some customers)"],
  description="An attacker got into the network of South Staffordshire Water, a UK water supplier, in September 2020 and stayed for almost two years before it was found in July 2022. Data of 633,887 people was then published on the dark web. The UK Information Commissioner’s Office found only 5% of its systems were monitored and fined it £963,900 in 2026.",
  source_name="UK Information Commissioner’s Office",
  source_url="https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/05/fine-of-nearly-1m-issued-against-south-staffordshire-plc-and-south-staffordshire-water-plc/",
  statement=None, disclosed="2022-08",
  outcomes=[{"kind": "fine", "text": "Fined £963,900 by the UK Information Commissioner’s Office", "year": 2026}])]},

 {"name": "Genea", "aliases": ["Genea Fertility"], "website": "genea.com.au", "breaches": [B(
  title="2025 attack on an IVF clinic", date="2025-01", status="confirmed", affected="Genea did not give a total",
  categories=["Names", "Contact details", "Medicare and health insurance details", "Medical history and treatment records"],
  description="From 31 January 2025 attackers were inside the systems of Genea, an Australian IVF provider, and took about 940 GB of data from its network, including its patient management system. Genea got a court order against anyone accessing or publishing the stolen data.",
  source_name="Genea (Supreme Court of NSW orders)",
  source_url="https://www.genea.com.au/sfsites/c/cms/delivery/media/MC32LVY2U5IFADDCDHSBHU4ZYQ4A?channelId=0apOd00000001Dp",
  statement=None, disclosed="2025-02",
  outcomes=[{"kind": "court", "text": "Court order banning anyone from accessing or publishing the stolen data", "year": 2025}])]},

 {"name": "MyDeal", "aliases": ["MyDeal.com.au", "Woolworths MyDeal"], "website": "mydeal.com.au", "breaches": [B(
  title="2022 breach of the customer database", date="2022-10", status="confirmed", affected="About 2.2 million customers",
  categories=["Names", "Email addresses", "Phone numbers", "Delivery addresses", "Dates of birth (some customers)"],
  description="In October 2022 someone used a stolen login to get into the customer system of MyDeal, an Australian online marketplace owned by Woolworths. About 2.2 million customers were affected; for 1.2 million only email addresses were exposed. Woolworths said payment details, ID documents and passwords were not taken.",
  source_name="Woolworths Group",
  source_url="https://www.woolworthsgroup.com.au/au/en/our-newsroom/media-releases/latest-news/2022/mydeal-data-breach-notification.html",
  statement=own("MyDeal data breach notification", "https://www.woolworthsgroup.com.au/au/en/our-newsroom/media-releases/latest-news/2022/mydeal-data-breach-notification.html"),
  disclosed="2022-10", outcomes=[])]},

 {"name": "HWL Ebsworth", "aliases": ["HWL Ebsworth Lawyers", "HWLE"], "website": "hwlebsworth.com.au", "breaches": [B(
  title="2023 ransomware attack on a law firm", date="2023-04", status="confirmed",
  affected="Clients and people named in its files; no total given",
  categories=["Legal case files containing personal information", "Client documents, including from government agencies"],
  description="In 2023 ransomware attackers stole files from HWL Ebsworth, one of Australia’s largest law firms, and published some of them. The files included client documents, among them material from Australian government agencies. Australia’s privacy regulator opened an investigation into how the firm protected personal information and told affected people.",
  source_name="Office of the Australian Information Commissioner",
  source_url="https://www.oaic.gov.au/news/media-centre/oaic-opens-investigation-into-hwl-ebsworth-over-data-breach",
  statement=None, disclosed="2023-05",
  outcomes=[{"kind": "investigation", "text": "Australia’s privacy regulator opened an investigation", "year": 2023}])]},

 {"name": "Juspay", "aliases": [], "website": "juspay.io", "breaches": [B(
  title="2020 breach of a payment company", date="2020-08", status="confirmed", affected="About 35 million card records",
  categories=["Masked card numbers", "Card fingerprints", "Email addresses", "Phone numbers"],
  description="On 18 August 2020 attackers got into a system of Juspay, an Indian payments company used by many big apps, and took about 35 million records with masked card numbers, along with email addresses and phone numbers. Juspay said full card numbers, PINs and order details were not taken, and disputed reports of a much larger breach.",
  source_name="Juspay", source_url="https://juspay.io/newsroom/your-security-our-first-concern-customer-transaction-related-data-is-secure",
  statement=own("Your security, our first concern: customer transaction-related data is secure", "https://juspay.io/newsroom/your-security-our-first-concern-customer-transaction-related-data-is-secure"),
  disclosed="2020-08", outcomes=[])]},

 {"name": "Hyatt", "aliases": ["Hyatt Hotels"], "website": "hyatt.com", "breaches": [B(
  title="2015 payment card malware at hotels", date="2015-08", status="confirmed",
  affected="Cards used at certain Hyatt hotels, mostly in restaurants; no total given",
  categories=["Cardholder names", "Payment card numbers", "Card expiry dates", "Card security codes"],
  description="Between August and December 2015 malware on payment systems at certain Hyatt-managed hotels, mostly in their restaurants, captured card details. Hyatt said no other customer information was affected and published a list of affected locations and dates.",
  source_name="Hyatt", source_url="https://newsroom.hyatt.com/news-releases?item=123453",
  statement=own("Hyatt Completes Payment Card Incident Investigation", "https://newsroom.hyatt.com/news-releases?item=123453"),
  disclosed="2015-12", outcomes=[])]},

 {"name": "Gemini", "aliases": ["Gemini Trust"], "website": "gemini.com", "breaches": [B(
  title="2022 leak through a supplier", date="2022-12", status="confirmed", affected="Gemini did not give a number",
  categories=["Email addresses", "Partial phone numbers"],
  description="In December 2022 a breach at a supplier of Gemini, a crypto exchange, exposed customers’ email addresses and partial phone numbers, which were then used in phishing campaigns. Gemini said its own systems and customer accounts and funds were not affected.",
  source_name="Gemini", source_url="https://www.gemini.com/blog/protecting-our-customers-from-phishing-campaigns",
  statement=own("Protecting Our Customers From Phishing Campaigns", "https://www.gemini.com/blog/protecting-our-customers-from-phishing-campaigns"),
  disclosed="2022-12", outcomes=[])]},
]

have = {c["name"].lower() for c in d["companies"]}
for c in new:
    assert c["name"].lower() not in have, "already in the database: " + c["name"]
d["companies"] += new
d["updated"] = "2026-11-18"
DATA.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("added %d companies, now %d" % (len(new), len(d["companies"])))
