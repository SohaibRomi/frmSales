# Trivia Night & Auction 2027 — Elementor **Free** build guide

Target site: https://idahoplaygroundproject.org/
Page title: **Trivia Night & Auction 2027**
Suggested slug: `/trivia-night/` (keep it evergreen — reuse it next year)

Everything below is buildable on **Elementor Free**. Where a widget is Pro-only,
the workaround is given inline. One free form plugin is required; nothing else.

---

## 0. Before you open Elementor

### 0.1 Page setup
1. **Pages → Add New** → title `Trivia Night & Auction 2027`.
2. Publish once (empty), then **Edit with Elementor**.
3. Elementor panel → **gear icon (Page Settings)** → **Page Layout: Elementor Full Width**.
   - Keeps the site's existing header and footer, removes the theme's content width.
   - Do *not* use *Elementor Canvas* — that strips the header/footer and breaks site navigation.
4. **Hide Title**: On.

### 0.2 Plugins to install (free)
| Need | Plugin | Why |
|---|---|---|
| Sponsorship enquiry form | **Fluent Forms Lite** (or WPForms Lite / Contact Form 7) | Elementor's Form widget is Pro. Insert the form with the free **Shortcode** widget. |
| Nothing else | — | Countdown and sticky mobile CTA are handled with the free **HTML** widget — snippets are in this repo. |

> If you'd rather not hand-code, **Happy Addons Free** or **Essential Addons Lite** both ship a
> free Countdown widget. It's one more plugin on the site; the HTML snippet avoids that.

### 0.3 Upload media
Upload from `assets/` in this folder:
- `trivia-neon-logo.png` — hero logo (transparent PNG)
- `venue-lounge.png` — hero + final CTA background
- `event-flyer.jpg` — flyer thumbnail, and set as the page's **social share image**
- `sponsorship-flyer.pdf` — linked as "Download the sponsorship packet"
- `host-michael-beers.jpg` — **low-res placeholder only (222px, cropped from the flyer).** Ask the client for the original headshot before launch.

Rename on upload so the alt text and filenames are descriptive, e.g.
`trivia-night-auction-2027-idaho-playground-project.jpg`.

---

## 1. Site Settings — do this first, once

Elementor → **hamburger menu (≡) → Site Settings**.

### 1.1 Global Colors
| Slot | Name | Hex |
|---|---|---|
| Primary | Night Plum | `#1E1033` |
| Secondary | IPP Magenta | `#B2185F` |
| Text | Body Grey | `#6B6382` |
| Accent | IPP Teal | `#00767A` |
| + Add custom | Neon Gold | `#FFC63F` |
| + Add custom | Neon Pink | `#FF4FB0` |
| + Add custom | IPP Indigo | `#4A55B5` |
| + Add custom | IPP Orange | `#C96A00` |
| + Add custom | IPP Sky | `#1B7FAA` |
| + Add custom | Soft Lilac | `#F6F4FA` |
| + Add custom | Hero Black | `#140B22` |

**Contrast rule:** never put white text on `#FFC63F`, `#F7941D` or `#29ABE2` — it fails WCAG AA.
Use `#140B22` text on those. The teal/magenta/orange values above are already darkened from the
flyer so white text passes at 4.5:1.

### 1.2 Global Fonts
| Slot | Family | Weight | Use |
|---|---|---|---|
| Primary | **Poppins** | 800 | H1, H2, H3 |
| Secondary | **Poppins** | 600 | Eyebrows, buttons, labels |
| Text | **Nunito Sans** | 400 | Body copy |
| Accent | **Yellowtail** | 400 | Script eyebrow lines only |

Type scale (desktop → mobile):
- H1 `46px → 32px`, line-height 1.15
- H2 `44px → 30px`, line-height 1.15
- H3 `24px → 20px`
- Body `18px → 16px`, line-height 1.7
- Small print `13px`, colour `#8A80A3`

### 1.3 Layout
- Content Width: **1200px**
- Widgets Space: **20px**
- Breakpoints: leave default (Mobile 767, Tablet 1024)

---

## 2. Global CSS

Elementor Free has no per-widget Custom CSS. Paste `additional-css.css` (in this folder) into
**Appearance → Customize → Additional CSS** and save. It adds:

