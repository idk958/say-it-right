# Claude Code prompt — "Say It Right" web companion

**What this is:** A polished single-file web app that pairs with the Canva slide deck. Peers can open it on their phone during/after the tutorial showcase, tap a greeting, hear it pronounced by a native speaker (video), and try it themselves. This is the "training resource" the assessment rubric explicitly rewards — it extends the 15-minute showcase into a self-paced practice tool.

**How to use this file:** Open Claude Code in this folder (`D:\enhance game\game echance`). Paste everything between START PASTE and END PASTE as your first message.

---

## START PASTE

Build a single-file web app called **Say It Right** — an interactive cross-cultural greetings pronunciation companion. Save as `say-it-right.html` in this folder. It is the web companion to the team's Canva slide deck `https://www.canva.com/design/DAHK9g8qWdc/` (which they will showcase live), so the look, voice, and tone should match the deck: warm orange/cream palette, friendly serif headlines, illustrated chibi-adjacent style.

This is for Macquarie University MQBS2010 Assessment 3 (group training activity, 30%). The deliverable extends a 15-minute showcase activity into a self-paced practice tool. The marking rubric rewards "a polished training activity ... [with] visual/audio aides [that are] creative and clear" — every detail below ladders up to that.

### Use the available plugins/skills in this exact order

