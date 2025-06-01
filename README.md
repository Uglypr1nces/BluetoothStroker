# BluetoothStroker

**BluetoothStroker** is a project that turns a Raspberry Pi Zero W into a USB HID device. Plug the Pi into a computer via USB, connect to it over Bluetooth, and send keystrokes remotely.

---

## 🧠 Project Splitting

**USB HID GADGET SETUP** – _uglypricess_  
→ Written in **C** to emulate a USB keyboard using the Linux HID gadget system.

**BLUETOOTH LISTENER** – _terry_  
→ Written in **Python** to manage Bluetooth connections and parse commands.

**OTHER SCRIPTS** – _shared_  
→ Optional setup and management scripts (bash, systemd, etc.).

---

## 📁 File Structure

BluetoothStroker/
├── bluetooth/     # Handles Bluetooth communication and command parsing
├── usb_em/        # USB HID emulation logic 
│   └── Makefile   # Build script for C code
├── scripts/       # Shell scripts for setup and runtime management
└── README.md      # Project documentation


---

## ✨ Features

- Emulates a USB keyboard when plugged into a host computer
- Accepts keystroke commands over Bluetooth
- Simple Python interface for sending keystrokes from any Bluetooth-enabled device

---

## 📦 Requirements

- Raspberry Pi Zero W (or similar SBC with USB OTG)
- Micro USB cable
- Bluetooth-enabled client device (e.g., phone or laptop)
- Linux OS with `g_hid` module (e.g., Raspberry Pi OS Lite)

---

## 🚀 Usage

1. Plug the Raspberry Pi into a computer via USB.
2. Connect to the Pi over Bluetooth (e.g., via mobile terminal app or custom client).
3. Send keystroke commands — they will be typed on the host computer as if from a physical keyboard.

---

## ⚠️ Disclaimer

> This tool is intended for educational and ethical use only.  
> Use **only** on systems you own or have explicit permission to interact with.

---

## 🪪 License

MIT License
