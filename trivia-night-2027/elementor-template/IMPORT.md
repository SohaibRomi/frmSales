# Importing the Elementor template

**File to import:** `trivia-night-2027-elementor.json`
(`trivia-night-2027-elementor.zip` is the same file zipped — use it if your
Elementor version's uploader refuses a bare `.json`.)

13 sections, 221 elements, **Elementor Free widgets only** — no Pro widget appears anywhere in it.

---

## Requirements

- **Elementor 3.16 or newer.** The template is built with flexbox **Containers**.
  Check: Elementor → Settings → Features. If you see a *Flexbox Container*
  experiment that is **Inactive**, switch it to **Active** before importing.
- A free form plugin for the sponsorship form (Fluent Forms Lite, WPForms Lite
  or Contact Form 7). Everything else is core Elementor Free.

---

## Step 1 — Paste the CSS first

**Appearance → Customize → Additional CSS** → paste all of `../additional-css.css` → **Publish**.

Do this *before* you look at the page. The countdown tiles, the sticky mobile
CTA bar, the card shadows and the neon glow all come from this file. Without it
the countdown renders as four bare numbers.

## Step 2 — Set up Site Settings

Elementor → **≡ → Site Settings** → Global Colors and Global Fonts.
Values are in `../ELEMENTOR-BUILD-GUIDE.md` §1. The template uses literal hex
everywhere, so it looks correct even if you skip this — but setting globals
means a future colour change is one edit instead of two hundred.

## Step 3 — Import

1. **Templates → Saved Templates → Import Templates** (top of the page).
2. Upload `trivia-night-2027-elementor.json` → **Import Now**.
3. It lands in the list as *Trivia Night & Auction 2027 — Idaho Playground Project*.

## Step 4 — Put it on a page

1. **Pages → Add New** → title `Trivia Night & Auction 2027` → Publish.
2. **Edit with Elementor**.
3. Grey folder icon in the canvas → **My Templates** → find it → **Insert**.
4. Asked *"Import document settings?"* → **Yes**. That applies the page layout
   (Elementor Full Width — keeps the site header and footer) and hides the page title.

---

## Step 5 — Add the five images

Every image in the template is **intentionally empty** — a template can't carry
binary files, and pointing at URLs that don't exist on your server yet would
import as broken images. Upload the files from `../assets/` to the Media
Library, then set them here:

| # | Where | File | Setting |
|---|---|---|---|
| 1 | Hero section — the container itself | `venue-lounge.png` | Container → Style → Background → Image |
| 2 | Hero — Image widget under the eyebrow | `trivia-neon-logo.png` | Alt text: `Trivia Night and Auction` |
| 3 | Host section — Image widget | `host-michael-beers.jpg` | ⚠️ 222px crop off the flyer — **get the real headshot before launch** |
| 4 | Final CTA section — the container itself | `venue-lounge.png` | Container → Style → Background → Image |
| 5 | Final CTA — Image widget | `event-flyer.jpg` | Also set this as the page's social share image |

Use the **Navigator** (bottom-left toggle, or `Cmd/Ctrl + I`) to find each one fast.

## Step 6 — Swap in the real form

In the *Secure your sponsorship* section there's an **HTML** widget holding a
dashed placeholder box. Its HTML comment lists every field and the exact
dropdown options.

1. Build the form in your form plugin.
2. Delete the HTML widget.
3. Drop a **Shortcode** widget in its place and paste the form's shortcode.
4. Set the notification email to `kim@idahoplaygroundproject.org` and turn on
   the plugin's honeypot.

## Step 7 — Link the sponsorship PDF

Upload `../assets/sponsorship-flyer.pdf` to the Media Library, copy its URL,
then in the *Secure your sponsorship* section open the Icon List item
**"Download the sponsorship packet (PDF)"** and paste the URL into its Link field.

## Step 8 — Clear the placeholders

Search the page for `[` — every outstanding item is bracketed:

- Host bio
- Where this year's proceeds go
- The three mission statistics (**confirm these — they came from press coverage, not the client**)
- Four FAQ answers: dress code, age policy, payment on the night, tax-deductibility
- Parking and accessibility at Gaslamp on 3rd

## Step 9 — Sponsor wall

The *Thank you to our 2027 sponsors* section is eight dashed placeholder tiles.
Right-click its container in the Navigator → **Disable** until there are real
logos. An empty thank-you wall reads worse than no wall.

## Step 10 — Mobile pass

Switch to the mobile viewport in Elementor and walk the page. The template
already carries mobile overrides for section padding, heading sizes and column
widths, but check: the hero logo, the date row wrapping to three lines, the
countdown as a 2×2 grid, and the sticky CTA bar at the bottom.

---

## Regenerating

`build-template.py` produced this JSON. Edit the Python and re-run it rather
than hand-editing 236KB of JSON:

```
python3 build-template.py
```

Element IDs are seeded, so re-running gives the same IDs — re-importing cleanly
replaces the old template instead of creating a near-duplicate.

---

## If something looks wrong after import

| Symptom | Cause |
|---|---|
| Countdown shows four dashes, no styling | `additional-css.css` not pasted into Additional CSS |
| Sections stack with no columns | Flexbox Container experiment is off, or Elementor is below 3.16 |
| Buttons are square and blue | Theme CSS overriding Elementor — set *Elementor → Settings → Style → Disable Default Colors/Fonts* to off |
| Fonts look like the theme's | Global Fonts not set, and Poppins/Nunito Sans/Yellowtail not yet fetched — open Site Settings once and save |
| "Buy tickets" goes nowhere | Check the three Zeffy buttons kept their link on import (hero, tickets card, final CTA) |
