# Heltec V4 Mac SE

**A 1 MB Macintosh SE running on a Heltec V4 Meshtastic board, played in your web browser, with sound.**

**Flash it from your browser:** [hardwaremack-prog.github.io/Heltec-V4-Mac-SE/](https://hardwaremack-prog.github.io/Heltec-V4-Mac-SE/) (Chrome or Edge on a computer).

Heltec V4 Mac SE turns a **Heltec WiFi LoRa 32 V4** (the ESP32-S3 board with 2 MB of PSRAM and
16 MB of flash) into a working **Macintosh SE**. The board emulates the Mac's 68000 processor
and its hardware, keeps a library of 800K and 1.44 MB floppy disks in its own flash, and serves
the Mac's screen and sound to any browser on your network. There's no app to install: open the
board's address on a PC, a Raspberry Pi or a phone, and you're at the Finder.

![A Mac SE with 1 MB running System 4.2 and Finder 6.0 on a Heltec V4](docs/heltec-mac-se.png)

*System 4.2 and Finder 6.0 on a Heltec V4, with 1,024K of memory.*

> Have a **Heltec V3** instead? It has no PSRAM, so it runs a 128K Mac. Flash it with
> [`flasher/Heltec-V3-Mac128k-Flasher.html`](flasher/Heltec-V3-Mac128k-Flasher.html) (or
> `firmware/Heltec-V3-Mac128k.bin`), included here for convenience. Its home is
> [Heltec V3 Mac 128K](https://github.com/hardwaremack-prog/Heltec-V3-Mac128k). Both share the same
> code, and a V3 and a V4 can sit on the same network.
>
> Just a **plain ESP32 dev board** (NodeMCU-32S / ESP32-DevKitC, 4 MB flash)? It runs the same
> 128K Mac: [`flasher/ESP32-Mac128k-Flasher.html`](flasher/ESP32-Mac128k-Flasher.html). See
> [Heltec V3 Mac 128K](https://github.com/hardwaremack-prog/Heltec-V3-Mac128k#also-on-a-plain-esp32-esp32-mac-128k)
> for what's different there.

## Highlights

- **A real Mac SE.** The SE's **ADB** keyboard and mouse (the Apple Desktop Bus, driven
  through the VIA as on the real logic board), its ROM overlay, and real VIA timers, which
  System 4 and later need for the Time Manager.
- **1 MB of RAM** in the V4's PSRAM, leaving the ESP32's own memory to Wi‑Fi and the web page.
- **System 4 to 6** from **800K and 1.44 MB HFS** disks. The Mac SE FDHD ROM reads
  high-density disks just like the real SuperDrive.
- **About 13 MB of disks** on the board: nine 1.44 MB disks or sixteen 800K disks.
- **Plays in any modern browser (HTML5).** The screen streams over a WebSocket, sending only
  the parts that changed. Mouse, keyboard, paste, full screen and an on-screen keyboard for
  phones all work.
- **Real Mac sound in the browser,** from the Mac's own sound hardware: the startup chime,
  alerts and game sounds.
- **Print to PDF.** Pick the ImageWriter in the Chooser, then **File > Print** in any app, and
  the page hands you a PDF.
- **A clock that knows the time,** from your browser or, with no browser open, from the
  internet.
- **Drop in almost any old Mac file:** `.img`, `.dsk`, DiskCopy 4.2 `.image`, `.zip`, `.7z`,
  `.sit` (including StuffIt 5), `.hqx`, `.bin`, `.gz`. Your browser unpacks them.
- **Board controls on the page:** **No disk**, battery level, uptime and why it last started,
  **Restart Mac**, **Restart board** and **Sleep board**.
- **Works anywhere:** on your home Wi‑Fi, or from the board's own hotspot.
- **One-page flasher** for Chrome or Edge, with backup, restore and clone.
- **Extras:** VNC on port 5900, a status display (or tiny live Mac screen) on the OLED, and a
  safe mode.

![Printed from TeachText on the Mac SE](docs/se-printout.png)

| The clock follows your computer | Programs on a System disk |
|---|---|
| ![Control Panel showing the current date and time](docs/clock.png) | ![The Finder](docs/finder.png) |

## What you need

- A **Heltec WiFi LoRa 32 V4** (ESP32-S3R2, 2 MB PSRAM, 16 MB flash) and a USB-C cable that
  carries data
- **Chrome or Edge** on a computer, for flashing
- Your own **Mac ROM** and **disk images**. Apple's software isn't included.

> Flashing Heltec V4 Mac SE replaces Meshtastic on the board. To go back, reflash Meshtastic from
> flasher.meshtastic.org.

## Quick start

### 1. Flash the board

Download [`flasher/Heltec-V4-Mac-SE-Flasher.html`](flasher/Heltec-V4-Mac-SE-Flasher.html) and open it
in Chrome or Edge. The firmware is built into the page. Plug in the board, click **Connect**,
pick it from the list, and click **Flash**. The V4 uses the ESP32-S3's own USB, so it needs no
driver. If it doesn't show up, put it in download mode (hold **PRG**, tap **RST**, let go) and
connect again.

![The flasher, with the backup and clone section](docs/flasher.png)

Prefer the command line? `esptool --chip esp32s3 write-flash 0x0 firmware/Heltec-V4-Mac-SE.bin`.
Updating later keeps your ROM, disks and Wi‑Fi settings.

**Back up or clone.** After **Connect**, **Back up this board** saves the whole 16 MB flash
(firmware, ROM, every disk and the Wi‑Fi settings) as one `.bin` file. **Write backup to this
board** puts it back, or onto a second V4 to make a clone. The file holds your Wi‑Fi password
and your ROM, so keep it private.

### 2. Put it on your Wi‑Fi

The first time, the board makes its own hotspot: **Heltec-V4-MacSE-Setup**, password
**heltecmac**. Join it, open **http://192.168.4.1**, pick your network under **Wi‑Fi**, and
click **Save & restart**. The OLED then shows the board's address. It also answers to
**heltec-macse.local** on most computers.

No Wi‑Fi around? Use the Mac straight from the hotspot at **http://192.168.4.1**. The board
answers your device's "am I online?" check so it stays on the hotspot, and picks the quietest
channel (1, 6 or 11).

### 3. Add a ROM

Under **Mac ROM**, upload your ROM file. The page checks it and tells you what it is.

| ROM | Size | Checksum | Notes |
|---|---|---|---|
| **Mac SE FDHD** | 256 KB | `B306E171` | **Recommended.** Reads 400K, 800K and 1.44 MB disks. |
| Mac SE | 256 KB | `B2E362A8` | Reads 400K and 800K disks. |
| Mac Plus (version 3) | 128 KB | `4D1F8172` | Runs as a Plus with up to 1 MB. |
| Mac 128K / 512K | 64 KB | `28BA61CE` | Runs as a 128K or 512K. |

### 4. Add disks and start the Mac

Under **Disks**, choose a disk image or an archive and click **Add**. If a file holds several
disks, tick the ones you want. Click **Use** next to a disk to start the Mac from it.

![The disk library on the board's web page](docs/disk-library.png)

## Using it

Open `http://<board address>` (or `http://heltec-macse.local`) and click the Mac screen.

- **Mouse:** click and drag on the screen. Any mouse button is the Mac's one button.
- **Keyboard:** **Ctrl** or the **Windows key** is **Command**, **Alt** is **Option**. The
  **⌘ Command** button holds Command for your next key or click, for shortcuts the browser
  keeps for itself.
- **Paste** text straight into the Mac, or use **Type into the Mac** for longer text.
- **Sound** starts at your first click. The **Sound** button turns it off.
- **No disk** takes the disk out and restarts the Mac with an empty drive, like ejecting it.
- **Restart Mac** is the reset switch. **Restart board** restarts the Heltec. **Sleep board**
  turns everything off until you press **PRG**. Each one saves the disk first.
- **Turbo** (under Machine) lets the Mac run flat out instead of at 8 MHz.

One browser at a time can view the Mac. Opening it somewhere else takes over.

**Disks:** **Use**, **No disk**, **Write-protect** and removing the disk in use restart only the
Mac, so Wi‑Fi stays up. **Download** saves a disk with your changes; **Remove** deletes one
(click **Sure?** within 4 seconds).

### Printing to PDF

![MacWrite's Sample Memo printed to a PDF](docs/print-pdf.png)

Open the **Chooser**, pick **ImageWriter** and the printer port, close it, then **File > Print**
as usual. The Mac thinks an Apple ImageWriter is plugged in. When it finishes, a box under the
screen offers **Open PDF** and **Download**. High and Standard quality print as pictures; Draft
prints real, searchable Courier text. Keep the page open while printing.

### Status, battery and sleep

<img src="docs/status.png" alt="The Status panel" width="372" align="right">

The **Status** panel shows the Mac's speed, who's watching, the battery, and how long the board
has been up and why it last started (power on, RST, restart, sleep, crash, watchdog or
brownout). With a LiPo connected, the OLED and the page show its voltage and charge.
<br clear="right">

### Over VNC

Any VNC viewer can connect to `<board address>:5900` with no password. VNC has no sound.

### The board itself

- **OLED:** the address and the Mac's status. Tap **PRG** for a tiny live view of the Mac.
- **Hold PRG for 2 seconds** to restart the Mac.
- **White LED:** a short, dim blink while someone is viewing.
- **Safe mode:** after three crashes in a row, it starts without the Mac so the page still works.

## How it works

- **Core 1** runs the Mac: the Musashi 68000 plus the SE's hardware (video, sound, VIA with
  timers, ADB, SCC, clock chip, floppy), based on the umac emulator. The 68000 runs in 0.5 ms
  slices so ADB and the VIA timers see the right timing.
- **Core 0** runs Wi‑Fi, the web page, the WebSocket stream and VNC.
- **Memory:** the Mac's 1 MB lives in the V4's 2 MB PSRAM. The ROM is read straight from flash.
- **Flash (16 MB):** 2 MB firmware, the ROM, and a 13.4 MB disk library.
- **Printing:** the SCC sends the printer port's bytes to the browser, and `web/imagewriter.js`
  turns ImageWriter commands into 144 dpi pages and a PDF.
- **Your browser** unpacks ZIP, 7-Zip, StuffIt and BinHex before sending disks to the board.

## Limitations

- The Mac's speed depends on the PSRAM, which is slower than the ESP32's own memory. Use
  **Turbo** if things feel slow.
- System 1 to 3 disks don't start on the SE ROM (they didn't on a real SE either). Use System 4
  or later, or the Mac 128K ROM.
- **Add to the disk in use** only copies programs onto 400K MFS disks for now, not HFS ones.
- ImageWriter 2.x waits a few seconds before printing, because it asks for an ImageWriter II's
  ID and the virtual printer doesn't answer.
- One floppy drive; no SCSI, AppleTalk or modem port.
- Not tested on every V4. If something misbehaves, the log from **Watch the board start** in
  the flasher helps.

## Troubleshooting

- **The board isn't in the flasher's list:** try another cable (many only charge), or put it in
  download mode: hold **PRG**, tap **RST**, release **PRG**.
- **The Mac freezes or the page drops off:** check **Up** in the Status panel. "brownout" means
  the power dipped: try another cable or port, or charge the battery.
- **Your device keeps leaving the hotspot:** at home, put the board on your home Wi‑Fi.
- **No sound:** click the Mac screen once and check the **Sound** button says **on**.

## Building from source

Arduino IDE (or arduino-cli) with the **esp32** core 3.x. Open
[`Heltec-Mac/Heltec-Mac.ino`](Heltec-Mac/Heltec-Mac.ino) and choose board
**Heltec WiFi LoRa 32(V4)** with **PSRAM: QSPI PSRAM**, **Flash Size: 16MB** and
**USB CDC On Boot: Enabled**. `partitions.csv` in the sketch folder is the V4 layout. The board
setting turns on the SE build (`heltec_config.h`). The app is bigger than the default 1.3 MB
limit, so with arduino-cli add `--build-property upload.maximum_size=2097152`.

`tools/build_firmware.sh` does all of this and writes `firmware/Heltec-V4-Mac-SE.bin`.

| Folder | What's in it |
|---|---|
| `Heltec-Mac/` | The firmware: emulator glue, web page, WebSocket view, VNC, disk library |
| `Heltec-Mac/src/core/` | The emulator core (umac + Musashi) with the SE's ADB, VIA timers and ROM patches |
| `web/` | The browser-side unpackers and the virtual ImageWriter |
| `flasher/` | The one-page flasher and the script that builds it |
| `host/` | A PC build of the same emulator and web page, for testing |
| `firmware/` | The ready-to-flash images: `Heltec-V4-Mac-SE.bin` (this SE build), plus `Heltec-V3-Mac128k.bin` and `ESP32-Mac128k.bin` (the 128K builds for the V3 and a plain ESP32) |

The PC build runs the same code on a desktop:

```
cd host && V4=1 ./build.sh
./machost-v4 --ram 1024 --rom macse.rom --disk system6.img   # web page at http://localhost:8080, VNC on 5900
```

After changing `web/*.js`, run `python3 tools/embed_js.py`. After changing the firmware,
`python3 flasher/make_flasher.py <esptool-js bundle> firmware/Heltec-V4-Mac-SE.bin --v4` rebuilds
the flasher.

## Credits and licences

- **umac** by Matt Evans (MIT, `licenses/umac-LICENSE.txt`), the compact Mac emulator at the
  heart of this.
- The SE's ADB keyboard and mouse (`src/core/adb.c`) follow **Mini vMac** by Paul C. Pratt
  (GNU GPL v2).
- **Musashi** 68000 emulator by Karl Stenerud (`licenses/Musashi-LICENSE.txt`), with
  **SoftFloat** by John R. Hauser (`licenses/SoftFloat-README.txt`).
- The floppy driver (`src/core/disc.c`, `sonydrv.h`) comes from **Basilisk II** by Christian
  Bauer (GNU GPL v2), so the firmware as a whole is distributed under the GPL v2.
- `web/sit-arsenic.js` ports StuffIt "Arsenic" decompression from **XADMaster** by MacPaw
  (GNU LGPL 2.1, `licenses/XADMaster-LGPL-2.1.txt`).
- **esptool-js** by Espressif (Apache 2.0, `licenses/esptool-js-LICENSE.txt`) powers the flasher.

Apple ROMs and system software are **not** included; use your own copies.
