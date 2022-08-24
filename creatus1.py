from logging import exception
import pyttsx3 #pip install text data into speech using Python
import datetime
import speech_recognition as sr #speech recognition
import smtplib
from secrets import senderemail, epwd, to
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit

engine = pyttsx3.init() #calls initial function of library (pyttsx3)
train = pyttsx3.init()
train.say("Welcome this is Prince Reshav'S first project")
train.runAndWait()
engine.say("I am Creatus. I was designed by Seraphic Nerv")
#engine.say("This is just the begining, you'll be shocked")
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

#while True:
audio = input("Enter the text to convert it into speech\n")
speak(audio)
    
'''def takeCommandHindi():
		
	r = sr.Recognizer()
	with sr.Microphone() as source:
		
		# seconds of non-speaking audio before
		# a phrase is considered complete
		print('Listening')
		r.pause_threshold = 0.7
		audio = r.listen(source)
		try:
			print("Recognizing")
			Query = r.recognize_google(audio, language='hi-In')
			
			# for listening the command in indian english
			print("the query is printed='", Query, "'")
		
		# handling the exception, so that assistant can
		# ask for telling again the command
		except Exception as e:
			print(e)
			print("Say that again sir")
			return "None"
		return Query



# Driver Code
		
# call the function
takeCommandHindi()
  '''  
def getvoices(voice):
    voices=engine.getProperty('voices')
    if voice == 1:
        engine.setProperty('voice',voices[0].id)
        speak ("Hello I am CREATUS")
        
    if voice == 2:
        engine.setProperty('voice',voices[1].id)
        speak ("Hello I am ZAMANTA")
    
    
#voice= int(input("Press 1 for David\nPress 2 for Zira\n"))
def quit():
    speak("Signing Off Good Bye")
  


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The Date is :")
    speak(date)
    speak(month)
    speak(year)



def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The Current Time is:")
    speak(Time)
   


def greetings():
    hour = datetime.datetime.now().hour
    if hour>=6 and hour <12:
        speak("Good Morning Sir!")
    elif hour >=12 and hour <18:
        speak("Good Afternoon sir!")
    elif hour >=18 and hour <24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night.")
        
def wishme():
    speak("Welcome Back")
    #getvoices(voice)
    date()
    time()
    greetings()
    speak("Creatus at your service")
    #date()
    #time()
#wishme()
'''def takeCommandCMD():
    query = input("please tell me how may i help you?\n")
    return query
'''
def takeCommandMic():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio= r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio , language = "en-IN")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(receiver, subject, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()#transfer layer security
    server.login(senderemail, epwd)
    email = EmailMessage()
    email['From']=senderemail
    email['To']=receiver
    email['Subject']=subject
    email.set_content(content)
    server.send_message(email) 
    #server.sendmail(senderemail, to, content)
    server.close()
    
def sendwhatsaapmsg(phone_no, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')
    
def searchgoogle():
    speak('What should I search for?')
    search= takeCommandMic()
    wb.open('https://www.google.com/search?q='+search)

if __name__ == "__main__":
    getvoices(2) #1 for Creatus & 2 for Zamanta
    wishme()
    while True:
        query= takeCommandMic().lower()
        if 'time' in query:
            time()
            
        elif 'date' in query:
            date()
                
        elif 'email' in query:
            email_list={
                'prince':'prince.reshav.5555@gmail.com'
            }
            try:
                speak("To whom you want to send the mail")
                name=takeCommandMic()
                receiver=email_list[name]
                speak("What is the subject of mail")
                subject=takeCommandMic()
                speak('What should I say')
                content = takeCommandMic()
                sendEmail(receiver, subject, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Unable to send the email")
                
        elif 'message' in query:
            user_name={
                'light' :'+91 6307 390 962'
            }
            
            try:
                speak("To whom you want to send the whatsaap message")
                name=takeCommandMic()
                phone_no=user_name[name]
                speak("What is the message")
                message=takeCommandMic()
                sendwhatsaapmsg(phone_no, message)
                speak("Message has been sent")
            except Exception as e:
                print(e)
                speak("Unable to send the message")
            
        elif 'wikipedia' in query:
            speak('searching on wikipedia....')
            query = query.replace("wikipedia", "")
            result=wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)
            
        elif 'search' in query:
            searchgoogle()
            
        elif 'youtube' in query:
            speak("What should I search on youtube?")
            topic=takeCommandMic()
            pywhatkit.playonyt(topic)
                
        #elif offline in query:
        #   quit()