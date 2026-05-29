#!/usr/bin/env python3
"""
Generate embedded pronunciation audio for say-it-right.html.

Reads the greetings out of the HTML, synthesizes each native word + each
time-of-day variant with gTTS (free, no API key), base64-encodes the MP3s,
and injects them into the `const TTS_AUDIO = {...}` object in the HTML.

Run:  python generate-tts.py
Re-run any time you change the greetings.
"""
import re, io, json, base64, sys
from gtts import gTTS

HTML = "say-it-right.html"

# gTTS language code per BCP-47 speechLang (just the primary subtag works)
def gtts_lang(speech_lang):
    return speech_lang.split("-")[0]   # zh-CN->zh, th-TH->th, ja-JP->ja, hi-IN->hi, ar-SA->ar

def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    html = open(HTML, encoding="utf-8").read()

    # Isolate just the GAME greetings array (stop at the GAME object close "\n};")
    start = html.index("greetings: [")
    end = html.index("\n};", start)
    region = html[start:end]

    # Split into one chunk per greeting object (each starts with  id: "...")
    chunks = re.split(r'\bid:\s*"', region)[1:]

    # Collect (text, gtts_lang) pairs, preserving order, de-duped
    pairs = []
    seen = set()
    for ch in chunks:
        m = re.search(r'speechLang:\s*(?:"([a-zA-Z\-]+)"|null)', ch)
        if not m or not m.group(1):
            continue                       # On Country (null) -> no audio, skip
        lang = gtts_lang(m.group(1))
        texts = []
        ns = re.search(r'nativeScript:\s*"([^"]+)"', ch)
        if ns:
            texts.append(ns.group(1))
        texts += re.findall(r'\bnative:\s*"([^"]+)"', ch)
        for t in texts:
            if t not in seen:
                seen.add(t)
                pairs.append((t, lang))

    if not pairs:
        print("No phrases found — aborting.", file=sys.stderr)
        sys.exit(1)

    print(f"Synthesizing {len(pairs)} phrases...")
    mapping = {}
    total = 0
    for text, lang in pairs:
        buf = io.BytesIO()
        gTTS(text, lang=lang).write_to_fp(buf)
        data = buf.getvalue()
        total += len(data)
        b64 = base64.b64encode(data).decode("ascii")
        mapping[text] = "data:audio/mpeg;base64," + b64
        print(f"  [{lang}] {text}  ({len(data)} bytes)")

    # Build the JS object and inject
    lines = [json.dumps(t, ensure_ascii=False) + ": " + json.dumps(durl)
             for t, durl in mapping.items()]
    js = "const TTS_AUDIO = {\n  " + ",\n  ".join(lines) + "\n};"

    if "const TTS_AUDIO = {};" not in html and not re.search(r'const TTS_AUDIO = \{[\s\S]*?\n\};', html):
        print("Placeholder `const TTS_AUDIO = {};` not found — aborting.", file=sys.stderr)
        sys.exit(1)

    # Replace either the empty placeholder or a previously-generated block
    if "const TTS_AUDIO = {};" in html:
        html = html.replace("const TTS_AUDIO = {};", js, 1)
    else:
        html = re.sub(r'const TTS_AUDIO = \{[\s\S]*?\n\};', js, html, count=1)

    open(HTML, "w", encoding="utf-8").write(html)
    print(f"\nInjected {len(mapping)} clips, {total/1024:.0f} KB raw "
          f"(~{total*4/3/1024:.0f} KB base64) into {HTML}.")

if __name__ == "__main__":
    main()
