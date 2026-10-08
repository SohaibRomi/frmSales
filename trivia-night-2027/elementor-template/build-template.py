#!/usr/bin/env python3
"""
Generates an Elementor template JSON for the Idaho Playground Project
"Trivia Night & Auction 2027" event page.

Output: trivia-night-2027-elementor.json
Import: Elementor -> Templates -> Saved Templates -> Import Templates

Built with flexbox CONTAINERS (Elementor 3.16+, free). Colours are written as
literal hex so the page looks right the moment it is imported, whether or not
Global Colors have been set up yet.

Run:  python3 build-template.py
"""

import json
import os
import random
import string

random.seed(20270122)  # stable ids across regenerations

PLUM = "#1E1033"
BLACK = "#140B22"
MAGENTA = "#B2185F"
TEAL = "#00767A"
INDIGO = "#4A55B5"
ORANGE = "#C96A00"
SKY = "#1B7FAA"
PURPLE = "#7A2BC4"
GOLD = "#FFC63F"
PINK = "#FF4FB0"
VIOLET = "#B778FF"
CYAN = "#00D6D8"
LILAC = "#F6F4FA"
BODY = "#6B6382"
MUTED = "#8A80A3"
WHITE = "#FFFFFF"
ON_DARK = "#D9D2EA"
ON_DARK_2 = "#BBB1D4"
ON_DARK_3 = "#A79CC4"
CARD_LINE = "#E4E0EE"

HEAD_FONT = "Poppins"
BODY_FONT = "Nunito Sans"
SCRIPT_FONT = "Yellowtail"

ZEFFY = ("https://www.zeffy.com/en-US/ticketing/"
         "2027-idaho-playground-project-trivia-night-and-auction")
SITE = "https://idahoplaygroundproject.org/"
MAILTO = "mailto:kim@idahoplaygroundproject.org"
INKIND = (MAILTO + "?subject=In-kind%20donation%20for%20Trivia%20Night%202027")
DIRECTIONS = "https://maps.google.com/?q=269+3rd+Ave+S,+Twin+Falls,+ID+83301"


def uid():
    return "".join(random.choice(string.hexdigits.lower()[:16]) for _ in range(7))


# --------------------------------------------------------------------------
# primitives
# --------------------------------------------------------------------------

def dim(top, right, bottom, left, unit="px"):
    return {"unit": unit, "top": str(top), "right": str(right),
            "bottom": str(bottom), "left": str(left), "isLinked": False}


def allsides(v, unit="px"):
    return {"unit": unit, "top": str(v), "right": str(v), "bottom": str(v),
            "left": str(v), "isLinked": True}


def size(v, unit="px"):
    return {"unit": unit, "size": v, "sizes": []}


def gap(v):
    return {"column": str(v), "row": str(v), "isLinked": True,
            "unit": "px", "size": v}


def icon(value, library="fa-solid"):
    return {"value": value, "library": library}


def link(url, external=True, nofollow=False):
    return {"url": url,
            "is_external": "on" if external else "",
            "nofollow": "on" if nofollow else "",
            "custom_attributes": ""}


def typo(prefix="typography", family=HEAD_FONT, fs=None, weight=None,
         lh=None, ls=None, transform=None, fs_mobile=None):
    """Elementor group typography control, flattened."""
    out = {f"{prefix}_typography": "custom", f"{prefix}_font_family": family}
    if weight:
        out[f"{prefix}_font_weight"] = str(weight)
    if fs is not None:
        out[f"{prefix}_font_size"] = size(fs)
    if fs_mobile is not None:
        out[f"{prefix}_font_size_mobile"] = size(fs_mobile)
    if lh is not None:
        out[f"{prefix}_line_height"] = size(lh, "em")
    if ls is not None:
        out[f"{prefix}_letter_spacing"] = size(ls)
    if transform:
        out[f"{prefix}_text_transform"] = transform
    return out


def widget(wtype, settings):
    return {"id": uid(), "elType": "widget", "widgetType": wtype,
            "settings": settings, "elements": [], "isInner": False}


def container(settings, children):
    return {"id": uid(), "elType": "container", "settings": settings,
            "elements": children, "isInner": False}


# --------------------------------------------------------------------------
# container helpers
# --------------------------------------------------------------------------

def section(children, bg=None, bg_image=False, overlay=None, pad=(96, 24, 96, 24),
            width=1200, extra=None, gap_px=24, min_height=None, css_class=None):
    s = {
        "content_width": "boxed",
        "width": size(width),
        "boxed_width": size(width),
        "flex_direction": "column",
        "flex_align_items": "center",
        "flex_gap": gap(gap_px),
        "padding": dim(*pad),
        "padding_mobile": dim(56, 20, 56, 20),
    }
    if bg:
        s["background_background"] = "classic"
        s["background_color"] = bg
    if bg_image:
        # left empty on purpose: pick the image in the media library after import
        s["background_image"] = {"url": "", "id": "", "size": "",
                                 "alt": "", "source": "library"}
        s["background_position"] = "center center"
        s["background_size"] = "cover"
        s["background_repeat"] = "no-repeat"
    if overlay is not None:
        s["background_overlay_background"] = "classic"
        s["background_overlay_color"] = BLACK
        s["background_overlay_opacity"] = size(overlay)
    if min_height is not None:
        s["min_height"] = size(min_height)
        s["min_height_mobile"] = {"unit": "px", "size": "", "sizes": []}
    if css_class:
        s["css_classes"] = css_class
        s["_css_classes"] = css_class
    if extra:
        s.update(extra)
    return container(s, children)


