# Builds the GitHub Pages landing page (index.html) that links to the flashers.
#   python3 tools/make_index.py index.html v3   (or v4 for the Heltec-V4-Mac-SE repo)
import sys
out, first = sys.argv[1], sys.argv[2]   # first = v3 or v4
V3 = dict(id='v3', name='Heltec V3 Mac 128K', board='Heltec WiFi LoRa 32 V3', mac='A Macintosh 128K (or Plus) with 128 KB', file='flasher/Heltec-V3-Mac128k-Flasher.html', usb='Windows needs the Silicon Labs CP210x driver.', repo='https://github.com/hardwaremack-prog/Heltec-V3-Mac128k', shot='docs/heltec-mac.png')
V4 = dict(id='v4', name='Heltec V4 Mac SE', board='Heltec WiFi LoRa 32 V4', mac='A 1 MB Macintosh SE: System 4 to 6, 800K and 1.44 MB disks', file='flasher/Heltec-V4-Mac-SE-Flasher.html', usb='Uses the board\'s own USB, so no driver is needed.', repo='https://github.com/hardwaremack-prog/Heltec-V4-Mac-SE', shot='docs/heltec-mac-se.png')
E32 = dict(id='esp32', name='ESP32 Mac 128K', board='Plain ESP32 dev board (NodeMCU)', mac='The same 128K Mac on a NodeMCU-32S / ESP32-DevKitC with 4 MB flash', file='flasher/ESP32-Mac128k-Flasher.html', usb='Windows needs the CP210x or CH340 driver; hold BOOT if it won\'t connect.', repo='https://github.com/hardwaremack-prog/Heltec-V3-Mac128k', shot='docs/heltec-mac.png')
main = V3 if first == 'v3' else V4
others = [b for b in (V3, V4, E32) if b is not main]
def card(b, primary):
    return f'''<section class="card{' main' if primary else ''}">
 <p class="tag">{b['board']}</p>
 <h2>{b['name']}</h2>
 <p>{b['mac']}. {b['usb']}</p>
 <a class="btn{' primary' if primary else ''}" href="{b['file']}">Open the {b['name'].replace('Heltec ','')} flasher</a>
</section>'''
html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{main['name']} Flasher</title>
<meta name="description" content="Flash {main['name']} onto a {main['board']} from your browser.">
<style>
:root{{--bg:#eceae4;--card:#f8f7f3;--ink:#1f1e1b;--mute:#66635c;--line:#cdc9bf;--accent:#2b5f8e;--accent-ink:#fff;--sans:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;--mono:ui-monospace,"Cascadia Mono",Menlo,Consolas,monospace;color-scheme:light}}
@media (prefers-color-scheme:dark){{:root{{--bg:#18191b;--card:#222326;--ink:#ebe9e4;--mute:#a19d95;--line:#3a3b3f;--accent:#6fa3d4;--accent-ink:#0f1720;color-scheme:dark}}}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 var(--sans)}}
main{{max-width:760px;margin:0 auto;padding:32px 16px 48px;display:grid;gap:18px}}
h1{{margin:0;font:600 28px/1.2 var(--mono);letter-spacing:.5px;text-wrap:balance}}
header p{{margin:6px 0 0;color:var(--mute)}}
img{{width:100%;height:auto;border:1px solid var(--line);border-radius:10px;display:block}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 18px}}
.card.main{{border-color:var(--accent)}}
.card h2{{margin:0 0 4px;font:600 18px var(--mono)}}
.card p{{margin:0 0 12px}}
.tag{{font:12px var(--mono);color:var(--mute);margin:0 0 2px!important;text-transform:uppercase;letter-spacing:.5px}}
.btn{{display:inline-block;font-weight:600;padding:10px 16px;border-radius:8px;border:1px solid var(--line);color:var(--ink);text-decoration:none;background:var(--bg)}}
.btn.primary{{background:var(--accent);border-color:var(--accent);color:var(--accent-ink)}}
.btn:focus-visible{{outline:3px solid var(--accent);outline-offset:2px}}
.note{{color:var(--mute);font-size:14px}} .note a{{color:var(--accent)}}
ol{{margin:0;padding-left:20px}}
</style></head><body><main>
<header><h1>{main['name']}</h1><p>A classic Macintosh on a Meshtastic radio board, played in your web browser with sound. Flash it right from this page.</p></header>
<img src="{main['shot']}" alt="{main['name']} running in a web browser" width="1280" height="900">
{card(main, True)}
<section class="card"><h2>How it works</h2><ol>
<li>Use <b>Chrome or Edge</b> on a computer (they can talk to USB boards; Firefox and Safari can't).</li>
<li>Plug in the board with a USB-C cable that carries data, open the flasher, click <b>Connect</b>, then <b>Flash</b>.</li>
<li>Join the board's hotspot, open <b>http://192.168.4.1</b>, and add your Wi-Fi, ROM and disks.</li>
</ol></section>
{''.join(card(b, False) for b in others)}
<p class="note">Source, instructions and the ready-made firmware: <a href="{main['repo']}">{main['repo'].split('/',3)[3]}</a>. Apple ROMs and system software aren't included.</p>
</main></body></html>
'''
open(out, 'w').write(html)