- `.tn-section` — standard section rhythm (96px desktop / 56px mobile)
- `.tn-card` — rounded card with the house shadow
- `.tn-neon` — the neon text-glow on dark headings
- `.tn-dashed` — dashed in-kind panel
- `.tn-sticky-cta` — the mobile sticky "Buy tickets" bar
- Countdown styling for the HTML widget

Apply a class to any element via **Advanced tab → CSS Classes** (this field *is* in Free).

---

## 3. Section-by-section build

Every section = one **Container** (flexbox). Pattern used throughout:

> Container → Layout: `Boxed`, Content Width `1200`, Direction `Column`, Align `Center`
> → Style → Background → (as noted)
> → Advanced → Padding `96 24 96 24` desktop, `56 20 56 20` mobile, CSS Class `tn-section`

---

### Section 1 — Hero (dark, neon)

**Container settings**
- Background → Classic → Image: `venue-lounge.png`, Position `center center`, Size `cover`
- Background Overlay → Classic → Colour `#140B22`, Opacity `0.78`
- Min Height: `720px` desktop / `auto` mobile
- Padding: `84 24 96 24`

**Widgets, top to bottom:**

1. **Heading** — `IDAHO PLAYGROUND PROJECT PRESENTS`
   - HTML tag `p`, Secondary font, 15px, letter-spacing `0.26em`, colour `#FFC63F`, centered.
2. **Image** — `trivia-neon-logo.png`
   - Max Width `620px`, Align center. **Alt text:** `Trivia Night and Auction`.
3. **Heading** — `DINNER · DRINKS · COMEDY · RAFFLES · SILENT & LIVE AUCTIONS`
   - tag `p`, 17px, letter-spacing `0.1em`, white, centered.
4. **Inner container** (Direction `Row`, Wrap `Wrap`, Justify `Center`, Gap `28`):
   - Heading `Friday` — Yellowtail 42px, `#FF4FB0`
   - Heading `January 22, 2027` — Poppins 800, 34px, white
   - Heading `Doors open 6:00 PM` — Poppins 600, 20px, `#FFC63F`
5. **Heading** — `Gaslamp on 3rd · 269 3rd Ave S, Twin Falls, ID` — tag `p`, 17px, `#D9D2EA`
6. **HTML widget** — paste `countdown-widget.html` (Pro Countdown replacement)
7. **Inner container** (Row, Center, Gap `16`):
   - **Button** `Buy tickets — $125`
     Link: `https://www.zeffy.com/en-US/ticketing/2027-idaho-playground-project-trivia-night-and-auction`
     (tick *Open in new tab* and *Add nofollow*)
     Style: Background `#FFC63F`, Text `#140B22`, Typography Poppins 700 17px,
     Padding `19 40 19 40`, Border Radius `999px`
   - **Button** `Become a sponsor` → link `#sponsorships`
     Style: Background `transparent`, Border `2px solid #FF4FB0`, Text white, same padding/radius
8. **Heading** — `Every ticket includes dinner, 1 drink ticket and 1 raffle ticket.` — tag `p`, 14px, `#A79CC4`

---

### Section 2 — Fact bar

- Container background `#1E1033`, Padding `0 24 0 24`
- Inner container: Direction `Row`, Wrap `Wrap`, Gap `1px`, background `rgba(255,255,255,0.08)`
- **4 × Icon Box**, each in its own container at `25%` width (Tablet `50%`, Mobile `100%`),
  background `#1E1033`, padding `32 28 32 28`
  - Icon position: **Left**, icon size 26, no icon background
  - Title tag `p` — the small uppercase label; Description — the two-line detail

| Icon | Label | Detail |
|---|---|---|
| Calendar | WHEN | Friday, January 22, 2027 / Doors 6:00 PM |
| Map pin | WHERE | Gaslamp on 3rd / 269 3rd Ave S, Twin Falls |
| Ticket | TICKETS | $125 per seat / Dinner + drink + raffle |
| Microphone | YOUR HOST | Michael Beers / Comedian & emcee |

Icon colours in order: `#FF4FB0`, `#FFC63F`, `#B778FF`, `#00D6D8`.

---

### Section 3 — What's included