def row(children, gap_px=24, justify="center", align="stretch", wrap="wrap",
        extra=None):
    s = {
        "content_width": "full",
        "flex_direction": "row",
        "flex_wrap": wrap,
        "flex_justify_content": justify,
        "flex_align_items": align,
        "flex_gap": gap(gap_px),
        "padding": allsides(0),
    }
    if extra:
        s.update(extra)
    return container(s, children)


def col(children, pct=100, tablet=100, mobile=100, bg=None, radius=None,
        pad=None, border=None, css_class=None, extra=None, align="flex-start",
        justify="flex-start"):
    s = {
        "content_width": "full",
        "width": size(pct, "%"),
        "width_tablet": size(tablet, "%"),
        "width_mobile": size(mobile, "%"),
        "flex_direction": "column",
        "flex_align_items": align,
        "flex_justify_content": justify,
        "flex_gap": gap(14),
        "padding": allsides(0),
    }
    if bg:
        s["background_background"] = "classic"
        s["background_color"] = bg
    if radius is not None:
        s["border_radius"] = allsides(radius)
    if pad is not None:
        s["padding"] = dim(*pad)
    if border:
        s["border_border"] = border.get("style", "solid")
        s["border_width"] = allsides(border.get("width", 1))
        s["border_color"] = border["color"]
    if css_class:
        s["css_classes"] = css_class
        s["_css_classes"] = css_class
    if extra:
        s.update(extra)
    return container(s, children)


# --------------------------------------------------------------------------
# widget helpers
# --------------------------------------------------------------------------

def heading(text, tag="h2", fs=44, weight=800, color=PLUM, family=HEAD_FONT,
            align="center", lh=1.15, ls=None, transform=None, fs_mobile=None,
            extra=None):
    s = {"title": text, "header_size": tag, "align": align,
         "align_mobile": "center", "title_color": color}
    s.update(typo(family=family, fs=fs, weight=weight, lh=lh, ls=ls,
                  transform=transform, fs_mobile=fs_mobile))
    if extra:
        s.update(extra)
    return widget("heading", s)


def eyebrow(text, color=GOLD, align="center"):
    return heading(text, tag="p", fs=13, weight=700, color=color, align=align,
                   lh=1.5, ls=2.6, transform="uppercase")


def script(text, color=MAGENTA, fs=34, align="center"):
    return heading(text, tag="p", fs=fs, weight=400, color=color,
                   family=SCRIPT_FONT, align=align, lh=1.1)


def para(html, color=BODY, fs=18, align="center", fs_mobile=16, extra=None):
    s = {"editor": f"<p>{html}</p>", "align": align, "text_color": color}
    s.update(typo(family=BODY_FONT, fs=fs, weight=400, lh=1.7,
                  fs_mobile=fs_mobile))
    if extra:
        s.update(extra)
    return widget("text-editor", s)


def button(label, url, bg=GOLD, fg=BLACK, border_color=None, align="center",
           external=True, nofollow=False, full=False, pad=(19, 40, 19, 40)):
    s = {
        "text": label,
        "link": link(url, external, nofollow),
        "align": align,
        "align_mobile": "justify" if full else "center",
        "size": "md",
        "button_text_color": fg,
        "border_radius": allsides(999),
        "text_padding": dim(*pad),
        "_css_classes": "tn-btn",
        "css_classes": "tn-btn",
    }
    # Button background is a Group_Control_Background: it needs the
    # "_background" discriminator or Elementor ignores the colour.
    s["background_background"] = "classic"
    s["background_color"] = bg if bg else "rgba(0,0,0,0)"
    s["button_background_color"] = s["background_color"]  # older-schema alias
    if border_color:
        s["border_border"] = "solid"
        s["border_width"] = allsides(2)
        s["border_color"] = border_color
    s.update(typo(family=HEAD_FONT, fs=17, weight=700))
    return widget("button", s)


def icon_box(title, desc, ic, icon_color=TEAL, position="top",
             title_color=PLUM, desc_color=BODY, title_size=22,
             icon_size=28, bg_shape=None):
    s = {
        "title_text": title,
        "description_text": desc,
        "selected_icon": ic,
        "position": position,
        "title_color": title_color,
        "description_color": desc_color,
        "primary_color": icon_color,
        "icon_space": size(20),
    }
    s.update(typo(prefix="title_typography", family=HEAD_FONT, fs=title_size,
                  weight=700, lh=1.3))
    s.update(typo(prefix="description_typography", family=BODY_FONT, fs=16,
                  weight=400, lh=1.65))
    if bg_shape:
        # stacked view: primary_color = tile fill, secondary_color = glyph
        s["view"] = "stacked"
        s["shape"] = "square"
        s["primary_color"] = bg_shape
        s["secondary_color"] = WHITE
        s["icon_padding"] = size(14)
        s["border_radius"] = allsides(16)
    s["icon_size"] = size(icon_size)
    return widget("icon-box", s)


