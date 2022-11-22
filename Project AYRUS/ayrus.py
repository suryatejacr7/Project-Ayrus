import pyttsx3 #for text to speech
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os #for playing songs
import smtplib
import playsound
from gtts import gTTS

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak(" Hello i'm Ayrus, at your service. what do you need sir?")
    print("What i can do")
    print("calculate your  BMI")
    print("send Email 📧")
    print("convert weigh to KG's or Pound's")
    print("leave you alone 😛")
    print("open youtube or google or even your personal pics.😈")
    print("call you Senpai or Sensai or even sama or V's")
    print("can tell time")


def takeCommand():
    #it takes mic input from me and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r .pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        print(e) #prints excedption basically


        print("Say that again please.....")
        return "NONE" 
    return query           

def get_audio(): 
    try:
         height=int(1.73*2)
         weight=int(70)
         dog=int(weight/height)
         print(dog)
         speak(dog)
    except Exception as e:
        print(e)
       
def convert_weight():
    weight=float(input("Enter your weight: "))
    unit=input("convert to KG's or to Pounds?: ")   
    if unit.upper== 'KG' or 'kg':
        convert = weight / 0.45
        print(convert)
        speak(convert)
    else:
        convert = weight * 0.45
        print(convert)
        speak(convert)
"""
def person_details_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        said=""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print(e)

    return said
text = person_details_voice()

if "surya" in text:
     print("Surya is a lord. The greatest of the greatest. The one True Lord Surya-Sama 👑👑👑")
     speak("Surya is a lord. The greatest of the greatest. The one True Lord Surya-Sama")
elif "what is your name" in text:
    speak("My name is Surya")
"""

def call_me():
    name=input("Enter the name: ")
    you_want=input("what do you want to add?: ")
    
    while True:
        if you_want =='sensei':
            print(name + ' '+ you_want)
            speak(name + you_want)
        elif you_want=='senpai':
            print(name +' ' +you_want)
            speak("Surya Senpai")
            return call_me()
        elif you_want =='sama':
            print(name + ' ' + you_want)
            speak('Surya sama')
            return call_me()        
        elif name =='surya teja':
            print("surya is varshini's boyfriend 😍❤️❤️❤️")
            speak("surya is varshinee's boyfriend")
            return call_me()
        elif you_want=='testing':
            print("Testing passed!")
            speak('Testing passed!')
            return call_me()
    
        elif name=='ravi':
            print(" Ravi is a world famous noob 😂😂🤣🤣")
            speak(" Ravi is a world famous noob")
            return call_me()
        elif name=='sushanth':
            print("Sushanth is a CEO of chithi eluka industries 🐁🐀🐭 ")
            speak("Sushanth is a CEO of chithi eluka industries")    
            return call_me()
        elif name=="mahesh":
            print('Sir Mahesh is a CEO of BMR private ltd 🚀🚁🛩️✈️🚗🚍🏢🏦🏦')
            speak('Sir Mahesh is a CEO of BMR private limited')
            return call_me()
        elif name=='shiva':
            print("shiva is a pussy 😂😂🤣🤣")
            speak('shiva is a pussy. hahahaha')
            return call_me()
        elif name=='surya':
            print("Surya is a lord. The greatest of the greatest. The one True Lord Surya-Sama 👑👑👑")
            speak("Surya is a lord. The greatest of the greatest. The one True Lord Surya-Sama")
            return call_me()
        elif name=='varshini':
            print("Varshini is the Queen of the universe. she is a lovely and the sweetest person ever born")
            speak("Varshinee is the Queen of the universe. she is a lovely and the sweetest person ever born")
            return call_me()
        elif name=='sharath babu':
            print("sharath babu is a papu of my family and greatest of the greatest noob ever born.PS: World's Best noob brother")
            speak("sharath babu is a pappu of my family and greatest of the greatest noob ever born.PS world's best noob brother")
            return call_me()
        
        elif name=='manasa':
            print("manasa is a highly qualified noob and most sophisticated loser ever lived on this planet.  Her most common dialogue: Over action cheyaku Oa 😒🤦🏻‍♀️🤦🏻‍♀️")
            speak("manasa is a highly qualified noob and most sophisticated loser ever lived on this planet. Her most common dialogue: Over action cheyaku")
            return call_me()
        elif name=='exit':
            exit()
        else:
            print("you got jebaited")
            speak('you got jebaited')
            return call_me()
def byebye():
    print("see you again lone soul, hahaha")
    speak("see you again lone soul, hahaha")
    exit()



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    file = open("D:\hey hey hey.txt","r")
    server.login('suryatejacr7@gmail.com', file.read())
    server.sendmail('suryatejacr7@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishme()
    while 1:
        
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'database' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching database...')
            query = query.replace("database", "")
            
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Database")
            print(results)
            speak(results)
        
        
        elif 'open google' in query:
            webbrowser.open("google.com") 

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")  

        
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0])) #can install random module and play random song instead of this    
         
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    #can add with dateeCCCC c
            speak(f"Sir, the time is {strTime}")


        elif 'open vs code' in query:
            codePath = "C:\\Program Files\\Microsoft VS Code"
            os.startfile(codePath)     

        elif 'open my pics' in query:
            picspath = "D:\\picsu & videosu\\navi"
            os.startfile(picspath)
        
        elif 'calculate body mass index' in query:
            try:
                speak("Give height and weight details")
                #content_1=get_audio(height,weight)
                get_audio()
            except Exception as e:
                speak("sorry boss there is an error")      

        elif 'exit now' in query:
            print("this is exiting")
            byebye()
        
        elif 'convert my weight' in query:
            speak("Please enter your weight details")
            convert_weight()

        elif 'person details' in query:
            speak("please enter the name: ")
            call_me()
            
        elif 'email to dolphin' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "varshinidasoju23@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                speak("sorry boss couldn't send this email, try again")    