from googletrans import Translator, constants
from pprint import pprint

# init the Google API translator
translator = Translator()

msrc = input("Enter the Text to be translated")

# translate a spanish text to arabic for instance
translation = translator.translate(msrc, src = "en", dest="de")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