def icon_list(items, icon_color=TEAL, text_color="#2B2440", fs=16,
              ic="fas fa-check", space=14):
    rows = []
    for t in items:
        rows.append({"text": t, "selected_icon": icon(ic), "_id": uid()})
    s = {
        "icon_list": rows,
        "space_between": size(space),
        "icon_color": icon_color,
        "text_color": text_color,
        "icon_size": size(17),
        "_css_classes": "tn-list",
        "css_classes": "tn-list",
    }
    s.update(typo(prefix="icon_typography", family=BODY_FONT, fs=fs,
                  weight=400, lh=1.55))
    return widget("icon-list", s)


def anchor(name):
    return widget("menu-anchor", {"anchor": name})


def spacer(px):
    return widget("spacer", {"space": size(px)})


def html_widget(code):
    return widget("html", {"html": code})


def image(width_px=None, align="center", caption=None, link_url=None):
    s = {
        "image": {"url": "", "id": "", "size": "", "alt": "",
                  "source": "library"},
        "image_size": "full",
        "align": align,
        "align_mobile": "center",
    }
    if width_px:
        s["width"] = size(width_px)
    if link_url:
        s["link_to"] = "custom"
        s["link"] = link(link_url)
    if caption:
        s["caption_source"] = "custom"
        s["caption"] = caption
    return widget("image", s)


# --------------------------------------------------------------------------
# sections
# --------------------------------------------------------------------------

def s_hero():
    date_row = row([
        heading("Friday", tag="p", fs=42, weight=400, color=PINK,
                family=SCRIPT_FONT, lh=1.0),
        heading("January 22, 2027", tag="p", fs=34, weight=800, color=WHITE,
                lh=1.2, fs_mobile=28),
        heading("Doors open 6:00 PM", tag="p", fs=20, weight=600, color=GOLD,
                lh=1.2),
    ], gap_px=28, align="center")

    cta_row = row([
        col([button("Buy tickets — $125", ZEFFY, bg=GOLD, fg=BLACK,
                    nofollow=True)], pct=48, tablet=48, mobile=100,
            align="center"),
        col([button("Become a sponsor", "#sponsorships", bg=None, fg=WHITE,
                    border_color=PINK, external=False)],
            pct=48, tablet=48, mobile=100, align="center"),
    ], gap_px=16, align="center")

    return section([
        eyebrow("Idaho Playground Project presents", GOLD),
        image(width_px=620),
        heading("Dinner · Drinks · Comedy · Raffles · Silent &amp; Live Auctions",
                tag="p", fs=17, weight=600, color=WHITE, lh=1.7, ls=1.7,
                transform="uppercase", fs_mobile=14),
        date_row,
        para("Gaslamp on 3rd · 269 3rd Ave S, Twin Falls, ID", color=ON_DARK,
             fs=17),
        html_widget(COUNTDOWN_HTML),
        cta_row,
        para("Every ticket includes dinner, 1 drink ticket and 1 raffle ticket.",
             color=ON_DARK_3, fs=14),
    ], bg=BLACK, bg_image=True, overlay=0.78, pad=(84, 24, 96, 24),
        width=1040, min_height=720, gap_px=26)


def s_factbar():
    facts = [
        ("When", "Friday, January 22, 2027<br>Doors 6:00 PM",
         icon("far fa-calendar-alt", "fa-regular"), PINK),
        ("Where", "Gaslamp on 3rd<br>269 3rd Ave S, Twin Falls",
         icon("fas fa-map-marker-alt"), GOLD),
        ("Tickets", "$125 per seat<br>Dinner + drink + raffle",
         icon("fas fa-ticket-alt"), VIOLET),
        ("Your host", "Michael Beers<br>Comedian &amp; emcee",
         icon("fas fa-microphone-alt"), CYAN),
    ]
    cells = []
    for label, detail, ic, color in facts:
        box = icon_box(label.upper(), detail, ic, icon_color=color,
                       position="left", title_color=ON_DARK_2,
                       desc_color=WHITE, title_size=12, icon_size=26)
        box["settings"].update(typo(prefix="title_typography",
                                    family=HEAD_FONT, fs=12, weight=700,
                                    lh=1.4, ls=1.9, transform="uppercase"))
        box["settings"].update(typo(prefix="description_typography",
                                    family=HEAD_FONT, fs=17, weight=700,
                                    lh=1.45))
        cells.append(col([box], pct=24.4, tablet=49, mobile=100, bg=PLUM,
                         pad=(32, 28, 32, 28)))
    return section([row(cells, gap_px=1, align="stretch")],
                   bg="rgba(255,255,255,0.08)", pad=(0, 24, 0, 24), gap_px=0,
                   extra={"background_color": PLUM})


