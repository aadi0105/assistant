import os
import pyttsx3
pyttsx3.speak("write which program you want to run")

while True:
        x=input()
        if "firefox" in x:
            pyttsx3.speak("hey aaditya i am opening firefox")
            os.system("firefox")
            

        elif "google" in x or "chrome" in x:
            pyttsx3.speak("hey aaditya i am opening google chrome")
            os.system("google-chrome")
            
 
        elif "obs" in x or "obs studio" in x:
            pyttsx3.speak("hey aaditya i am opening o b s studio")
            os.system("obs-studio")
            
        elif  "vs code" in x:
            pyttsx3.speak("hey aaditya i am opening  v s code")
            os.system("code")
            
        elif "youtube" in x:
            pyttsx3.speak("hey aaditya i am opening  youtube")
            os.system("google-chrome www.youtube.com")
            
        elif "jupyter" in x or "jupyter notebook" in x:
            pyttsx3.speak("hey aaditya i am opening  jupiter notebook")
            os.system("jupyter notebook")       
              
        elif "github" in x or "Github" in x:
            pyttsx3.speak("hey aaditya i am opening  github dot com")
            os.system("google-chrome www.github.com")       
                
        else:
            pyttsx3.speak("do not support")

   
