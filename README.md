# JM Electrical Solutions website (draft for review)

Plain HTML/CSS with one tiny script. No frameworks, no build step needed to host it.
Open `index.html` in any browser to preview. Upload the whole folder to any static host
(Vercel, Netlify, Cloudflare Pages, or the current web host).

## Pages (15)
Home · Services · 8 service pages (Panel Upgrades, EV Chargers, Lighting & Ceiling Fans,
Rewiring, Generators, Smart Home, Outlets & Switches, Emergency Service) · Reviews · About ·
Service Areas · Contact · Thank-you (shown after a form is sent).

## Must fix before going live (everything tagged in yellow on the pages)
1. **Review excerpts are samples.** They were written from the themes in JM's real reviews
   (clean, clear explanations, fair pricing, punctual, Jamie/Nic/Dan, small jobs). Replace each
   with a verbatim Google review, then delete the yellow "Sample" tag.
2. **Financing.** The brief asks for "financing options available". Confirm Jamie actually
   offers financing, with which lender and on what terms, before it goes live.
3. **"Insured"** in the trust bar: confirm, ideally with carrier details on the About page.
4. **Timelines** on service pages are typical for the trade, not JM's own numbers. Jamie to confirm.
5. **Neighborhood list** on Service Areas: Jamie to confirm which areas he covers.
6. **Hours** (Contact page) and **Jamie/Nic/Dan bios** (About page): not provided.
7. **Photos.** Striped boxes describe the real job photo to shoot for each spot.
8. **Domain.** Replace `https://www.YOUR-DOMAIN.com` (canonical tags, schema, sitemap, robots).
9. **Google reviews link.** Set `GOOGLE_REVIEWS_URL` (currently `#`).
10. **Form delivery.** Forms validate and go to the thank-you page but do not email anyone yet.
    Create a free form endpoint (Formspree or similar) and paste it into `FORM_ENDPOINT`
    in `assets/js/main.js`.

## SEO notes
- Each page has its own title, meta description, canonical URL and one H1 with service + location.
- schema.org markup: `Electrician` (a LocalBusiness type) on every page, plus `Service`,
  `FAQPage` and `BreadcrumbList` on service pages.
- The star rating is deliberately NOT in the schema: Google ignores (and can flag) star ratings
  a business marks up about itself. The rating shows on the page, which is what matters.
- Name/address/phone are identical in header and footer on every page.

## Editing
All pages are generated from `../jm-electrical-site-src/build.py`, where the phone, address,
license, services and FAQs live in one place. Edit there and run `python3 build.py`, or edit
the HTML files directly for one-off changes.
