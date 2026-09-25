# APEX Marketing Email — Design System

## 1. Design Direction

The APEX email should translate the visual identity of the supplied **GNE'S APEX 2026** brochure into a modern HTML-email system.

The source PDF establishes a visual language built around:

- Deep navy backgrounds.
- Warm ivory/off-white content surfaces.
- Gold accents and ornamental detailing.
- Dark navy typography.
- Large, confident display headings.
- Serif/script-inspired decorative headings in selected sections.
- Rounded image frames.
- Gold-lined borders and separators.
- Formal institutional presentation combined with youthful event photography.

The email should retain this identity while reducing the visual complexity of the 20-page brochure.

---

# 2. Primary Color Palette

The following palette is a **design-system approximation derived from the visible PDF artwork**. Exact RGB/HEX values should be finalized from the original design assets if available.

| Role | Suggested HEX | Usage |
|---|---|---|
| Deep Navy | `#061A33` | Main dark background, footer, header |
| Navy Blue | `#0D2748` | Secondary dark surfaces and cards |
| Ivory | `#F7F4EC` | Main email background/content panels |
| Warm White | `#FCFBF7` | Clean content areas |
| Antique Gold | `#C9A45A` | Borders, dividers, icons, accents |
| Light Gold | `#E1C77A` | Secondary decorative elements |
| Dark Gold | `#A9853E` | Strong accent text and highlights |
| Charcoal | `#20252B` | Main body text |
| Muted Navy | `#536277` | Secondary text |
| Pure White | `#FFFFFF` | Text on dark backgrounds |

---

# 3. Color Application Rules

## 3.1 Deep Navy

Use the deepest navy as the principal brand surface.

Recommended uses:

- Hero background.
- Footer.
- Feature-card background where appropriate.
- Institutional credibility section.
- Decorative side panels.

Do not use navy behind every section. The source PDF deliberately alternates dark and light areas.

---

## 3.2 Ivory

Ivory should be the principal reading surface.

Recommended uses:

- Main content sections.
- Event-domain cards.
- Introduction.
- CTA support area.
- Contact section.

This reproduces the source document's warm, premium paper-like appearance.

---

## 3.3 Gold

Gold is an **accent**, not the dominant fill color.

Use it for:

- Thin borders.
- Section separators.
- Small labels.
- Decorative lines.
- Icons.
- Important numbers.
- Underlines.
- Small CTA details.
- Ornamental elements.

Avoid using large blocks of saturated gold because it can reduce readability and make the email feel overly decorative.

---

# 4. Typography System

The typography system is built around a pure, highly structured institutional and academic aesthetic:

```text
Premium • Academic • Institutional • Elegant • Modern • Highly Readable
```

## 4.1 Font Stack Hierarchy

| Element Role | Primary Font | Weight | Fallback Stack | Usage |
|---|---|---|---|---|
| **Hero / APEX Title** | **Cormorant Garamond** | 700 / 800 Bold | `Georgia, 'Times New Roman', serif` | Main APEX mark, GNE'S prefix, 2026 year, Prize amounts |
| **Section Headings** | **Playfair Display** | 700 Bold / 600 SemiBold | `Georgia, 'Times New Roman', serif` | Major section titles, institutional college headings, closing quote |
| **Labels, Badges & CTA** | **Montserrat** | 600 SemiBold / 500 Medium | `Arial, Helvetica, sans-serif` | Eyebrow badges, event card labels, feature titles, button CTA, headers |
| **Body Text & Descriptions** | **Source Sans 3** | 400 Regular | `Arial, Helvetica, sans-serif` | Intro narrative, card descriptions, award subtext, contact details |

## 4.2 Letter Spacing Rules

- **Uppercase Eyebrows & Badges:** `letter-spacing: 2px` to `2.5px`
- **Hero Display Headings:** `letter-spacing: 6px` to `8px`
- **CTA Button:** `letter-spacing: 2px`
- **Body Text:** Standard natural letter spacing with `line-height: 1.5` to `1.6`

