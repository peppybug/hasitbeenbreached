"""Batch 10 (November 2026): New York Attorney General and financial regulator settlements, mostly health care.

Run from the repository root:  python3 tools/batches/2026-11-batch-10.py
Then rebuild the pages:        python3 tools/build_pages.py
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "breaches.json"
d = json.loads(DATA.read_text(encoding="utf-8"))

def B(**k):
    return k

NYAG = "New York State Attorney General"
DFS = "New York State Department of Financial Services"

new = [
 {"name": "Personal Touch Home Care", "aliases": ["Personal Touch", "Personal Touch Holding Corp"], "website": "pthomecare.com", "breaches": [B(
  title="2021 ransomware attack on a home care company", date="2021-01", status="confirmed", affected="About 316,845 New Yorkers",
  categories=["Names", "Health and medical information", "Health insurance details", "Employee personal data"],
  description="In January 2021 an employee of Personal Touch, a Long Island home health care company, opened a malicious attachment in a phishing email, which let ransomware attackers in. Unencrypted patient files of about 316,845 New Yorkers were exposed. In 2023 Personal Touch paid $350,000 to New York State and offered free credit monitoring.",
  source_name=NYAG, source_url="https://ag.ny.gov/press-release/2023/attorney-general-james-secures-350000-long-island-home-health-care-company",
  statement=None,
  outcomes=[{"kind": "settlement", "text": "Paid $350,000 to New York State", "year": 2023}])]},

 {"name": "Practicefirst", "aliases": ["Practicefirst Medical Management Solutions", "Professional Business Systems", "PBS Medcode"], "website": "practicefirst.com", "breaches": [B(
  title="2020 ransomware attack on a medical billing company", date="2020-12", status="confirmed", affected="More than 1.2 million people",
  categories=["Names", "Home addresses", "Dates of birth", "Social Security numbers", "Driver’s licence numbers", "Medical information"],
  description="In December 2020 ransomware attackers took 79,000 files from Practicefirst, a medical management company in Erie County, New York, that handles billing for doctors. More than 1.2 million people were affected. New York’s Attorney General found it had not updated its software or tested its security, and it paid $550,000 in 2023.",
  source_name=NYAG, source_url="https://ag.ny.gov/press-release/2023/attorney-general-james-recoups-550000-erie-county-medical-management-company",
  statement=None,
  outcomes=[{"kind": "settlement", "text": "Paid $550,000 to New York State", "year": 2023}])]},

 {"name": "Refuah Health Center", "aliases": ["Refuah Health"], "website": "refuahhealth.org", "breaches": [B(
  title="2021 ransomware attack on a health centre", date="2021-05", status="confirmed", affected="More than 260,000 patients",
  categories=["Names", "Home addresses", "Social Security numbers", "Driver’s licence numbers", "Bank account numbers", "Health insurance numbers", "Health information"],
  description="In May 2021 ransomware attackers got into Refuah Health Center, a Hudson Valley health provider, and reached files on more than 260,000 patients. It had not closed old accounts, used two-step login or encrypted patient data. In 2024 it agreed to spend $1.2 million on security and pay New York State.",
  source_name=NYAG, source_url="https://ag.ny.gov/press-release/2024/attorney-general-james-reaches-agreement-hudson-valley-health-care-provider",
  statement=None,
  outcomes=[{"kind": "settlement", "text": "Agreed to spend $1.2 million on security and pay $450,000 ($100,000 suspended)", "year": 2024}])]},

 {"name": "Albany ENT & Allergy", "aliases": ["AENT", "Albany ENT & Allergy Services"], "website": "albanyentandallergy.com", "breaches": [B(
  title="2023 ransomware attacks on a medical practice", date="2023", status="confirmed", timing_unclear=True, affected="213,935 New Yorkers",
  categories=["Names", "Dates of birth", "Social Security numbers (some patients)", "Health records"],
  description="In 2023 ransomware attackers got into the systems of Albany ENT & Allergy, a medical practice in New York’s Capital Region, and reached patient records of 213,935 New Yorkers. It had no in-house security expert and did not properly oversee its IT suppliers. In 2024 it agreed to pay $500,000 and spend $2.25 million on security.",
  source_name=NYAG, source_url="https://ag.ny.gov/press-release/2024/attorney-general-james-secures-225-million-capital-region-health-care-provider",
  statement=None,
  outcomes=[{"kind": "settlement", "text": "Paid $500,000 and agreed to spend $2.25 million on security", "year": 2024}])]},

 {"name": "Healthplex", "aliases": [], "website": "healthplex.com", "breaches": [B(
  title="2021 phishing attack on a dental insurer", date="2021-11", status="confirmed", affected="Tens of thousands of consumers",
  categories=["Health information", "Dental insurance ID numbers", "Names"],
  description="In late 2021 a customer service employee at Healthplex, a New York dental insurance company, clicked a phishing email and gave attackers access to an email account holding consumer health data. It had no two-step login on email and reported the breach months late. New York’s financial regulator fined it $2 million in 2025.",
  source_name=DFS, source_url="https://www.dfs.ny.gov/reports_and_publications/press_releases/pr20250814",
  statement=None,
  outcomes=[{"kind": "fine", "text": "Fined $2 million by New York’s financial regulator", "year": 2025}])]},

 {"name": "Unum", "aliases": ["First Unum", "Paul Revere Life Insurance", "Unum Group"], "website": "unum.com", "breaches": [B(
  title="Phishing of employee email accounts", date="2018-09", status="confirmed", affected="Thousands of customers nationally",
  categories=["Customer personal information and insurance claims", "Health information (some customers)"],
  description="From September 2018 phishing emails tricked employees of First Unum and Paul Revere, US insurers owned by Unum, into giving away their email passwords. Customer data in those mailboxes was exposed. The companies had not fully set up two-step login, despite certifying they had. New York’s financial regulator fined them $1.8 million in 2021.",
  source_name=DFS, source_url="https://www.dfs.ny.gov/reports_and_publications/press_releases/pr202105131",
  statement=None,
  outcomes=[{"kind": "fine", "text": "Fined $1.8 million by New York’s financial regulator", "year": 2021}])]},

 {"name": "Heidell, Pittoni, Murphy & Bach", "aliases": ["HPMB"], "website": "hpmb.com", "breaches": [B(
  title="2021 ransomware attack on a law firm", date="2021-12", status="confirmed",
  affected="Patients and others named in legal files; no total given in the summary",
  categories=["Medical and personal information in legal files"],
  description="Around Christmas 2021 LockBit ransomware hit HPMB, a New York law firm that represents hospitals in lawsuits, and the firm paid a $100,000 ransom. Its files held patients’ medical and personal information. The firm later settled with New York’s Attorney General.",
  source_name=NYAG, source_url="https://ag.ny.gov/sites/default/files/aod_-_final_hpmb.pdf",
  statement=None,
  outcomes=[{"kind": "settlement", "text": "Settled with New York’s Attorney General", "year": 2023}])]},

 {"name": "National Amusements", "aliases": ["Showcase Cinemas"], "website": "nationalamusements.com", "breaches": [B(
  title="Breach of employee data at a cinema company", date="2022", status="confirmed", timing_unclear=True,
  affected="More than 23,000 New York employees and contractors",
  categories=["Names", "Dates of birth", "Social Security numbers", "Passport numbers", "Bank account numbers", "Driver’s licence numbers", "Health insurance account numbers"],
  description="An attacker used an employee’s stolen VPN login, which had no two-step login, to get into the network of National Amusements, which runs Showcase Cinemas. Data of more than 23,000 New York employees and contractors was exposed, and the company waited over a year to tell them. It said cinema customers were not affected. It paid $250,000 to New York State in 2024.",
  source_name=NYAG, source_url="https://ag.ny.gov/press-release/2024/attorney-general-james-secures-250000-movie-theater-operator-failing-protect",
  statement=None,
  outcomes=[{"kind": "settlement", "text": "Paid $250,000 to New York State", "year": 2024}])]},

 {"name": "HealthAlliance", "aliases": ["HealthAlliance Hospital", "Margaretville Hospital"], "website": "hahv.org", "breaches": [B(
  title="2023 attack through an unpatched flaw", date="2023-09", status="confirmed", affected="About 242,641 New Yorkers",
  categories=["Names", "Home addresses", "Dates of birth", "Social Security numbers", "Medical diagnoses", "Lab test results", "Medications (health information)"],
  description="HealthAlliance, which runs hospitals in New York’s Hudson Valley, knew of a security flaw but couldn’t patch it and kept the system running. In September and October 2023 attackers used it to steal patient and employee records. In 2024 it agreed to a $1.4 million penalty, of which it pays $550,000.",
  source_name=NYAG, source_url="https://ag.ny.gov/press-release/2024/attorney-general-james-secures-550000-hudson-valley-health-care-facility",
  statement=None,
  outcomes=[{"kind": "settlement", "text": "Agreed to a $1.4 million penalty, paying $550,000 (the rest suspended)", "year": 2024}])]},

 {"name": "Wojeski & Company", "aliases": [], "website": "wojeski.com", "breaches": [B(
  title="Ransomware attack and data breach at an accounting firm", date="2023-07", status="confirmed", affected="More than 4,700 New Yorkers",
  categories=["Names", "Dates of birth", "Social Security numbers", "Driver’s licence numbers", "Bank account numbers", "Medical benefits information"],
  description="Wojeski & Company, an accounting firm in Albany, New York, suffered a ransomware attack in July 2023 and a data breach in May 2024, exposing clients’ personal and financial details. In 2025 it paid $60,000 to New York State and agreed to tighten its security.",
  source_name=NYAG, source_url="https://ag.ny.gov/press-release/2025/attorney-general-james-announces-settlement-accounting-firm-failing-protect-new",
  statement=None,
  outcomes=[{"kind": "settlement", "text": "Paid $60,000 to New York State", "year": 2025}])]},

 {"name": "US Radiology Specialists", "aliases": ["Windsong Radiology"], "website": "usradiology.com", "breaches": [B(
  title="2021 attack through an old network device", date="2021-12", status="confirmed", affected="198,260 patients",
  categories=["Names", "Dates of birth", "Social Security numbers", "Health insurance details", "Medical information"],
  description="In December 2021 an attacker used a known flaw in outdated network hardware to get into US Radiology Specialists and stole personal and health information of 198,260 patients of Windsong Radiology in Western New York. In 2023 it paid $450,000 to New York State.",
  source_name=NYAG, source_url="https://ag.ny.gov/press-release/2023/attorney-general-james-secures-450000-medical-company-providing-services-western",
  statement=None,
  outcomes=[{"kind": "settlement", "text": "Paid $450,000 to New York State", "year": 2023}])]},

 {"name": "OrthopedicsNY", "aliases": ["OrthoNY"], "website": "orthony.com", "breaches": [B(
  title="2023 theft of patient and employee files", date="2023", status="confirmed", timing_unclear=True, affected="About 656,000 people",
  categories=["Names", "Social Security numbers (about 110,000 people)", "Health information"],
  description="In 2023 attackers used a stolen login to get remote access to the network of OrthopedicsNY, an orthopaedic practice in New York’s Capital Region, and downloaded unencrypted files about 656,000 patients and employees. In 2025 it paid $500,000 to New York State and funded a year of free credit monitoring.",
  source_name=NYAG, source_url="https://ag.ny.gov/press-release/2025/attorney-general-james-secures-500000-capital-region-health-care-provider",
  statement=None,
  outcomes=[{"kind": "settlement", "text": "Paid $500,000 to New York State", "year": 2025}])]},

 {"name": "Sports Warehouse", "aliases": ["Tennis Warehouse", "Running Warehouse"], "website": "tennis-warehouse.com", "breaches": [B(
  title="Theft from a server of card data stored since 2002", date="2020", status="confirmed", timing_unclear=True,
  affected="Up to 1.8 million payment cards and 1.2 million logins",
  categories=["Payment card numbers (stored unencrypted)", "Account logins"],
  description="An attacker got into the shop server of Sports Warehouse, which runs online stores such as Tennis Warehouse and Running Warehouse. It held payment card details for nearly every purchase since 2002, in plain text, plus customer logins. In 2023 the company paid $300,000 to New York State.",
  source_name=NYAG, source_url="https://ag.ny.gov/press-release/2023/attorney-general-james-secures-300000-online-sporting-goods-retailers-failing",
  statement=None,
  outcomes=[{"kind": "settlement", "text": "Paid $300,000 to New York State", "year": 2023}])]},
]

have = {c["name"].lower() for c in d["companies"]}
for c in new:
    assert c["name"].lower() not in have, "already in the database: " + c["name"]
d["companies"] += new
d["updated"] = "2026-11-18"
DATA.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("added %d companies, now %d" % (len(new), len(d["companies"])))
