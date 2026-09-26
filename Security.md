# Security.md

## Current static-site risk profile
This project has no server-side code, database, authentication, payment flow, file upload, or privileged admin function. Its primary security surface is browser-delivered HTML/CSS/JS and third-party assets.

## Production requirements
- Enforce HTTPS and redirect HTTP to HTTPS.
- Add a strict Content Security Policy. If images remain remote, allow `images.unsplash.com`; if images are localized, use `img-src 'self' data:`.
- Prefer self-hosted fonts for the strictest CSP and privacy posture.
- Add `Referrer-Policy: strict-origin-when-cross-origin`, `X-Content-Type-Options: nosniff`, and appropriate `Permissions-Policy` headers.
- Keep external links using `rel="noopener noreferrer"` when opening a new tab.
- Never trust client-side email validation as a security control.
- When connecting the notification form to a backend, use server-side validation, rate limiting, CSRF protection where applicable, bot mitigation, safe parameterized database access, logging, and abuse monitoring.
- Do not put API keys, SMTP credentials or secrets in frontend JavaScript.
- Escape or sanitize all user-controlled output before rendering it into HTML.

## Dependency posture
The current build intentionally avoids JavaScript frameworks and package-manager dependencies to reduce the supply-chain attack surface.
