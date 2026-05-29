# Claude Code patch prompt — Say It Right web companion

**Use this in the SAME Claude Code session that built `say-it-right.html`.** Paste between START PASTE and END PASTE.

---

## START PASTE

Three additions to `say-it-right.html`. Build on the existing structure — don't rebuild from scratch. The `GAME` object at the top stays; add fields to it. The engine code keeps working.

### 1. Audio Play buttons on EVERY time-of-day variant

Right now only the main greeting has a 🔊 button. Add a Play button at the right end of every row in the time-of-day variants table so peers can hear "good morning", "good afternoon", "good evening" individually — each in the correct language.

Each row in `timeOfDay` already has fields like `{ native: "早上好", roman: "Zǎoshang hǎo", english: "Good morning" }`. The button taps into the same audio function as the main greeting, passing the `roman` (or `native` if available and the voice supports it) and the greeting's `speechLang`.

Touch target ≥ 44 px. Same "speaking…" indicator. Same Slow / Loop options available via long-press OR a small kebab menu (keep this simple — long-press for slow, double-tap for loop, with discoverable hints on first use).

### 2. Make the audio "just work" — find its own sources, no manual setup

Right now the audio relies on Web Speech API. That works on most phones but fails silently when the user's device doesn't have the language voice installed (common on older Android, sometimes on Windows desktop). Make it bulletproof with a three-tier fallback chain.

**Tier 1 — Web Speech API (current behaviour).** Keep this as the default. On page load, call `speechSynthesis.getVoices()` and also add a `voiceschanged` event listener (voices load async on iOS — first call returns empty). For each greeting, check if a voice is available for its `speechLang`. Also try partial matches (e.g. `zh-CN` falls back to any `zh-*` voice; `ar-SA` to any `ar-*`).

**Tier 2 — Wikimedia Commons embedded audio.** Add a new field `audioFallback` to each greeting in the `GAME` object — a direct URL to a stable Wikimedia Commons audio file (`.ogg` or `.mp3`). **Find these URLs yourself during the build using WebSearch + WebFetch.** Wikimedia Commons has pronunciation files for every common greeting; their URLs are stable for years and free to embed.

Search for files in these categories (use whatever search query Wikimedia accepts):
- "Mandarin pronunciation Nǐ hǎo" — site: commons.wikimedia.org
- "Thai pronunciation Sawasdee" — site: commons.wikimedia.org
- "Japanese pronunciation Konnichiwa" — site: commons.wikimedia.org
- "Hindi pronunciation Namaste" — site: commons.wikimedia.org
- "Arabic pronunciation As-salamu alaykum" — site: commons.wikimedia.org

Pick the cleanest, shortest clip per greeting (usually a `Zh-X.ogg` or similar pattern under `https://upload.wikimedia.org/wikipedia/commons/...`). Verify each URL returns audio by fetching the head before baking it in. If you can find clips for the time-of-day variants too, even better — add `audioFallback` to each time-of-day row as well.

When the Web Speech API has no matching voice, the play button creates an `<audio>` element with the Wikimedia URL, plays it, and shows the same "speaking…" indicator. The fallback should be transparent to the user — they tap Play, they hear audio, they don't know which tier delivered it.

**Tier 3 — External link.** If both Web Speech AND Wikimedia fail (rare), show a small fallback link below the Play button: "🔗 hear it on Forvo" → opens `https://forvo.com/word/<greeting>/` in a new tab.

**Diagnostic transparency.** At the bottom of the page, add a small "🔧 audio diagnostics" expandable section (closed by default) that shows: which voices the user's browser has, which greetings are using which tier, and a "Test audio" button per greeting. This is for the team's testing day-of, not for peers — but peers can open it if curious.

### 3. A second video per greeting — the GESTURE

Right now each greeting has one `videoEmbed` for pronunciation. Add a second field `gestureVideoEmbed` for a video showing how to perform the gesture (the bow, the wai, the namaste, hand-to-chest).

In the expanded card, render TWO video tiles:
- 🗣 **Hear it** — pronunciation video (existing)
- 🙏 **See the gesture** — gesture video (new)

On desktop: side-by-side. On mobile (<600 px): stacked. Same placeholder treatment as the existing pronunciation video — when the field is `"REPLACE_WITH_YOUTUBE_ID"`, show the friendly placeholder; when a real ID is filled in, embed the iframe.

