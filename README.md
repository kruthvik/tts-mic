# tts-mic
A simple app that allows you to use text-to-speech while using your microphone (requires Soundux)
[https://soundux.rocks/](url)

src folder contains python files and a requirements.txt if you don't want to use the .exe file

# SETUP FOR config.yaml
```
voice: matthew
press: altright
hotkey: ctrl+space
autocorrect: false
```
- Choose avaliable voices from [https://lazypy.ro/tts/?voice=Russell&service=StreamElements&text=asdf&lang=English&g=A](url) and type the name into voice.
- Check [https://wingware.com/doc/custom/key-names](url) for additional info on the key names.
- Choose a key (**THIS WILL BE PRESSED FOR THE SOUNDUX SOUNDBOARD TO WORK**) for press.
- Choose a hotkey which will open up the messagebox to enter text.
- Change autocorrect to true if you want your message to be autocorrected before enter

1. DOWNLOAD SOUNDUX FROM THE LINK ABOVE
2. SET THE FOLDER OF THE DOWNLOAD AS A SOUNDUX TAB
3. RUN THE PROGRAM AND WAIT FOR IT TO CREATE A MAIN.WAV
4. REFRESH AND SET A KEYBIND WHICH YOU WANT TO PRESS FOR THE SOUND TO BE PLAYED
5. CHANGE THE config.yaml FILE WITH THE KEYBIND YOU CHOSE


# INSTRUCTIONS FOR SETUP (.exe)
**EXE COMING SOON**


# INSTRUCTIONS FOR SETUP (.py)
1. Extract folder
2. Enter pip install -r requirements.txt
3. Run py main.py
