from gtts import gTTS
import os

def convert(text):
	global STATICFILES_DIRS
	myobj = gTTS(text=text, lang='en', slow=False)
	myobj.save("tts.mp3")