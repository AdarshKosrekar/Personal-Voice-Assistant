from urllib.parse import quote_from_bytes
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
import pyautogui
import requests
import PyPDF2
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
#import psutil
import speedtest#pip install speedtest-cli
from twilio.rest import Client
import MyAlarm
import urllib.request
import cv2
import numpy as np
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from mainUI import Ui_JarvisUI
from sys import exit #write this only if running in spyder
engine=pyttsx3.init("sapi5")
engine. setProperty("rate", 173)
voices=engine.getProperty('voices')
#print(voices)
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)#For male voice
#engine.setProperty('voice',voices[1].id)#For female voice

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to convert voice into text
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=0.6
        audio=r.listen(source,phrase_time_limit=8)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        speak("Say that again please")
        return "none"
    query=query.lower()
    return query

#to wish
def wish():
    hour=int(datetime.datetime.now().hour)
    tt=time.strftime("%I:%M %p")
    #print(hour)
    if hour>=0 and hour<=12:
        speak(f"Good morning, its {tt}")
    elif hour>=12 and hour<=18:
        speak(f"Good afternoon, its {tt}")
    else:
        speak(f"Good evening, its {tt}")
    #speak("I am Jarvis sir. Please tell me how can I help you")

#to sendmail
def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("youremailid","yourpassword")
    server.sendmail("youremailid",to,content)
    speak("Email has been sent")

#to fetch news
def news():
    #email:woloso3371@brayy.com
    #username:abc
    #password:abc@1234
    #API key=5d573c332b6b4a2aa71c5683d2b6485f
    main_url="http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=83263a48521a48a797182dbc3926e513"
    #main_url="https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=83263a48521a48a797182dbc3926e513"
    main_page=requests.get(main_url).json()
    articles=main_page["articles"]
    head=[]
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)-5):
        #print(f"today's {day[i]} news is:{head[i]}")
        speak(f"Today's {day[i]} news is: {head[i]}")

#to read pdf
def pdf_reader():
    book=open('TheAlchemist.pdf','rb')
    pdfReader=PyPDF2.PdfFileReader(book)
    pages=pdfReader.numPages
    speak(f"Total numbers of pages in this book {pages}")
    speak("Sir please tell the page number I have to read")
    #pg=int(input("Please enter the page number: "))
    pg=takecommand()
    #print(pg)
    #print(type(pg))
    pg=int(pg)
    #print(type(pg))
    page=pdfReader.getPage(pg-1)
    text=page.extractText()
    speak(text)

