# GNE'S APEX 2026 — School Invitation Email Campaign

This repository contains the production-ready responsive HTML invitation email for **GNE'S APEX 2026**, an inter-school multi-event initiative organized by the **Causmic Club** under the aegis of the **Department of Applied Sciences**, Guru Nanak Dev Engineering College (GNDEC), Ludhiana.

---

## 📁 Project Structure

```text
apex-mailing/
│
├── index.html                   # Master production HTML email template (using jsDelivr CDN)
├── index-hosted.html            # Hosted CDN version of the template
├── index-local.html             # Local asset version of the template
├── index-embedded.html          # Standalone Base64 embedded template (~400KB)
├── Apex-2026-brochure.pdf       # Official event brochure PDF
├── README.md                    # Project documentation
├── architecture.md              # Email architecture and flow strategy
├── design.md                    # Design system and typography guidelines
├── sources.md                   # Source of truth data and registry
│
├── assets/
│   ├── logos/                   # Institutional brand logos
│   │   ├── causmic-club-logo.png
│   │   └── gndec-logo.png
│   │
│   ├── photography/             # 4 Glimpses images (2x2 Grid)
│   │   ├── tech-robotics.jpg    # Innovation & Robotics
│   │   ├── creative-art.jpg     # Art & Creative Design
│   │   ├── performance-stage.jpg# Stage & Cultural Performance
│   │   └── campus-gndec.jpg     # GNDEC Campus & Spirit
│   │
│   ├── icons/                   # Custom ivory/gold academic icons
│   │   ├── icon-academic.png
│   │   ├── icon-art.png
│   │   ├── icon-calendar.png
│   │   ├── icon-connect.png
│   │   ├── icon-create.png
│   │   ├── icon-email.png
│   │   ├── icon-innovate.png
│   │   ├── icon-learn.png
│   │   ├── icon-location.png
│   │   ├── icon-performance.png
│   │   ├── icon-phone.png
│   │   ├── icon-tech.png
│   │   └── icon-trophy.png
│   │
│   └── decorative/              # Gold dividers & ornamental assets
│       ├── gold-divider.png
│       └── gold-star.png
│
└── scripts/                     # Utility scripts
    ├── inline_images.py         # Inlines all assets to Base64 (index-embedded.html)
    ├── optimize_assets.py       # Compresses assets to email-friendly dimensions
    ├── send_mail.py             # Automated Python SMTP email dispatcher
    └── update_image_urls.py     # Updates HTML image paths with GitHub/CDN URLs
```

---

## 🎯 Key Sections in Template

1. **Brand Bar:** Dual institutional lockup for Causmic Club & GNDEC Ludhiana with white circular seal background.
2. **Hero Header:** Clean typographic title block: `YOU ARE CORDIALLY INVITED TO GNE'S APEX 2026`, theme (*“ONE LEGACY. MANY STORIES. LIMITLESS FUTURE.”*), and confirmed date badge (`Friday, 30th October 2026`).
3. **Formal Invitation Letter Section:**
   - Formal salutation to **Respected Principal / Teacher In-charge**.
   - Academic introduction highlighting alignment with **NEP 2020** vision.
   - **Special Feature:** Diwali-themed **APEX FAIR** (cultural performances, traditional crafts, delicacies, games).
4. **Key Event Information at a Glance:**
   - 4-card high-contrast summary (Event Date & Time: 8:30 AM, Eligibility: Classes 9–12, Registration: Free, Deadline: 12 Noon, 26th Oct 2026).
5. **14 Events Structured Matrix (Tabular Format):**
   - **Individual Events (7):** Pencil Shaders, Rangoli Marvels, Prompt Engineering, Digital Identity, Reel Artistry, Sufi Singing, The Logic Challenge.
   - **Group Events (6):** Web Wizards (2), SQL Masters (2), Media Spotlight (2), Working Model Quest (3), Mime (6), Line Following Robo (4).
   - **For Teachers (1):** My Best Classroom Management Trick (2).
6. **Official Participation Guidelines:** School authority letter, student ID cards, school codes, free refreshments, and direct Google Drive brochure link.
7. **Glimpses of APEX (2×2 Grid):** 4 curated authentic photographs representing Robotics/Tech, Creative Art, Cultural Performance, and Campus Life.
8. **Exciting Prize Pool Section:**
   - **Overall Best School:** ₹11,000 + Champion Trophy + Gold Medals
   - **1st Runner-Up School:** ₹7,000 + Runner-Up Trophy + Medals
   - **2nd Runner-Up School:** ₹5,000 + Trophy + Medals
   - **E-Certificates** for all participants & winners (*Minimum 10 of 14 events to qualify for overall school trophy*).
9. **Primary Action (CTA):** `REGISTER YOUR SCHOOL →` linking to `https://causmic.gndec.ac.in/apex`.
10. **Official Brochure Direct Access Card:** Direct Google Drive access button to view/download the full PDF.
11. **Formal Sign-Off & Closing:** Warm regards from Team Causmic Club, Dept of Applied Sciences, GNDEC.
12. **Helpdesk & Institutional Footer:** Ishmeet Singh (+91 77194 50870), Harleen Kaur (+91 94631 06543), `gnesapex@gmail.com`, college address, and official links.

---

## ⚙️ Campaign Configuration Variables
- **Event Date:** Friday, 30th October 2026 (Reporting: 8:30 AM)
- **Registration Deadline:** 12 Noon, Monday, 26th October 2026
- **Registration URL:** https://causmic.gndec.ac.in/apex (Free Registration)
- **Official Brochure Link:** [Google Drive PDF](https://drive.google.com/file/d/1T2Y1zPWM5Hg8QFUzdpHfGRu_6GOX27eP/view?usp=sharing)
- **General Email:** gnesapex@gmail.com
- **Helpdesk Contacts:** Ishmeet Singh (+91 77194 50870), Harleen Kaur (+91 94631 06543)
- **Eligibility:** Classes 9th – 12th (+ Dedicated Teachers event)
- **Prize Pool:** Overall Best School: ₹11,000 | 1st Runner-Up: ₹7,000 | 2nd Runner-Up: ₹5,000
