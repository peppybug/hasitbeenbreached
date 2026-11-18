"""Batch 9 (November 2026): New York Attorney General settlements, payments and automotive.

Run from the repository root:  python3 tools/batches/2026-11-batch-9.py
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

NYAG = "New York State Attorney General"
CARD = ["Cardholder names", "Payment card numbers", "Card expiry dates", "Card security codes"]

new = [
 {"name": "Global Payments", "aliases": [], "website": "globalpayments.com", "breaches": [B(
  title="2012 theft of card data from a payment processor", date="2012", status="confirmed", timing_unclear=True,
  affected="Fewer than 1.5 million card numbers may have been taken",
  categories=["Payment card data read from the card (numbers and expiry dates)"],
  description="In early 2012 attackers got into part of the processing system of Global Payments, a large US card payment processor, in North America and may have taken card data. The company said fewer than 1.5 million card numbers could have been exported, and that names, addresses and Social Security numbers were not taken. It recorded a pre-tax charge of $84.4 million.",
  source_name="Global Payments filing (US Securities and Exchange Commission)",
  source_url="https://www.sec.gov/Archives/edgar/data/0001123360/000112336012000025/april12012pressrelease.htm",
  statement=own("Global Payments update on data security incident (April 2012)", "https://www.sec.gov/Archives/edgar/data/0001123360/000112336012000025/april12012pressrelease.htm"),
  disclosed="2012-03", outcomes=[])]},

 {"name": "Nissan Oceania", "aliases": ["Nissan Australia", "Nissan New Zealand", "Nissan Financial Services"], "website": "nissan.com.au", "breaches": [B(
  title="2023 ransomware attack in Australia and New Zealand", date="2023-12", status="confirmed",
  affected="Customers, staff and others in Australia and New Zealand; no total given in the notice",
  categories=["Names", "Contact details", "Copies of driver’s licences, passports, Medicare cards and visas (some people)", "Tax file numbers (some people)", "Loan details"],
  description="In December 2023 attackers got into the systems of Nissan’s Australian and New Zealand businesses, including Nissan Financial Services, and later published stolen data on the dark web. For some people this included copies of ID documents and tax file numbers. Nissan offered credit monitoring and paid to replace ID documents.",
  source_name="Nissan Oceania", source_url="https://www.nissan.com.au/content/dam/Nissan/AU/Files/notice/Notice-%20Cyber%20security%20incident%20impacting%20Nissan%20Australia%20and%20New%20Zealand.pdf",
  statement=own("Notice: Cyber security incident impacting Nissan Australia and New Zealand", "https://www.nissan.com.au/content/dam/Nissan/AU/Files/notice/Notice-%20Cyber%20security%20incident%20impacting%20Nissan%20Australia%20and%20New%20Zealand.pdf"),
  disclosed="2023-12", outcomes=[])]},

 {"name": "Wegmans", "aliases": ["Wegmans Food Markets"], "website": "wegmans.com", "breaches": [B(
  title="Customer data left open in the cloud", date="2018-01", status="confirmed", affected="More than 3 million customers",
  categories=["Email addresses", "Account passwords", "Names", "Home addresses", "Data derived from driver’s licence numbers"],
  description="Two cloud storage containers of Wegmans, a US supermarket chain, were set up so anyone could reach them, one of them since January 2018. They held customer database backups, including email addresses and passwords, until a researcher reported it in April 2021. In 2022 Wegmans paid $400,000 to New York State and agreed to tighten its security.",
  source_name=NYAG, source_url="https://ag.ny.gov/press-release/2022/attorney-general-james-secures-400000-wegmans-after-data-breach-exposed-consumers",
  statement=None, disclosed="2021-06",
  outcomes=[{"kind": "settlement", "text": "Paid $400,000 to New York State", "year": 2022}])]},

 {"name": "Dunkin’", "aliases": ["Dunkin", "Dunkin'", "Dunkin' Donuts", "DD Perks"], "website": "dunkindonuts.com", "breaches": [B(
  title="Repeated break-ins to customer accounts", date="2015", status="confirmed", timing_unclear=True,
  affected="Tens of thousands of customer accounts",
  categories=["Account logins", "Gift card account balances", "Names", "Email addresses"],
  description="From 2015 attackers used passwords leaked from other sites to break into tens of thousands of Dunkin’ app and website accounts and use the money on stored cards. New York’s Attorney General sued, saying Dunkin’ did not properly investigate or tell customers. In 2020 Dunkin’ agreed to pay $650,000, refund customers and reset passwords.",
  source_name=NYAG, source_url="https://ag.ny.gov/press-release/2020/attorney-general-james-gets-dunkin-fill-holes-security-reimburse-hacked-customers",
  statement=None,
  outcomes=[{"kind": "court", "text": "Sued by New York’s Attorney General", "year": 2019},
            {"kind": "settlement", "text": "Paid $650,000 to New York and agreed to refund customers", "year": 2020}])]},

 {"name": "Trump Hotels", "aliases": ["Trump Hotel Collection", "Trump SoHo"], "website": "trumphotels.com", "breaches": [B(
  title="Two hotel payment card breaches", date="2014", status="confirmed", timing_unclear=True, affected="More than 70,000 payment cards",
  categories=CARD,
  description="Attackers put card-stealing malware on 39 systems at five Trump hotels, including Trump SoHo New York, and a second breach followed in 2016. More than 70,000 card numbers were exposed. In 2016 the company paid $50,000 to New York State and agreed to improve its security.",
  source_name=NYAG, source_url="https://ag.ny.gov/press-release/2016/ag-schneiderman-announces-settlement-trump-hotel-collection-after-data-breaches",
  statement=None,
  outcomes=[{"kind": "settlement", "text": "Paid $50,000 to New York State", "year": 2016}])]},

 {"name": "TD Bank", "aliases": ["TD Bank N.A."], "website": "td.com", "breaches": [B(
  title="Lost unencrypted backup tapes", date="2012-03", status="confirmed", affected="About 260,000 customers",
  categories=["Names", "Home addresses", "Social Security numbers", "Bank account numbers"],
  description="In 2012 TD Bank lost unencrypted backup tapes in transit in Massachusetts. They held personal information of about 260,000 US customers. In 2014 the bank settled with nine US states and agreed to encrypt backup tapes before moving them.",
  source_name=NYAG, source_url="https://ag.ny.gov/press-release/2014/ag-schneiderman-announces-multi-state-settlement-td-bank-over-data-breach",
  statement=None,
  outcomes=[{"kind": "settlement", "text": "Settled with nine US states", "year": 2014}])]},

 {"name": "Filters Fast", "aliases": [], "website": "filtersfast.com", "breaches": [B(
  title="2019–2020 theft of card data at checkout", date="2019-07", status="confirmed", affected="About 320,000 customers",
  categories=CARD + ["Billing addresses"],
  description="From July 2019 to July 2020 attackers used a known flaw in the checkout of Filters Fast, a US online seller of water and air filters, to steal card details. The company missed a warning in February 2020 and only told customers in August 2020. It paid New York State in 2021 and agreed to a full security programme.",
  source_name=NYAG, source_url="https://ag.ny.gov/press-release/2021/attorney-general-james-announces-agreement-filters-fast-after-2019-data-breach",
  statement=None, disclosed="2020-08",
  outcomes=[{"kind": "settlement", "text": "Agreed to pay $200,000 to New York State ($100,000 suspended)", "year": 2021}])]},

 {"name": "Root Insurance", "aliases": ["Root"], "website": "joinroot.com", "breaches": [B(
  title="Attacks on the online quote tool", date="2021-01", status="confirmed", affected="About 72,852 driver’s licence numbers",
  categories=["Driver’s licence numbers"],
  description="From January 2021 scammers used Root’s online car insurance quote tool, which showed full driver’s licence numbers in a PDF, to collect about 73,000 licence numbers, mostly of New Yorkers, for unemployment fraud. In 2025 Root paid $975,000 to New York State.",
  source_name=NYAG, source_url="https://ag.ny.gov/press-release/2025/attorney-general-james-secures-975000-auto-insurance-company-over-data-breach",
  statement=None,
  outcomes=[{"kind": "settlement", "text": "Paid $975,000 to New York State", "year": 2025}])]},

 {"name": "Noblr", "aliases": [], "website": "noblr.com", "breaches": [B(
  title="Attacks on the online quote tool", date="2021-01", status="confirmed", affected="More than 80,000 New Yorkers",
  categories=["Driver’s licence numbers"],
  description="Noblr’s online car insurance quote tool showed full driver’s licence numbers in several places. From January 2021 scammers abused it to collect licence numbers, some used for unemployment fraud during the pandemic. Noblr was slow to notice because it did not watch site traffic in real time. It paid $500,000 to New York State in 2024.",
  source_name=NYAG, source_url="https://ag.ny.gov/press-release/2024/attorney-general-james-secures-500000-auto-insurance-company-over-data-breach",
  statement=None,
  outcomes=[{"kind": "settlement", "text": "Paid $500,000 to New York State", "year": 2024}])]},

 {"name": "Acer", "aliases": ["Acer Service Corporation"], "website": "acer.com", "breaches": [B(
  title="Theft of card data from the online store", date="2015", status="confirmed", timing_unclear=True,
  affected="More than 35,000 payment cards",
  categories=CARD + ["Home addresses"],
  description="Attackers took card details from customers of Acer’s online store. Discover found Acer was the last legitimate shop used by hundreds of cards later used for fraud. In 2017 Acer paid $115,000 to New York State and agreed to keep up card industry security standards.",
  source_name=NYAG, source_url="https://ag.ny.gov/press-release/2017/ag-schneiderman-announces-settlement-computer-manufacturer-after-data-breach",
  statement=None,
  outcomes=[{"kind": "settlement", "text": "Paid $115,000 to New York State", "year": 2017}])]},

 {"name": "EmblemHealth", "aliases": ["Group Health Incorporated", "GHI"], "website": "emblemhealth.com", "breaches": [B(
  title="Social Security numbers printed on mailing labels", date="2016-10", status="confirmed", affected="81,122 members",
  categories=["Social Security numbers (printed on mailing labels)", "Names", "Home addresses"],
  description="In 2016 EmblemHealth, a New York health insurer, posted Medicare drug plan packets to 81,122 members with each person’s Social Security number printed on the mailing label, as part of their insurance claim number. In 2018 it paid $575,000 to New York State and agreed to check its mailings.",
  source_name=NYAG, source_url="https://ag.ny.gov/press-release/2018/ag-schneiderman-announces-575000-settlement-emblemhealth-after-data-breach",
  statement=None, disclosed="2016-10",
  outcomes=[{"kind": "settlement", "text": "Paid $575,000 to New York State", "year": 2018}])]},

 {"name": "Nationwide", "aliases": ["Nationwide Mutual Insurance", "Allied Insurance"], "website": "nationwide.com", "breaches": [B(
  title="2012 hack of insurance quote data", date="2012-10", status="confirmed", affected="1.27 million people",
  categories=["Names", "Social Security numbers", "Driver’s licence numbers", "Credit scores", "Dates of birth", "Occupation and marital status"],
  description="In October 2012 hackers took data of 1.27 million people from Nationwide, a US insurer, through a flaw it had not patched. Many had only asked for a quote and never became customers, but Nationwide kept their data. In 2017 it paid $5.5 million to 33 US states.",
  source_name=NYAG, source_url="https://ag.ny.gov/press-release/2017/ag-schneiderman-announces-55-million-multi-state-settlement-nationwide-mutual",
  statement=None,
  outcomes=[{"kind": "settlement", "text": "Paid $5.5 million to 33 US states", "year": 2017}])]},

 {"name": "Marymount Manhattan College", "aliases": ["MMC"], "website": "mmm.edu", "breaches": [B(
  title="2021 ransomware attack on a college", date="2021-11", status="confirmed",
  affected="191,752 students, employees, alumni and applicants",
  categories=["Social Security numbers", "Bank and payment card details", "Passport and driver’s licence numbers", "Medical information"],
  description="In November 2021 a hacker got into the systems of Marymount Manhattan College in New York, accessed data of more than 190,000 current, past and prospective students and staff, and demanded a ransom, which the college paid. In 2023 it agreed with New York’s Attorney General to spend $3.5 million on security, including two-step login.",
  source_name=NYAG, source_url="https://ag.ny.gov/press-release/2023/attorney-general-james-reaches-agreement-marymount-manhattan-college-invest-35",
  statement=None,
  outcomes=[{"kind": "settlement", "text": "Agreed to spend $3.5 million on security under a deal with New York’s Attorney General", "year": 2023}])]},
]

have = {c["name"].lower() for c in d["companies"]}
for c in new:
    assert c["name"].lower() not in have, "already in the database: " + c["name"]
d["companies"] += new
d["updated"] = "2026-11-18"
DATA.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("added %d companies, now %d" % (len(new), len(d["companies"])))
