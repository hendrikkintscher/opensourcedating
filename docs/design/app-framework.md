# App framework: which one, and why

*Design note, 11 Oct 2026. Compares React Native/Expo, Flutter, Kotlin Multiplatform and fully
native apps for the Android + iOS client. Points marked "inferred" are judgement, not measured.*

## Recommendation

**React Native with Expo** (development builds, not Expo Go), with all chat cryptography in a
small native module of our own: Kotlin calling Signal's official `libsignal-android` on Android,
Swift calling the official `LibSignalClient` on iOS. Keys and session state never leave that
native module; the JavaScript side only hands it plaintext to encrypt and gets plaintext back.

Why, in one paragraph: every cross-platform option needs a native bridge for libsignal anyway,
so the libsignal constraint doesn't decide the question by itself. What decides it is that
React Native/Expo is the fastest way for one person working with Claude to ship the
non-crypto 90 % of the app (profiles, search, map, settings, moderation screens) on both
platforms, it has the biggest contributor pool for an open-source project, the two existing
open-source dating apps (Alovoa, Duolicious) use it and can be read for reference, and the
native libsignal module we'd have to write is exactly the reusable component the NLnet
application can fund. If the bridge ever disappoints, the module is already Kotlin and Swift,
so moving to fully native later throws away UI code, not the crypto.

## The constraint that matters: libsignal

- Signal ships official bindings only for **Java/Kotlin** (`org.signal:libsignal-client` /
  `libsignal-android`), **Swift** (`LibSignalClient`) and **TypeScript for Node.js**
  (desktop/server, not React Native). All three wrap the same Rust core.
