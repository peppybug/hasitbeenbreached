"""Batch 4 (November 2026): US health, insurance and retail breaches with regulator or attorney general action.

Run from the repository root:  python3 tools/batches/2026-11-batch-4.py
Then rebuild the pages:        python3 tools/build_pages.py
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "breaches.json"
d = json.loads(DATA.read_text(encoding="utf-8"))

def B(**k):
    return k

HHS = "US Department of Health and Human Services, Office for Civil Rights"
DFS = "New York State Department of Financial Services"
NYAG = "New York State Attorney General"

new = [
 {"name": "Premera Blue Cross", "aliases": ["Premera"], "website": "premera.com", "breaches": [B(
  title="2014 cyber attack on a health insurer", date="2014-05", status="confirmed", affected="More than 10.4 million people",
  categories=["Names", "Home addresses", "Dates of birth", "Email addresses", "Social Security numbers", "Bank account details", "Health plan clinical information"],
  description="In May 2014 attackers used a phishing email to put malware on the systems of Premera Blue Cross, a US health insurer, and went unnoticed for nearly nine months. Data of more than 10.4 million people was exposed. Premera paid $10 million to US states in 2019 and $6.85 million to the US health department in 2020, which found it had never properly assessed its security risks.",
  source_name=HHS, source_url="https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/agreements/premera/index.html",
  statement=None, disclosed="2015-03",
  outcomes=[{"kind": "settlement", "text": "Paid $10 million to US states", "year": 2019},
            {"kind": "settlement", "text": "Paid $6.85 million to the US health department", "year": 2020}])]},

 {"name": "Excellus Health Plan", "aliases": ["Excellus", "Excellus BlueCross BlueShield", "Lifetime Healthcare"], "website": "excellusbcbs.com", "breaches": [B(
  title="Cyber attack on a health insurer (2013–2015)", date="2013-12", status="confirmed", affected="9,358,891 people",
  categories=["Names", "Dates of birth", "Social Security numbers", "Home addresses", "Phone numbers", "Member ID numbers", "Bank account details", "Health claims information"],
  description="Attackers were inside the systems of Excellus, a New York health insurer, from December 2013 or earlier until May 2015. Data of more than 9.3 million people was exposed. In 2021 Excellus paid $5.1 million to the US health department, which found it had not properly assessed its security risks.",
  source_name=HHS, source_url="https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/agreements/excellus/index.html",
  statement=None, disclosed="2015-09",
  outcomes=[{"kind": "settlement", "text": "Paid $5.1 million to the US health department", "year": 2021}])]},

 {"name": "Banner Health", "aliases": [], "website": "bannerhealth.com", "breaches": [B(
  title="2016 cyber attack on a hospital system", date="2016-06", status="confirmed", affected="2.81 million people",
  categories=["Names", "Dates of birth", "Home addresses", "Social Security numbers", "Health insurance details", "Clinical information", "Payment card details (food outlets)"],
  description="In 2016 attackers got into the systems of Banner Health, a large hospital system in Arizona, and reached data of 2.81 million patients and others, as well as card data from its food outlets. The US health department found long-term, widespread failures to follow health data security rules. Banner paid $1.25 million in 2023.",
  source_name=HHS, source_url="https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/agreements/banner-health/index.html",
  statement=None, disclosed="2016-08",
  outcomes=[{"kind": "settlement", "text": "Paid $1.25 million to the US health department", "year": 2023}])]},

 {"name": "Carnival", "aliases": ["Carnival Cruise Line", "Princess Cruises", "Holland America Line", "Seabourn", "Costa Cruises"], "website": "carnivalcorp.com", "breaches": [B(
  title="Series of cyber incidents (2019–2021)", date="2019", status="confirmed", timing_unclear=True,
  affected="Guests and employees in four incidents; no total given",
  categories=["Names", "Home addresses", "Passport numbers", "Dates of birth", "Health information (some people)", "Social Security numbers (some people)"],
  description="Carnival’s cruise brands had four cyber incidents between 2019 and 2021, including phishing of employee email accounts and a 2020 ransomware attack, which exposed guest and employee data. New York’s financial regulator found they lacked two-step login and security training, and were slow to report. Carnival paid $5 million to New York and $1.25 million to 45 US states in 2022.",
  source_name=DFS, source_url="https://www.dfs.ny.gov/reports_and_publications/press_releases/pr202206241",
  statement=None,
  outcomes=[{"kind": "fine", "text": "Fined $5 million by New York’s financial regulator", "year": 2022},
            {"kind": "settlement", "text": "Paid $1.25 million to 45 US states", "year": 2022}])]},

 {"name": "EyeMed", "aliases": ["EyeMed Vision Care"], "website": "eyemed.com", "breaches": [B(
  title="2020 phishing attack on a shared mailbox", date="2020-06", status="confirmed", affected="About 2.1 million people",
  categories=["Names", "Home addresses", "Dates of birth", "Social Security numbers", "Health insurance numbers", "Eye health and treatment details"],
  description="In mid-2020 an attacker got into a shared email inbox at EyeMed, a vision insurance company, that held six years of customer data. Nine employees shared its password and it had no two-step login. New York’s financial regulator fined EyeMed $4.5 million in 2022.",
  source_name=DFS, source_url="https://www.dfs.ny.gov/reports_and_publications/press_releases/pr202210181",
  statement=None, disclosed="2020-09",
  outcomes=[{"kind": "fine", "text": "Fined $4.5 million by New York’s financial regulator", "year": 2022}])]},

 {"name": "Wawa", "aliases": [], "website": "wawa.com", "breaches": [B(
  title="2019 payment card malware", date="2019-03", status="confirmed", affected="About 34 million payment cards",
  categories=["Payment card numbers", "Card expiry dates", "Cardholder names"],
  description="Hackers got into the network of Wawa, a US convenience store and petrol station chain, and from spring to December 2019 used malware to take card details at its stores. About 34 million cards were affected. PINs and card security codes were not taken. Wawa paid $8 million to seven US states and Washington, DC in 2022.",
  source_name="New Jersey Office of the Attorney General",
  source_url="https://www.njoag.gov/acting-ag-platkin-co-leads-8-million-settlement-with-wawa-inc-over-data-breach-that-compromised-millions-of-payment-cards-in-new-jersey/",
  statement=None, disclosed="2019-12",
  outcomes=[{"kind": "settlement", "text": "Paid $8 million to seven US states and Washington, DC", "year": 2022}])]},

 {"name": "Neiman Marcus", "aliases": ["Neiman Marcus Group"], "website": "neimanmarcus.com", "breaches": [B(
  title="2013 payment card breach", date="2013-07", status="confirmed", affected="About 370,000 payment cards",
  categories=["Payment card numbers", "Card expiry dates"],
  description="Over three months in 2013 attackers took card data from 77 Neiman Marcus stores. About 370,000 cards were exposed and at least 9,200 were used for fraud. In 2019 the luxury retailer paid $1.5 million to 43 US states and Washington, DC.",
  source_name="Nevada Attorney General",
  source_url="https://ag.nv.gov/News/PR/2019/Attorney_General_Aaron_Ford_Reaches_$1_5M_Settlement_with_Retailer_Neiman_Marcus_Over_2013_Data_Breach/",
  statement=None, disclosed="2014-01",
  outcomes=[{"kind": "settlement", "text": "Paid $1.5 million to 43 US states and Washington, DC", "year": 2019}])]},

 {"name": "Montefiore Medical Center", "aliases": ["Montefiore"], "website": "montefiore.org", "breaches": [B(
  title="Employee stole and sold patient data", date="2013-01", status="confirmed", affected="12,517 patients",
  categories=["Names", "Dates of birth", "Social Security numbers", "Home addresses"],
  description="Over six months in 2013 an employee of Montefiore, a New York City hospital system, looked up 12,517 patients’ records and sold some of the data to an identity theft ring. The hospital found out in 2015 after police alerted it. The US health department said it lacked basic monitoring, and Montefiore paid $4.75 million in 2024.",
  source_name=HHS, source_url="https://www.hhs.gov/about/news/2024/02/06/hhs-office-civil-rights-settles-malicious-insider-cybersecurity-investigation.html",
  statement=None, disclosed="2015-05",
  outcomes=[{"kind": "settlement", "text": "Paid $4.75 million to the US health department", "year": 2024}])]},

 {"name": "Community Health Systems", "aliases": ["CHS", "CHSPSC"], "website": "chs.net", "breaches": [B(
  title="2014 attack by a hacking group", date="2014-04", status="confirmed", affected="About 6 million people",
  categories=["Names", "Home addresses", "Dates of birth", "Phone numbers", "Social Security numbers"],
  description="In 2014 a hacking group known as APT18 used stolen administrator logins to get into the systems of Community Health Systems, which runs hospitals across the US. Patient identification data of about 6 million people was copied; the company said medical and card data were not. It only found out when the FBI told it. It paid $2.3 million to the US health department and $5 million to US states in 2020.",
  source_name=HHS, source_url="https://www.hhs.gov/about/news/2020/09/23/hipaa-business-associate-pays-2.3-million-settle-breach.html",
  statement=None, disclosed="2014-08",
  outcomes=[{"kind": "settlement", "text": "Paid $5 million to US states", "year": 2020},
            {"kind": "settlement", "text": "Paid $2.3 million to the US health department", "year": 2020}])]},

 {"name": "First American", "aliases": ["First American Financial", "First American Title"], "website": "firstam.com", "breaches": [B(
  title="800 million property documents open online", date="2003", status="confirmed", timing_unclear=True,
  affected="More than 800 million documents, many with personal data",
  categories=["Bank account numbers", "Social Security numbers", "Driver’s licence images", "Mortgage and tax records"],
  description="A flaw in First American’s document-sharing website meant anyone with a link could see property deal documents dating back to 2003, more than 800 million in total, many with bank and Social Security details. A journalist exposed it in May 2019. The US Securities and Exchange Commission fined the company in 2021, and New York’s financial regulator in 2023.",
  source_name="US Securities and Exchange Commission", source_url="https://www.sec.gov/newsroom/press-releases/2021-102",
  statement=None, disclosed="2019-05",
  outcomes=[{"kind": "fine", "text": "Fined $487,616 by the US Securities and Exchange Commission", "year": 2021},
            {"kind": "fine", "text": "Fined $1 million by New York’s financial regulator", "year": 2023}])]},

 {"name": "Herff Jones", "aliases": [], "website": "herffjones.com", "breaches": [B(
  title="2021 theft of payment card data", date="2021-04", status="confirmed",
  affected="Thousands of customers, mostly students, including more than 40,000 New Yorkers",
  categories=["Payment card details", "Names", "Home addresses"],
  description="In April 2021 attackers took card details from the website of Herff Jones, which makes graduation caps, gowns and class rings. Most of the customers affected were students. The New York and Pennsylvania Attorneys General found weak security, and the company paid $200,000 in 2022.",
  source_name=NYAG, source_url="https://ag.ny.gov/press-release/2022/attorney-general-james-secures-200000-student-cap-and-gown-producer-herff-jones",
  statement=None, disclosed="2021-05",
  outcomes=[{"kind": "settlement", "text": "Paid $200,000 to New York and Pennsylvania", "year": 2022}])]},

 {"name": "GEICO", "aliases": [], "website": "geico.com", "breaches": [B(
  title="Attacks on the online quote tool", date="2020-11", status="confirmed", affected="About 116,000 people",
  categories=["Driver’s licence numbers"],
  description="From November 2020 attackers abused GEICO’s online car insurance quote tool to pull up people’s driver’s licence numbers, which were then used to file fake unemployment claims during the pandemic. In 2024 GEICO paid $9.75 million to New York’s Attorney General and financial regulator.",
  source_name=NYAG, source_url="https://ag.ny.gov/press-release/2024/attorney-general-james-and-dfs-superintendent-harris-secure-113-million-auto",
  statement=None, disclosed="2021-04",
  outcomes=[{"kind": "settlement", "text": "Paid $9.75 million to New York State", "year": 2024}])]},

 {"name": "Travelers", "aliases": ["Travelers Insurance"], "website": "travelers.com", "breaches": [B(
  title="Attacks on the online quote tool", date="2021", status="confirmed", timing_unclear=True, affected="About 4,000 people",
  categories=["Driver’s licence numbers"],
  description="Attackers abused Travelers’ online car insurance quote tool to pull up people’s driver’s licence numbers, part of a wave of similar attacks on US insurers. In 2024 Travelers paid $1.55 million to New York’s Attorney General and financial regulator.",
  source_name=NYAG, source_url="https://ag.ny.gov/press-release/2024/attorney-general-james-and-dfs-superintendent-harris-secure-113-million-auto",
  statement=None,
  outcomes=[{"kind": "settlement", "text": "Paid $1.55 million to New York State", "year": 2024}])]},

 {"name": "Morgan Stanley", "aliases": ["Morgan Stanley Smith Barney"], "website": "morganstanley.com", "breaches": [B(
  title="Customer data left on discarded devices", date="2015", status="confirmed", timing_unclear=True,
  affected="About 15 million customers",
  categories=["Unencrypted customer records, including Social Security numbers"],
  description="From 2015 Morgan Stanley got rid of old servers and hard drives that still held unencrypted customer data, some through a moving company with no data destruction experience. Some devices were later sold online, and most were never recovered. The US Securities and Exchange Commission fined the bank $35 million in 2022, and it paid $6.5 million to US states in 2023.",
  source_name="US Securities and Exchange Commission", source_url="https://www.sec.gov/newsroom/press-releases/2022-168",
  statement=None,
  outcomes=[{"kind": "fine", "text": "Fined $35 million by the US Securities and Exchange Commission", "year": 2022},
            {"kind": "settlement", "text": "Paid $6.5 million to US states", "year": 2023}])]},

 {"name": "American Medical Collection Agency", "aliases": ["AMCA", "Retrieval-Masters Creditors Bureau"], "website": "amca.com", "breaches": [B(
  title="Hack of a medical debt collector (2018–2019)", date="2018-08", status="confirmed",
  affected="More than 27.5 million people, mostly patients of US labs such as Quest and Labcorp",
  categories=["Names", "Dates of birth", "Home addresses", "Social Security numbers", "Payment card numbers", "Bank account details", "Medical test information"],
  description="From August 2018 to March 2019 attackers were inside the payment website of AMCA, a debt collector used by medical labs including Quest Diagnostics and Labcorp. Data of more than 27.5 million people was exposed. AMCA went bankrupt. In 2021 it settled with US states, including a $21 million penalty that was suspended because of the bankruptcy.",
  source_name="New Jersey Office of the Attorney General",
  source_url="https://www.njoag.gov/ag-grewal-announces-multistate-settlement-with-american-medical-collection-agency-over-2019-data-breach/",
  statement=None, disclosed="2019-06",
  outcomes=[{"kind": "settlement", "text": "Settled with US states, including a $21 million penalty suspended because of bankruptcy", "year": 2021}])]},

 {"name": "Labcorp", "aliases": ["LabCorp", "Laboratory Corporation of America"], "website": "labcorp.com", "breaches": [B(
  title="Patient data stolen from its debt collector (AMCA)", date="2018-08", status="confirmed", affected="About 7.7 million Labcorp patients",
  categories=["Names", "Dates of birth", "Home addresses", "Phone numbers", "Payment card or bank details (some patients)", "Account balance information"],
  description="Labcorp, one of the largest US medical testing companies, used American Medical Collection Agency (AMCA) to collect unpaid bills. Attackers inside AMCA’s systems from 2018 to 2019 reached data of about 7.7 million Labcorp patients. In 2026 Labcorp settled with 44 US attorneys general and agreed to stronger protections for patient data.",
  source_name="Pennsylvania Office of Attorney General",
  source_url="https://www.attorneygeneral.gov/taking-action/attorney-general-sunday-announces-multistate-settlement-with-labcorp-over-american-medical-collection-agency-data-breach/",
  statement=None, disclosed="2019-06",
  outcomes=[{"kind": "settlement", "text": "Settled with 44 US attorneys general", "year": 2026}])]},
]

have = {c["name"].lower() for c in d["companies"]}
for c in new:
    assert c["name"].lower() not in have, "already in the database: " + c["name"]
d["companies"] += new
d["updated"] = "2026-11-18"
DATA.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("added %d companies, now %d" % (len(new), len(d["companies"])))
