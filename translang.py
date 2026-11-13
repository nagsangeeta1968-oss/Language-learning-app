
def displanguages() :
    from googletrans import Translator, constants
    from pprint import pprint

    import pandas as pd

    # init the Google API translator
    translator = Translator()

    # detect a language
    detection = translator.detect("नमस्ते दुनिया")
    print("Language code:", detection.lang)
    print("Confidence:", detection.confidence)
    
    print("Language:", constants.LANGUAGES[detection.lang])
    
    # print all available languages
    print("Total supported languages:", len(constants.LANGUAGES))
    print("Languages:")
    tlanguages = constants.LANGUAGES
    n = len(tlanguages)
    print(type(tlanguages))
    print(n)
    lcode = []
    llanguage = []
    for key,value in tlanguages.items() :
        lcode.append(key)
        llanguage.append(value)

    df = pd.DataFrame(list(zip(lcode, llanguage)),columns =['Language Code', 'Language Name'])
    df.to_csv("Languages.csv", index = False)


def engtoany() :
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
    print(translator)

    msrc = input("Enter the Text to be translated")
    print(msrc)

    # translate a spanish text to arabic for instance
    translation = translator.translate(msrc, src = "en", dest= mdest)
    
    
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
    
    d = {"sourcecode":["en"],
         "destinationcode":[mdest],
         "SourceText":[translation.origin],
         "DestinationText":[translation.text]}
    print(d)
    newdf = pd.DataFrame(d)
    print(newdf)
    newdf.to_csv("translatedlanguage.csv", index = False)

def texttoaudio() :
    from gtts import gTTS
  
    # This module is imported so that we can 
    # play the converted audio
    import os
    import pandas as pd
  
    # The text that you want to convert to audio
    df1 = pd.read_csv('translatedlanguage.csv')
    mytext = df1.iloc[0,2]
    
    #mytext = 'Welcome to geeksforgeeks!'
  
    # Language in which you want to convert
    language = df1.iloc[0,0]
    
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=True)
  
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

def texttoaudiotl() :
    from gtts import gTTS
  
    # This module is imported so that we can 
    # play the converted audio
    import os
    import pandas as pd
  
    # The text that you want to convert to audio
    df1 = pd.read_csv('translatedlanguage.csv')
    mytext = df1.iloc[0,3]
    
    #mytext = 'Welcome to geeksforgeeks!'
  
    # Language in which you want to convert
    language = df1.iloc[0,1]
    
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=True)
  
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
