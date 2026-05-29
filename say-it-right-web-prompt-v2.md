# Claude Code prompt — Say It Right web companion, round 2

Paste this between START PASTE and END PASTE in the same Claude Code session you've been using.

---

## START PASTE

Three more features to add to `say-it-right.html`. The current build is great — keep the warm orange/cream design, the inline SVG chibi figures, the editorial type, the On Country treatment, all of it. This round adds depth to the audio and a second video per greeting.

### Feature 1 — A 🔊 Play button on every time-of-day variant

Right now there's one main Play button per greeting (e.g. one for "Ni Hao"). Add a Play button on every row of the time-of-day table too — so peers can tap "good morning", "good afternoon", and "good evening" individually and hear each one in the correct language.

Each variant already has its `roman` and `native` text and the greeting has its `speechLang`. Wire each button to the same audio engine, just passing the variant's text. Touch target ≥ 44 px. Same "speaking…" indicator. Same Slow / Loop options available via long-press for Slow and double-tap for Loop, with a small first-use hint.

### Feature 2 — Audio that finds its own sources, no manual setup

The Web Speech API works on most phones, but quietly fails on devices that don't have the language voice installed (common on older Android, sometimes on Windows desktop browsers). Build a three-tier fallback chain so audio always plays.

**Tier 1 — Web Speech API (current default).** Keep this. Call `speechSynthesis.getVoices()` on page load AND attach a `voiceschanged` listener — iOS loads voices async, so the first call returns empty. For each greeting, look for a voice matching its `speechLang`. Try a partial match if exact fails (`zh-CN` → any `zh-*`, `ar-SA` → any `ar-*`).

**Tier 2 — Wikimedia Commons embedded audio.** Add an `audioFallback` field to each greeting's data — a direct stable URL to a Wikimedia Commons audio file (`.ogg` or `.mp3`). **Find these URLs yourself during the build** using WebSearch + WebFetch. Wikimedia has pronunciation files for every common greeting; URLs are stable for years; no account, no API key, free to embed.

Search queries to try:
- `Mandarin pronunciation Ni hao site:commons.wikimedia.org`
- `Thai pronunciation Sawasdee site:commons.wikimedia.org`
- `Japanese pronunciation Konnichiwa site:commons.wikimedia.org`
- `Hindi pronunciation Namaste site:commons.wikimedia.org`
- `Arabic pronunciation As-salamu alaykum site:commons.wikimedia.org`

Pick the shortest clean clip per greeting. URL pattern is usually `https://upload.wikimedia.org/wikipedia/commons/...`. Verify each by fetching the head before baking it in. If you can also find clips for the morning/afternoon/evening variants, even better — add `audioFallback` to each time-of-day row too.

When Web Speech has no matching voice, the play button transparently creates an `<audio>` element with the Wikimedia URL and plays that. Users don't see which tier delivered the audio — they tap, they hear.

**Tier 3 — External link.** If both Web Speech AND Wikimedia fail (rare), show a small fallback link below the Play button: "🔗 hear it on Forvo" → opens `https://forvo.com/word/<word>/` in a new tab.

**Diagnostic transparency.** Add a small "🔧 audio diagnostics" expandable section at the very bottom of the page (closed by default). Inside: the user's browser voice list, which greetings use which tier, and a "Test all audio" button. This is for the team to verify on showcase day across different phones; peers can ignore it.

### Feature 3 — A second video per greeting, for the gesture

Each greeting currently has one `videoEmbed` slot (the pronunciation). Add a second slot `gestureVideoEmbed` for a video showing how to perform the gesture (the bow, the wai, the namaste, hand-to-chest).

In the expanded greeting card, render TWO video tiles:
- 🗣 **Hear it** — pronunciation video (existing)
- 🙏 **See the gesture** — gesture video (new)

Side-by-side on desktop, stacked on mobile (<600 px). Same friendly placeholder treatment as the existing pronunciation video — when the field is `"REPLACE_WITH_YOUTUBE_ID"`, show the "your team will add this" placeholder; when a real ID is filled in, embed the iframe.

Update the HTML comment at the top of the file with sourcing suggestions for gesture videos:

```
GESTURE VIDEO SOURCES (search YouTube):
- Mandarin: "Chinese business greeting etiquette" or "how to greet in Chinese culture"
- Thai: "how to wai" or "Thai wai gesture explained"
- Japanese: "Japanese bow levels" or "how to bow properly in Japan"
- Hindi: "how to do namaste correctly" or "namaste gesture meaning"
- Arabic: "Arabic greeting etiquette" or "right hand to chest gesture"

BEST option for the rubric — record your own team demonstrating each gesture
(10-second phone clip, upload as Unlisted to YouTube, paste the ID below).
```

### What the GAME object looks like after this round

```js
{
  id: "mandarin",
  language: "Mandarin",
  flag: "🇨🇳",
  nativeScript: "你好",
  phonetic: "NEE-how",
  meaning: "Hello",
  speechLang: "zh-CN",
  audioFallback: "https://upload.wikimedia.org/wikipedia/commons/...",   // NEW
  timeOfDay: [
    {
      native: "早上好",
      roman: "Zǎoshang hǎo",
      english: "Good morning",
      audioFallback: "https://upload.wikimedia.org/wikipedia/commons/..."   // NEW (optional per row)
    },
    // ...
  ],
  gesture: { /* unchanged */ },
  culturalNote: "...",
  videoEmbed: "REPLACE_WITH_YOUTUBE_ID",            // pronunciation video (existing)
  videoTitle: "How to say Ni Hao",
  gestureVideoEmbed: "REPLACE_WITH_YOUTUBE_ID",     // NEW — gesture demo video
  gestureVideoTitle: "How to greet someone in Chinese culture"   // NEW
}
```

### What stays untouched

- **The On Country card (Warami / Yaama).** Indigenous languages must be heard from a human, not a synthesiser. This card explicitly does NOT get: time-of-day audio buttons, Wikimedia fallback, Forvo link, pronunciation video, gesture video. Keep its "should be heard from a person, not a machine" treatment exactly as it is. Optionally add one line directing peers to the [50 Words Project](https://50words.online/) for authentic Indigenous pronunciation if a Walanga Muru contact isn't available.
- The overall page layout, palette, type, motion, SVG illustrations, Stakes section, footer, Acknowledgement of Country
- The `[hidden]` fix and the AA contrast adjustments from the last round

### Acceptance criteria (verify before saying done)

- [ ] Every time-of-day row has its own 🔊 Play button that speaks that specific variant in the correct language
- [ ] `speechSynthesis.getVoices()` runs on page load AND on `voiceschanged` event; iOS async voice loading handled
- [ ] When a language voice is missing, the button transparently falls back to a `<audio>` element with the Wikimedia URL
- [ ] All 5 main greetings have a real, verified Wikimedia Commons `audioFallback` URL baked in
- [ ] Forvo fallback link appears only when both other tiers fail
- [ ] Audio diagnostics panel at the bottom of the page works
- [ ] Every greeting (except On Country) shows TWO video tiles: pronunciation + gesture
- [ ] Both video tiles show the friendly placeholder until a real YouTube ID is added; embed iframe when present
- [ ] Mobile viewport at 380 px: doubled video content stacks cleanly; no horizontal scroll
- [ ] On Country card unchanged — no synthesised audio, no Wikimedia fallback, no videos
- [ ] All editable fields still live in the single `GAME` object at the top
- [ ] `design:design-critique` and `design:accessibility-review` both run; top fixes addressed; AA contrast and keyboard reachability preserved
- [ ] No console errors; fully offline-capable except for YouTube iframes and the Wikimedia audio fetch

### Update the readme

Edit `say-it-right-readme.md`:
- Add a section "How the audio works" explaining the three tiers (Web Speech → Wikimedia → Forvo) in one short paragraph
- Note that audio now works on more devices, including older Android and Windows desktops without language packs
- Update the "what to add" section: each greeting needs TWO YouTube IDs (pronunciation + gesture)
- Add a one-liner: *"The On Country card is intentionally machine-audio-free. Indigenous languages deserve a human voice."*

## END PASTE