def s_included():
    cards = [
        ("Dinner is served",
         "A full dinner is included with every ticket, plus one drink ticket "
         "to get the night started.", "fas fa-utensils", TEAL),
        ("Live trivia, team style",
         "Multiple rounds, big screens, and bragging rights on the line. Come "
         "as a table of eight or let us seat you.", "fas fa-brain", MAGENTA),
        ("Comedy all night",
         "Comedian Michael Beers hosts, keeps score, and may gently roast your "
         "table along the way.", "fas fa-theater-masks", INDIGO),
        ("Silent &amp; live auctions",
         "Bid on packages donated by Magic Valley businesses and neighbours. "
         "Auction catalogue posts closer to the night.", "fas fa-gavel", ORANGE),
        ("Raffles",
         "One raffle ticket comes with your seat. More are available on the "
         "night — bring cash or a card.", "fas fa-gift", SKY),
        ("The Balloon Pop",
         "Pop a balloon, win what's inside. Prizes are stuffed in by our "
         "Balloon Sponsor — in their brand colours.",
         "fas fa-birthday-cake", PURPLE),
    ]
    tiles = []
    for title, desc, ic, color in cards:
        box = icon_box(title, desc, icon(ic), icon_color=color, position="top",
                       bg_shape=color)
        box["settings"]["align"] = "left"
        tiles.append(col([box], pct=31.8, tablet=48.5, mobile=100, bg=LILAC,
                         radius=18, pad=(34, 30, 34, 30), css_class="tn-card"))

    return section([
        script("One good night", MAGENTA),
        heading("Here's what you're walking into", fs=44, fs_mobile=30),
        para("Grab seven friends, name your team something ridiculous, and "
             "play for Idaho kids. Dinner, drinks, trivia, comedy and a "
             "bidding war — all under one roof on 3rd Avenue."),
        spacer(24),
        row(tiles, gap_px=24, align="stretch"),
    ], bg=WHITE)


def s_host():
    left = col([image(width_px=260)], pct=24, tablet=100, mobile=100,
               align="center", css_class="tn-ring")
    right = col([
        eyebrow("Your host for the evening", GOLD, align="left"),
        heading("Michael Beers", fs=46, color=WHITE, align="left", lh=1.1,
                fs_mobile=32, extra={"_css_classes": "tn-neon",
                                     "css_classes": "tn-neon"}),
        script("Comedian &amp; host", PINK, fs=30, align="left"),
        para("[HOST BIO — 60 to 80 words from the client. Where he's from, "
             "where he's performed, and why he said yes to hosting for Idaho "
             "Playground Project.]", color=ON_DARK, align="left"),
        para("Expect fast rounds, sharp commentary and absolutely no mercy for "
             "the table that googles an answer.", color=ON_DARK_3, fs=16,
             align="left"),
    ], pct=68, tablet=100, mobile=100)

    return section([row([left, right], gap_px=48, align="center")],
                   bg=BLACK, pad=(88, 24, 88, 24), width=1060)


def s_mission():
    left = col([
        eyebrow("Why we're doing this", TEAL, align="left"),
        heading("Every kid deserves a playground they can actually use",
                fs=44, align="left", fs_mobile=30),
        para("Idaho Playground Project builds inclusive, accessible "
             "playgrounds so that children with mobility and sensory needs "
             "aren't stuck watching from the sidelines. One night of trivia "
             "pays for real equipment on real schoolyards.", align="left"),
        para("[CLIENT: 2–3 sentences on where this year's proceeds go — which "
             "school or park, and what gets built.]", align="left"),
        button("More about our mission", SITE, bg=TEAL, fg=WHITE, align="left",
               pad=(16, 34, 16, 34)),
    ], pct=56, tablet=100, mobile=100)

    def stat(number, suffix, prefix, body, color):
        s = {
            "starting_number": 0,
            "ending_number": number,
            "prefix": prefix,
            "suffix": suffix,
            "duration": 1800,
            "thousand_separator": "yes",
            "title": "",
            "number_color": color,
        }
        s.update(typo(prefix="typography", family=HEAD_FONT, fs=48, weight=800,
                      lh=1.0))
        return col([widget("counter", s),
                    para(body, fs=16, align="left")],
                   pct=100, tablet=100, mobile=100, bg=WHITE, radius=18,
                   pad=(28, 30, 28, 30))

    right = col([
        stat(100, "", "", "inclusive playgrounds across Idaho by 2033 — the "
                          "goal we're building toward.", MAGENTA),
        stat(70, "%", "", "of Idaho elementary playgrounds don't meet ADA "
                          "accessibility guidelines.", TEAL),
        stat(250, "K+", "$", "is what one accessible playground costs to "
                             "build. That's why nights like this matter.", INDIGO),
        para("[CONFIRM all three figures with Idaho Playground Project before "
             "publishing.]", color=MUTED, fs=13, align="left"),
    ], pct=38, tablet=100, mobile=100, extra={"flex_gap": gap(16)})

    return section([row([left, right], gap_px=56, align="flex-start")],
                   bg=LILAC)