## 4.3 Fallback Rule
Do not use decorative, playful, handwritten, or script fonts. Email client fallbacks are strictly defined as web-safe serif (`Georgia, 'Times New Roman', serif`) and sans-serif (`Arial, Helvetica, sans-serif`).

---

# 5. Typography Scale

Recommended desktop email scale:

| Element | Size | Weight | Treatment |
|---|---:|---|---|
| Hero APEX | 58–72 px | 700–800 | Uppercase |
| Hero supporting line | 16–20 px | 600 | Uppercase / tracked |
| Major heading | 30–38 px | 700 | Serif |
| Secondary heading | 22–28 px | 700 | Serif/Sans |
| Eyebrow | 11–13 px | 700 | Uppercase |
| Body | 15–17 px | 400 | Sans-serif |
| Feature title | 16–19 px | 700 | Uppercase |
| Feature body | 13–15 px | 400 | Sans-serif |
| CTA | 14–16 px | 700 | Uppercase |
| Footer | 11–13 px | 400 | Sans-serif |

Mobile recommendation:

- Hero: 42–52 px.
- Major headings: 26–32 px.
- Body: 14–16 px.
- CTA: 15–16 px.

---

# 6. Typography Hierarchy

The email should communicate hierarchy immediately.

Recommended visual hierarchy:

```text
APEX
   ↓
2026
   ↓
ONE LEGACY. MANY STORIES. LIMITLESS FUTURE.
   ↓
SECTION HEADING
   ↓
BODY COPY
   ↓
CTA
```

The source cover uses **APEX** as the dominant visual word, with **GNE'S** and **2026** supporting it. The email should preserve this relationship.

---

# 7. Layout Grid

## Desktop

Recommended:

```text
Maximum width: 640 px
Outer padding: 20–24 px
Content padding: 32–40 px
Section spacing: 36–56 px
Card gap: 12–16 px
```

## Mobile

Recommended:

```text
Width: 100%
Outer padding: 16 px
Content padding: 20–24 px
Section spacing: 28–40 px
Card gap: 12 px
```

The email should remain visually balanced at approximately **320–430 px** viewport widths.

---

# 8. Hero Design

The hero should be the strongest section.

## Structure

```text
┌──────────────────────────────────────┐
│              LOGOS                   │
│                                      │
│              GNE'S                   │
│              APEX                    │
│              2026                    │
│                                      │
│ ONE LEGACY. MANY STORIES.            │
│ LIMITLESS FUTURE.                    │
│                                      │
│       [ EXPLORE APEX ]               │
└──────────────────────────────────────┘
```

## Styling

- Background: Deep Navy.
- Main title: Ivory/White.
- Gold: decorative separators and selected highlights.
- Hero image: rounded corners or an editorial collage.
- Use subtle gold framing around the image.
- Keep the hero visually uncluttered.

The PDF cover uses a combination of event photography, navy/ivory surfaces, gold accents and a large APEX title. fileciteturn0file0L5-L13

---

# 9. Decorative Language

The PDF repeatedly uses ornamental motifs, including:

- Floral/mandala-like line art.
- Curved gold borders.
- Thin ornamental separators.
- Gold corner details.
- Decorative horizontal rules.

These should become **lightweight email decorations**.

Recommended HTML-email equivalents:

```text
────── ✦ ──────
```

or

```text
────────────
```

with a small gold ornamental element in the center.

Do not reproduce complex full-page decorative illustrations as CSS. Use optimized images where necessary.

---

# 10. Section Heading Style

The source PDF frequently uses a strong heading + gold decorative line treatment.

Recommended HTML pattern:

```text
SECTION TITLE
──────── ✦ ────────
```

Example:

```text
WHY APEX?
──────── ✦ ────────
```

Alternative premium style:

```text
WHY
APEX
```

with `APEX` highlighted in gold.

---

# 11. Feature Cards

Use a refined card system rather than heavy boxes.

## Light card

```text
Background: #FCFBF7
Border: 1px solid #D9C58A
Radius: 14px
Padding: 20px
```

## Dark card

