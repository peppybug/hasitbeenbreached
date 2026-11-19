# Chrome Web Store listing: text to paste

Everything below goes into the Chrome Web Store Developer Dashboard. This file is not part of the extension zip.

## Store listing tab

**Name:** Has it been Breached?

**Summary** (max 132 characters):
See a company's data breach history while you browse. Free, no account, and the sites you visit never leave your browser.

**Category:** Tools (or Privacy & Security, if offered)

**Language:** English

**Description:**

Before you trust a company with your data, check their history.

Has it been Breached? lights up when you visit the website of a company with data breaches on public record. Click the icon to see, in plain language:

• When each breach happened and how many people were affected
• What was exposed, coloured by risk: high (like passwords or payment cards), medium (like home addresses) or lower (like names)
• How long the company took to make it known
• Fines, settlements and court cases that followed
• The company's official statement, and the regulator or company source each record is based on

You can also search any company in the database from the popup. Every record links to its full page on hasitbeenbreached.com, with an official source.

PRIVATE BY DESIGN
The site you're on is checked against our company list on your own device. Your browsing history is never sent to us or anyone else. No account, no tracking, no ads. Once a day the extension downloads the public company list from hasitbeenbreached.com, and that's the only network request it makes.

GOOD TO KNOW
The database is written by hand from public sources and is still growing (over 200 companies). No result never means a company has never had a breach. Records are not a security rating and not legal, financial or security advice.

Missing a company? Request it at contact@hasitbeenbreached.com.

**Screenshots:** store-1.png, store-2.png, store-3.png (1280×800)
**Small promo tile:** tile.png (440×280)
**Icon:** icons/icon-128.png (already in the zip)

**Official URL / Homepage:** https://hasitbeenbreached.com/
**Support URL:** https://hasitbeenbreached.com/contact.html

## Privacy practices tab

**Single purpose:**
Shows whether the website in the current tab has data breaches on public record, and lets the user look up a company's breach history.

**Permission justifications:**
- **tabs:** Needed to read the address of the active tab so the toolbar icon can show whether that site is in the breach database. The address is only compared with a list stored on the device and is never transmitted.
- **storage:** Stores the public company list on the device so matching works without contacting any server.
- **alarms:** Refreshes the stored company list once a day.
- **Host permission (https://hasitbeenbreached.com/\*):** Downloads the public company list from the extension's own website.

**Remote code:** No, the extension does not use remote code. (It downloads a JSON data file only.)

**Data usage:** Tick **"Web history"** only if the form insists, because the extension reads the active tab's address; then confirm it is not sold, not transferred, and used only for the single purpose above. Tick all three certifications:
- I do not sell or transfer user data to third parties, outside of the approved use cases
- I do not use or transfer user data for purposes that are unrelated to my item's single purpose
- I do not use or transfer user data to determine creditworthiness or for lending purposes

**Privacy policy URL:** https://hasitbeenbreached.com/privacy.html
