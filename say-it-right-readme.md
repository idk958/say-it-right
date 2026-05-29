# Say It Right — web companion

A self-paced practice tool that pairs with the *Say It Right* Canva deck. Peers open it on their phone, tap a greeting, **hear** it (native-speaker video + instant audio), see the gesture, and **try** it themselves with a built-in pairing timer.

It's a single file — `say-it-right.html`. No install, no accounts, no internet needed except for the YouTube videos.

---

## Quick start

**Open the file, tap a greeting, listen, watch, try.**

1. Double-click `say-it-right.html` — it opens in any browser.
2. Tap a card to expand it.
3. Tap **🔊 Play** to hear the greeting (uses your phone's built-in voice, with automatic fallbacks — see below).
4. Watch the two videos, then scroll to **Try It Yourself**, press start, and practise in pairs.

That's the whole experience. Everything below is for the team setting it up.

> **For the videos to play inline you need to host the page** (any free option below). Opened as a local file, the video tiles become "Watch on YouTube" links instead — YouTube blocks embedding on `file://`. The audio and timer work locally either way.

---

## How the audio works (no setup needed)

Tap **🔊 Play** and the app finds its own sound, automatically — you never configure anything. Crucially, **every greeting and every time-of-day variant has a built-in audio clip embedded right in the file**, so a tap is *never silent* and never needs a special voice installed:

1. **Your device's built-in voice** (Web Speech), if it has one for that language — instant, offline, and uses the nicer native voice (most phones have these).
2. **A verified Wikimedia Commons clip** for the five headline words (real human recordings).
3. **A built-in embedded clip** (base64 MP3, generated with gTTS) for every greeting *and* every "good morning/afternoon/evening" variant. This is what makes it **play inline on a PC or older phone that has no voice for the language** — and it works **offline**, since the audio is inside the HTML file.

The upshot: **every 🔊 button plays inline on every device**, including a Windows PC with only English voices. No new tabs, no setup. Each button cascades automatically — if the device voice is missing **or installed but silent** (a known quirk for some Hindi and cloud voices), it falls through to the recorded clip, then the built-in offline clip, so a tap is never silent.

> If you change the greetings and want to regenerate the embedded audio, run `python generate-tts.py` (needs `pip install gTTS` and internet — it re-synthesizes every phrase and re-injects the clips). You don't need to do this unless you edit the words.

Every time-of-day variant ("good morning", "good afternoon"…) has its own 🔊 button too. **Tap** = play, **hold** = slow, **double-tap** = repeat.

---

## The videos — two per greeting, already filled in

Each greeting now has **two** video tiles:

- **🗣 Hear it** — a native speaker pronouncing the word (`videoEmbed`)
- **🙏 See the gesture** — the bow / wai / namaste / hand-to-chest (`gestureVideoEmbed`)

Working, embeddable starter videos are **already baked in** so the page is complete out of the box. **You should still verify each one and, ideally, replace them with your own team's clips** — the rubric rewards visible team contribution, and your own 10-second phone clips (uploaded to YouTube as **Unlisted**) are more authentic and avoid any licence questions.

**To swap a video:** open the YouTube video, copy the part of the URL after `watch?v=` (e.g. `…watch?v=dQw4w9WgXcQ` → `dQw4w9WgXcQ`), and paste it into `videoEmbed` or `gestureVideoEmbed` for that greeting in the `GAME` object. Save.

> **Videos only play once the page is hosted online** (http/https). YouTube blocks embedding on a local `file://` page, so if you double-click the file the video tiles become "Watch on YouTube" links instead. Host it (see below) and the inline players appear. This is why hosting is required for the showcase anyway.

**On Country (Warami):** this card has **no video and no synthesised audio**, by design — an Indigenous greeting should be heard from a person, not a machine or a stock clip. It points to the **50 Words Project** for authentic pronunciation. Do not add a video unless a Traditional Custodian or Walanga Muru approves one: <https://www.mq.edu.au/about/indigenous-strategy>

**APA citation** (required for any external source — videos and audio): list every clip you keep, e.g.
> Easy Languages. (2023, March 15). *Easy Mandarin 1 – Ni hao* [Video]. YouTube. https://youtube.com/watch?v=...
>
> Wikimedia Commons audio credits live in each greeting's `audioFallbackCredit` field in the HTML.

---

## How to swap any content

Everything editable lives in one place: the `GAME = { ... }` object near the top of the `<script>` in `say-it-right.html`. You never need to touch the engine code below it.

| Want to change… | Edit this in `GAME` |
|---|---|
| Team name | `copy.teamChip` and `copy.footerCredit` |
| Any on-screen wording | the `copy` object |
| A greeting's text, phonetic, gesture, note | the matching entry in `greetings` |
| Pronunciation video | `videoEmbed` (paste the YouTube ID) |
| Gesture video | `gestureVideoEmbed` (paste the YouTube ID) |
| Fallback audio clip | `audioFallback` (a direct Wikimedia upload URL) |

Each greeting object has the same shape, so a teammate can add or reorder greetings without breaking anything. The `speechLang` field (e.g. `"zh-CN"`, `"ja-JP"`) tells the phone which voice to use — leave it as-is.

---

## How to put it online (so peers can open it on their phones)

A `file://` link only works on your own laptop. For the showcase, peers need a real URL. All of these are free and take a few minutes:

- **Netlify Drop** — go to <https://app.netlify.com/drop> and drag `say-it-right.html` onto the page. Instant public URL. Easiest option.
- **GitHub Pages** — create a repo, upload the file (rename to `index.html`), enable Pages in Settings → Pages. URL looks like `yourname.github.io/say-it-right`.
- **Cloudflare Pages** — connect a repo or upload directly; similar to Netlify.

Tip: rename the file to `index.html` before hosting so the URL is clean (no `/say-it-right.html` on the end).

Make a QR code of the final URL (search "free QR code generator") and put it on the deck so peers can scan and open it instantly.

---

## For Canva slide 14

> **Practise on your own:** open the companion at **[your-url]** — videos, audio, and a pairing timer included.

---

## What's inside (for your write-up)

- **5 greetings** — Mandarin, Thai, Japanese, Hindi, Arabic — each with native script, phonetics, meaning, three audio speeds, **two videos** (pronunciation + gesture), time-of-day variants (each with its own play button), an inline gesture illustration, and a cultural note.
- **Cascading audio** — device voice → verified Wikimedia Commons clip → built-in offline clip → Forvo link. Each step only fires if the previous one fails to make sound (including a voice that's installed but silent), so a greeting plays on any device.
- **An On Country card** — Warami (Dharug) — the most local greeting, framed for the assessment's global-citizenship lens. Deliberately **machine-audio-free and video-free** — an Indigenous greeting should be heard from a person, not a synthesiser — and it points to the **50 Words Project**, with a reminder to confirm protocol with Walanga Muru.
- **Try It Yourself** — a 60-second pairing timer that switches partners at the 30-second mark with a soft chime, fully driven by the browser (no audio files).
- **Built for phones** — single file, no tracking, no accounts. Accessible: AA-contrast colours, full keyboard support, ≥44 px tap targets, screen-reader announcements on the timer, and reduced-motion support.