- No option gets libsignal "for free" in shared code:
  - **React Native**: write an Expo native module (Kotlin + Swift) around the official bindings.
  - **Flutter**: either the same via platform channels, or a community Dart FFI package
    (`libsignal` on pub.dev, one maintainer, built on flutter_rust_bridge, not from Signal).
  - **Kotlin Multiplatform**: Android uses the Java binding directly; iOS can't call the Swift
    binding from Kotlin directly (Swift export isn't stable yet), so you either write a Swift
    wrapper behind a Kotlin interface or bind the C FFI (`signal_ffi.h`) yourself.
  - **Native**: use each official binding directly. Zero bridge, two apps.
- So the honest comparison is: how big is the bridge, and how much else is shared.
  The bridge is small (inferred: around ten calls such as create identity, publish prekeys,
  start session from a bundle, encrypt, decrypt, plus a key store backed by the
  Android Keystore / iOS Keychain).

## Comparison

| | React Native + Expo | Flutter | Kotlin Multiplatform (+ Compose MP) | Native (Kotlin + Swift) |
|---|---|---|---|---|
| libsignal | Own Expo module over official bindings | Platform channels over official bindings, or unofficial Dart FFI package | Android direct; iOS needs Swift wrapper or C FFI binding | Official bindings directly, best |
| Shared code | ~90 % (UI + logic), inferred | ~90 % (UI + logic), inferred | Logic shared; UI shared with Compose MP (iOS stable since May 2025) | None |
| Passkeys (Ory Kratos) | Community libraries over native APIs | Community packages over native APIs | expect/actual over native APIs | Native APIs, best |
| Map, 500 m grid | MapLibre React Native, mature | maplibre_gl, mature | MapLibre Compose, younger | MapLibre native SDKs, best |
| Speed for a solo dev with Claude | Fastest (inferred: Claude is strongest in TypeScript/React) | Fast | Medium (fewer examples, iOS edge cases) | Slowest, every screen twice |
| Contributor pool for open source | Largest (JS/TS) | Large | Small but growing | Split across two |
| Reference apps | Alovoa, Duolicious both use it | None found in dating | None found | Signal itself |
| Web build for demos | Yes (no chat crypto on web) | Yes, weaker | Experimental | No |
| F-Droid | Possible with local builds, no proprietary push | Possible | Possible | Easiest |
| Supply chain / security surface | Large npm tree; keep it lean and pinned | Smaller | Small | Smallest |
| Lock-in if we switch later | Low: crypto module already Kotlin/Swift | Medium | Low on Android | n/a |

## Pros and cons

### React Native + Expo (recommended)
**Pros**
- One TypeScript codebase for both platforms; quickest to a working pilot.
- Expo Modules API makes writing the Kotlin/Swift libsignal module straightforward and keeps it
  isolated and testable on its own.
- That module is a clean, reusable deliverable for **NLnet (deadline 3 Nov)** and fits the
  "public-interest infrastructure" angle for the **Prototype Fund (30 Nov)**; funding.md already
  suggests exactly this.
- Biggest pool of potential contributors; Alovoa's and Duolicious's apps are readable examples.
- Optional web build is handy for demos and screenshots for grant reviewers.

**Cons**
- Crypto lives across a bridge: must be designed so keys never enter JavaScript.
- Large npm dependency tree; needs pinning, lockfile review and few dependencies.
- Expo's hosted services (EAS builds, Expo push) are optional and must stay optional: build
  locally or in GitHub Actions, send push directly via FCM/APNs with empty "new message"
  payloads so no content or metadata goes through a third party.
- Upgrades between React Native versions occasionally break native modules.

### Flutter
**Pros**
- Very consistent UI on both platforms, good performance, smaller dependency tree.
- A community Dart FFI wrapper for libsignal exists and is actively updated.

**Cons**
- That wrapper is unofficial and has one maintainer; trusting it for E2EE needs an audit we
  can't afford yet. Using official bindings means the same platform-channel bridge as React
  Native, so Flutter's advantage disappears.
- Dart is a smaller contributor pool; no open-source dating app to learn from.
- Accessibility and platform look need extra work (it draws its own widgets).

### Kotlin Multiplatform (+ Compose Multiplatform)
**Pros**
- Android side uses the official libsignal binding with no bridge at all.
- Native performance; Compose UI on iOS has been stable since May 2025.

**Cons**
- iOS libsignal still needs a hand-written Swift wrapper or our own C FFI binding, which is
  more error-prone than the Expo module.
- Younger ecosystem: map, passkeys and many small libraries need expect/actual glue.
- Fewer worked examples, so slower for a solo developer leaning on Claude (inferred).

### Fully native (Kotlin + Swift)
**Pros**
- Best possible crypto, passkey and Keychain/Keystore integration; what Signal itself does.
- Smallest attack surface and easiest F-Droid build.

**Cons**
- Two apps, every screen and fix twice, two test suites. For one person on a grant timeline
  this roughly doubles the work (inferred).
- Contributors split into two camps.

## What would change the recommendation
- If an independent audit of a cross-platform libsignal wrapper appears, Flutter becomes as
  attractive as React Native.
- If the pilot shows the bridge causing real security or reliability problems, move to native;
  the crypto module carries over unchanged.
- If a funder wants a component for the Kotlin ecosystem, KMP would earn a second look.

## Next steps once decided
1. Set up an Expo app (TypeScript, development builds) in `app/`, built locally/CI, no EAS
   or Expo push required.
2. Write the `libsignal` Expo module (Kotlin + Swift) with its own tests; keys in
   Keystore/Keychain.
3. Pitch that module plus the store-until-delivered relay to NLnet by 3 Nov.

## Sources
- libsignal (official bindings: Java, Swift, TypeScript): https://github.com/signalapp/libsignal
- Expo Modules API: https://docs.expo.dev/modules/overview/
- Community Dart wrapper: https://pub.dev/packages/libsignal
- Compose Multiplatform 1.8.0 (iOS stable): https://blog.jetbrains.com/kotlin/2025/05/compose-multiplatform-1-8-0-released
- KMP roadmap, Swift export status: https://blog.jetbrains.com/kotlin/2025/08/kmp-roadmap-aug-2025/
- Alovoa app (Expo): https://github.com/Alovoa/alovoa-expo
- Project research: `research/data-security.md`, `research/alovoa-dossier.md`, `research/funding.md`
