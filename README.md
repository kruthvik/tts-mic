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



# INSTRUCTIONS FOR SETUP (.exe)
1. Download Soundux from the link above
2. Download the .exe file after extracting the base folder.
3. Run the file and allow it to create a config.yaml file.
4. Change config.yaml with what you want according to its instructions. (backup always avaliable here)
5. Set the directory of the project as a Soundux tab and create a hotkey for it
6. Put the hotkey in the config.yaml file





# INSTRUCTIONS FOR SETUP (.py)
1. Extract folder
2. Enter pip install -r requirements.txt
3. Run py main.py
