# 8. Age check (18+)

*Decided by Hendrik, 11 Oct 2026. Background: safety-and-moderation.md §2 and
legal-gdpr-berlin.md §7 in the project research.*

## Decided

- **Fake-data test phase:** a self-declared date of birth at sign-up. Under 18 cannot sign up.
- **Before real users join:** date of birth plus a selfie age estimate that runs only on the
  phone; the selfie is discarded right after. Anyone estimated close to 18 (for example under
  25) needs a stronger check. The EU age-verification app becomes the preferred method once it
  is available in Germany.
- **What is stored:** only the result, "over 18: yes, method, date", in the safety service.
  Never the selfie, a face template or an ID document.
- **Built behind one interface** from the start, so the method can change (self-declared,
  selfie estimate, EU app, German eID) without touching the rest of the app.

## Still open

- Which stronger check to use near the line before the EU app exists (lawyer: what level of age
  assurance the JMStV expects for a dating app without explicit content).
- Which on-device age-estimation model to use.
