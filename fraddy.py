import pyttsx3
import subprocess
import requests
import json
import pyautogui
import paramiko
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import platform
from googlesearch import search
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#engine = pyttsx3.init('sapi5')

#voices= engine.getProperty('voices') #getting details of current voice

#engine.setProperty('voice', voice[0].id)

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('4L3Q5Q-T6RHHHXPJ2')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('t5987726@gmail.com', '7669247298')
    server.sendmail('t5987726@gmail.com', to, content)
    server.close()


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH != 0:
        speak('Good Evening!')


greetMe()

speak('Hello Sir, I am your digital assistant fraddy!')
speak('How may I help you?')


def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        query = myCommand();
        query = query.lower()
    if 'keyboard' in query:
        speak('Sir you can type the command')
        query = str(input('Command: '))

    return query


if __name__ == '__main__':

    while True:

        query = myCommand();
        query = query.lower()

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')
        elif 'play music' in query:
            speak('okay')
            webbrowser.open('https://www.youtube.com/watch?v=s-bZD3O3P80&list=RDMM&start_radio=1')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif 'open pycharm' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains"
            os.startfile(codePath)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "search on wikipedia" in query:
            results = wikipedia.summary(query, sentences=2)
            speak('Got it.')
            speak('WIKIPEDIA says - ')
            speak(results)
        elif "shutdown" in query or "power off" in query or "power of" in query or "shut down" in query:
            
            speak('Do you wish to shutdown your computer ?')
            shutdown = myCommand()
  
            if shutdown == 'no':
                #exit()
                continue
            else:
                os.system("shutdown /s /t 1")
        elif "system information" in query or "system info" in query or "system details" in query:
            my_system = platform.uname()
            speak(f"System: {my_system.system}")
            speak(f"Node Name: {my_system.node}")
            speak(f"Release: {my_system.release}")
            speak(f"Version: {my_system.version}")
            speak(f"Machine: {my_system.machine}")
            speak(f"Processor: {my_system.processor}")

        elif "news" in query or "headlines" in query:
            def NewsFromBBC():
     
                # BBC news api
                # following query parameters are used
                # source, sortBy and apiKey
                query_params = {
                  "source": "bbc-news",
                  "sortBy": "top",
                  "apiKey": "4272f1f9a4f643588bab78d58d3acf2d"
                }
                main_url = " https://newsapi.org/v1/articles"
             
                # fetching data in json format
                res = requests.get(main_url, params=query_params)
                open_bbc_page = res.json()
             
                # getting all articles in a string article
                article = open_bbc_page["articles"]
             
                # empty list which will
                # contain all trending news
                results = []
                 
                for ar in article:
                    results.append(ar["title"])
                     
                for i in range(len(results)):
                     
                    # printing all trending news
                    print(i + 1, results[i])
             
                #to read the news out loud for us
                from win32com.client import Dispatch
                speak = Dispatch("SAPI.Spvoice")
                speak.Speak(results)                
             
            # Driver Code
            if __name__ == '__main__':
                 
                # function call
                NewsFromBBC()

            
        elif "weather" in query:
            def time_from_utc_with_timezone(utc_with_tz):
                local_time = datetime.datetime.utcfromtimestamp(utc_with_tz)
                return local_time.time()

            # Enter your API key
            api_key = "4e92fd21e7f60643ec54ca1972052500"

            # Get city name from user
            city_name = "noida"

            # API url
            weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key

            # Get the response from weather url
            response = requests.get(weather_url)

            # response will be in json format and we need to change it to pythonic format
            weather_data = response.json()

            # Make sure you get 200 as response to proceed
            # SAMPLE DATA: {'coord': {'lon': 78.4744, 'lat': 17.3753}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}],
            # 'base': 'stations', 'main': {'temp': 293.04, 'feels_like': 293.44, 'temp_min': 291.15, 'temp_max': 294.82, 'pressure': 1015, 'humidity': 72},
            # 'visibility': 6000, 'wind': {'speed': 1.58, 'deg': 163}, 'clouds': {'all': 0}, 'dt': 1614196800, 'sys': {'type': 1, 'id': 9213, 'country': 'IN',
            # 'sunrise': 1614215239, 'sunset': 1614257484}, 'timezone': 19800, 'id': 1269843, 'name': 'Hyderabad', 'cod': 200}
            # weather_data['cod'] == '404' means city not found

            if weather_data['cod'] == 200:
                kelvin = 273.15 # Temperature shown here is in Kelvin and I will show in Celsius
                temp = int(weather_data['main']['temp'] - kelvin)
                feels_like_temp = int(weather_data['main']['feels_like'] - kelvin)
                pressure = weather_data['main']['pressure']
                humidity = weather_data['main']['humidity']
                wind_speed = weather_data['wind']['speed'] * 3.6
                sunrise = weather_data['sys']['sunrise']
                sunset = weather_data['sys']['sunset']
                timezone = weather_data['timezone']
                cloudy = weather_data['clouds']['all']
                description = weather_data['weather'][0]['description']

                sunrise_time = time_from_utc_with_timezone(sunrise + timezone)
                sunset_time = time_from_utc_with_timezone(sunset + timezone)

                
                speak(f"Weather Information for City: {city_name}")
                speak(f"Temperature (Celsius): {temp}")
                speak(f"Feels like in (Celsius): {feels_like_temp}")
                speak(f"Pressure: {pressure} hPa")
                speak(f"Humidity: {humidity}%")
                speak("Wind speed: {0:.2f} Kilo Meter Per Hour".format(wind_speed))
                speak(f"Sunrise at {sunrise_time} and Sunset at {sunset_time}")
                speak(f"Cloud: {cloudy}%")
                speak(f"Info: {description}")
            else:
                print(f"City Name: {city_name} was not found!")


        elif 'search on web' in query:
                speak('What can i search for you ')
                goog = myCommand()
                speak('It Take Few Seconds Sir! ')
                for j in search(goog, tld="co.in", num=10, stop=6, pause=9):
                    print(j)
                speak('Here is the result Sir. I hope you Like it!!')


        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif "joke" in query or 'jokes' in query:
            stMsgs = ['What do you get if you divide the circumference of a pumpkin by its diameter? ............                  Pumpkin pi', 'How does our solar system keep its pants up? ......................... With an asteroid belt ', 'Why are electricians always up to date? .........................Because they are current specialists ', 'This one is an acquired taste: .......... Why do fish live in salt water? ............................... Because pepper water makes them sneeze' , 'This one is an acquired taste: ........ Can a kangaroo jump higher than a house? .............Of course! Houses cannot jump. ','What is large, grey, and doesnt matter?..............An irrelephant','The missing sailor was a little TOO into swabbing the deck .....................I think he went overboard! ','How do you say goodbye to a vampire? ............. So long, sucker','The right eye said to the left eye,..............between you and me, something smells','Why did the banker switch careers?..........She lost interest','Did you know that all clouds have dandruff? ..........That is where snowflakes come from']
            speak(random.choice(stMsgs))
        elif "screenshot" in query or "screen shot" in query:
            speak('Under what name do i have to save the screenshot ??')
            
            ssname=myCommand()
            
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(fr'C:\Users\Jalaj\OneDrive\Pictures\{ssname}.png')
            speak('Screenshot Taken :)')
            

        elif "get location of ip" in query:
            import paramiko
            host = "192.168.121.45"

            port = 22

            username = "hellcat"

            password = "JP@singh"
            usercmd=input("Enter IP ADDRESS :")


            command = "cd /opt/IPGeoLocation/ && python3 ipgeolocation.py -t " + usercmd + "> tt.txt"

            #command = "cd /opt/seeker/ && ./ngrok http 8080"
            ssh = paramiko.SSHClient()

            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            ssh.connect(host, port, username, password)


            stdin, stdout, stderr = ssh.exec_command(command)
            #stdin, stdout, stderr = ssh.exec_command(command)

            lines = stdout.readlines()

            print(lines)
            speak('Data is stored is IP Location file ! ')


        elif "my ip address" in query:
            import paramiko
            host = "192.168.121.45"

            port = 22

            username = "hellcat"

            password = "JP@singh"


            command = "cd /opt/IPGeoLocation/ && python3 ipgeolocation.py -m > tt.txt"
            command1= "cat /opt/IPGeoLocation/tt.txt"
            #command = "cd /opt/seeker/ && ./ngrok http 8080"
            ssh = paramiko.SSHClient()

            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            ssh.connect(host, port, username, password)


            stdin, stdout, stderr = ssh.exec_command(command)
            stdin, stdout1, stderr = ssh.exec_command(command1)

            lines = stdout1.readlines()
            count=0
            

            print(lines)
            speak('Data is stored is IP Location file ! ')

        elif "notepad" in query or "write a note" in query:
            file1 = open("notepad.txt","a")
            speak('What You Want to Write ')
            L = myCommand()
            x=str(datetime.datetime.now())
            file1.write(f"\n")
            file1.write(x)
            file1.write(f"\n")
            file1.writelines(L)
            file1.close() #to change file access modes
        elif "show notes" in query or "see my notes" in query or "see my note" in query or "show my notepad" in query:
            file1 = open("notepad.txt","r+")
            speak('Opening File Named Notepad.txt')
  
            #print("Output of Read function is ")
            #print(file1.readlines())
            #print()
              
            count = 0
             
            while True:
                count += 1
             
                # Get next line from file
                line = file1.readline()
             
                # if line is empty
                # end of file is reached
                if not line:
                    break
                print("Line{}: {}".format(count, line.strip()))
             
            file1.close()

        elif "ip location file" in query or "ip location files" in query:
            import paramiko
            host = "192.168.121.45"

            port = 22

            username = "hellcat"

            password = "JP@singh"

            command = "cd /opt/IPGeoLocation/ && cat tt.txt"
            #command = "cat Untitled1.ipynb"
            #command = "cd /opt/seeker/ && ./ngrok http 8080"
            ssh = paramiko.SSHClient()

            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            ssh.connect(host, port, username, password)


            stdin, stdout, stderr = ssh.exec_command(command)
            #stdin, stdout, stderr = ssh.exec_command(command)

            lines = stdout.readlines()

            print(lines)

        elif "linux" in query:
            import paramiko
            host = "192.168.121.45"

            port = 22

            username = "hellcat"

            password = "JP@singh"
            speak('What command do you want to execute ??')

            command = myCommand()
            #command = "cat Untitled1.ipynb"
            #command = "cd /opt/seeker/ && ./ngrok http 8080"
            ssh = paramiko.SSHClient()

            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            ssh.connect(host, port, username, password)


            stdin, stdout, stderr = ssh.exec_command(command)
            #stdin, stdout, stderr = ssh.exec_command(command)

            lines = stdout.readlines()

            print(lines)
        elif "search on youtube" in query or "search something on youtube" in query:
            
            speak('What do you want to Search ..')
            searchtext=myCommand()
   
            # giving the path of chromedriver to selenium webdriver
            path = "C:\\Users\\Jalaj\\OneDrive\\Desktop\\New folder\\chromedriver.exe"
             
            url = "https://www.youtube.com/"
            driver = webdriver.Chrome(path)
            driver.get(url)
            driver.find_element_by_name("search_query").send_keys(searchtext)
            driver.find_element_by_css_selector("#search-icon-legacy.ytd-searchbox").click()
             
            # For finding the right match search
            WebDriverWait(driver, 0).until(expected_conditions.title_contains(myCommand()))
             
            # clicking on the match search having same as in searched query
            WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.ID, "img"))).click()
                
            

        elif 'email to john' in query:
            try:
                speak("What should I say?")
                content = myCommand()
                to = "tt613562@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry jalaj bhai. I am not able to send this email")
                    
            


        elif 'nothing' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'thank you' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'hello' in query or 'hi' in query or 'hey' in query:
            rep=['Hello Sir','Hello!','Hello Sir. How i Can Help You!','Hello Sir. How Are you!']
            speak(random.choice(rep))

        


        elif 'local music' in query or 'music from local computer' in query:
            music_folder = "C:\\Users\\Jalaj\\Music\\"
            music = ["Soch","Lehra","Maafi","Maiyya"]
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)

            speak('Okay, here is your music! Enjoy!')
        elif 'open visual studio' in query:
            pat="C:\\Users\\Jalaj\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            subprocess.call(pat)
            speak('Opening Visual Studio.. ')
            


        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    #speak('Got it.')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                speak("Sir. I am not able to do that! But here\'s the some data available on Internet")
                goog = query
                speak('It Take Few Seconds Sir! ')
                for j in search(goog, tld="co.in", num=10, stop=6, pause=9):
                   print(j)

        speak('Next Command! Sir!')
