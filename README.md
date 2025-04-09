# 📸 SnapChat Automation Script

A Python-based automation tool designed to send snaps on Snapchat web version by simulating mouse interactions. Easily set and save button positions, and automate sending snaps with custom timing and configuration.

---

## 🚀 Features

- 🔧 **Interactive Position Setup**  
  Manually set on-screen button positions.

- 💾 **Save & Load Button Positions**  
  Save positions to a JSON file for future sessions.

- ⚙️ **Configurable Parameters**  
  Set the number of snaps, interval between snaps, and delay between actions.

- 🧵 **Threaded Execution**  
  Automation runs smoothly in a separate thread.

- ❌ **Exit Anytime**  
  Press `ESC` to stop the script immediately.

---

## 📦 Prerequisites

Ensure you have the following installed before running the script:

- Python **3.8+**
- Required Python libraries:
  - `pyautogui`
  - `keyboard`

Install dependencies with:

```bash
pip install pyautogui keyboard
```

---

## 🛠️ How to Use

### 1. 📥 Clone the Repository

```bash
git clone https://github.com/ghosthasgone/SnapScoreBooster.git
cd SnapScoreBooster
```

---

### 2. 🖱️ Set Up Button Positions

Run the script to interactively define button positions:

```bash
python main.py
```

- The program will prompt you to hover over specific buttons (e.g., **Take Picture**, **Send To**, etc.).
- Press `ENTER` while the IDE or terminal is in focus to capture each position.
- All positions will be saved to `ButtonPosition.json` for future use.

---

### 3. 🔁 Load Existing Positions

If you have already saved button positions, you can load them instead:

```bash
python main.py
```

- When prompted, enter `n` to load from `ButtonPosition.json`.
- Note, any time the location of the camera changes, you'll need to redo the positions.

---

### 4. ⚙️ Configure Snap-Sending Parameters

The program will ask for:

- **Number of Snaps** – Total snaps to send *(default: 10)*  
- **Interval** – Time between snaps in seconds *(default: 1)*  
- **Delay** – Time between actions in seconds *(default: 0.5)*  
- **Recipient Username** – Username of the person you want to send snaps to
- **IMPORTANT** - It is possible (but not advised) to go below the recommended values.

---

### 5. ▶️ Start the Automation

After configuration, the script will begin automating the snap-sending process.  
You can monitor the progress in your terminal.

---

### 6. 🛑 Exit Anytime

Press the `ESC` key during execution to immediately stop the program.

---

## 📁 File Structure

```
SnapBoost/
│
├── main.py               # Main automation script
├── ButtonPosition.json   # Saved button positions
└── README.md             # You're here!
```

---

## 📬 Notes

- This tool is intended for **educational and personal use** only.
- Use responsibly and respect Snapchat’s terms of service.

---

## 📜 License

MIT License © GhostHasGone
