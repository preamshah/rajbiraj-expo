# Rajbiraj Expo — Modern Morphism Landing Page

A responsive, modern glassmorphism/neumorphism-inspired landing page for Rajbiraj Expo.

## Verified source content
The public Rajbiraj Expo site currently states:
- Launching Soon.
- Location context: Rajbiraj • Saptari • Nepal.
- The event is being prepared to bring business, innovation, entrepreneurship, local products, culture, entertainment and new opportunities together.
- Highlighted themes: Business & Trade, Ideas & Innovation, Culture & Experience.
- Official dates and announcements will be published soon.

This package deliberately does **not** invent an expo date, sponsor, ticket price, venue name or organizer information.

## Quick start
Open `index.html` directly, or use a local static server:

```bash
python -m http.server 8080
```

Then visit `http://localhost:8080`.

## Localize Unsplash images
The HTML ships with verified Unsplash image URLs so it works immediately. To download them into `assets/images/` and rewrite the HTML to use local files:

```bash
python download-images.py
```

Run this in an environment with internet access. The script is idempotent and keeps source attribution in `image-sources.md`.

## Footer requirement
- Desktop: copyright on the left, developer credit on the right.
- Mobile: developer credit appears below the copyright section.
- Developer link: `https://preamshah.com/`.

## Deployment
Upload all files and folders while preserving structure. Use HTTPS. For Hostinger, upload the project contents to the target site's `public_html` directory.
