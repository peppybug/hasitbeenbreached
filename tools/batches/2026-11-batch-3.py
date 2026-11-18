"""Batch 3 (November 2026): Asia, US healthcare and finance, and tech companies.

Run from the repository root:  python3 tools/batches/2026-11-batch-3.py
Then rebuild the pages:        python3 tools/build_pages.py
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "breaches.json"
d = json.loads(DATA.read_text(encoding="utf-8"))

def B(**k):
    return k

PIPC = "Personal Information Protection Commission (South Korea)"

new = [
 {"name": "LG Uplus", "aliases": ["LG U+", "LGU+"], "website": "lguplus.com", "breaches": [B(
  title="Theft of customer data from a mobile network operator", date="2022", status="confirmed", timing_unclear=True,
  affected="About 297,000 people",
  categories=["Names", "Phone numbers", "Home addresses", "Dates of birth", "SIM card (USIM) numbers"],
  description="A hacker took customer data from systems of LG Uplus, one of South Korea’s three big mobile operators, and offered it for sale. The company found out in January 2023. South Korea’s data protection commission found its security was inadequate and fined it 6.8 billion won (about US$5 million) in 2023, a record for a telecom company at the time.",
  source_name=PIPC,
  source_url="https://pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=9030",
  statement=None, disclosed="2023-01",
  outcomes=[{"kind": "fine", "text": "Fined 6.8 billion won by South Korea’s data protection commission", "year": 2023}])]},

 {"name": "Golfzon", "aliases": [], "website": "golfzon.com", "breaches": [B(
  title="2023 ransomware attack", date="2023-11", status="confirmed", affected="About 2.2 million users and employees",
  categories=["Names", "Phone numbers", "Resident registration numbers", "Bank account numbers (some people)"],
  description="In November 2023 ransomware attackers used an employee’s remote access login to get into Golfzon, a South Korean screen golf company, and took files from a shared server that held large amounts of personal data. The files were later published on the dark web. South Korea’s data protection commission fined Golfzon 7.5 billion won (about US$5.5 million) in 2024, then the largest fine it had given a company.",
  source_name=PIPC,
  source_url="https://pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=10158",
  statement=None,
  outcomes=[{"kind": "fine", "text": "Fined 7.5 billion won by South Korea’s data protection commission", "year": 2024}])]},

 {"name": "Benesse", "aliases": ["Benesse Holdings", "Benesse Corporation"], "website": "benesse.co.jp", "breaches": [B(
  title="Contractor employee sold customer data", date="2013", status="confirmed", timing_unclear=True,
  affected="About 29 million customers (35 million records sold)",
  categories=["Children’s names", "Parents’ names", "Home addresses", "Phone numbers", "Children’s dates of birth"],
  description="An employee of a contractor working on the systems of Benesse, a Japanese education company, used his access to copy customer data and sell it to list brokers. About 35 million records were sold, covering an estimated 29 million customers, many of them families with children. It came to light in July 2014. Japan’s trade ministry ordered improvements, and courts later held Benesse liable to compensate affected families.",
  source_name="Benesse (company report)",
  source_url="https://www.benesse.co.jp/customer/bcinfo/report.html",
  statement={"title": "Benesse’s report on the 2014 customer information leak (Japanese)", "url": "https://www.benesse.co.jp/customer/bcinfo/report.html"},
  disclosed="2014-07",
  outcomes=[{"kind": "order", "text": "Japan’s Ministry of Economy, Trade and Industry ordered improvements", "year": 2014},
            {"kind": "court", "text": "Appeal courts held Benesse liable to compensate affected customers", "year": 2019}])]},

 {"name": "LINE Yahoo", "aliases": ["LINE", "LY Corporation", "Yahoo Japan"], "website": "lycorp.co.jp", "breaches": [B(
  title="2023 breach through a contractor’s network", date="2023-10", status="confirmed",
  affected="About 510,000 records of users, business partners and employees",
  categories=["LINE user details such as age group and gender", "Service usage history", "Business partner and employee contact details"],
  description="Attackers got into LINE Yahoo’s systems through malware on a computer at a contractor of Naver, its Korean partner, which shared network access with the company. About 510,000 records were exposed. Japan’s communications ministry ordered LINE Yahoo twice in 2024 to fix its security and reduce its dependence on Naver.",
  source_name="LY Corporation (LINE Yahoo) report to the ministry",
  source_url="https://www.lycorp.co.jp/en/news/2024/20240401_appendix_en.pdf",
  statement={"title": "Report on measures to prevent recurrence (April 2024)", "url": "https://www.lycorp.co.jp/en/news/2024/20240401_appendix_en.pdf"},
  disclosed="2023-11",
  outcomes=[{"kind": "order", "text": "Japan’s communications ministry ordered security fixes, twice", "year": 2024}])]},

 {"name": "Marina Bay Sands", "aliases": ["MBS", "Sands LifeStyle"], "website": "marinabaysands.com", "breaches": [B(
  title="2023 breach of loyalty programme accounts", date="2023-10", status="confirmed", affected="665,495 members",
  categories=["Names", "Email addresses", "Phone numbers", "Countries of residence", "Membership numbers and tiers"],
  description="An attacker used the logins of six members to get into records of about 665,000 members of the Singapore resort’s non-casino loyalty programme. Singapore’s data protection commission found the resort left key security work during a system migration to a single employee, and fined it S$315,000 in 2025.",
  source_name="Personal Data Protection Commission Singapore",
  source_url="https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/commissions-decisions/gd_mbs_28102025(final)v2.pdf",
  statement=None, disclosed="2023-11",
  outcomes=[{"kind": "fine", "text": "Fined S$315,000 by Singapore’s data protection commission", "year": 2025}])]},

 {"name": "HCA Healthcare", "aliases": ["HCA"], "website": "hcahealthcare.com", "breaches": [B(
  title="2023 theft of patient contact data", date="2023-07", status="confirmed", affected="About 11 million patients",
  categories=["Names", "Home addresses", "Email addresses", "Phone numbers", "Dates of birth", "Appointment dates and locations"],
  description="In July 2023 a list of HCA patient information appeared on an online forum. It came from an outside storage location HCA used to send emails such as appointment reminders. About 11 million patients of the large US hospital group were affected. HCA said it did not include medical, payment or Social Security details.",
  source_name="HCA Healthcare",
  source_url="https://investor.hcahealthcare.com/news/news-details/2023/HCA-Healthcare-Reports-Data-Security-Incident/default.aspx",
  statement={"title": "HCA Healthcare Reports Data Security Incident", "url": "https://investor.hcahealthcare.com/news/news-details/2023/HCA-Healthcare-Reports-Data-Security-Incident/default.aspx"},
  disclosed="2023-07", outcomes=[])]},

 {"name": "loanDepot", "aliases": [], "website": "loandepot.com", "breaches": [B(
  title="2024 ransomware attack", date="2024-01", status="confirmed", affected="About 16.9 million people",
  categories=["Names", "Home addresses", "Email addresses", "Phone numbers", "Dates of birth", "Social Security numbers", "Bank account numbers"],
  description="In January 2024 attackers got into systems of loanDepot, a large US mortgage lender, and took sensitive personal information of about 16.9 million people. Customers couldn’t make payments online for a while. The company set aside $25 million to settle class actions.",
  source_name="loanDepot filing (US Securities and Exchange Commission)",
  source_url="https://www.sec.gov/Archives/edgar/data/1831631/000183163124000011/pressrelease.htm",
  statement={"title": "loanDepot update on cyber incident", "url": "https://www.sec.gov/Archives/edgar/data/1831631/000183163124000011/pressrelease.htm"},
  disclosed="2024-01",
  outcomes=[{"kind": "settlement", "text": "Set aside $25 million to settle class actions", "year": 2024}])]},

 {"name": "Mr. Cooper", "aliases": ["Mr Cooper", "Nationstar Mortgage"], "website": "mrcooper.com", "breaches": [B(
  title="2023 cyber attack on a mortgage company", date="2023-10", status="confirmed",
  affected="Substantially all current and former customers, about 14.7 million people",
  categories=["Names", "Home addresses", "Phone numbers", "Dates of birth", "Social Security numbers", "Bank account numbers"],
  description="On 31 October 2023 Mr. Cooper, one of the largest US mortgage servicers, found attackers in its systems and shut many of them down, so customers couldn’t make payments for days. The company later said personal information of substantially all its current and former customers had been taken, about 14.7 million people.",
  source_name="Mr. Cooper filing (US Securities and Exchange Commission)",
  source_url="https://www.sec.gov/Archives/edgar/data/933136/000093313623000109/nsm-20231102.htm",
  statement=None, disclosed="2023-11", outcomes=[])]},

 {"name": "Ascension", "aliases": ["Ascension Health"], "website": "ascension.org", "breaches": [B(
  title="2024 ransomware attack on a hospital network", date="2024-05", status="confirmed", affected="About 5.6 million people",
  categories=["Names", "Medical information", "Health insurance details", "Payment information", "Government ID numbers"],
  description="In May 2024 a ransomware attack hit Ascension, one of the largest US hospital networks, and staff had to work on paper for weeks. Files with patient and staff information were taken. Ascension later notified about 5.6 million people.",
  source_name="Ascension financial statements",
  source_url="https://about.ascension.org/-/media/project/ascension/about/section-about/financials/2025/consolidated-ascension-financial-statements-q3-fy25.pdf",
  statement=None, disclosed="2024-05", outcomes=[])]},

 {"name": "Yale New Haven Health", "aliases": ["YNHHS", "Yale New Haven Hospital"], "website": "ynhhs.org", "breaches": [B(
  title="2025 theft of patient data", date="2025-03", status="confirmed", affected="About 5.5 million people",
  categories=["Names", "Dates of birth", "Home addresses", "Phone numbers", "Email addresses", "Social Security numbers (some patients)", "Medical record numbers"],
  description="On 8 March 2025 an attacker got into the network of Yale New Haven Health, Connecticut’s largest health system, and copied patient data. About 5.5 million people were affected. The health system said medical records and treatment information, and payment details, were not accessed.",
  source_name="Yale New Haven Health",
  source_url="https://www.ynhhs.org/news/yale-new-haven-health-notifies-patients-of-data-security-incident",
  statement={"title": "Yale New Haven Health notifies patients of data security incident", "url": "https://www.ynhhs.org/news/yale-new-haven-health-notifies-patients-of-data-security-incident"},
  disclosed="2025-03", outcomes=[])]},

 {"name": "MyHeritage", "aliases": [], "website": "myheritage.com", "breaches": [B(
  title="Leak of email addresses and passwords", date="2017-10", status="confirmed", affected="92,283,889 users",
  categories=["Email addresses", "Hashed passwords"],
  description="In June 2018 a security researcher found a file on an outside server with the email addresses and scrambled (hashed) passwords of everyone who had signed up to the family history site up to October 2017. MyHeritage said DNA data is stored separately and was not affected, reset all passwords and added two-step login.",
  source_name="MyHeritage",
  source_url="https://blog.myheritage.com/2018/06/myheritage-statement-about-a-cybersecurity-incident/",
  statement={"title": "MyHeritage Statement About a Cybersecurity Incident", "url": "https://blog.myheritage.com/2018/06/myheritage-statement-about-a-cybersecurity-incident/"},
  disclosed="2018-06", outcomes=[])]},

 {"name": "Quora", "aliases": [], "website": "quora.com", "breaches": [B(
  title="2018 breach of user accounts", date="2018-11", status="confirmed", affected="About 100 million users",
  categories=["Names", "Email addresses", "Hashed passwords", "Data imported from linked social networks", "Private activity such as direct messages"],
  description="In November 2018 an attacker got into Quora’s systems. Account details of about 100 million users were exposed, including names, email addresses, scrambled passwords and data imported from linked networks, along with private activity such as direct messages. Quora logged out affected users and reset their passwords.",
  source_name="Quora",
  source_url="https://help.quora.com/hc/en-us/articles/360020212652-Quora-Security-Update-FAQ",
  statement={"title": "Quora Security Update – FAQ", "url": "https://help.quora.com/hc/en-us/articles/360020212652-Quora-Security-Update-FAQ"},
  disclosed="2018-12", outcomes=[])]},

 {"name": "DoorDash", "aliases": [], "website": "doordash.com", "breaches": [B(
  title="2019 breach through a third-party provider", date="2019-05", status="confirmed", affected="About 4.9 million customers, drivers and restaurants",
  categories=["Names", "Email addresses", "Delivery addresses", "Phone numbers", "Order history", "Hashed passwords", "Last four digits of payment cards (some customers)", "Driver’s licence numbers (about 100,000 drivers)"],
  description="In May 2019 an attacker got into DoorDash data through a third-party service provider. About 4.9 million customers, delivery drivers and restaurants who joined before April 2018 were affected. DoorDash said full card numbers were not taken.",
  source_name="DoorDash",
  source_url="https://blog.doordash.com/important-security-notice-about-your-doordash-account-ddd90ddf5996",
  statement={"title": "Important security notice about your DoorDash account", "url": "https://blog.doordash.com/important-security-notice-about-your-doordash-account-ddd90ddf5996"},
  disclosed="2019-09", outcomes=[])]},

 {"name": "Hertz", "aliases": ["Dollar", "Thrifty"], "website": "hertz.com", "breaches": [B(
  title="Data taken through a file transfer supplier", date="2024-10", status="confirmed", timing_unclear=True,
  affected="Customers in several countries; Hertz did not give a total",
  categories=["Names", "Contact details", "Dates of birth", "Driver’s licence details", "Payment card details", "Passport details (very few people)"],
  description="Attackers used security flaws in Cleo, file transfer software from a Hertz supplier, in late 2024 and took Hertz customer data. Hertz confirmed it in February 2025 and told customers in the US, Europe, Australia and elsewhere. It offered two years of free identity monitoring.",
  source_name="Hertz",
  source_url="https://www.hertz.com/content/dam/hertz/global/resources/Notice_of_Data_Incident-United_States.pdf",
  statement={"title": "Notice of Data Incident", "url": "https://www.hertz.com/content/dam/hertz/global/resources/Notice_of_Data_Incident-United_States.pdf"},
  disclosed="2025-04", outcomes=[])]},

 {"name": "DaVita", "aliases": [], "website": "davita.com", "breaches": [B(
  title="2025 ransomware attack on a kidney care provider", date="2025-04", status="confirmed", affected="About 2.7 million people",
  categories=["Names", "Home addresses", "Dates of birth", "Social Security numbers", "Health insurance details", "Lab test results", "Clinical information"],
  description="In April 2025 ransomware hit DaVita, a large US dialysis provider, and attackers took data, mainly from its laboratory business. About 2.7 million patients and former patients were notified. Billing and new patient intake were disrupted.",
  source_name="DaVita filing (US Securities and Exchange Commission)",
  source_url="https://www.sec.gov/Archives/edgar/data/927066/000119312525079593/d948299d8k.htm",
  statement=None, disclosed="2025-04", outcomes=[])]},

 {"name": "Delta Dental of California", "aliases": ["Delta Dental"], "website": "deltadentalins.com", "breaches": [B(
  title="2023 MOVEit file transfer breach", date="2023-05", status="confirmed", affected="About 7 million people",
  categories=["Names", "Social Security numbers", "Driver’s licence numbers", "Bank account details", "Health information"],
  description="Between 28 and 30 May 2023 attackers used a flaw in MOVEit file transfer software, which thousands of organisations used, to take files from Delta Dental of California and its affiliates. About 7 million people were affected.",
  source_name="Delta Dental of California",
  source_url="https://www1.deltadentalins.com/content/dam/ddins/en/pdf/banners/notice-of-moveit-data-security-incident-en.pdf",
  statement={"title": "Notice of MOVEit Data Security Incident", "url": "https://www1.deltadentalins.com/content/dam/ddins/en/pdf/banners/notice-of-moveit-data-security-incident-en.pdf"},
  disclosed="2023-12", outcomes=[])]},

 {"name": "Trezor", "aliases": ["SatoshiLabs"], "website": "trezor.io", "breaches": [B(
  title="2024 breach of a support ticket system", date="2024-01", status="confirmed", affected="Up to 66,000 users",
  categories=["Email addresses", "Names or nicknames"],
  description="In January 2024 someone got unauthorised access to the outside support ticket system used by Trezor, a maker of crypto hardware wallets. Contact details of up to 66,000 people who had contacted support were exposed, and the intruder emailed some of them asking for their recovery phrases. Trezor said no funds or recovery phrases were compromised.",
  source_name="Trezor",
  source_url="https://blog.trezor.io/trezor-security-update-stay-vigilant-against-potential-phishing-attack-bb05015a21f8",
  statement={"title": "Trezor security alert: Stay vigilant against a potential phishing attack", "url": "https://blog.trezor.io/trezor-security-update-stay-vigilant-against-potential-phishing-attack-bb05015a21f8"},
  disclosed="2024-01", outcomes=[])]},
]

have = {c["name"].lower() for c in d["companies"]}
for c in new:
    assert c["name"].lower() not in have, "already in the database: " + c["name"]
d["companies"] += new
d["updated"] = "2026-11-18"
DATA.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("added %d companies, now %d" % (len(new), len(d["companies"])))
