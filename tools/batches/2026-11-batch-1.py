"""Adds the November 2026 batch of companies to data/breaches.json. Safe to run once; refuses duplicates.

Run from the repository root:  python3 tools/batches/2026-11-batch-1.py
Then rebuild the pages:        python3 tools/build_pages.py
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "breaches.json"
d = json.loads(DATA.read_text(encoding="utf-8"))

def B(**k):
    return k

ICO = "UK Information Commissioner’s Office"
CNIL_URL = "https://cnil.fr/fr/violation-de-donnees-de-deux-operateurs-de-tiers-payant-la-cnil-ouvre-une-enquete-et-rappelle-aux"

new = [
 {"name": "Transavia", "aliases": ["Transavia Airlines"], "website": "transavia.com", "breaches": [B(
  title="2019 hack of internal systems", date="2019-09", status="confirmed",
  affected="About 83,000 people whose data was downloaded",
  categories=["Names", "Contact details", "Booking details", "Medical information (367 passengers)"],
  description="A hacker got into Transavia’s systems in September 2019 through two IT accounts that had easy-to-guess passwords and no two-step login. Data on about 83,000 people was downloaded, including medical details such as wheelchair use for 367 passengers. The hacker could in principle reach data on about 25 million people. The Dutch Data Protection Authority fined Transavia €400,000 in 2021.",
  source_name="Autoriteit Persoonsgegevens (Dutch Data Protection Authority)",
  source_url="https://www.autoriteitpersoonsgegevens.nl/en/current/dutch-dpa-fines-transavia-for-poor-personal-data-security",
  statement=None,
  outcomes=[{"kind": "fine", "text": "Fined €400,000 by the Dutch Data Protection Authority for poor security", "year": 2021}])]},

 {"name": "TalkTalk", "aliases": ["TalkTalk Telecom"], "website": "talktalk.co.uk", "breaches": [B(
  title="2015 cyber attack", date="2015-10", status="confirmed", affected="156,959 customers",
  categories=["Names", "Home addresses", "Dates of birth", "Phone numbers", "Email addresses", "Bank account details (15,656 customers)"],
  description="Attackers used a well-known technique (SQL injection) on old web pages TalkTalk had inherited when it bought Tiscali’s UK business. They took personal details of 156,959 customers, and bank details of 15,656 of them. The UK Information Commissioner’s Office said the attack could have been prevented and fined TalkTalk a record £400,000 in 2016.",
  source_name=ICO,
  source_url="https://ico.org.uk/about-the-ico/media-centre/talktalk-cyber-attack-how-the-ico-investigation-unfolded/",
  statement=None, disclosed="2015-10",
  outcomes=[{"kind": "fine", "text": "Fined £400,000 by the UK Information Commissioner’s Office", "year": 2016}])]},

 {"name": "Cathay Pacific", "aliases": ["Cathay Pacific Airways"], "website": "cathaypacific.com", "breaches": [B(
  title="Passenger data breach found in 2018", date="2014-10", status="confirmed", timing_unclear=True,
  affected="About 9.4 million passengers worldwide",
  categories=["Names", "Nationalities", "Dates of birth", "Phone numbers", "Email addresses", "Home addresses",
              "Passport and ID card numbers", "Frequent flyer numbers", "Customer service notes", "Travel history"],
  description="Cathay Pacific’s systems lacked proper security from October 2014 to May 2018, and attackers got into them. Database backups were not encrypted, against the airline’s own policy. About 9.4 million passengers were affected. The UK Information Commissioner’s Office fined the airline £500,000 in 2020, the most it could under the law at the time.",
  source_name=ICO + ", penalty notice",
  source_url="https://ico.org.uk/media2/migrated/2617314/cathay-pacific-mpn-20200210.pdf",
  statement=None, disclosed="2018-10",
  outcomes=[{"kind": "fine", "text": "Fined £500,000 by the UK Information Commissioner’s Office", "year": 2020}])]},

 {"name": "Currys", "aliases": ["Currys PC World", "Dixons Carphone", "DSG Retail", "Dixons Travel"], "website": "currys.co.uk", "breaches": [B(
  title="Malware on shop tills", date="2017-07", status="confirmed",
  affected="At least 14 million people, including 5.6 million payment cards",
  categories=["Payment card numbers and expiry dates", "Names", "Postcodes", "Email addresses"],
  description="Hackers installed malware on 5,390 tills in Currys PC World and Dixons Travel shops between July 2017 and April 2018. The UK Information Commissioner’s Office blamed weak security, such as missing patches and firewalls, and fined the company £500,000 in 2020. After years of appeals the case ended in 2026 with the company agreeing to pay £200,000.",
  source_name=ICO,
  source_url="https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/02/ico-wins-court-of-appeal-case-in-dsg-retail-ruling/",
  statement=None, disclosed="2018-06",
  outcomes=[{"kind": "fine", "text": "Fined £500,000 by the UK Information Commissioner’s Office", "year": 2020},
            {"kind": "court", "text": "A tribunal cut the fine to £250,000; the case then went through further appeals", "year": 2022},
            {"kind": "settlement", "text": "Agreed to pay £200,000 to end the case", "year": 2026}])]},

 {"name": "Capita", "aliases": ["Capita plc", "Capita Pension Solutions"], "website": "capita.com", "breaches": [B(
  title="2023 ransomware attack", date="2023-03", status="confirmed", affected="6.6 million people",
  categories=["Names", "Pension and employment records", "Bank account details (some people)",
              "Criminal record information (some people)", "Health and other sensitive information (some people)"],
  description="Ransomware attackers got into Capita’s network in March 2023 and stole personal information of 6.6 million people, much of it from pension schemes Capita runs for employers. A high-priority security alert went unanswered for 58 hours. The UK Information Commissioner’s Office fined Capita £14 million in 2025, and Capita accepted the fine.",
  source_name=ICO,
  source_url="https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2025/10/capita-fined-14m-for-data-breach-affecting-over-6m-people/",
  statement=None, disclosed="2023-03",
  outcomes=[{"kind": "fine", "text": "Fined £14 million by the UK Information Commissioner’s Office", "year": 2025}])]},

 {"name": "Ahold Delhaize", "aliases": ["Food Lion", "Stop & Shop", "Giant Food", "Hannaford"], "website": "aholddelhaize.com", "breaches": [B(
  title="2024 cyberattack on US systems", date="2024-11", status="confirmed",
  affected="About 2.2 million people, mostly current and former US employees",
  categories=["Names", "Contact details", "Dates of birth", "Government ID numbers", "Bank account details",
              "Health information from employment records"],
  description="In November 2024 attackers got into some of Ahold Delhaize’s US business systems. In April 2025 the company confirmed that files had been taken, mainly employment records. A notice filed with US authorities put the number of people affected at about 2.2 million. The company said customer payment and pharmacy systems were not affected.",
  source_name="Ahold Delhaize",
  source_url="https://newsroom.aholddelhaize.com/update-on-ahold-delhaizes-cybersecurity-incident/",
  statement={"title": "Update on Ahold Delhaize’s cybersecurity incident",
             "url": "https://newsroom.aholddelhaize.com/update-on-ahold-delhaizes-cybersecurity-incident/"},
  disclosed="2025-04", outcomes=[])]},

 {"name": "Revolut", "aliases": [], "website": "revolut.com", "breaches": [B(
  title="2022 social engineering attack", date="2022-09", status="confirmed", affected="50,150 customers worldwide",
  categories=["Names", "Home addresses", "Email addresses", "Phone numbers", "Partial payment card details", "Account details"],
  description="In September 2022 an attacker tricked their way into a Revolut database. Details of 50,150 customers were exposed, about 20,000 of them in Europe. Revolut said card numbers, PINs and passwords were not accessed. Lithuania’s data protection authority, Revolut’s lead regulator in the EU, opened an investigation.",
  source_name="State Data Protection Inspectorate of Lithuania",
  source_url="https://vdai.lrv.lt/en/news/the-state-data-protection-inspectorate-has-initiated-an-investigation-regarding-personal-data-breach-in-revolut",
  statement=None, disclosed="2022-09",
  outcomes=[{"kind": "investigation", "text": "Lithuania’s data protection authority opened an investigation", "year": 2022}])]},

 {"name": "UniCredit", "aliases": [], "website": "unicredit.it", "breaches": [B(
  title="2018 attack on the mobile banking portal", date="2018-10", status="confirmed",
  affected="About 778,000 customers and former customers in Italy",
  categories=["Names", "Tax ID numbers (codice fiscale)", "Customer ID codes"],
  description="In 2018 an attack on UniCredit’s mobile banking portal exposed names, tax ID numbers and customer codes of about 778,000 current and former customers. Italy’s data protection authority fined the bank €2.8 million in 2024. UniCredit said no banking data was affected and that it would challenge the fine in court.",
  source_name="Garante per la protezione dei dati personali (Italian Data Protection Authority)",
  source_url="https://www.garanteprivacy.it/garante/doc.jsp?ID=9991101",
  statement=None, disclosed="2018-10",
  outcomes=[{"kind": "fine", "text": "Fined €2.8 million by the Italian Data Protection Authority (UniCredit is appealing)", "year": 2024}])]},

 {"name": "Viamedis", "aliases": [], "website": "viamedis.fr", "breaches": [B(
  title="2024 attack on a health insurance payment platform", date="2024-01", status="confirmed",
  affected="Part of more than 33 million people affected across Viamedis and Almerys",
  categories=["Names", "Dates of birth", "Social security numbers", "Marital status", "Health insurer and cover details"],
  description="Viamedis handles payments between French health insurers and pharmacies, doctors and hospitals. In early 2024 attackers broke into its systems, and around the same time into those of Almerys, which does the same work. France’s data protection authority said more than 33 million people were affected across the two. It said contact details and bank details were not involved.",
  source_name="CNIL (French Data Protection Authority)", source_url=CNIL_URL,
  statement=None, disclosed="2024-02",
  outcomes=[{"kind": "investigation", "text": "France’s data protection authority opened an investigation", "year": 2024}])]},

 {"name": "Almerys", "aliases": [], "website": "almerys.com", "breaches": [B(
  title="2024 attack on a health insurance payment platform", date="2024-02", status="confirmed",
  affected="Part of more than 33 million people affected across Almerys and Viamedis",
  categories=["Names", "Dates of birth", "Social security numbers", "Marital status", "Health insurer and cover details"],
  description="Almerys handles payments between French health insurers and healthcare providers. In February 2024 attackers broke into its systems, shortly after a similar attack on Viamedis. France’s data protection authority said more than 33 million people were affected across the two. It said contact details and bank details were not involved.",
  source_name="CNIL (French Data Protection Authority)", source_url=CNIL_URL,
  statement=None, disclosed="2024-02",
  outcomes=[{"kind": "investigation", "text": "France’s data protection authority opened an investigation", "year": 2024}])]},

 {"name": "Air Europa", "aliases": [], "website": "aireuropa.com", "breaches": [B(
  title="2023 theft of payment card data", date="2023-08", status="confirmed", affected="Not disclosed",
  categories=["Payment card numbers", "Card expiry dates", "Card security codes (CVV)", "Names",
              "ID and passport numbers", "Frequent flyer numbers"],
  description="Between August and September 2023 attackers took payment card details, including security codes, from Air Europa’s online sales system. The airline emailed affected customers in October and told them to cancel their cards. It later said some customers’ names, ID or passport numbers and frequent flyer codes may also have been exposed. It never said how many people were affected.",
  source_name="INCIBE (Spanish National Cybersecurity Institute)",
  source_url="https://www.incibe.es/node/503991",
  statement=None, disclosed="2023-10", outcomes=[])]},

 {"name": "Ashley Madison", "aliases": ["Ruby Corp", "Avid Life Media"], "website": "ashleymadison.com", "breaches": [B(
  title="2015 hack and leak of user data", date="2015-07", status="confirmed", affected="More than 36 million users",
  categories=["Profile information including sexual preferences", "Email addresses", "Account passwords", "Billing addresses and payment history"],
  description="Hackers broke into the dating site in July 2015 and published profile, account and billing details of more than 36 million users a month later. Some had paid for a ‘full delete’ of their profile that didn’t fully remove their data. In 2016 the operators settled with the US Federal Trade Commission and 13 states, agreeing to pay $1.6 million.",
  source_name="US Federal Trade Commission",
  source_url="https://www.ftc.gov/news-events/news/press-releases/2016/12/operators-ashleymadisoncom-settle-ftc-state-charges-resulting-2015-data-breach-exposed-36-million",
  statement=None, disclosed="2015-07",
  outcomes=[{"kind": "settlement", "text": "Agreed to pay $1.6 million to the FTC and US states", "year": 2016}])]},

 {"name": "Xfinity", "aliases": ["Comcast"], "website": "xfinity.com", "breaches": [B(
  title="2023 breach through a Citrix flaw", date="2023-10", status="confirmed", affected="About 35.9 million customers",
  categories=["Usernames", "Hashed passwords", "Names", "Contact details", "Dates of birth",
              "Last four digits of Social Security numbers", "Security questions and answers"],
  description="Between 16 and 19 October 2023 attackers used a known flaw in Citrix software to get into Xfinity’s systems. Usernames and scrambled (hashed) passwords were taken, and for some customers also names, contact details, birth dates, partial Social Security numbers and security questions. Xfinity made customers reset their passwords. A filing with US authorities put the number affected at about 35.9 million.",
  source_name="Xfinity (Comcast)", source_url="https://www.xfinity.com/dataincident/",
  statement={"title": "Notice To Customers of Data Security Incident", "url": "https://www.xfinity.com/dataincident/"},
  disclosed="2023-12", outcomes=[])]},

 {"name": "PlayStation Network", "aliases": ["Sony", "PSN", "Sony Interactive Entertainment", "Qriocity"], "website": "playstation.com", "breaches": [B(
  title="2011 PlayStation Network hack", date="2011-04", status="confirmed", affected="About 77 million accounts",
  categories=["Names", "Home addresses", "Email addresses", "Dates of birth", "Passwords", "Security question answers", "Purchase history"],
  description="Between 17 and 19 April 2011 attackers broke into Sony’s PlayStation Network and Qriocity services and took account details. Sony shut the network down for weeks. It said it had no evidence card data was taken but couldn’t rule it out. In 2013 the UK Information Commissioner’s Office fined Sony £250,000, saying the attack could have been prevented.",
  source_name="PlayStation Blog (Sony)",
  source_url="https://blog.playstation.com/2011/04/26/update-on-playstation-network-and-qriocity/",
  statement={"title": "Update on PlayStation Network and Qriocity",
             "url": "https://blog.playstation.com/2011/04/26/update-on-playstation-network-and-qriocity/"},
  disclosed="2011-04",
  outcomes=[{"kind": "fine", "text": "Fined £250,000 by the UK Information Commissioner’s Office", "year": 2013}])]},

 {"name": "Volkswagen", "aliases": ["VW", "Cariad", "Audi", "Skoda", "Seat"], "website": "volkswagen.com", "breaches": [B(
  title="Exposed location data of electric cars", date="2024-11", status="confirmed", timing_unclear=True,
  affected="About 800,000 electric cars, with precise locations for about 460,000",
  categories=["Precise vehicle location history", "Owner names and contact details"],
  description="Volkswagen’s software company Cariad left a cloud storage system open to the internet. It held months of location data from about 800,000 electric cars from Volkswagen, Audi, Skoda and Seat, linked to owners’ contact details. A tip-off reached the Chaos Computer Club, which warned Volkswagen in November 2024 and went public in December. Volkswagen blamed a configuration mistake and closed the gap.",
  source_name="Chaos Computer Club", source_url="https://www.ccc.de/de/updates/2024/wir-wissen-wo-dein-auto-steht",
  statement=None, disclosed="2024-12", outcomes=[])]},

 {"name": "easyJet", "aliases": [], "website": "easyjet.com", "breaches": [B(
  title="2020 cyber attack", date="2020-01", status="confirmed", timing_unclear=True,
  affected="About 9 million customers, with card details of 2,208",
  categories=["Email addresses", "Travel and booking details", "Payment card details (2,208 customers)"],
  description="easyJet learned of a cyber attack in January 2020 and announced it in May. The attacker saw email addresses and travel details of about 9 million customers, and card details of 2,208 of them. The UK Information Commissioner’s Office investigated and closed the case in 2023 without taking action. A group legal claim by customers was filed in 2020.",
  source_name="easyJet plc filing (London Stock Exchange)",
  source_url="https://www.rns-pdf.londonstockexchange.com/rns/0027D_1-2024-2-13.pdf",
  statement=None, disclosed="2020-05",
  outcomes=[{"kind": "investigation", "text": "The UK Information Commissioner’s Office investigated and closed the case without action", "year": 2023}])]},
]

have = {c["name"].lower() for c in d["companies"]}
for c in new:
    assert c["name"].lower() not in have, "already in the database: " + c["name"]
d["companies"] += new
d["updated"] = "2026-11-18"
DATA.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("added %d companies, now %d" % (len(new), len(d["companies"])))