#for 'how to do mode'
def search_wikihow(query,max_results=10,lang='en'):
    return list(WikiHow.search(query, max_results, lang))

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        self.TaskExecution()

    #to convert voice into text
    def takecommand(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            #r.pause_threshold=1
            audio=r.listen(source,timeout=5)
        try:
            print("Recognizing...")
            query=r.recognize_google(audio,language='en-in')
            print(f"User said: {query}")
        except Exception as e:
            speak("Say that again please")
            return "none"
        query=query.lower()
        return query

    def TaskExecution(self):    
        #if __name__=='__main__':
        wish()
        while True:
            self.query=takecommand()
            #print(query)
            # if 'the time' in self.query:
            #     strTime=datetime.datetime.now().strftime("%H:%M:%S")
            #     speak(f"Sir, the time is {strTime}")
            if 'open notepad' in self.query:
                path="C:\\Windows\\System32\\notepad.exe"
                os.startfile(path)
            elif 'open command prompt' in self.query:
                os.system("start cmd")
            elif 'open camera' in self.query:
                cap=cv2.VideoCapture(0)
                while True:
                    ret, img=cap.read()
                    cv2.imshow('webcam', img)
                    k=cv2.waitKey(50)
                    if k==27:
                        break
                cap.release()
                cv2.destroyAllWindows()
            elif 'play music' in self.query:
                music_dir="G:\\mp3\\Alan Walker Songs"
                songs=os.listdir(music_dir)
                rd=random.choice(songs)
                print(songs)
                #for song in songs:
                #    if song.endswith('.mp3'):
                os.startfile(os.path.join(music_dir,rd))
            elif 'ip address' in self.query:
                ip=get('https://api.ipify.org').text
                speak(f"Your IP address is {ip}")
            elif 'wikipedia' in self.query:
                speak("Searching wikipedia...")
                try:
                    self.query=self.query.replace("wikipedia","")
                    results=wikipedia.summary(self.query,sentences=2)
                    speak("According to wikipedia")
                    speak(results)
                except Exception as e:
                    speak(e)
            # elif 'search' in self.query:
            #     self.query=self.query.replace("search ","")
            #     webbrowser.open(self.query)
            elif 'open youtube' in self.query:
                webbrowser.open("www.youtube.com")
            elif 'open facebook' in self.query:
                webbrowser.open("www.facebook.com")
            elif 'open stack overflow' in self.query:
                webbrowser.open("www.stackoverflow.com")
            elif 'open google' in self.query:
                webbrowser.open("www.google.com")
            elif 'search on google' in self.query:
                speak("What should I search on google")
                cn=takecommand().lower()
                #webbrowser.open(f"{cn}")
                webbrowser.open(f"https://www.google.com/search?q={cn}")
            elif "send message" in self.query:
                speak("Tell your message")
                msg=takecommand()
                kit.sendwhatmsg("+91XXXXXXXXXX",msg,20,48)
                print("Message sent.")
            elif 'play song on youtube' in self.query:
                speak("Which song should I play")
                s=takecommand()
                kit.playonyt(s)
            elif "send email" in self.query:
                try:
                    speak("What should I say?")
                    content=takecommand().lower()
                    to="receiver@gmail.com"
                    sendEmail(to,content)
                    speak("Email has been sent to receiver")
                except Exception as e:
                    print(e)
            elif "no thanks" in self.query or "exit" in self.query:
                speak("Thanks for using me sir, have a good day.")
                sys.exit()
            elif "close notepad" in self.query:
                speak("Okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")
            elif "set alarm" in self.query:
                # nn=int(datetime.datetime.now().hour)
                # if nn==13:
                #     music_dir="G:\\MP3\\Alan Walker Songs"
                #     songs=os.listdir(music_dir)
                #     os.startfile(os.path.join(music_dir,songs[2]))
                speak("Sir please tell me the time to set alarm. For example 'set alarm to 4:15 pm'")
                tt=takecommand()
                #print(tt)      
                tt=tt.replace("set alarm to ","")
                #print(tt)
                tt=tt.replace(".","")
                #print(tt)
                tt=tt.upper()
                #print(tt)
                MyAlarm.alarm(tt)
            elif "joke" in self.query:
                joke=pyjokes.get_joke()
                speak(joke)
            elif "shutdown the system" in self.query:
                os.system("shutdown /s /t 5")
            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")
            elif "switch the window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(3)
                pyautogui.keyUp("alt")
            elif "tell me news" in self.query:
                speak("Please wait sir, fetching latest news")
                news()
            elif "where i am" in self.query or "where we are" in self.query:
                speak("Wait sir,let me check")
                try:
                    import requests
                    res=requests.get('https://ipinfo.io/')
                    data=res.json()
                    #print(data)
                    city=data['city']
                    #print(city)
                    region=data['region']
                    #print(city)
                    country=data['country']
                    #print(country)
                    speak(f"Sir I think we are in {city} city of {region} state")
                    # ipAdd=requests.get('https://api.ipify.org').text
                    # print(ipAdd)
                    # url='https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    # geo_requests=requests.get(url)
                    # geo_data=geo_requests.json()
                    # #print(geo_data)
                    # city=geo_data['city']
                    # print(city)
                    # country=geo_data['country']
                    
                    # print(country)
                    # region=geo_data['region']
                    # print(region)
                    # speak(f"Sir I am not sure,but i think we are in {city} city of {country} country")
                except Exception as e:
                    speak("Sorry sir,Due to network issue I am not able to find where we are.")
                    pass
            elif "take screenshot" in self.query or "take a screenshot" in self.query:
                speak("Sir,please tell me the name for this screenshot file")
                name=takecommand().lower()
                speak("Please sir hold the screen for few seconds,I am taking screenshot")
                time.sleep(3)
                img=pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("I have successfully saved screenshot in main folder")
            elif "read pdf" in self.query:
                pdf_reader()
            elif "hide all files" in self.query or "hide this folder" in self.query or "visible this folder" in self.query:
                speak("Sir please tell me you want to hide this folder or make it visible")
                condition=takecommand().lower()
                if "hide" in condition:
                    os.system("attrib +h /s /d")
                    speak("Sir,all the files in this folder are now hidden")
                elif "visible" in condition:
                    os.system("attrib -h /s /d")
                    speak("Sir,all the files in this folder are now visible")
                elif "leave it" in condition or "leave for now" in condition:
                    speak("Ok sir")
            elif "hello" in self.query or "hey" in self.query:
                speak("Hello Sir, how may I help you")
            elif "how are you" in self.query:
                speak("I am fine sir, what about you")
            elif "also good" in self.query or "fine" in self.query:
                speak("That's great to hear")
            elif "temperature" in self.query:
                import requests
                speak("Please tell place")
                pl=takecommand()
                search=f"temperature in {pl}"
                url=f"https://www.google.com/search?q={search}"
                r= requests.get(url)
                data=BeautifulSoup(r.text,"html.parser")
                temp=data.find("div",class_="BNeawe").text
                speak(f"Current {search} is {temp}")         
            elif "activate how to do mode" in self.query:
                from pywikihow import search_wikihow
                speak("How to do mode is activated, Please tell me what you want to know")
                how=takecommand()
                max_results=1
                how_to=search_wikihow(how,max_results)
                #print(how_to)
                assert len(how_to)==1
                #how_to[0].print()
                speak(how_to[0].summary)
                speak("How to do mode deactivated")
            elif "internet speed" in self.query:
                speak("Wait Sir, fetching internet speed")
                st=speedtest.Speedtest()
                dl=st.download()/1000000
                dl=round(dl,2)
                up=st.upload()/1000000
                up=round(up,2)
                speak(f"Sir we have {dl} Mbps download speed and {up} Mbps upload speed")
                #speak(f"Sir we have {dl} bit per second download speed and {up} bit per second upload speed")
                # try:
                #     os.system('cmd /k "speedtest"')
                # except:
                #     speak("There is no internet connection")
            elif "volume up" in self.query:
                pyautogui.press("volumeup")
            elif "volume down" in self.query:
                pyautogui.press("volumedown")
            elif "volume mute" in self.query or "mute" in self.query:
                pyautogui.press("volumemute")
            elif "open mobile camera" in self.query:
                URL="http://25.121.114.9:8080/shot.jpg"
                while True:
                    img_arr=np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                    img=cv2.imdecode(img_arr,-1)
                    cv2.imshow('IPWebcam',img)
                    q=cv2.waitKey(50)
                    if q==27:
                        break;
                cv2.destroyAllWindows()
            elif "weather" in self.query:
                import requests
                api_key = "cd90bf33b7a8aff915a0c660362056b1"
                base_url = "http://api.openweathermap.org/data/2.5/weather?"
                speak("Speak City name")
                city_name = takecommand()
                #print("City name",city_name)
                complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                #print(complete_url)
                response = requests.get(complete_url)
                x = response.json()
                if x["cod"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_pressure = y["pressure"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    #print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
                    speak("Temperature (in kelvin unit)="+str(current_temperature)+"\nAtmospheric pressure (in hPa unit)="+str(current_pressure)+"\nHumidity (in percentage)="+str(current_humidiy) +"\nDescription="+str(weather_description))
                else:
                    speak(" City Not Found ")

            # elif "how much power left" in query or "battery" in query:
            #     battery=psutil.sensors_battery()
            #     percentage=battery.percent
            #     speak(f"sir our system have {percentage} percent battery")

startExecution=MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_JarvisUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
    def startTask(self):
        self.ui.movie=QtGui.QMovie("7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("T8bahf.gif")
        self.ui.label_1.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer=QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
    def showTime(self):
        current_time=QTime.currentTime()
        current_date=QDate.currentDate()
        label_time=current_time.toString("hh:mm:ss")
        label_date=current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)
app=QApplication(sys.argv)
jarvis=Main()
jarvis.show()
exit(app.exec_())