def s_tickets():
    card_a = col([
        eyebrow("Individual seat", GOLD, align="left"),
        heading("$125", tag="p", fs=60, weight=800, color=WHITE, align="left",
                lh=1.0),
        icon_list([
            "Dinner included",
            "1 drink ticket",
            "1 raffle ticket",
            "A spot at a trivia table, comedy and both auctions",
        ], icon_color=GOLD, text_color="#E6E0F2"),
        button("Buy a ticket", ZEFFY, bg=GOLD, fg=BLACK, nofollow=True,
               pad=(18, 28, 18, 28)),
        para("Processed securely through Zeffy.", color=ON_DARK_3, fs=13),
    ], pct=48.5, tablet=100, mobile=100, bg="#2A1748", radius=22,
        pad=(40, 36, 40, 36),
        border={"color": "rgba(255,198,63,0.35)", "width": 1})

    card_b = col([
        eyebrow("Bring your whole team", PINK, align="left"),
        heading("$1,000", tag="p", fs=60, weight=800, color=WHITE,
                align="left", lh=1.0),
        para("Table Sponsor — a reserved table for 8 guests.",
             color=ON_DARK_2, fs=16, align="left"),
        icon_list([
            "Reserved table for 8 guests",
            "Your logo on the table and in the program",
            "Full trivia and entertainment experience",
        ], icon_color=PINK, text_color="#E6E0F2"),
        button("See sponsorship levels", "#sponsorships", bg=None, fg=WHITE,
               border_color=PINK, external=False, pad=(18, 28, 18, 28)),
        para("Each sponsor seat includes dinner, a drink ticket and a raffle "
             "ticket.", color=ON_DARK_3, fs=13),
    ], pct=48.5, tablet=100, mobile=100, bg="rgba(255,255,255,0.04)",
        radius=22, pad=(40, 36, 40, 36),
        border={"color": "rgba(255,255,255,0.14)", "width": 1})

    return section([
        anchor("tickets"),
        script("Save your seat", GOLD),
        heading("Tickets", fs=44, color=WHITE, fs_mobile=30,
                extra={"_css_classes": "tn-neon", "css_classes": "tn-neon"}),
        spacer(20),
        row([card_a, card_b], gap_px=24, align="stretch"),
    ], bg=PLUM, width=1060)


TIERS = [
    {
        "label": "Title sponsor — only 1 available",
        "name": "The Big Kahuna",
        "price": "$10,000",
        "color": TEAL,
        "label_color": "#BDF3F4",
        "blurb": "Take center stage as our event's top supporter. Your brand "
                 "is front and center — on screens, in programs, and "
                 "highlighted throughout the night.",
        "items": [
            "2 VIP tables (16 seats) with premium placement",
            "Logo on all event materials — program cover, signage and screens",
            "Dedicated social media spotlight featuring your impact",
            "Recognition throughout the event by hosts and comedian",
            "Option to have your tables playfully teased by the comedian",
            "3 raffle tickets per VIP guest",
        ],
        "featured": True,
    },
    {
        "label": "Entertainment — up to 4 available",
        "name": "The Game Changer",
        "price": "$5,000",
        "color": MAGENTA,
        "label_color": "#FFD6E8",
        "blurb": "Cover our comedian, trivia rounds and the essentials — "
                 "food, beverages and venue rental — keeping the night fun "
                 "and seamless for every guest.",
        "items": [
            "1 VIP table (8 seats)",
            "Logo on event signage, program and trivia screens",
            "Social media recognition",
            "Shout-outs from the stage",
        ],
        "featured": False,
    },
    {
        "label": "Balloon sponsor — only 1 available",
        "name": "The Pop of Fun",
        "price": "$2,500",
        "color": INDIGO,
        "label_color": "#D7DBFA",
        "blurb": "Bring excitement to the night with our Balloon Pop. Sponsor "
                 "the balloons that hold prizes and joy — all in your brand "
                 "colours.",
        "items": [
            "1 regular table (8 seats)",
            "Recognition for helping bring play to Idaho kids",
            "Choice of balloon colours with your logo on them",
            "Social media thank-you and stage mention",
        ],
        "featured": False,
    },
    {
        "label": "Support from afar",
        "name": "The &ldquo;I Love Play But Hate Being Social&rdquo; Sponsor",
        "price": "$1,000 or $500",
        "color": ORANGE,
        "label_color": "#FFE4C2",
        "blurb": "Want to support our mission but won't be attending the "
                 "event? This tier is perfect — you can still make a big "
                 "impact from afar.",
        "items": [
            "Option to include 2 event tickets",
            "Social media shout-out",
            "Logo featured in the event program",
        ],
        "featured": False,
    },
    {
        "label": "Bring your people",
        "name": "Table Sponsor",
        "price": "$1,000",
        "color": SKY,
        "label_color": "#CCEBF8",
        "blurb": "Bring friends, family or colleagues for a night of fun and "
                 "philanthropy.",
        "items": [
            "Reserved table for 8 guests",
            "Logo on the table and in the program",
            "Full trivia and entertainment experience",
        ],
        "featured": False,
    },
]


