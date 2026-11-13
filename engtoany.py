from googletrans import Translator, constants
from pprint import pprint
import pandas as pd

df1 = pd.read_csv('selectedlanguage.csv')
msellang = df1.iloc[0,0]
print(msellang)

df2 = pd.read_csv('Languages.csv')
mdf = df2[df2['Language Name'] == msellang]
mdest = mdf.iloc[0,0]
print(mdest)

# init the Google API translator
translator = Translator()

msrc = input("Enter the Text to be translated")

# translate a spanish text to arabic for instance
translation = translator.translate(msrc, src = "en", dest= mdest)
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os
  
# The text that you want to convert to audio
mytext = msrc
  
# Language in which you want to convert
language = mdest
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")
  
# Playing the converted file
os.system("welcome.mp3")

# import required module
from playsound import playsound
 
# for playing note.wav file
playsound('/path/note.wav')
print('playing sound using  playsound')

