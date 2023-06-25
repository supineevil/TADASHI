import speech_recognition as sr
import pyttsx3
import webbrowser as wb
import datetime
import os
import wikipedia
import easygui
import smtplib

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('rate',140)
engine.setProperty('voice',voices[1].id)


def say(text):
    engine.say(text)
    engine.runAndWait()

def wish():
        hr = int(datetime.datetime.now().hour)
        if hr >= 0 and hr <=12:
            say("It's such a lovely morning today, good morning sir!")
        elif hr > 12 and hr <18:
            say("good afternoon sir!")
        else:
            say("good evening sir!")
        say("Hello I am TADASHI from earth-6 one 6 , your personal AI assistant . how may i help you sir ?")

def sendmail(to,content):
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('raunak_g.it2020@msit.edu.in','PASSWORD')
        server.sendmail('raunak_g.it2020@msit.edu.in',to,content)
        server.close()

def listen():
    print("Listening.... ")    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Processing voice...")
        r.pause_threshold=1
        audio=r.listen(source)    
        try:
            print("Recognising...")
            query=r.recognize_google(audio,language='en-in')
            print(f"user said: {query}\n")
        except Exception as e:
            print("say that again pls......")
            return "None"
        return query
        
if __name__=='__main__':
    wish()
    while True: 
        query= listen().lower()
        
        if 'stop' in query:
            say('I will see you soon sir!')
            exit()
        elif 'shutdown'in query:
                say("Are you sure you want to shutdown your pc?")
                shut= listen().lower()
                if 'yes' in shut:
                    os.system("shutdown /s /t 1")
                else:
                    exit()
        elif 'open' in query:
            sites=[["youtube","http://www.youtube.com"],["google","http://www.google.com"],["leetcode","http://leetcode.com"]]
            for site in sites:
                if f"open {site[0]}" in query.lower():
                    say(f"Opening {site[0]} sir")
                    wb.open(site[1])
        elif 'the time' in query:
            hr=str(datetime.datetime.now().hour)
            mi=str(datetime.datetime.now().minute)
            second=str(datetime.datetime.now().second)
            temp="am"
            if(datetime.datetime.now().hour > 12 ):
                temp="pm"
                hr=str(datetime.datetime.now().hour-12)
            say(f"The time is {hr} hour {mi} minute {second} second {temp}")
        elif 'shutdown'in query:
                say("Are you sure you want to shutdown your pc?")
                shut= say.listen().lower()
                if 'yes' in shut:
                    os.system("shutdown /s /t 1")
                else:
                    exit()    
        elif 'wikipedia' in query:
                say("searching wikipedia....")
                query= query.replace("wikipedia","")
                results=wikipedia.summary(query,sentences=2)
                say("According to my search results")
                print(results)
                say(results)
                say("that's all in brief ,sir!")    
        elif 'open file' in query or 'open explorer' in query or 'open database' in query:
                file = easygui.fileopenbox()
        elif 'send email' in query:
            #Add names in mailbox
            mailbox={"mom":"rubybhowmickghosh@gmail.com",
            "rohit":"sharma2007rohit@gmail.com",
            "aastha":"aasthasingh111222333@gmail.com"}
            say("To whom should i send the email?")
            name_recipients = listen().lower()
            if name_recipients in mailbox.keys():
                try:
                    say("what should i say?")
                    msg=listen()
                    to=mailbox[name_recipients]
                    print(f"confirm to send mail to : {to} ")
                    say(f"confirm to send mail to : {to} ")
                    ch= say().lower()
                    if 'yes' in ch:
                        sendmail(to,msg)
                        say("Email successfully sent")
                    else :
                        say("action terminated")
                except Exception as e:
                    print(e)
                    say("Something went wrong")
            else:
                say("No such name in mailbox")
    