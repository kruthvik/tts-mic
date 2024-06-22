from tkinter import messagebox, simpledialog
from pyautogui import press
from keyboard import add_hotkey, wait
from autocorrect import Speller
from yaml import safe_load
from tts import TTS

# loads config.yaml file to get settings
config = safe_load(open("config.yaml"))

DEFAULT_TEXT = "# check README.md for info on config\nvoice: matthew\npress: altright\nhotkey: ctrl+space\nautocorrect: false\npath: main.wav"

# checks if config.yaml file exists and contains required settings
if (config is None or "voice" not in config or "press" not in config or "hotkey" not in config or "path" not in config or "autocorrect" not in config):
    # if not, displays an error message and asks user if they want to generate a default config.yaml
    cont = messagebox.askquestion(title="Configuration Error", message="Invalid config.yaml file. Check README.md for info on config. Would you like to generate a default config.yaml?")

    if cont == "yes":
        with open("config.yaml", "w") as f:
            f.write(DEFAULT_TEXT)
        messagebox.showinfo(title="Default Config", message="Default config.yaml generated successfully. Please modify it according to your needs.")
        
    exit()
    
# gets voice, press key, and hotkey from config.yaml

voice = config["voice"].title()
press_key = config["press"]
hotkey = config["hotkey"]
autocorrect = config['autocorrect']
path = config['path']

# creates an instance of speller for autocorrect
spell = Speller()

def text_to_speech(text):
    # generates tts audio file and presses the specified press key
    data = TTS(text, voice)
    
    with open(path, "+wb") as file:
        file.write(data)

    press(press_key)

def runTTS():
    try:
        text = simpledialog.askstring(title="TTS",
                                      prompt="Enter: ")
        if (text != ""):
            if (autocorrect):
                text = spell(text)

            text_to_speech(text)
    except Exception as e:
        messagebox.showerror(title="Error", message="An error occurred while trying to convert the text")
        
# adds a hotkey to runTTS function when the specified hotkey is pressed
add_hotkey(hotkey, runTTS)

wait()