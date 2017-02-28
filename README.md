# Ableton Export Bot 
A GUI automation tool to export an Ableton Live set with the send effects printed to each stem.

This quick script will save you manually soloing and exporting each track in the entire session, which usually can be quite time consuming.

It's probably the least optimal solution to perform this, at least until Ableton implements the functionality into the application. Or provides an API that allows access to exporting functions.

## Installation
The bot uses a GUI automation library called [PyAutoGUI](https://github.com/asweigart/pyautogui) to manipulate the computer mouse and keyboard. PyAutoGUI also requires the installation of pyobjc-core and pyobjc (in that order). More information installation for PyAutoGUI can be found [here](https://github.com/asweigart/pyautogui).

1. Install pyobjc-core: `pip install pyobjc-core`
2. Install pyobjc: `pip install pyobjc`
3. Install pyautogui: `pip install pyautogui`
4. Clone or download repository: `git clone https://github.com/hankijord/ableton-export-bot.git`

## Usage
1. Solo the all tracks you wish to export in Ableton
2. Select the range of time on the master track, and ensure your export settings are as you wish
3. Run the export bot:
```python
python main.py
```

You will then be required to type the name of your project (for file naming). After this point it is essential that you do not touch the mouse & keyboard until the program finishes running.
The tool is designed for you to start, grab lunch, then come back to your desktop full of sparkly stems.

This [video](https://www.youtube.com/watch?v=w8e5fUh5dSM) gives you a demo of how the tool runs.