- Background `#FFFFFF`
- Heading block (centered, max-width 740px):
  - Yellowtail eyebrow `One good night` 34px `#B2185F`
  - H2 `Here's what you're walking into`
  - Body paragraph (see `copy-deck.md`)
- **6 × Icon Box** in a Row container, 3 per row (Tablet 2, Mobile 1), Gap `24`
  - Each box: container background `#F6F4FA`, radius `18px`, padding `34 30 34 30`, CSS class `tn-card`
  - Icon: **top** position, custom size 28, icon wrapper 56×56 with its own fill colour and 16px radius
  - Tile colours in order: `#00767A`, `#B2185F`, `#4A55B5`, `#C96A00`, `#1B7FAA`, `#7A2BC4`

Titles: Dinner is served · Live trivia, team style · Comedy all night ·
Silent & live auctions · Raffles · The Balloon Pop

---

### Section 4 — Host spotlight

- Background `#140B22`, padding `88 24 88 24`
- Row container, Gap `48`, Align `Center`:
  - **Image** (width 260, Border Radius `999px`, 6px gradient ring — use `tn-ring` class from the CSS file)
  - Column:
    - Eyebrow `YOUR HOST FOR THE EVENING` — `#FFC63F`, 13px, letter-spacing `0.22em`
    - H2 `Michael Beers` — white, CSS class `tn-neon`
    - Yellowtail `Comedian & host` 30px `#FF4FB0`
    - **Text Editor** — bio (⚠️ still a placeholder, see Open Questions)

---

### Section 5 — Mission + stats

- Background `#F6F4FA`
- Row container, Gap `56`, Align `Flex start`
  - **Left (60%)**: eyebrow, H2 `Every kid deserves a playground they can actually use`,
    two paragraphs, Button `More about our mission` → `https://idahoplaygroundproject.org/`
  - **Right (40%)**: 3 stacked white cards, each **Counter** widget + Text Editor
    - Counter 1: `100` — colour `#B2185F`
    - Counter 2: `70` suffix `%` — colour `#00767A`
    - Counter 3: `250` prefix `$` suffix `K+` — colour `#4A55B5`
    - Counter typography: Poppins 800, 48px
    - ⚠️ **Confirm all three figures with the client before publishing.**

---

### Section 6 — Tickets

- Background `#1E1033`, anchor: add a **Menu Anchor** widget with ID `tickets` at the top
- Two cards in a Row container, Gap `24`, Align `Stretch`

**Card A — Individual seat**
- Container: background `#2A1748`, border `1px solid rgba(255,198,63,0.35)`, radius `22px`, padding `40 36 40 36`
- Eyebrow `INDIVIDUAL SEAT` `#FFC63F` → Heading `$125` Poppins 800 60px white
- **Icon List** (free) — check icon `#FFC63F`, text `#E6E0F2` 16px:
  Dinner included / 1 drink ticket / 1 raffle ticket / A spot at a trivia table, comedy and both auctions
- Button `Buy a ticket` → Zeffy link, full width, gold
- Small print `Processed securely through Zeffy.`

**Card B — Table Sponsor**
- Container: background `rgba(255,255,255,0.04)`, border `1px solid rgba(255,255,255,0.14)`
- Eyebrow `BRING YOUR WHOLE TEAM` `#FF4FB0` → `$1,000` → subtitle
- Icon List (pink checks) → Button `See sponsorship levels` → `#sponsorships` (outline style)

> Elementor's **Price Table** is Pro. This container-plus-Icon-List build is the free equivalent
> and gives you more styling control anyway.

---

### Section 7 — Sponsorship levels

- Background `#FFFFFF`
- **Menu Anchor** widget at the top with ID `sponsorships`
- Centered heading block (Yellowtail eyebrow + H2 + intro paragraph)

**Build ONE card, then right-click → Duplicate ×4.** Card structure:

```
Container (radius 20, overflow hidden, border 2px, direction column, stretch)
├── Container (the coloured head, padding 26 28)
│   ├── Heading  — availability label, 11px, 0.18em tracking, tinted white
│   ├── Heading  — tier name, H3, 27px, white
│   └── Heading  — price, Poppins 800, 40px, white
└── Container (body, padding 28, flex-grow 1)
    ├── Text Editor — tier blurb
    ├── Icon List   — the "Includes" bullets
    └── Button      — "Claim this level" → #sponsor-form
```