def tier_card(t, pct, tablet):
    head = col([
        heading(t["label"], tag="p", fs=11, weight=700, color=t["label_color"],
                align="left", lh=1.5, ls=1.9, transform="uppercase"),
        heading(t["name"], tag="h3", fs=27, weight=800, color=WHITE,
                align="left", lh=1.2, fs_mobile=22),
        heading(t["price"], tag="p", fs=40, weight=800, color=WHITE,
                align="left", lh=1.0, fs_mobile=32),
    ], pct=100, bg=t["color"], pad=(26, 28, 26, 28),
        extra={"flex_gap": gap(10)})

    body = col([
        para(t["blurb"], fs=16, align="left"),
        icon_list(t["items"], icon_color=t["color"], fs=15, space=12),
        button("Claim this level", "#sponsor-form", bg=t["color"], fg=WHITE,
               external=False, pad=(16, 24, 16, 24)),
    ], pct=100, pad=(28, 28, 28, 28), extra={"flex_gap": gap(20)})

    border = {"color": t["color"] if t["featured"] else CARD_LINE, "width": 2}
    return col([head, body], pct=pct, tablet=tablet, mobile=100, radius=20,
               border=border, bg=WHITE,
               css_class="tn-card" if t["featured"] else None,
               extra={"flex_gap": gap(0), "overflow": "hidden"})


def s_sponsorships():
    row1 = row([tier_card(t, 31.8, 48.5) for t in TIERS[:3]], gap_px=24,
               align="stretch")
    row2 = row([tier_card(t, 48.5, 48.5) for t in TIERS[3:]], gap_px=24,
               align="stretch")

    inkind = col([
        row([
            col([
                heading("Not a sponsorship person? Donate an item.", tag="h3",
                        fs=28, weight=800, align="left", lh=1.2, fs_mobile=24),
                para("If a sponsorship isn't the right fit, we're grateful for "
                     "in-kind donations — live auction items, silent auction "
                     "packages or raffle prizes. Thank you for helping us "
                     "bring play to life.", color="#5C4B35", fs=17,
                     align="left"),
            ], pct=64, tablet=100, mobile=100),
            col([button("Donate an item", INKIND, bg=ORANGE, fg=WHITE,
                        pad=(18, 36, 18, 36))],
                pct=30, tablet=100, mobile=100, align="center",
                justify="center"),
        ], gap_px=32, align="center"),
    ], pct=100, bg="#FFF4E3", radius=20, pad=(40, 40, 40, 40),
        border={"color": ORANGE, "width": 2, "style": "dashed"},
        css_class="tn-dashed")

    return section([
        anchor("sponsorships"),
        script("Put your name on the night", MAGENTA),
        heading("Sponsorship levels", fs=44, fs_mobile=30),
        para("Sponsors cover the room, the food and the comedian — which means "
             "more of every ticket goes straight into playground equipment. "
             "Each starred level includes event tickets."),
        spacer(24),
        row1,
        row2,
        para("Every sponsor seat includes dinner, 1 drink ticket and 1 raffle "
             "ticket. Individual tickets are $125.", fs=14, align="left"),
        inkind,
    ], bg=WHITE)


def s_form():
    left = col([
        eyebrow("Talk to a human", MAGENTA, align="left"),
        heading("Secure your sponsorship", fs=40, align="left", fs_mobile=30),
        para("Fill in the form and we'll be in touch within two business days, "
             "or reach out directly — we're happy to talk through which level "
             "fits your business.", fs=17, align="left"),
        icon_list(["Kim Leonard — Idaho Playground Project"],
                  icon_color=TEAL, text_color=PLUM, fs=17,
                  ic="fas fa-user"),
        icon_list(["kim@idahoplaygroundproject.org"], icon_color=TEAL,
                  text_color=MAGENTA, fs=17, ic="fas fa-envelope"),
        icon_list(["208-490-1103"], icon_color=TEAL, text_color=MAGENTA,
                  fs=17, ic="fas fa-phone-alt"),
        icon_list(["Download the sponsorship packet (PDF)"], icon_color=MAGENTA,
                  text_color=MAGENTA, fs=15, ic="fas fa-file-pdf"),
    ], pct=40, tablet=100, mobile=100)

    right = col([
        html_widget(FORM_PLACEHOLDER),
    ], pct=56, tablet=100, mobile=100, bg=WHITE, radius=22,
        pad=(40, 38, 40, 38), css_class="tn-card")

    return section([anchor("sponsor-form"),
                    row([left, right], gap_px=48, align="flex-start")],
                   bg=LILAC, width=1100)


