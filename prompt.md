# Master Development Prompt — Rajbiraj Expo

Build a production-quality, fully responsive, premium modern **morphism-style landing page for RAJBIRAJ EXPO** using semantic HTML5, modern CSS and lightweight vanilla JavaScript. The visual style must combine refined **glassmorphism** with subtle **neumorphic depth**, dark navy/charcoal surfaces, translucent cards, soft internal highlights, blurred ambient gradients, crisp typography and restrained micro-interactions. It must look polished on the latest mobile phones, tablets, laptops, desktops and wide screens without horizontal overflow.

## Authoritative source
Use `https://rajbirajexpo.com/` as the factual source. At the time of implementation it presents Rajbiraj Expo as **Launching Soon**, identifies the location context as **Rajbiraj • Saptari • Nepal**, and states that the expo is being prepared to bring **business, innovation, entrepreneurship, local products, culture, entertainment and new opportunities** together. Its highlighted pillars are **Business & Trade**, **Ideas & Innovation**, and **Culture & Experience**. It also states that official event details, dates and announcements will be published soon.

Do not invent event dates, venue names, sponsor names, ticket prices, organizer names, statistics or schedules. Clearly label anything that is a placeholder or demo.

## Required page structure
Create a sticky translucent navigation bar with a compact RX logo/mark, `RAJBIRAJ EXPO`, the tagline `Connect • Create • Celebrate`, anchor navigation and a mobile hamburger menu. Build a high-impact hero with the label `Launching Soon • Rajbiraj • Saptari • Nepal`, the headline `Something extraordinary is coming.`, official introductory copy, a `Notify Me` CTA and `Explore the vision` CTA. Include a large relevant exhibition image in a glass card with small floating morphism info cards for `Rajbiraj, Saptari, Nepal` and `One platform, Many possibilities`.

Add a Vision/Highlights section containing exactly the three factual themes from the source: `Business & Trade`, `Ideas & Innovation`, and `Culture & Experience`. Follow with a strong split-layout section that explains the platform's focus on entrepreneurship, local products, innovation, trade, culture and entertainment. Add another visual experience section that feels locally relevant to Nepal without falsely claiming the image depicts Rajbiraj Expo itself.

Add a `Be first to know` update-subscription section with an email field. Client-side behavior may be a clearly labeled demo unless a real backend is provided. Use a neutral success message saying the email was captured only in the demo interface and production integration is still required.

## Images
Use only a small number of relevant Unsplash images: trade show/exhibition, business networking and a Nepal public/cultural gathering. Avoid random decorative stock images. Prefer locally downloaded optimized copies for production, keep source attribution in project documentation, use meaningful alt text, explicit width/height and lazy loading below the fold.

## Footer
The footer must include `© Rajbiraj Expo. All rights reserved.` and the exact credit text `Designed and Developed By Pream Shah`. Make only `Pream Shah` a clickable link to `https://preamshah.com/`, opening safely in a new tab. On desktop, keep copyright on the left and the developer credit on the right. On mobile, place the developer credit below the copyright section on its own row.

## UX, responsiveness and accessibility
Use fluid type with `clamp()`, CSS Grid/Flexbox, touch-friendly targets, keyboard-accessible navigation, focus states, meaningful labels, semantic section headings, appropriate ARIA only when needed, a reduced-motion fallback and sufficient contrast. The page must render correctly from 320px mobile width through 4K displays. Avoid bloated libraries and unnecessary animations.

## SEO & performance
Create a concise page title and meta description, theme color, favicon, descriptive alt text, good heading hierarchy and clean semantic HTML. Keep JavaScript minimal and defer it. Prevent cumulative layout shift by setting image dimensions. Use lazy loading for below-the-fold imagery. Optimize images and avoid unnecessary network requests.

## Security
No secrets in frontend code. If the notification form is connected to a backend, implement server-side validation, rate limiting, safe data handling and anti-abuse controls. Recommend HTTPS, CSP, nosniff, referrer and permissions-policy headers.

## Required files
Deliver at minimum:
- `index.html`
- `assets/css/style.css`
- `assets/js/main.js`
- `assets/images/favicon.svg`
- relevant images or a reliable image-localization mechanism
- `architecture.md`
- `prompt.md`
- `Security.md`
- `Error handling.md`
- `readme.md`
- `Licence.md`
- `Phases.md`
- `image-sources.md`

Package the complete project into a ZIP while preserving the directory structure.
