# Rajbiraj Expo — Architecture

## Project type
Static, responsive landing page designed for simple deployment on shared hosting, Hostinger, Netlify, Vercel, GitHub Pages, or any standard web server.

## Structure
- `index.html` — semantic page structure and content.
- `assets/css/style.css` — responsive morphism UI, layout, components, animation and accessibility states.
- `assets/js/main.js` — mobile navigation, email-form demo validation, dynamic copyright year, reveal animation.
- `assets/images/favicon.svg` — local favicon.
- `assets/images/` — intended local image destination when image downloader is run.
- `download-images.py` — downloads the three selected Unsplash images and rewrites image references to local files.
- Documentation files — implementation, security, errors, licensing and phases.

## UI architecture
1. Sticky glassmorphism navigation.
2. Hero with launch status, official introductory copy and exhibition visual.
3. Vision section with Business & Trade, Ideas & Innovation, Culture & Experience.
4. Participation/pillars section.
5. Experience section with Nepal-focused public gathering visual.
6. Email notification CTA.
7. Responsive footer with developer credit.

## Responsive strategy
- Desktop: two-column hero, split content sections, horizontal footer bottom.
- Tablet: adaptive one/two-column grids and collapsible navigation.
- Mobile: single-column layout, full-width CTA buttons, stacked footer. Developer credit appears below copyright as requested.

## Data policy
Only public statements visible on `https://rajbirajexpo.com/` as reviewed on 2026-09-26 are treated as official event facts. No event dates, ticket prices, sponsors, organizer names or venue details are invented.
