// Which board this firmware is for.
//
//  * Heltec WiFi LoRa 32 V3 (8 MB flash, no PSRAM): Heltec-Mac, a Mac 128K / Plus with 128 KB.
//  * Heltec WiFi LoRa 32 V4 (16 MB flash, 2 MB PSRAM): Heltec V4 Mac SE, a 1 MB Mac SE (or Plus),
//    using the V4's PSRAM for the Mac's memory. Picked automatically when you compile for
//    "Heltec WiFi LoRa 32(V4)". This repo's partitions.csv is the V4's 16 MB layout.
#pragma once
#if defined(ARDUINO) && defined(__has_include)
#if __has_include("sdkconfig.h")
#include "sdkconfig.h"
#endif
#endif

#if defined(WIFI_LORA_32_V4) && !defined(HELTEC_V4)
#define HELTEC_V4
#endif
//  * A plain ESP32 dev board (NodeMCU-32S / ESP32-DevKitC, ESP32-WROOM, 4 MB flash, no PSRAM):
//    ESP32 Mac 128K, the same 128K Mac as the V3. Picked automatically when you compile for
//    "ESP32 Dev Module"; use partitions-esp32.csv as partitions.csv (see README).
#if defined(CONFIG_IDF_TARGET_ESP32) && !defined(BOARD_ESP32)
#define BOARD_ESP32
#endif
// A plain ESP32 never has one free 128 KB piece of memory, so its Mac's RAM is two 64 KB
// banks (see machw.h). The PC test build can try it with -DUMAC_RAM_SPLIT.
#if defined(BOARD_ESP32) && !defined(UMAC_RAM_SPLIT)
#define UMAC_RAM_SPLIT
#endif

#ifdef HELTEC_V4
#define BOARD_NAME      "Heltec V4 Mac SE"
#define BOARD_HEADER    "HELTEC V4 MAC SE"
#define BOARD_AP_SSID   "Heltec-V4-MacSE-Setup"
#define BOARD_HOSTNAME  "heltec-macse"
#define BOARD_OLED      " V4 MAC SE"
#define BOARD_MODEL     "Heltec WiFi LoRa 32 V4"
#elif defined(BOARD_ESP32)
#define BOARD_NAME      "ESP32 Mac 128K"
#define BOARD_HEADER    "ESP32 MAC 128K"
#define BOARD_AP_SSID   "ESP32-Mac-Setup"
#define BOARD_HOSTNAME  "esp32-mac"
#define BOARD_OLED      " ESP32 MAC"
#define BOARD_MODEL     "ESP32 dev board (NodeMCU)"
#else
#define BOARD_NAME      "Heltec V3 Mac 128K"
#define BOARD_HEADER    "HELTEC V3 MAC 128K"
#define BOARD_AP_SSID   "Heltec-V3-Mac-Setup"
#define BOARD_HOSTNAME  "heltec-mac"
#define BOARD_OLED      " V3 MAC"
#define BOARD_MODEL     "Heltec WiFi LoRa 32 V3"
#endif