def s_venue():
    maps = {
        "address": "269 3rd Ave S, Twin Falls, ID 83301",
        "zoom": size(15),
        "height": size(360),
        "height_mobile": size(280),
        "_border_radius": allsides(20),
    }
    left = col([widget("google_maps", maps)], pct=62, tablet=100, mobile=100)

    right = col([
        col([icon_box("Parking",
                      "[CLIENT: street parking, nearest lot, and anything "
                      "guests should know about arriving downtown.]",
                      icon("fas fa-parking"), icon_color=TEAL, position="top",
                      title_size=19)],
            pct=100, bg=LILAC, radius=18, pad=(26, 28, 26, 28)),
        col([icon_box("Accessibility",
                      "[CLIENT: step-free entrance, accessible restrooms, "
                      "reserved seating — worth saying plainly for an "
                      "accessibility charity.]",
                      icon("fas fa-wheelchair"), icon_color=TEAL,
                      position="top", title_size=19)],
            pct=100, bg=LILAC, radius=18, pad=(26, 28, 26, 28)),
        button("Get directions", DIRECTIONS, bg=TEAL, fg=WHITE,
               pad=(17, 28, 17, 28)),
    ], pct=34, tablet=100, mobile=100, extra={"flex_gap": gap(16)})

    return section([
        script("Find us", TEAL),
        heading("Gaslamp on 3rd", fs=44, fs_mobile=30),
        para("269 3rd Ave S, Twin Falls, ID 83301"),
        spacer(20),
        row([left, right], gap_px=24, align="stretch"),
    ], bg=WHITE)


def s_faq():
    faqs = [
        ("Do I need a full team of eight?",
         "No. Buy single seats and we'll put you at a table with other guests, "
         "or grab a Table Sponsorship and bring all eight yourself."),
        ("What's included in the $125 ticket?",
         "Dinner, one drink ticket and one raffle ticket — plus the trivia, "
         "the comedy and both auctions."),
        ("What should I wear?",
         "[CLIENT: confirm dress code — e.g. cocktail, smart casual, or team "
         "costumes encouraged.]"),
        ("Is this a 21+ event?",
         "[CLIENT: confirm age policy for Gaslamp on 3rd and for the comedy "
         "content.]"),
        ("How do I pay for auction wins and raffle tickets?",
         "[CLIENT: confirm payment methods accepted on the night — card, cash, "
         "cheque — and how bidding is run.]"),
        ("Is my ticket or sponsorship tax-deductible?",
         "[CLIENT: confirm wording with your accountant, including the "
         "fair-market value of dinner, before this goes live.]"),
    ]
    tabs = [{"tab_title": q, "tab_content": f"<p>{a}</p>", "_id": uid()}
            for q, a in faqs]
    s = {
        "tabs": tabs,
        "selected_icon": icon("fas fa-chevron-down"),
        "selected_active_icon": icon("fas fa-chevron-up"),
        "title_color": PLUM,
        "tab_active_color": MAGENTA,
        "icon_color": MAGENTA,
        "icon_active_color": MAGENTA,
        "content_color": BODY,
        "border_width": size(0),
        "toggle_background": WHITE,
    }
    s.update(typo(prefix="title_typography", family=HEAD_FONT, fs=18,
                  weight=700, lh=1.4))
    s.update(typo(prefix="content_typography", family=BODY_FONT, fs=17,
                  weight=400, lh=1.7))

    return section([
        heading("Questions, answered", fs=44, fs_mobile=30),
        spacer(16),
        widget("accordion", s),
    ], bg=LILAC, width=860)


def s_sponsor_wall():
    tiles = [col([para("[Sponsor logo]", color=MUTED, fs=13)],
                 pct=23.5, tablet=48, mobile=48, bg=LILAC, radius=14,
                 pad=(40, 10, 40, 10), align="center", justify="center",
                 border={"color": "#C9C1DC", "width": 1, "style": "dashed"})
             for _ in range(8)]
    return section([
        heading("Thank you to our 2027 sponsors", fs=32, fs_mobile=26),
        para("This wall fills up as sponsors come on board.", fs=17),
        spacer(16),
        row(tiles, gap_px=18, align="stretch"),
    ], bg=WHITE, pad=(80, 24, 80, 24))


def s_final():
    left = col([
        script("See you Friday", PINK, fs=38, align="left"),
        heading("January 22, 2027 — Gaslamp on 3rd", fs=46, color=WHITE,
                align="left", lh=1.12, fs_mobile=30,
                extra={"_css_classes": "tn-neon", "css_classes": "tn-neon"}),
        para("Seats are limited to the room, and tables go first. Grab yours, "
             "or sponsor the night and put your name on a playground.",
             color=ON_DARK, align="left"),
        row([
            col([button("Buy tickets", ZEFFY, bg=GOLD, fg=BLACK,
                        nofollow=True)], pct=46, tablet=48, mobile=100,
                align="flex-start"),
            col([button("Sponsor the night", "#sponsorships", bg=None,
                        fg=WHITE, border_color=WHITE, external=False)],
                pct=46, tablet=48, mobile=100, align="flex-start"),
        ], gap_px=16, justify="flex-start", align="center"),
    ], pct=62, tablet=100, mobile=100)

    right = col([
        image(width_px=250),
        para("Share the flyer with your team", color=ON_DARK_3, fs=13),
    ], pct=28, tablet=100, mobile=100, align="center")

    return section([row([left, right], gap_px=48, align="center")],
                   bg=BLACK, bg_image=True, overlay=0.88, width=1040)


def s_sticky():
    return section([html_widget(STICKY_HTML)], pad=(0, 0, 0, 0), gap_px=0)


# --------------------------------------------------------------------------
# raw HTML widget payloads
# --------------------------------------------------------------------------