Update the HTML comment at the top of the file with gesture-video sourcing suggestions:

```
GESTURE VIDEO SOURCES (search YouTube):
- Mandarin: "Chinese business greeting etiquette" or "how to greet in Chinese culture"
- Thai: "how to wai" or "Thai wai gesture explained"
- Japanese: "Japanese bow levels" or "how to bow properly in Japan"
- Hindi: "how to do namaste correctly" or "namaste gesture meaning"
- Arabic: "Arabic greeting etiquette" or "right hand to chest gesture"

OR — best for the rubric — record your own team demonstrating each gesture
(10-second phone clip, upload as Unlisted to YouTube, paste the ID below).
```

### Update the GAME object structure

The new shape of each greeting object:

```js
{
  id: "mandarin",
  language: "Mandarin",
  flag: "🇨🇳",
  nativeScript: "你好",
  phonetic: "NEE-how",
  meaning: "Hello",
  speechLang: "zh-CN",
  audioFallback: "https://upload.wikimedia.org/wikipedia/commons/...",  // NEW — Wikimedia URL
  timeOfDay: [
    {
      native: "早上好",
      roman: "Zǎoshang hǎo",
      english: "Good morning",
      audioFallback: "https://upload.wikimedia.org/..."   // NEW — optional per-variant
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

### Don't break — explicit list

- **The On Country card (Warami / Yaama) stays special.** It explicitly does NOT get:
  - Web Speech / Wikimedia / Forvo audio (Indigenous languages must be heard from a person, not a synthesizer)
  - Time-of-day audio buttons
  - A pronunciation video unless one explicitly cleared by Walanga Muru
  - A gesture video unless culturally appropriate
  - Keep the "should be heard from a person, not a machine" treatment intact. Add a note to that card directing peers to Walanga Muru / 50 Words Project (https://50words.online/) for authentic pronunciation.
- The existing `GAME` object structure — add fields, don't rename or remove existing ones
- The page layout — the new video tiles slot into the existing card flow; no full redesign
- The colour palette, type system, motion design — leave them alone
- The Stakes section with the Kohli & Solórzano citation and HSBC example — untouched

### Acceptance criteria (verify before saying done)

- [ ] Every greeting card shows a 🔊 Play button at the end of each time-of-day row
- [ ] Tapping a time-of-day Play button speaks that specific variant (e.g. "Zǎoshang hǎo" not "Nǐ hǎo") in the correct language
- [ ] `speechSynthesis.getVoices()` is called on page load AND on `voiceschanged` event
- [ ] When a language voice is missing, the audio button transparently falls back to the Wikimedia `<audio>` element with the user noticing nothing
- [ ] Every main greeting has a real working Wikimedia Commons `audioFallback` URL baked into the data
- [ ] When BOTH fail, the small Forvo external link appears
- [ ] Audio diagnostics panel at bottom of page works and shows real voice list
- [ ] Every greeting card (except On Country) shows TWO video tiles: pronunciation + gesture
- [ ] Both video tiles show the friendly placeholder until a real YouTube ID is added
- [ ] Mobile viewport at 380 px: doubled video content stacks cleanly; no horizontal scroll
- [ ] On Country card has NO time-of-day audio buttons, NO Wikimedia fallback, NO videos — exactly as before
- [ ] `design:design-critique` run; top 2 fixes addressed
- [ ] `design:accessibility-review` run; all AA contrast still passes; all new interactive elements keyboard-reachable; new audio Play buttons have descriptive aria-labels ("Play good morning in Mandarin")
- [ ] No console errors, no horizontal scroll, fully offline-capable except for YouTube embeds and the Wikimedia audio fetch
- [ ] All editable fields still in the single `GAME` object at the top

### Update the readme

Edit `say-it-right-readme.md`:
- Add a "How the audio works" section explaining the three tiers (Web Speech → Wikimedia → Forvo)
- Note that the audio now works on more devices than before (older Android, Windows without language packs)
- Update the "what to add" section to mention TWO videos per greeting (pronunciation + gesture)
- Add a tiny line: *"The On Country card is intentionally machine-audio-free. Indigenous languages deserve a human voice."*

## END PASTE