| Tier | Price | Head colour | Availability label |
|---|---|---|---|
| The Big Kahuna | $10,000 | `#00767A` | TITLE SPONSOR — ONLY 1 AVAILABLE |
| The Game Changer | $5,000 | `#B2185F` | ENTERTAINMENT — UP TO 4 AVAILABLE |
| The Pop of Fun | $2,500 | `#4A55B5` | BALLOON SPONSOR — ONLY 1 AVAILABLE |
| "I Love Play But Hate Being Social" | $1,000 or $500 | `#C96A00` | SUPPORT FROM AFAR |
| Table Sponsor | $1,000 | `#1B7FAA` | BRING YOUR PEOPLE |

Layout: row 1 = 3 cards (33.33% each), row 2 = 2 cards (50% each). Tablet 2-up, mobile 1-up.
Give **The Big Kahuna** a `2px solid #00767A` border and the `tn-card` shadow so it reads as the hero tier.

Bullet copy is in `copy-deck.md`, taken verbatim from the client's sponsorship PDF.

Below the cards: a note — `Every sponsor seat includes dinner, 1 drink ticket and 1 raffle ticket. Individual tickets are $125.`

---

### Section 8 — In-kind donations band

- Inside the same section, a container with background `#FFF4E3`, `2px dashed #C96A00`,
  radius `20px`, padding `40`, CSS class `tn-dashed`
- Row: H3 + paragraph on the left, Button on the right
- Button → `mailto:kim@idahoplaygroundproject.org?subject=In-kind%20donation%20for%20Trivia%20Night%202027`

---

### Section 9 — Sponsor form

- Background `#F6F4FA`
- **Menu Anchor** with ID `sponsor-form`
- Row container, Gap `48`:
  - **Left**: eyebrow, H2 `Secure your sponsorship`, paragraph, then an **Icon List** with
    Kim Leonard / `kim@idahoplaygroundproject.org` (mailto) / `208-490-1103` (tel),
    then a text link → `sponsorship-flyer.pdf` ("Download the sponsorship packet (PDF)")
  - **Right**: white card (radius 22, padding 40, `tn-card`) containing a **Shortcode** widget
    with your form plugin's shortcode.

**Form fields:** Your name · Business/organisation · Email · Phone ·
Sponsorship level (dropdown, options below) · Anything we should know? (textarea)

Dropdown options:
```
The Big Kahuna — $10,000
The Game Changer — $5,000
The Pop of Fun — $2,500
I Love Play But Hate Being Social — $1,000 or $500
Table Sponsor — $1,000
In-kind donation
Not sure yet — please advise
```

Set the form's notification email to `kim@idahoplaygroundproject.org`, add an autoresponder, and
turn on the plugin's honeypot/anti-spam. Style inputs to match: `1px solid #D8D2E6`, radius `10px`,
height `50px`. Submit button: `#B2185F`, white text, radius `999px`, min-height `56px`.

---

### Section 10 — Venue & parking

- Background `#FFFFFF`
- Centered heading block: Yellowtail `Find us` + H2 `Gaslamp on 3rd` + address line
- Row container, Gap `24`:
  - **Google Maps widget** (free) — address `269 3rd Ave S, Twin Falls, ID 83301`,
    Zoom 15, Height `360`, radius `20px`
  - Column with two **Icon Box**/card blocks — **Parking** and **Accessibility** (⚠️ copy needed)
    plus a Button `Get directions` → `https://maps.google.com/?q=269+3rd+Ave+S,+Twin+Falls,+ID+83301`

> For an accessibility charity, the Accessibility card is not optional — get that copy from the client.

---

### Section 11 — FAQ

- Background `#F6F4FA`, container max-width `860px`
- **Accordion widget** (free), 6 items:
  1. Do I need a full team of eight?
  2. What's included in the $125 ticket?
  3. What should I wear? ⚠️
  4. Is this a 21+ event? ⚠️
  5. How do I pay for auction wins and raffle tickets? ⚠️
  6. Is my ticket or sponsorship tax-deductible? ⚠️