```text
Background: #0D2748
Border: 1px solid #C9A45A
Radius: 14px
Padding: 20px
```

Cards should have:

- Small icon.
- Short title.
- 1–2 sentence description.
- Consistent height.

Avoid excessive shadows because the source visual language is primarily based on **flat premium surfaces and linework**, rather than modern SaaS-style floating cards.

---

# 12. Event Domain Cards

Suggested visual grouping:

### Academic

Dark navy title + gold accent.

### Technical & Innovation

Ivory card + navy typography + gold border.

### Creative & Artistic

Ivory card + decorative gold element.

### Performance

Dark navy card + ivory typography.

The categories are an email presentation device. The source PDF formally separates the events into **individual events and group events**. fileciteturn0file0L224-L239

---

# 13. Image Treatment

The source PDF makes extensive use of photography, particularly:

- Participants working.
- Technical projects.
- Performances.
- Classroom/event environments.
- Campus visuals.
- Organizing team portraits.

The image treatment should therefore feel authentic rather than stock-heavy.

## Recommended style

```text
Border radius: 12–18px
Border: 1px solid Gold
Aspect ratio: 4:3 or 1:1
Object fit: cover
```

For hero photography:

```text
Aspect ratio: approximately 16:9
Radius: 18–22px
```

For supporting images:

```text
Aspect ratio: 4:3
Radius: 12–16px
```

---

# 14. Photography Direction

Prioritize images that communicate:

1. People participating.
2. Students creating or solving.
3. Technical projects.
4. Cultural/performance moments.
5. Campus environment.

Avoid using only posed portraits.

The PDF's **Glimpses** section demonstrates a collage-oriented approach with multiple real-event photographs. fileciteturn0file0L567-L572

---

# 15. CTA Design

The primary CTA should contrast strongly with its surrounding section.

Recommended:

```text
Background: #C9A45A
Text: #061A33
Radius: 8–10px
Padding: 14px 28px
Font: Arial / Helvetica
Weight: 700
```

Button:

```text
EXPLORE APEX →
```

or, when registration is confirmed:

```text
REGISTER NOW →
```

Use only one dominant CTA.

Secondary text links should use gold or navy without button styling.

---

# 16. CTA Section

Recommended composition:

```text
┌──────────────────────────────────────┐
│                                      │
│       READY TO EXPERIENCE APEX?      │
│                                      │
│   Discover the events, explore the   │
│   experience and be part of APEX.    │
│                                      │
│          [ EXPLORE APEX ]            │
│                                      │
└──────────────────────────────────────┘
```

Background:

- Deep Navy.

Text:

- Ivory.

Accent:

- Gold.

---

# 17. Institutional Section

The final brochure page establishes GNDEC using a formal navy-and-gold visual treatment and campus imagery. fileciteturn0file0L587-L594

Translate this into a compact email section:

```text
CAUSMIC CLUB
under the aegis of
DEPARTMENT OF APPLIED SCIENCES

GURU NANAK DEV ENGINEERING COLLEGE
Ludhiana, Punjab
```

Use:

- Navy background.
- Gold divider.
- White/ivory typography.
- Small institutional logo.

---

# 18. Footer Design

The footer should be visually quiet.

```text
Background: #061A33
Text: #FFFFFF
Secondary text: #C9A45A
```

Structure:

```text
CAUSMIC CLUB
Guru Nanak Dev Engineering College

Website · Instagram · LinkedIn

gnesapex@gmail.com
+91 XXXXX XXXXX

© 2026 Causmic Club. All rights reserved.
```

---

# 19. Borders and Radius

The PDF uses many rounded containers and framed visual elements.

Recommended email system:

| Component | Radius |
|---|---:|
| Hero image | 18–22 px |
| Feature card | 12–16 px |
| Event card | 12–16 px |
| CTA button | 8–10 px |
| Image tile | 12–16 px |
| Main container | 0–4 px |

Do not round every element. Use rounded corners primarily for photographs, cards and CTA components.

---

# 20. Shadows

Use shadows very sparingly.

Recommended:

```css
box-shadow: 0 4px 16px rgba(6, 26, 51, 0.08);
```

However, because many email clients have inconsistent CSS support, a clean border-based design is preferred.

The visual character should come primarily from:

- color contrast,
- borders,
- photography,
- typography,
- spacing,
- ornaments.

---

# 21. Background Treatment

Use alternating sections:

```text
NAVY
↓
IVORY
↓
WHITE/IVORY
↓
NAVY
↓
IVORY
↓
NAVY FOOTER
```

This prevents visual fatigue and mirrors the dark/light rhythm visible throughout the PDF.

---

# 22. Gold Usage Ratio

A useful approximate ratio:

```text
Navy / dark surfaces     30–35%
Ivory / white surfaces   50–55%
Gold accents              5–10%
Photography              integrated
```

Gold should remain visually special.

---

# 23. Icons

Use simple line icons where possible.

Recommended icon concepts:

- Lightbulb → learning/ideas.
- Spark/gear → innovation.
- Palette → creativity.
- Users → collaboration.
- Trophy → competition.
- Code brackets → technical events.

Icon style:

```text
Outline / line-based
Gold or navy
Small
Consistent stroke
```

Avoid mixing multiple icon styles.

---

# 24. Visual Rhythm

Each section should follow:

```text
EYEBROW
    ↓
HEADING
    ↓
GOLD DIVIDER
    ↓
SHORT COPY
    ↓
VISUAL / CARDS
    ↓
OPTIONAL ACTION
```

This creates consistent scanning behavior throughout the email.

---

# 25. Accessibility

The final HTML should include:

- Meaningful `alt` text.
- Sufficient text/background contrast.
- Real HTML text rather than text baked into images whenever possible.
- Large enough CTA text.
- Logical reading order.
- No essential information communicated only through color.
- Proper link labels.
- Mobile responsive behavior.

---

# 26. Email Client Compatibility

Prefer:

- Table-based structure.
- Inline CSS.
- Web-safe fonts.
- Explicit image dimensions.
- `display:block` on images.
- Simple responsive media queries.
- Background colors rather than CSS gradients where possible.

Avoid depending on:

- Complex CSS positioning.
- JavaScript.
- External font loading.
- CSS-only decorative effects.
- Advanced animations.

---

# 27. Overall Visual Formula

The final design should follow:

```text
                 APEX
        ┌───────────────────┐
        │   DEEP NAVY       │
        │   GOLD DETAILS    │
        └───────────────────┘

              ↓

        WARM IVORY CONTENT
        SERIF HEADINGS
        CLEAN BODY TEXT

              ↓

       REAL EVENT PHOTOGRAPHY

              ↓

        GOLD-LINED CARDS

              ↓

       DEEP NAVY CTA SECTION
           [ EXPLORE APEX ]

              ↓

       NAVY INSTITUTIONAL
             FOOTER
```

---

# 28. Brand Personality

The design should communicate these qualities:

- **Prestigious** — through institutional navy and gold.
- **Youthful** — through authentic student photography.
- **Creative** — through ornamental visual details.
- **Technical** — through structured layouts and event categories.
- **Trustworthy** — through GNDEC/Causmic Club branding.
- **Energetic** — through strong typography and photography.
- **Professional** — through restrained spacing and consistent hierarchy.

---

# 29. What to Avoid

Do not make the email:

- A 20-page brochure squeezed into HTML.
- Completely dark.
- Gold-heavy.
- Overloaded with decorative flourishes.
- Dependent on images for core information.
- Filled with long paragraphs.
- Filled with multiple competing CTAs.
- Visually similar to a generic corporate newsletter.
- Too minimalist to lose the APEX identity.
- Too ornate to become difficult to scan.

---

# 30. Final Design Target

The ideal result is:

> **A premium navy-and-gold institutional event invitation, softened by warm ivory surfaces and authentic student photography, with strong serif display typography, restrained ornamental details, and a clear modern CTA.**

The email should immediately feel connected to the APEX brochure while being **cleaner, shorter, more responsive, and more conversion-oriented** for digital communication.