1. **Read first** — call `Read` on `theme-factory/SKILL.md` and `design:ux-copy/SKILL.md`. Internalize the warm orange/cream palette and the "small greetings, big respect" voice before you write anything.
2. **Theme** — `theme-factory` to set up a palette: deep warm orange (~#d97842) as accent, off-white cream (~#fdf3e7) background, charcoal text (~#3a2b1f), one soft secondary (mint or dusty gold). Match the Canva deck.
3. **UX copy** — `design:ux-copy` for every visible string. Tone is warm, slightly playful, never preachy.
4. **Build** the web app.
5. **Critique** — when playable end-to-end, run `design:design-critique` and iterate on its top 3 fixes.
6. **Accessibility** — finish with `design:accessibility-review`; fix any AA-level contrast or keyboard issues.

### Tech constraints (read carefully — multiple soft rules here)

- **Single HTML file**: `say-it-right.html`. Embedded CSS + JS. Open by double-click; runs offline for everything except the embedded videos.
- **Vanilla JS only** — no React, no jQuery, no build step.
- **Two external dependencies allowed**:
  - YouTube iframe embeds (videos)
  - The browser's built-in Web Speech API (`speechSynthesis`) for instant pronunciation playback — no internet needed for this; works offline; no API key
- **No npm packages, no CDN libraries** beyond YouTube iframe.
- **Mobile-first**. Designed to be opened on a phone. Test by resizing to 380 px wide.
- **No accounts, no tracking, no localStorage required**. Use `sessionStorage` only if needed (e.g. to remember the user's progress within a session).
- **Works on iOS Safari, Chrome, Firefox** (the three browsers a Macquarie tutorial peer will be using).

### Content — the 5 greetings (full data the app must include)

Build the data as a `const GREETINGS = [...]` array at the top of the script so a teammate can swap content without touching engine code. Each greeting object has the same shape:

```js
{
  id: "mandarin",
  language: "Mandarin",
  flag: "🇨🇳",
  nativeScript: "你好",
  phonetic: "NEE-how",
  meaning: "Hello",
  speechLang: "zh-CN",     // BCP-47 code for Web Speech API
  timeOfDay: [
    { native: "早上好", roman: "Zǎoshang hǎo", english: "Good morning" },
    { native: "下午好", roman: "Xiàwǔ hǎo",   english: "Good afternoon" },
    { native: "晚上好", roman: "Wǎnshang hǎo", english: "Good evening" }
  ],
  gesture: {
    name: "Light nod or handshake",
    description: "No bow. Eye contact is normal. A small nod or a Western-style handshake works in most professional contexts.",
    image: "svg-or-emoji-fallback"   // see Visual design section
  },
  culturalNote: "Mandarin uses four tones — the same syllable means four different things depending on pitch. Don't worry about perfection; locals appreciate the effort.",
  videoEmbed: "YOUTUBE_VIDEO_ID_HERE",   // see Video Sourcing section below
  videoTitle: "How to say Ni Hao — native speaker"
},
// Then: Thai, Japanese, Hindi, Arabic — full data below
```

Fill in for all 5 (copy this data into the GAME object verbatim, then enrich with culturally accurate detail you verify):

**Thai (สวัสดี Sawasdee)**
- Phonetic: `sa-wat-DEE`
- speechLang: `th-TH`
- Time-of-day: Arun sawat (morning), Sawasdee ton bai (afternoon), Sawasdee ton yen (evening)
- Politeness particles: append `krap` (male speaker) or `ka` (female speaker)
- Gesture: **the wai** — hands pressed together at chest, slight head bow. Higher hands = more respect (to monks, elders, teachers)
- Cultural note: the wai is essential for first meetings; skipping it can read as cold

**Japanese (こんにちは Konnichiwa)**
- Phonetic: `kon-NEE-chee-wah`
- speechLang: `ja-JP`
- Time-of-day: Ohayō (morning, casual) / Ohayō gozaimasu (morning, formal) / Konnichiwa is afternoon / Konbanwa (evening)
- Gesture: **the bow** — 15° casual, 30° respectful, 45° most respectful (apology or deep gratitude). Eye contact varies by context.
- Cultural note: the bow can replace a handshake entirely — bowing while shaking hands looks awkward, so pick one

**Hindi (नमस्ते Namaste)**
- Phonetic: `nuh-muh-STAY`
- speechLang: `hi-IN`
- Time-of-day: Suprabhāt (morning), Shubh dopahar (afternoon), Shubh sandhyā (evening)
- Gesture: **the namaste mudra** — palms together at heart-level, slight head bow
- Cultural note: meaning of the gesture is roughly "the divine in me bows to the divine in you" — explain this if there's time

**Arabic (السلام عليكم As-salāmu ʿalaykum)**
- Phonetic: `as-sa-LAA-mu a-LAY-kum`
- speechLang: `ar-SA`
- Meaning: "peace be upon you"
- Reply (important — include this!): `Wa ʿalaykum as-salām` — "and peace be upon you"
- Time-of-day: Sabah al-khayr (morning), Masa al-khayr (afternoon and evening — Arabic doesn't strongly split these)
- Gesture: **right hand to chest** after handshake — sincerity and warmth. Right hand only (avoid left for cultural reasons).
- Cultural note: the reply matters — without it, the greeting feels incomplete

### Video sourcing — explicit instructions

**The team will fill in YouTube video IDs themselves before the showcase.** Your job is to:

1. Leave clear `videoEmbed: "REPLACE_WITH_YOUTUBE_ID"` placeholders in each greeting object
2. In the HTML, render the placeholder as a friendly "▶ video coming — paste your YouTube link in `say-it-right.html`" tile so the layout isn't broken
3. Inside an HTML comment at the very top of the file, leave a **detailed sourcing guide** with these recommendations for them to follow:

```html
<!--
=========================================================
HOW TO ADD VIDEOS — read this once, takes 5 minutes total
=========================================================

For each greeting, find a 10–20 second YouTube clip of a native speaker
pronouncing the word with the gesture visible if possible.

RECOMMENDED CHANNELS (search YouTube directly):
- Mandarin: "Yoyo Chinese — Ni Hao" or "Mandarin Blueprint pronunciation"
- Thai: "Learn Thai with Mod — sawasdee" or "PaiThaiFood — greetings"
- Japanese: "JapanesePod101 — konnichiwa" or "Speak Japanese Naturally"
- Hindi: "Learn Hindi with Anil Mahato — namaste" or "Hindi Bhasha — pronunciation"
- Arabic: "ArabicPod101 — as-salamu alaykum" or "Easy Arabic"

ALTERNATIVE — record your team's own clips (recommended by the assessment
rubric for visible team contribution):
- Each team member learns one greeting
- Records a 10-sec phone clip pronouncing it + doing the gesture
- Uploads to YouTube as Unlisted
- Pastes the video ID in below

ALSO acceptable, all free + embeddable:
- Wikimedia Commons audio: commons.wikimedia.org/wiki/Category:Greetings_(audio)
- Forvo.com (pronunciations) — they have embed widgets

TO ADD A VIDEO:
1. Open the YouTube video
2. Copy the part of the URL after "watch?v=" — that's the video ID
   Example: https://www.youtube.com/watch?v=dQw4w9WgXcQ → ID is "dQw4w9WgXcQ"
3. Paste it inside the quotes for videoEmbed in the GREETINGS array below
4. Save the file. Done.

CITATION (the assessment requires APA citation for any external source):
- Note the channel name + video title + upload date in your reference list
- Example: "Easy Languages. (2023, March 15). Easy Mandarin 1 — Ni hao. YouTube. https://youtube.com/watch?v=..."
=========================================================
-->
```

In the rendered page, also include a tiny "🎥 No video yet — your team will add these" note on each greeting card when the placeholder is the current value. When a real YouTube ID is added, the card should swap to an embedded iframe player automatically.

### Audio playback — Web Speech API (works offline, no setup)

Every greeting has a **🔊 Play** button. Tapping it uses the browser's built-in `speechSynthesis` to speak the phrase in the correct language. This is browser-native (no library, no API key, no internet), works on all modern phones, and quality is surprisingly good. Implementation:

```js
function playGreeting(text, langCode) {
  const u = new SpeechSynthesisUtterance(text);
  u.lang = langCode;        // "zh-CN", "th-TH", etc.
  u.rate = 0.85;            // slower than default for learners
  speechSynthesis.cancel(); // stop anything already playing
  speechSynthesis.speak(u);
}
```

Each greeting card has THREE audio buttons:
- 🔊 **Play** — normal speed
- 🐢 **Slow** — rate 0.5
- 🔁 **Loop** — play 3 times with a 1-second gap

Show a subtle "speaking…" indicator while audio is playing (use `speechSynthesis.speaking` and the `onstart` / `onend` events).

If `speechSynthesis` is unavailable on a device (rare), fall back gracefully: hide the audio buttons and show "Tap the video for pronunciation."

### Page structure (5 sections, top-to-bottom)

**1. Hero**
- Big title: *Say It Right*
- Subtitle: *Small greetings, big respect.*
- One sentence: *"Tap a greeting. Listen. Watch. Try."*
- Small chip: *"From the MQBS2010 'Say It Right' team — [team name placeholder]"*

**2. Greeting Cards** (the meat of the app)
- 5 cards in a vertical stack on mobile, 2-column grid on tablet+, 3-column on desktop
- Each card has a collapsed and expanded state — collapsed shows native script + romanization + one play button; tap anywhere on the card to expand to full detail
- Full detail expanded view shows:
  - Native script (big, centred, serif)
  - Phonetic with stress marked
  - Meaning
  - Three audio buttons (Play / Slow / Loop)
  - Video embed (or placeholder if no video yet)
  - Time-of-day variants table (3 rows)
  - Gesture explanation with illustration (SVG you draw inline — simple chibi figure doing the bow / wai / namaste etc., one per greeting)
  - Cultural note in a callout box
- Card colour: warm cream background, deep orange accent border, soft shadow. The current card (expanded) is slightly larger with a softer glow.

**3. Try It Yourself** (interactive timer)
- Heading: *Try It Yourself*
- Sub: *Pair up. 30 seconds each. Greet, then swap.*
- A big visible countdown timer: starts at 60s on tap, beeps softly at 30s (when switching) and at 0s
- Show whose turn it is in big text: *"Partner A's turn"* → switch at 30s → *"Partner B's turn"* → end
- After the timer ends, show a soft *"How did it go? Try a different greeting →"* prompt that scrolls back to the cards
- Use the Web Audio API for soft beeps (no audio files)

**4. The Stakes** (one-screen visual reminder of why this matters)
- Two short cards stacked:
  - **Micro:** *A 2012 UCLA study found students whose teachers mispronounced their names often hid their language, culture, and family — at school, then at work. (Kohli & Solórzano, 2012)*
  - **Macro:** *HSBC's slogan "Assume Nothing" translated as "Do Nothing" in several markets. The 2009 rebrand cost $10 million.*
- Below: *"Same skill. Same stakes. Just different scale."*

**5. Footer**
- *"Small efforts matter."* one-liner
- Team credit chip (placeholder for team names)
- A small "📥 Send us feedback" link — `mailto:` opens an email draft with subject pre-filled (placeholder email in code; team replaces)
- APA citations for sources used (Kohli & Solórzano 2012; HSBC source) in tiny text
- Acknowledgement of Country line: *"We acknowledge the Wallumattagal people of the Dharug Nation, on whose Country Macquarie sits."*

### Visual design (matches the Canva deck)

- **Palette:** Deep warm orange `#d97842` (accent + headings), cream `#fdf3e7` (background), charcoal `#3a2b1f` (body text), mint `#aed9c1` (secondary), soft gold `#e8c780` (highlights). All AA-compliant.
- **Typography:** Serif for headlines (Georgia / system serif), clean sans for body (system-ui). Friendly, slightly playful, never corporate.
- **Components:**
  - Cards: rounded corners (16–20 px), soft shadows, 1 px warm border
  - Buttons: rounded pill shape, deep orange fill, white text, lift on hover
  - Native scripts: extra-large size (3–4 rem on desktop), centred, with subtle letter-spacing
  - Audio buttons: small icon + label, grouped
- **Illustrations** (you draw these inline as SVG):
  - 5 chibi character illustrations — one per culture's gesture:
    - Mandarin: simple person nodding (subtle head tilt)
    - Thai: hands together at chest, head slightly bowed (wai)
    - Japanese: torso bow at 30° angle
    - Hindi: namaste mudra — hands together at heart
    - Arabic: right hand on chest, slight smile
  - All in the same simple flat style as the Canva deck — round head, soft body, dot eyes, no shading
  - Each SVG ~120 × 120 px, embedded inline (no separate files)
- **Animations:** Subtle. Cards fade-and-slide-in on scroll. Buttons gently scale on tap. Don't overdo it.
- **Mobile:** Stack cards vertically. Time-of-day table becomes simple rows. Native script stays prominent. Timer becomes thumb-friendly.

### Editable content block

Put EVERYTHING writeable at the very top of the script tag in a single `const GAME = { greetings: [...], stakes: [...], copy: {...} }` object. Comment block above:

```js
// =========================================================
// EVERYTHING YOU MIGHT WANT TO EDIT IS BELOW.
// Greetings, video IDs, copy, team name, contact email — all here.
// The engine below this object does not need to be touched.
// =========================================================
```

### Acceptance criteria (verify before saying done)

- [ ] `say-it-right.html` opens by double-click in Chrome, Safari, and Firefox; no console errors
- [ ] All 5 greeting cards render with native script, phonetic, meaning visible
- [ ] Audio play button works in at least 4 of the 5 languages (Web Speech API support varies)
- [ ] Slow + Loop variants work
- [ ] Tapping a card expands it to full detail; tapping again collapses
- [ ] Video iframe loads correctly when a YouTube ID is provided; placeholder displays cleanly when not
- [ ] Time-of-day table appears for each greeting
- [ ] Gesture SVG illustrations render and visually distinguish each culture
- [ ] Cultural note callouts render in a visually distinct box
- [ ] Try It Yourself timer counts down from 60s, switches at 30s with a soft beep, ends with a final beep
- [ ] The Stakes section displays both Micro and Macro cards correctly
- [ ] Footer credits, Acknowledgement of Country, and feedback link all present
- [ ] Mobile viewport at 380 px: every section readable; no horizontal scroll; tap targets are at least 44 px
- [ ] `design:design-critique` run and top 3 fixes addressed
- [ ] `design:accessibility-review` run; no AA contrast failures; every interactive element keyboard-reachable; speech announces phase changes
- [ ] No external CSS or JS libraries loaded other than YouTube iframe
- [ ] All editable content (greetings, copy, team name, contact) in the single `GAME` object at top
- [ ] APA citations present in footer for the two real sources

### Companion file

Also write `say-it-right-readme.md` in the same folder with:
- Quick-start: "Open the file, tap a greeting, listen, watch, try."
- How to add YouTube videos (mirrors the HTML comment but in a separate file the team can email each other)
- How to swap content (point to the `GAME` object)
- How to host the file online (free options: GitHub Pages, Netlify drop, Cloudflare Pages). Important for the showcase — peers need a URL to open on their phones; `file://` won't work for them.
- One-line description suitable for the team's Canva slide 14: *"Open the companion at [your-url].github.io to practice on your own — videos, audio, and a timer included."*

### Don't do these

- No frameworks (no React, jQuery, Vue, anything else)
- No external CSS or JS libraries beyond YouTube iframe
- No image files — all illustrations are inline SVG you generate
- No audio files — Web Audio API for beeps, Web Speech API for pronunciation
- No tracking / analytics / cookies / fingerprinting
- No real player names embedded; everything is `[team name placeholder]` for the team to fill in
- No copyrighted text; all in-app copy is original
- No raw AI-generated text dropped in unedited — every visible string passes through `design:ux-copy`
- No corporate noir aesthetic. Warm orange / cream only. Match the Canva deck or it doesn't go.
- No "tips" or "fun facts" boxes that introduce extra cognitive load. Keep it focused: greeting → pronunciation → gesture → try.

### Why this fits the assessment

For the team's own reference (don't add this to the HTML):

- **Visual/audio aides creative and clear** — the rubric's HD descriptor. Inline SVG, embedded video, Web Speech audio, three playback speeds.
- **Engages participants in practicing the skill** — the timer + audio + try-yourself flow IS practice.
- **Polished training activity** — single page, mobile-first, real research citations.
- **The lens (Developing inclusive communication)** — the whole app is built around the lesson that effort > perfection, and that mispronouncing a greeting is a small daily exclusion that compounds. The Stakes section explicitly cites Kohli & Solórzano (2012).
- **The skill (Cross-cultural greeting)** — taught five times, practiced once, framed as transferable.

## END PASTE
