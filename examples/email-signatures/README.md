# Email signatures — POF v1.0

3 templates Outlook + Gmail compatible (inline CSS, table-based, base64 logo).

| File | Entity |
|------|--------|
| factories.html | Plastic Odyssey Factories |
| academy.html | Plastic Odyssey Academy |
| sunu-po.html | Sunu Plastic Odyssey |

## Variables to replace

- `{{first_name}}` — first name
- `{{last_name}}` — last name
- `{{role}}` — role / position
- `{{phone_e164}}` — phone in international format `+XX X XX XX XX XX`
- `{{email}}` — email address
- `{{linkedin_url}}` — optional LinkedIn URL

## Installation

### Gmail
1. Settings → See all settings → General → Signature → Create new
2. Open the .html in your browser, select all, copy
3. Paste into the Gmail signature field

### Outlook desktop (Mac/Win)
1. File → Options → Mail → Signatures → New
2. Open the .html in your browser, select all, copy
3. Paste

### Apple Mail / Outlook web
1. Open the .html in your browser
2. Select all, copy
3. Paste in the signature editor

## Notes

- Logo is base64-encoded (no external asset to break)
- Fonts use web-safe fallback (Arial) when Poppins/Raleway not loaded
- Disclaimer GDPR included
- Tested on Gmail web, Outlook 365, Apple Mail
