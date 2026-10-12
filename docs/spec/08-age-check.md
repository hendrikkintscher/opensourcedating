# 8. Age check (18+)

*Decided by Hendrik, 11 Oct 2026. Stronger check reviewed 12 Oct 2026 (design review decision
D10: deferred).*

## Decided

- **Fake-data phases (2 to 4):** a self-declared date of birth at sign-up. Under 18 cannot sign up.
- **Before real users join (gate to phase 5):** date of birth plus a selfie age estimate that runs only on the
  phone; the selfie is discarded right after. Anyone estimated close to 18 (for example under
  25) needs a stronger check. The EU age-verification app becomes the preferred method once it
  is available in Germany.
- **What is stored:** only the result, "over 18: yes, method, date", in the safety service.
  Never the selfie, a face template or an ID document.
- **Built behind one interface** from the start, so the method can change (self-declared,
  selfie estimate, EU app, German eID) without touching the rest of the app.

## Deferred: the stronger check, decided before real users (gate to phase 5, D10)

Hendrik deferred this decision on 12 Oct. The fake-data phases keep the self-declared date of
birth. The stronger check is chosen before real users join, and sign-up does not open to the
public before it exists.

Why it matters: the Commission's DSA Art. 28 guidelines (published 10 Oct 2025) reject
self-declaration and expect verification, not estimation, for high-risk services. A micro
enterprise is exempt from Art. 28, but regulators, the KJM and app stores will still compare
against it once real users arrive.

| Option | Pros | Cons |
|---|---|---|
| A. German eID age-only query for anyone the estimate puts under 25 | Strong and privacy-friendly: only "over 18" comes back | Needs a Berechtigungszertifikat and integration work; many people never activated their eID |
| B. ID-document scan through an EU vendor | Strong and familiar | Creates an ID dataset at the vendor; cost per check |
| C. Human video check | No vendor | Staff time; close to biometric processing; uncomfortable for users |

**Recommendation (not decided):** A, the German eID age-only query, with B, an ID scan through an
EU vendor, as the fallback for people without a working eID. The EU age app becomes the default
once Germany offers it.

## Still open

- The stronger check itself (above), decided before real users.
- What level of age assurance the JMStV expects for a dating app without explicit content
  (lawyer).
- Whether on-device facial age estimation counts as biometric categorisation under the AI Act
  (Annex III 1(b)) or is excluded as ancillary (lawyer).
- Which on-device age-estimation model to use.

## Background

Project research: safety and moderation (age verification section), legal
(legal-and-org/legal.md, age and youth protection).
