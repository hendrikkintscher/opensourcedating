# 1. Accounts and identity

*Decided by Hendrik, 11 Oct 2026. Account ID and recovery updated 12 Oct 2026 (design review
decisions D1 and D3); email provider rules added 12 Oct 2026 (D14).*

## Decisions

- **Sign-in:** Ory Kratos with passkeys first and email one-time codes as the fallback. No
  passwords, no phone number required. (Decided earlier, see data-security.md §12.2 in the
  project research.)
- **Account ID (decided 12 Oct):** a random, opaque 128-bit ID. It contains no server name (no
  `@server`) and is not derived from any key. Every table, chat key, block and report refers to
  this ID. The email address is only a login detail and is never used as a key or shown to
  anyone.
  - The ID is bound to the phone's current device key by a signed certificate. When the key
    changes (new phone, lost phone), a new certificate is issued and the ID stays the same.
  - This works with Kratos in stage 1 and with the stage 2 design (see
    [12](12-stage-2-network.md)) without a migration. Replaces the earlier `id@server` form.
- **Device key beside Kratos:** at sign-up the phone creates a signing key in its secure
  hardware and registers it next to the Kratos identity. In stage 1 it only signs requests; it is
  there so stage 2 needs no re-enrolment. It adds to Kratos, it does not replace it.
- **One phone per account during the pilot.** Signal-protocol multi-device support is extra work
  and can be added later without changing the account ID.
- **No chat backup in the pilot.** Chats exist only on the phone.
- **Lost or new phone:** the account comes back by signing in with an email code, after the
  recovery waiting period below. Old chats are gone. The app creates new chat keys, and the
  people the user was writing with see a notice that the security code changed. An encrypted
  chat backup is possible later.
- **Recovery waiting period (decided 12 Oct):** an account recovered on a new phone gets access
  only after 24 hours. During that time the old phone gets a notice with a way to cancel the
  recovery ("this wasn't me"). This stops someone who can read the email inbox (for example an
  ex-partner) from silently taking over the account and its chats.

## Email for login codes and notices (decided 12 Oct, D14)

An email alone can reveal that someone uses a dating app, so:

- **An EU-based transactional email provider with a data processing agreement (GDPR Art. 28).**
  Not a US provider.
- **Minimal content:** "your code is ...", and no app name in the subject line if possible. No
  profile data, names or message text in any email.
- Kratos sends email over plain SMTP, so the provider can be changed without touching code.

**Which provider is not decided.** A short comparison (12 Oct 2026, from the providers' own pages
and directory listings; check prices and the DPA before signing):

| Provider | Company and data location | DPA | Rough price | Open-source friendliness |
|---|---|---|---|---|
| Scaleway Transactional Email | French cloud provider; Scaleway says TEM data is hosted and processed only in the EU, with no non-EU sub-processors in the TEM stack | Yes, part of Scaleway's standard DPA | Pay as you go: 300 emails a month included, then about 0.25 EUR per 1,000 | SMTP and REST API; supported by common open-source mail libraries (for example Anymail) |
| Lettermint | Dutch company, EU infrastructure, built for transactional email only | Yes, an Art. 28 DPA for every customer by default | Free for 300 emails a month; about 10 to 15 EUR a month for 10,000 | SMTP and official SDKs; the service itself is not open source |
| Brevo (formerly Sendinblue) | French company; databases on OVH in France and Germany and Google Cloud in Belgium | Yes, downloadable in the account settings | Free tier for small volumes; paid plans from roughly 9 to 25 EUR a month (sources differ) | SMTP and API; a marketing platform first, so tracking has to be switched off |

**Recommendation (not decided):** Scaleway or Lettermint, because both are transactional-only and
say the data stays in the EU (check each sub-processor list before signing). Brevo works too, but is a marketing
platform with open and click tracking that would need turning off. For the fake-data test the free
tiers are enough.

## Follows from this

- Sessions are listed in settings, with "log out everywhere".
- Re-authentication before deleting the account, exporting data or changing the email address.
- Signing in on a second phone ends the first phone's session and chat keys (after the waiting
  period, if it is a recovery).
- Certificates binding the account ID to the device key are issued by the admission service
  (sign-up checks, age result, bans). Recommended: run admission as its own service from the
  start, even on one machine, so it can become part of the sealed level in stage 2.

## Still open

- **Spike before building login:** confirm in a one-day test that the Apache-licensed Kratos
  supports passkeys in native apps (API flows from React Native, with iOS AuthenticationServices
  and Android Credential Manager). Fallback if not: a small, well-reviewed WebAuthn library in
  our API for passkeys, with Kratos for email codes and sessions.
- An optional recovery PIN, and whether the waiting period should be longer than 24 hours.
