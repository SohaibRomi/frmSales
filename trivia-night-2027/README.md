# Trivia Night & Auction 2027 — event page for Idaho Playground Project

A landing page for the Idaho Playground Project fundraiser on **Friday, January 22, 2027**
at Gaslamp on 3rd, Twin Falls — designed to be built entirely in **Elementor Free**.

## What's here

| File | What it is |
|---|---|
| `elementor-template/trivia-night-2027-elementor.json` | **Importable Elementor template** — the whole page, 13 sections, free widgets only |
| `elementor-template/IMPORT.md` | Import steps and the 10 things to do after importing |
| `elementor-template/build-template.py` | Generator for the JSON — edit this, not the JSON |
| `ELEMENTOR-BUILD-GUIDE.md` | Section-by-section build instructions: containers, widgets, exact settings, mobile pass, launch checklist |
| `copy-deck.md` | Every line of copy, paste-ready, with `[PLACEHOLDERS]` marked |
| `additional-css.css` | Paste into **Appearance → Customize → Additional CSS** |
| `countdown-widget.html` | Free replacement for Elementor Pro's Countdown widget (HTML widget) |
| `sticky-mobile-cta.html` | Free replacement for Pro's sticky CTA bar (HTML widget) |
| `assets/` | Images and the client's sponsorship PDF |

**Fastest path:** paste `additional-css.css` into Appearance → Customize → Additional CSS, then
import `elementor-template/trivia-night-2027-elementor.json` and follow `elementor-template/IMPORT.md`.
The build guide is there if you'd rather assemble it by hand or need to understand a decision.

The **visual design** lives in a Claude Artifact canvas — the full page design plus a brand-kit
board with the colour/type values to paste into Elementor Site Settings:
https://claude.ai/artifact/Uf1uiDDBwa8Lxy8mM9ZquQ
(private by default — share it from the page's Share menu before sending it to the client).

## Page structure

1. Hero — neon logo, date, venue, countdown, two CTAs
2. Fact bar — when / where / tickets / host
3. What's included — 6 cards
4. Host spotlight — Michael Beers
5. Mission + 3 stat counters
6. Tickets — $125 individual, $1,000 table
7. Sponsorship levels — the 5 tiers from the client's PDF
8. In-kind donations band
9. Sponsorship enquiry form + Kim Leonard's contact details
10. Venue, parking, accessibility, map
11. FAQ accordion
12. Sponsor wall (hidden until logos exist)
13. Final CTA + flyer download

## Design decisions

- **Two palettes, deliberately.** The hero, host, tickets and final CTA sections keep the flyer's
  dark neon look so the page matches what people saw on the flyer and on social. Everything in
  between switches to the Idaho Playground Project brand colours — teal, magenta, indigo, orange,
  sky — so the page still reads as the charity's, not a nightclub's.
- **Contrast was fixed, not copied.** The flyer's teal, orange and sky blue all fail WCAG AA with
  white text. The build guide uses darkened versions (`#00767A`, `#C96A00`, `#1B7FAA`) that pass.
  This matters more than usual for an accessibility charity.
- **Two CTAs, everywhere, in the same order.** Buy tickets (gold, always) then Become a sponsor
  (outline). The gold button only ever goes to the Zeffy ticketing link.
- **Sponsorship copy is verbatim** from the client's sponsorship PDF — tiers, prices, availability
  limits and bullets were not reworded.
- **No page-builder lock-in beyond Elementor Free.** One free form plugin is the only addition.

## Open questions for the client

Search the page for `[` before publishing — every placeholder is bracketed.

1. **Michael Beers bio** (60–80 words) and a **high-resolution headshot**.
   The file in `assets/` is a 222px crop from the flyer — fine for a mockup, too small to ship.
2. **The three mission statistics** (100 playgrounds by 2033 / 70% not ADA compliant / $250K+ per
   playground) came from press coverage, not from the client. Confirm all three.
3. **Where this year's proceeds go** — which school or park, and what gets built.
4. **FAQ answers** — dress code, age policy, payment methods on the night, and tax-deductibility
   wording (that one needs their accountant).
5. **Parking and accessibility** at Gaslamp on 3rd.
6. **Response time** on the sponsorship form — the draft says "within two business days".
7. **Table Sponsor appears twice** in the sponsorship PDF — at $1,000 as its own tier, and the
   "I Love Play But Hate Being Social" tier is also $1,000. Worth confirming that's intentional
   before it goes on a public page.
8. **Sponsorship deadline** — is there a cut-off date for logos to make the printed program?
   If so, it should go on the page.

## Note on the site itself

This container's network policy blocked `idahoplaygroundproject.org`, so the design was built from
the flyer, the neon logo, the venue image and the sponsorship PDF rather than from the live site's
CSS. Before building, check the existing site's header font and button radius and nudge the
Site Settings values to match if they differ.