- Style: Title Poppins 700 18px `#1E1033`, item background white, radius `14px`, space between `12px`,
  active icon colour `#B2185F`
- ⚠️ = answer still needs the client. Answers 1 and 2 are written in `copy-deck.md`.

---

### Section 12 — Sponsor wall

- Background `#FFFFFF`, padding `80 24 80 24`
- H2 `Thank you to our 2027 sponsors` + line `This wall fills up as sponsors come on board.`
- **Basic Gallery** (free) or 8 × Image in a 4-column grid, 110px tall tiles
- **Hide this whole section until there are real logos** — Advanced → Responsive → hide on all
  devices, or right-click the container → Disable. An empty "thank you" wall reads badly.

---

### Section 13 — Final CTA

- Same treatment as the hero: `venue-lounge.png` background, `#140B22` overlay at `0.88`
- Row container, Gap `48`:
  - Left: Yellowtail `See you Friday` → H2 `January 22, 2027 — Gaslamp on 3rd` (`tn-neon`) →
    paragraph → two Buttons (`Buy tickets` gold, `Sponsor the night` white outline)
  - Right: **Image** `event-flyer.jpg`, width 250px, radius 14px, caption `Share the flyer with your team`,
    link set to Media File so people can open and save it

---

## 4. Mobile pass (do this before launch)

Switch Elementor to the mobile viewport and check each one:

1. Hero H1/logo — logo max-width `320px`, padding top `56`
2. The `Friday / January 22, 2027 / Doors 6PM` row wraps to 3 centered lines
3. Countdown tiles — 2×2 grid, not 4 across (handled by the CSS file)
4. Every multi-column row set to **100% width** on mobile
5. Buttons: full width on mobile, min-height `56px` (thumb-friendly)
6. Section padding drops to `56 20`
7. The sticky mobile CTA bar (`tn-sticky-cta` in the CSS file) appears below 767px —
   it keeps "Buy tickets" one tap away through the whole scroll
8. Google Map doesn't overflow — set height `280px` on mobile

---

## 5. Launch checklist

- [ ] All three Zeffy buttons point at the live ticketing URL and open in a new tab
- [ ] `#sponsorships`, `#sponsor-form`, `#tickets` anchors scroll correctly (Menu Anchor widgets placed)
- [ ] Form sends a test entry to `kim@idahoplaygroundproject.org` **and** the autoresponder arrives
- [ ] Sponsorship PDF downloads
- [ ] Every image has real alt text; hero logo alt = `Trivia Night and Auction`
- [ ] Social share image set to `event-flyer.jpg` (Yoast/Rank Math → Social tab)
- [ ] Meta title: `Trivia Night & Auction 2027 | Idaho Playground Project`
- [ ] Meta description: `Dinner, comedy, trivia and auctions at Gaslamp on 3rd in Twin Falls, Friday January 22, 2027. Tickets $125 — every seat builds inclusive playgrounds for Idaho kids.`
- [ ] Page added to the site menu (and linked from the homepage)
- [ ] Mobile + tablet pass done
- [ ] Contrast spot-check with a checker on the gold and teal buttons
- [ ] Countdown shows the right number of days
- [ ] Every ⚠️ placeholder replaced — search the page for `[` before you publish

---

## 6. What was Pro — and what we did instead

| Pro feature | Free replacement used here |
|---|---|
| Countdown widget | HTML widget + `countdown-widget.html` snippet |
| Form widget | Fluent Forms Lite (or similar) via the Shortcode widget |
| Price Table | Styled container + Heading + Icon List + Button |
| Call to Action / Flip Box | Container with background overlay + Heading + Button |
| Per-widget Custom CSS | `additional-css.css` in Appearance → Customize → Additional CSS, applied with CSS Classes |
| Sticky header / sticky CTA | `tn-sticky-cta` CSS in the same file |
| Motion effects on scroll | Elementor Free **entrance animations** (Advanced → Motion Effects → Entrance Animation: Fade In Up, 600ms) — use sparingly, on section headings only |
| Theme Builder (custom header) | Not needed — page uses the theme's existing header via *Elementor Full Width* |
| Nav Menu widget | Not needed on this page |
