import os
import translang as tl
n = 1
while (n == 1) :
    print("Choose from the given option")
    print("===============================================")
    print(" ENGLISH TO ANY LANGUAGE")
    print("===============================================")
    print("1. GENERATE LANGUAGES THAT YOU CAN TRANSLATE TO")
    print("2. DISPLAY ALL THE LANGUAGES")
    print("3. CONVERT ANY THING IN ENGLISH TO OUR SELECTED LANGUAGE")
    print("4. AUDIO OF THE ORIGINAL LANGUAGE")
    print("5. AUDIO OF THE TRANSLATED LANGUAGE")
    print("6. Exit")
    print("===============================================")
    ch = int(input("enter your choice"))
    if(ch == 1) :
        os.system('cls')
        tl.displanguages()
    if(ch==2) :
        import subprocess
        subprocess.run(["python", "popupmenuwin.py"])
    if(ch == 3):
        tl.engtoany()
    if(ch == 4) :
        tl.texttoaudio()
    if(ch == 5) :
        tl.texttoaudiotl()
    if(ch == 6) :
        n = 0
    
        
        
