# Error Handling.md

## Frontend behavior
- Email field rejects malformed addresses and exposes status via an ARIA live region.
- JavaScript uses optional chaining for non-critical DOM hooks where appropriate.
- The page remains readable if JavaScript fails; only menu toggling, reveal effects and demo form behavior are affected.
- Images include descriptive alt text and explicit dimensions to reduce layout shift.

## Production form handling
When the demo form is connected to a real endpoint:
1. Disable the submit button while the request is pending.
2. Use a request timeout and handle network errors.
3. Show neutral messages for 4xx/5xx failures without exposing stack traces.
4. Log server-side failures with a correlation/request ID.
5. Return structured JSON such as `{ "ok": false, "code": "VALIDATION_ERROR" }`.
6. Do not expose SMTP, database or infrastructure details to visitors.
7. Handle duplicate subscription requests idempotently.

## Image failure strategy
For guaranteed availability, run `download-images.py` in a network-enabled environment and deploy the downloaded files locally. This removes runtime dependence on Unsplash image delivery.