COUNTDOWN_HTML = """<!-- Countdown — free replacement for Elementor Pro's Countdown widget.
     Styling lives in additional-css.css (.tn-countdown).
     Change data-target if the date or time moves. -->
<ul class="tn-countdown" data-target="2027-01-22T18:00:00-07:00">
  <li><span class="tn-num" data-unit="days">&mdash;</span><span class="tn-lab">Days</span></li>
  <li><span class="tn-num" data-unit="hours">&mdash;</span><span class="tn-lab">Hours</span></li>
  <li><span class="tn-num" data-unit="minutes">&mdash;</span><span class="tn-lab">Minutes</span></li>
  <li><span class="tn-num" data-unit="seconds">&mdash;</span><span class="tn-lab">Seconds</span></li>
</ul>
<p class="tn-countdown-done" style="display:none;font-size:17px;color:#FFC63F;text-align:center;margin-top:12px">
  It's tonight. See you at Gaslamp on 3rd.
</p>
<script>
(function () {
  var wrap = document.currentScript.parentNode;
  var root = wrap.querySelector('.tn-countdown');
  if (!root) return;
  var done = wrap.querySelector('.tn-countdown-done');
  var target = new Date(root.getAttribute('data-target')).getTime();
  var cells = {
    days: root.querySelector('[data-unit="days"]'),
    hours: root.querySelector('[data-unit="hours"]'),
    minutes: root.querySelector('[data-unit="minutes"]'),
    seconds: root.querySelector('[data-unit="seconds"]')
  };
  function pad(n) { return n < 10 ? '0' + n : String(n); }
  function tick() {
    var diff = target - Date.now();
    if (diff <= 0) {
      root.style.display = 'none';
      if (done) done.style.display = 'block';
      clearInterval(timer);
      return;
    }
    var s = Math.floor(diff / 1000);
    cells.days.textContent = String(Math.floor(s / 86400));
    cells.hours.textContent = pad(Math.floor((s % 86400) / 3600));
    cells.minutes.textContent = pad(Math.floor((s % 3600) / 60));
    cells.seconds.textContent = pad(s % 60);
  }
  tick();
  var timer = setInterval(tick, 1000);
})();
</script>"""

STICKY_HTML = """<!-- Sticky mobile CTA — free replacement for Elementor Pro's Sticky effect.
     Only visible below 767px. Styling is in additional-css.css. -->
<div class="tn-sticky-cta">
  <a class="tn-buy" href="%s" target="_blank" rel="noopener nofollow">Buy tickets</a>
  <a class="tn-sponsor" href="#sponsorships">Sponsor</a>
</div>""" % ZEFFY

FORM_PLACEHOLDER = """<!-- ======================================================================
     SPONSORSHIP FORM GOES HERE

     Elementor's Form widget is Pro. Install a free form plugin
     (Fluent Forms Lite, WPForms Lite or Contact Form 7), build the form with
     the fields below, then REPLACE this HTML widget with a Shortcode widget
     holding your form's shortcode.

     Fields:
       Your name                (text,     required)
       Business / organisation  (text)
       Email                    (email,    required)
       Phone                    (tel)
       Sponsorship level        (dropdown, required) — options:
           The Big Kahuna — $10,000
           The Game Changer — $5,000
           The Pop of Fun — $2,500
           I Love Play But Hate Being Social — $1,000 or $500
           Table Sponsor — $1,000
           In-kind donation
           Not sure yet — please advise
       Anything we should know? (textarea)

     Submit label : Send my sponsorship request
     Notify       : kim@idahoplaygroundproject.org
     Also         : turn on the plugin's honeypot / anti-spam
     ====================================================================== -->
<div style="border:2px dashed #D8D2E6;border-radius:14px;padding:40px 28px;text-align:center;font-family:'Nunito Sans',sans-serif">
  <p style="font-family:'Poppins',sans-serif;font-size:18px;font-weight:700;color:#1E1033;margin:0 0 10px">
    Sponsorship form
  </p>
  <p style="font-size:15px;color:#6B6382;line-height:1.65;margin:0">
    Replace this HTML widget with a <strong>Shortcode</strong> widget containing your
    form plugin's shortcode. Field list is in this widget's HTML comment and in
    <code>copy-deck.md</code>.
  </p>
</div>"""


# --------------------------------------------------------------------------
# assemble
# --------------------------------------------------------------------------

def build():
    content = [
        s_hero(),
        s_factbar(),
        s_included(),
        s_host(),
        s_mission(),
        s_tickets(),
        s_sponsorships(),
        s_form(),
        s_venue(),
        s_faq(),
        s_sponsor_wall(),
        s_final(),
        s_sticky(),
    ]
    return {
        "version": "0.4",
        "title": "Trivia Night & Auction 2027 — Idaho Playground Project",
        "type": "page",
        "page_settings": {
            "template": "elementor_header_footer",
            "hide_title": "yes",
        },
        "content": content,
    }


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "trivia-night-2027-elementor.json")
    doc = build()
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1)
    print(f"wrote {out}")
    print(f"  top-level sections: {len(doc['content'])}")
