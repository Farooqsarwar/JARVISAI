import datetime
import time
from email.message import EmailMessage
import pyautogui
import pyttsx3
import speech_recognition as sr
import smtplib
import webbrowser as wb
import requests
from newsapi import NewsApiClient
import openai
import os

import psutil
senderemail = 'xyz@gmail.com'
epwd = ''

engine = pyttsx3.init()
aiapikey = 'your  key'


class jarvis:
    chatStr = ""

    def speak(self, audio):
        engine.say(audio)
        engine.runAndWait()

    def getvoices(self):
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)

    def time(self):
        Time = datetime.datetime.now().strftime("%I:%M:%S")
        self.speak("the current time is")
        self.speak(Time)

    # def date(self):
    #     year = int(datetime.datetime.now().year)
    #     month = int(datetime.datetime.now().month)
    #     datee = int(datetime.datetime.now().day)
    #     self.speak("the date is ")
    #     self.speak(datee)
    #     self.speak(month)
    #     self.speak(year)

    def greeting(self):
        hour = datetime.datetime.now().hour
        if 6 <= hour < 12:
            self.speak("good morning ")
        elif hour >= 12 and hour < 18:
            self.speak("good afternoon")
        elif hour >= 18 and hour < 24:
            self.speak("good evening ")
        else:
            self.speak("good night ")

    def wishme(self):
        self.speak("welcome back sir")
        # self.time()
        # self.date()
        self.greeting()
        self.speak("jarvis at your service how can i help you")

    def takecommandCMD(self):
        query = input("please tell me how can i help you?")
        return query

    def takecommandmic(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:   # Use a microphone as the audio source
            print("LISTENING....")
            r.pause_threshold = 1  #for pause in recognizing
            audio = r.listen(source) # listen to the audio
        try:
            print("recognizing....")
            query = r.recognize_google(audio, language="en-IN")      # Use Google's speech recognition API to convert audio to text (in English - India)

            print(query)
        except Exception as e:
            print(e)
            self.speak("say it again.....")
            return "none"
        return query

    def sendEmail(self, content, receiver, subject):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(senderemail, epwd)
        email = EmailMessage()
        email['From'] = senderemail
        email['To'] = receiver
        email['Subject'] = subject
        email.set_content(content)
        server.send_message(email)
        server.close()

    def weather(self):
        city = 'islamabad'
        url = f'your key'
        result = requests.get(url)
        data = result.json()
        weather = data['weather'][0]['main']
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        temperature = round((temperature - 32) * 5 / 9)
        print(weather)
        print(temperature)
        print(description)
        self.speak(f'weather in {city} is ')
        self.speak('temperature:{} degree  '.format(temperature))
        self.speak('and  is {}'.format(description))

    def googlesearch(self):
        self.speak("what should i search for!")
        search = self.takecommandCMD().lower()
        wb.open('https://www.google.com/search?q=' + search)

    def news(self):
        api_key = 'your key'
        newsapi = NewsApiClient(api_key=api_key)
        self.speak("what should i search for!")
        search = self.takecommandCMD().lower()
        top_headlines = newsapi.get_top_headlines(q=search, language='en')
        articles = top_headlines['articles']
        for i in range(0, 1):
            article = articles[i]
            self.speak(article['title'])
            print(article['title'])
            self.speak(article['description'])
            print(article['description'])
        self.speak("Thank you for listening")

    def ai(self):
        openai.api_key = aiapikey
        self.speak("how can i assist  you?")
        query = self.takecommandCMD().lower()
        text = f"OpenAI response: {query}\n\n\n"
        try:
            if "and make a file" in query.lower():
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=query,
                    temperature=0.7,
                    max_tokens=256,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                text += response["choices"][0]["text"]
                if not os.path.exists("Openai"):
                    os.mkdir("Openai")

                with open(f"Openai/{''.join(query.split('intelligence')[1:]).strip()}.txt", "w") as f:
                    f.write(text)
                    print("File created successfully!")
            else:
                while True:
                    response = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=query,
                        temperature=0.7,
                        max_tokens=256,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0
                    )
                    reply_text = response["choices"][0]["text"]
                    self.speak(reply_text)
                    text += f"Jarvis: {reply_text}\n"

                    if "goodbye" in reply_text.lower():
                        break
                    query = self.takecommandCMD().lower()
        except Exception as e:
            print("An error occurred:", e)

    def joke(self):
        self.speak("shut upp ! ")

    def screenshot(self):
        name = "jarvis pro"
        name = 'C:\\Users\\Generation\\Documents\\{}.png'.format(name)
        image = pyautogui.screenshot(name)
        image.show()

    def cpu_usage(self):
        usage = str(psutil.cpu_percent())
        self.speak("cpu is at " + usage)
        battery = psutil.sensors_battery()
        self.speak("battery is at")
        self.speak(battery.percent)
