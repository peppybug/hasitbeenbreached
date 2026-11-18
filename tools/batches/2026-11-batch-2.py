"""Batch 2 (November 2026): companies with a regulator decision, settlement or court ruling.

Run from the repository root:  python3 tools/batches/2026-11-batch-2.py
Then rebuild the pages:        python3 tools/build_pages.py
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "breaches.json"
d = json.loads(DATA.read_text(encoding="utf-8"))

def B(**k):
    return k

FTC = "US Federal Trade Commission"
ICO = "UK Information Commissioner’s Office"

new = [
 {"name": "Drizly", "aliases": [], "website": "drizly.com", "breaches": [B(
  title="2020 hack through an executive’s GitHub account", date="2020-07", status="confirmed", affected="About 2.5 million customers",
  categories=["Email addresses", "Dates of birth", "Hashed passwords", "Home addresses", "Phone numbers", "Order history", "Location"],
  description="In July 2020 an attacker reused a password from an unrelated breach to get into a Drizly executive’s GitHub account, found database keys there and stole data on about 2.5 million customers of the alcohol delivery app. The US Federal Trade Commission said Drizly had been warned about security problems two years earlier. Its 2023 order also binds the CEO personally at future companies.",
  source_name=FTC,
  source_url="https://www.ftc.gov/news-events/news/press-releases/2022/10/ftc-takes-action-against-drizly-its-ceo-james-cory-rellas-security-failures-exposed-data-25-million",
  statement=None, disclosed="2020-07",
  outcomes=[{"kind": "order", "text": "FTC order requiring data deletion and a security program, also binding the CEO", "year": 2023}])]},

 {"name": "Blackbaud", "aliases": [], "website": "blackbaud.com", "breaches": [B(
  title="2020 ransomware attack", date="2020-02", status="confirmed",
  affected="Millions of people whose data was held by charities, schools and hospitals",
  categories=["Names", "Contact details", "Dates of birth", "Social Security numbers", "Bank account details", "Donation history"],
  description="Blackbaud makes software that charities, universities and hospitals use to manage donors and members. An attacker was inside its systems from February to May 2020 and stole data held for thousands of these organisations. Blackbaud paid a ransom for a promise that the data would be deleted. The US Federal Trade Commission said Blackbaud waited two months to tell its customers and at first wrongly said no sensitive data was taken.",
  source_name=FTC,
  source_url="https://www.ftc.gov/news-events/news/press-releases/2024/05/ftc-finalizes-order-blackbaud-related-allegations-firms-security-failures-led-data-breach",
  statement=None, disclosed="2020-07",
  outcomes=[{"kind": "settlement", "text": "Agreed to pay $49.5 million to 49 US states and Washington, DC", "year": 2023},
            {"kind": "order", "text": "FTC order requiring data deletion and a security program", "year": 2024}])]},

 {"name": "CafePress", "aliases": ["Residual Pumpkin", "PlanetArt"], "website": "cafepress.com", "breaches": [B(
  title="2019 breach and cover-up", date="2019-02", status="confirmed", affected="About 22 million accounts",
  categories=["Email addresses", "Poorly protected passwords", "Names", "Home addresses", "Phone numbers", "Security questions and answers", "Social Security numbers (about 180,000)", "Partial payment card numbers"],
  description="Hackers broke into the custom merchandise site in February 2019 and stole account details, including Social Security numbers that were stored in plain text. The US Federal Trade Commission said the company covered up the breach and kept its security weak. In 2022 it ordered the former owner to pay $500,000 for victims and required stronger security.",
  source_name=FTC,
  source_url="https://www.ftc.gov/news-events/news/press-releases/2022/06/ftc-finalizes-action-against-cafepress-covering-data-breach-lax-security-0",
  statement=None, disclosed="2019-09",
  outcomes=[{"kind": "order", "text": "FTC order: $500,000 for victims and a security program", "year": 2022}])]},

 {"name": "Wyndham Hotels & Resorts", "aliases": ["Wyndham"], "website": "wyndhamhotels.com", "breaches": [B(
  title="Three hotel payment system breaches", date="2008", status="confirmed", timing_unclear=True,
  affected="More than 619,000 payment cards",
  categories=["Payment card numbers", "Card expiry dates", "Card security codes"],
  description="Between 2008 and 2010 hackers broke into Wyndham’s hotel networks three times and took payment card data. The US Federal Trade Commission sued, and a US appeals court confirmed in 2015 that the FTC can act over weak data security. Wyndham settled the same year and agreed to yearly security audits.",
  source_name=FTC,
  source_url="https://www.ftc.gov/news-events/news/press-releases/2015/12/wyndham-settles-ftc-charges-it-unfairly-placed-consumers-payment-card-information-risk",
  statement=None,
  outcomes=[{"kind": "court", "text": "US appeals court confirmed the FTC could take action over its data security", "year": 2015},
            {"kind": "settlement", "text": "Settled with the FTC and agreed to yearly security audits", "year": 2015}])]},

 {"name": "TJX", "aliases": ["TJ Maxx", "T.J. Maxx", "TK Maxx", "Marshalls", "HomeGoods"], "website": "tjx.com", "breaches": [B(
  title="2005–2007 payment card theft", date="2005-07", status="confirmed",
  affected="Tens of millions of payment cards, and personal details of about 455,000 people",
  categories=["Payment card numbers", "Driver’s licence numbers (about 455,000 people)", "Names", "Home addresses"],
  description="From mid-2005 an intruder got into the networks of TJX, owner of TJ Maxx, Marshalls and TK Maxx, and took data on tens of millions of payment cards. Personal details of about 455,000 people who returned goods without a receipt were also taken. It was made public in January 2007. In 2008 TJX settled with the US Federal Trade Commission and agreed to 20 years of independent security audits.",
  source_name=FTC,
  source_url="https://www.ftc.gov/news-events/news/press-releases/2008/03/agency-announces-settlement-separate-actions-against-retailer-tjx-data-brokers-reed-elsevier-seisint",
  statement=None, disclosed="2007-01",
  outcomes=[{"kind": "settlement", "text": "Settled with the FTC and agreed to 20 years of security audits", "year": 2008}])]},

 {"name": "Ring", "aliases": ["Amazon Ring"], "website": "ring.com", "breaches": [B(
  title="Staff access to private videos and hacked camera accounts", date="2017", status="confirmed", timing_unclear=True,
  affected="About 55,000 US customers whose accounts were hacked",
  categories=["Private home camera videos", "Live camera streams", "Account details"],
  description="The US Federal Trade Commission said any Ring employee or contractor could watch customers’ private videos, and one employee watched thousands of recordings of female customers in intimate spaces. It also said Ring failed to stop hackers, who took over about 55,000 US customers’ accounts and cameras. In 2023 Ring agreed to pay $5.8 million, which went to customers as refunds.",
  source_name=FTC,
  source_url="https://www.ftc.gov/news-events/news/press-releases/2023/05/ftc-says-ring-employees-illegally-surveilled-customers-failed-stop-hackers-taking-control-users",
  statement=None,
  outcomes=[{"kind": "settlement", "text": "Agreed to pay $5.8 million, used for customer refunds", "year": 2023}])]},

 {"name": "Interserve", "aliases": ["Interserve Group"], "website": "interserve.com", "breaches": [B(
  title="2020 cyber attack on staff records", date="2020-03", status="confirmed", affected="Up to 113,000 employees",
  categories=["Names", "Home addresses", "Bank account details", "National Insurance numbers", "Salary details", "Ethnicity, religion and health information"],
  description="Between March and May 2020 attackers got into the network of Interserve, a UK construction and outsourcing company, after an employee opened a phishing email. Personal information of up to 113,000 employees was affected. The UK Information Commissioner’s Office fined Interserve £4.4 million in 2022 for failing to keep the data secure.",
  source_name=ICO + ", annual report 2022/23",
  source_url="https://ico.org.uk/media2/migrated/4025864/annual-report-2022-23.pdf",
  statement=None,
  outcomes=[{"kind": "fine", "text": "Fined £4.4 million by the UK Information Commissioner’s Office", "year": 2022}])]},

 {"name": "Advanced Computer Software Group", "aliases": ["Advanced", "OneAdvanced"], "website": "oneadvanced.com", "breaches": [B(
  title="2022 ransomware attack on NHS software supplier", date="2022-08", status="confirmed", affected="79,404 people",
  categories=["Names", "Contact details", "Health and care records", "Home access details (890 people receiving care at home)"],
  description="In August 2022 attackers got into the health and care systems of Advanced, which supplies software to the NHS, through a customer account without two-step login. Data of 79,404 people was taken, including how to get into the homes of 890 people receiving care at home. NHS 111 and other services were disrupted. The UK Information Commissioner’s Office fined Advanced £3.07 million in 2025.",
  source_name=ICO,
  source_url="https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2025/03/software-provider-fined-3m-following-2022-ransomware-attack/",
  statement=None, disclosed="2022-08",
  outcomes=[{"kind": "fine", "text": "Fined £3.07 million by the UK Information Commissioner’s Office", "year": 2025}])]},

 {"name": "Desjardins", "aliases": ["Desjardins Group", "Mouvement Desjardins"], "website": "desjardins.com", "breaches": [B(
  title="Employee stole member data over two years", date="2017", status="confirmed", timing_unclear=True,
  affected="About 9.7 million people",
  categories=["Names", "Home addresses", "Dates of birth", "Social insurance numbers", "Email addresses", "Phone numbers", "Banking products and habits"],
  description="An employee of the Canadian financial cooperative copied member data for at least 26 months before police discovered it during a separate investigation in 2019. About 9.7 million people in Canada and abroad were affected. Canada’s Privacy Commissioner found in 2020 that Desjardins broke federal privacy law. A class action settlement of about C$200 million followed.",
  source_name="Office of the Privacy Commissioner of Canada",
  source_url="https://www.priv.gc.ca/en/opc-actions-and-decisions/investigations/investigations-into-businesses/2020/pipeda-2020-005/",
  statement=None, disclosed="2019-06",
  outcomes=[{"kind": "investigation", "text": "Canada’s Privacy Commissioner found it broke federal privacy law", "year": 2020},
            {"kind": "settlement", "text": "Class action settlement of about C$200 million", "year": 2022}])]},

 {"name": "LifeLabs", "aliases": [], "website": "lifelabs.com", "breaches": [B(
  title="2019 cyber attack on lab testing company", date="2019-10", status="confirmed", timing_unclear=True,
  affected="About 8.6 million people",
  categories=["Names", "Home addresses", "Email addresses", "Dates of birth", "Health card numbers", "Login details", "Lab test results (some people)"],
  description="Attackers broke into the systems of LifeLabs, Canada’s largest medical lab testing company, and took customer data. LifeLabs paid a ransom to get it back. It first said up to 15 million people could be affected; regulators later counted about 8.6 million. The Ontario and British Columbia privacy commissioners found in 2020 that LifeLabs failed to protect the data.",
  source_name="Information and Privacy Commissioner of Ontario",
  source_url="https://www.ipc.on.ca/en/media-centre/news-releases/ontario-ipc-and-bc-oipc-find-lifelabs-failed-protect-personal-information-2019-breach",
  statement=None, disclosed="2019-12",
  outcomes=[{"kind": "order", "text": "Ontario and British Columbia privacy commissioners ordered security fixes", "year": 2020}])]},

 {"name": "Carousell", "aliases": [], "website": "carousell.com", "breaches": [B(
  title="2022 data scrape through a faulty system", date="2022-10", status="confirmed", affected="About 2.6 million users",
  categories=["Email addresses", "Phone numbers", "Dates of birth"],
  description="A software change at the Singapore-based marketplace left out a filter, so an attacker could pull users’ private details. Data of about 2.6 million users was put up for sale online. Singapore’s data protection commission fined Carousell S$58,000, which also covered a second incident that year.",
  source_name="Personal Data Protection Commission Singapore",
  source_url="https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/commissions-decisions/gd_carousell_28122023.pdf",
  statement=None, disclosed="2022-10",
  outcomes=[{"kind": "fine", "text": "Fined S$58,000 by Singapore’s data protection commission", "year": 2023}])]},

 {"name": "Snapchat", "aliases": ["Snap", "Snap Inc."], "website": "snapchat.com", "breaches": [B(
  title="Leak of usernames and phone numbers", date="2013-12", status="confirmed", affected="About 4.6 million users",
  categories=["Usernames", "Phone numbers"],
  description="Weak protections in Snapchat’s Find Friends feature let attackers build and publish a database of about 4.6 million usernames and phone numbers. The US Federal Trade Commission also said Snapchat’s promise that messages disappear was false. Snapchat settled in 2014 and agreed to 20 years of privacy monitoring.",
  source_name=FTC,
  source_url="https://www.ftc.gov/news-events/news/press-releases/2014/05/snapchat-settles-ftc-charges-promises-disappearing-messages-were-false",
  statement=None, disclosed="2014-01",
  outcomes=[{"kind": "settlement", "text": "Settled with the FTC and agreed to 20 years of privacy monitoring", "year": 2014}])]},

 {"name": "SHEIN", "aliases": ["ROMWE", "Zoetop"], "website": "shein.com", "breaches": [B(
  title="2018 hack of customer accounts", date="2018-06", status="confirmed",
  affected="39 million SHEIN accounts and 7 million ROMWE accounts",
  categories=["Email addresses", "Hashed passwords", "Payment card details (some customers)"],
  description="In 2018 attackers stole account details for 39 million SHEIN and 7 million ROMWE accounts. New York’s Attorney General found the company told customers far fewer were affected than really were, and handled the response poorly. In 2022 the owner, Zoetop, agreed to pay $1.9 million.",
  source_name="New York State Attorney General",
  source_url="https://ag.ny.gov/press-release/2022/attorney-general-james-secures-19-million-e-commerce-shein-and-romwe-owner-zoetop",
  statement=None, disclosed="2018-08",
  outcomes=[{"kind": "settlement", "text": "Agreed to pay $1.9 million to New York State", "year": 2022}])]},

 {"name": "Hilton", "aliases": ["Hilton Hotels", "Hilton Worldwide"], "website": "hilton.com", "breaches": [B(
  title="2015 hotel payment card breaches", date="2015", status="confirmed", affected="More than 350,000 payment cards",
  categories=["Payment card numbers", "Card expiry dates", "Card security codes", "Names"],
  description="In 2015 attackers put malware on payment systems at Hilton hotels and took more than 350,000 card numbers. The New York and Vermont Attorneys General found Hilton was too slow to tell customers and did not keep reasonable security. Hilton paid $700,000 in 2017 and agreed to yearly payment security checks.",
  source_name="New York State Attorney General",
  source_url="https://ag.ny.gov/press-release/2017/ag-schneiderman-announces-700000-joint-settlement-hilton-after-data-breach",
  statement=None, disclosed="2015",
  outcomes=[{"kind": "settlement", "text": "Paid $700,000 to New York and Vermont", "year": 2017}])]},

 {"name": "PayPal", "aliases": [], "website": "paypal.com", "breaches": [B(
  title="2022 account takeovers with reused passwords", date="2022-12", status="confirmed", affected="About 35,000 accounts",
  categories=["Names", "Dates of birth", "Social Security numbers", "Home addresses", "Tax ID numbers"],
  description="In December 2022 attackers logged into about 35,000 PayPal accounts using passwords leaked from other sites. Because of a change PayPal had made for US tax forms, they could see full Social Security numbers. New York’s financial regulator said PayPal lacked qualified staff and training for key security work, and fined it $2 million in 2025.",
  source_name="New York State Department of Financial Services",
  source_url="https://www.dfs.ny.gov/reports_and_publications/press_releases/pr20250123",
  statement=None, disclosed="2023-01",
  outcomes=[{"kind": "fine", "text": "Fined $2 million by New York’s financial regulator", "year": 2025}])]},

 {"name": "Pearson", "aliases": ["Pearson plc", "AIMSweb"], "website": "pearson.com", "breaches": [B(
  title="2018 theft of student data", date="2018", status="confirmed", timing_unclear=True,
  affected="Millions of student records from US schools",
  categories=["Student names", "Dates of birth", "Email addresses", "School administrator logins (13,000 accounts)"],
  description="An attacker took millions of rows of student data from Pearson’s AIMSweb school software, along with logins for 13,000 school and university accounts. The US Securities and Exchange Commission found Pearson called it a ‘hypothetical’ risk to investors after it had already happened, and understated it once public. Pearson paid $1 million in 2021.",
  source_name="US Securities and Exchange Commission",
  source_url="https://www.sec.gov/newsroom/press-releases/2021-154",
  statement=None, disclosed="2019-07",
  outcomes=[{"kind": "fine", "text": "Paid $1 million to the SEC for misleading investors about the breach", "year": 2021}])]},

 {"name": "Vastaamo", "aliases": ["Psykoterapiakeskus Vastaamo"], "website": "vastaamo.fi", "breaches": [B(
  title="Theft and extortion of psychotherapy records", date="2018-11", status="confirmed",
  affected="More than 30,000 patients",
  categories=["Names", "Contact details", "National ID numbers (henkilötunnus)", "Psychotherapy notes (health information)"],
  description="A hacker stole the patient database of Vastaamo, a Finnish psychotherapy provider, in 2018 and 2019, then in 2020 tried to blackmail the company and its patients and published therapy notes online. Vastaamo had not reported the breach in time and went bankrupt. Finland’s data protection authority fined it €608,000 in 2021, and the hacker was jailed in 2024.",
  source_name="Office of the Data Protection Ombudsman (Finland)",
  source_url="https://tietosuoja.fi/en/-/administrative-fine-imposed-on-psychotherapy-centre-vastaamo-for-data-protection-violations",
  statement=None, disclosed="2020-10",
  outcomes=[{"kind": "fine", "text": "Fined €608,000 by Finland’s data protection authority", "year": 2021},
            {"kind": "court", "text": "The hacker was convicted and jailed", "year": 2024}])]},

 {"name": "Morele.net", "aliases": ["Morele"], "website": "morele.net", "breaches": [B(
  title="2018 theft of customer data", date="2018-11", status="confirmed", affected="About 2.2 million customers",
  categories=["Names", "Email addresses", "Phone numbers", "Home addresses", "Income and education details (loan applicants)"],
  description="Attackers took customer data from Morele.net, a large Polish electronics webshop, in late 2018. For some customers this included details from instalment loan applications, such as income and education. Poland’s data protection authority fined the company 2.8 million złoty in 2019. After a court overturned that decision, it fined Morele.net again, over 3.8 million złoty, which a court upheld in 2024.",
  source_name="UODO (Polish Data Protection Authority)",
  source_url="https://uodo.gov.pl/pl/138/2983",
  statement=None,
  outcomes=[{"kind": "fine", "text": "Fined 2.8 million złoty by Poland’s data protection authority", "year": 2019},
            {"kind": "court", "text": "Poland’s top administrative court overturned the first decision", "year": 2023},
            {"kind": "fine", "text": "Fined again, over 3.8 million złoty; upheld by a court", "year": 2024}])]},

 {"name": "Australian Clinical Labs", "aliases": ["Medlab Pathology", "ACL"], "website": "clinicallabs.com.au", "breaches": [B(
  title="2022 attack on Medlab Pathology", date="2022-02", status="confirmed", affected="More than 223,000 people",
  categories=["Names", "Medical records and test results", "Medicare numbers", "Payment card details (some people)"],
  description="In February 2022 attackers got into the systems of Medlab Pathology, owned by Australian Clinical Labs, and took personal and health information of more than 223,000 people. The company was slow to assess the breach and to tell the regulator. In 2025 a court ordered it to pay A$5.8 million, the first civil penalty under Australia’s Privacy Act.",
  source_name="Office of the Australian Information Commissioner",
  source_url="https://www.oaic.gov.au/news/media-centre/australian-clinical-labs-ordered-to-pay-penalties-in-relation-to-medlab-pathology-data-breach-in-first-for-privacy-act",
  statement=None, disclosed="2022-07",
  outcomes=[{"kind": "court", "text": "Court ordered A$5.8 million in penalties, a first under Australia’s Privacy Act", "year": 2025}])]},
]

have = {c["name"].lower() for c in d["companies"]}
for c in new:
    assert c["name"].lower() not in have, "already in the database: " + c["name"]
d["companies"] += new
d["updated"] = "2026-11-18"
DATA.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("added %d companies, now %d" % (len(new), len(d["companies"])))
