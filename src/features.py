import webbrowser
import datetime
import wikipedia
import os
import platform
import requests
import smtplib
import random
import pyautogui
import paramiko
import subprocess
from googlesearch import search
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.assistant import speak, myCommand
from src import config

def open_youtube():
    speak('Opening YouTube.')
    webbrowser.open('https://www.youtube.com')

def open_google():
    speak('Opening Google.')
    webbrowser.open('https://www.google.co.in')

def play_music_online():
    speak('Playing music from YouTube.')
    webbrowser.open('https://www.youtube.com/watch?v=s-bZD3O3P80&list=RDMM&start_radio=1')

def open_gmail():
    speak('Opening Gmail.')
    webbrowser.open('https://www.gmail.com')

def get_time():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time is {strTime}")

def search_wikipedia():
    speak("What should I search for on Wikipedia?")
    search_query = myCommand()
    try:
        results = wikipedia.summary(search_query, sentences=2)
        speak('According to Wikipedia...')
        speak(results)
    except wikipedia.exceptions.PageError:
        speak(f"Sorry, I could not find a Wikipedia page for {search_query}.")
    except wikipedia.exceptions.DisambiguationError as e:
        speak(f"That query is ambiguous. Here are some options: {e.options}")
    except Exception as e:
        speak(f"An error occurred: {e}")

def system_shutdown():
    speak('Are you sure you want to shutdown your computer? Please say YES to confirm.')
    confirmation = myCommand()
    if 'yes' in confirmation:
        speak('Shutting down.')
        os.system("shutdown /s /t 1")
    else:
        speak('Shutdown cancelled.')

def get_system_info():
    my_system = platform.uname()
    speak(f"System: {my_system.system}")
    speak(f"Node Name: {my_system.node}")
    speak(f"Release: {my_system.release}")
    speak(f"Version: {my_system.version}")
    speak(f"Machine: {my_system.machine}")
    speak(f"Processor: {my_system.processor}")

def get_news():
    if not config.NEWSAPI_API_KEY or config.NEWSAPI_API_KEY == 'YOUR_API_KEY':
        speak("News API key is not configured in config.ini")
        return
    query_params = {"source": "bbc-news", "sortBy": "top", "apiKey": config.NEWSAPI_API_KEY}
    main_url = "https://newsapi.org/v1/articles"
    try:
        res = requests.get(main_url, params=query_params)
        res.raise_for_status()
        open_bbc_page = res.json()
        article = open_bbc_page.get("articles", [])
        results = [ar.get("title", "No title") for ar in article]
        if not results:
            speak("Sorry, I couldn't fetch the news right now.")
            return
        speak("Here are the top 5 headlines from BBC News:")
        for result in results[:5]:
            speak(result)
    except requests.exceptions.RequestException as e:
        speak(f"Sorry, I couldn't connect to the news service. Error: {e}")

def get_weather():
    if not config.OPENWEATHERMAP_API_KEY or config.OPENWEATHERMAP_API_KEY == 'YOUR_API_KEY':
        speak("OpenWeatherMap API key is not configured in config.ini")
        return
    speak("Which city's weather would you like to know?")
    city_name = myCommand()
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={config.OPENWEATHERMAP_API_KEY}&units=metric'
    try:
        response = requests.get(weather_url)
        response.raise_for_status()
        weather_data = response.json()
        if weather_data['cod'] == 200:
            temp = int(weather_data['main']['temp'])
            description = weather_data['weather'][0]['description']
            speak(f"The weather in {city_name} is currently {description} with a temperature of {temp} degrees Celsius.")
        else:
            speak(f"City Name: {city_name} was not found!")
    except requests.exceptions.RequestException as e:
        speak(f"Sorry, I couldn't connect to the weather service. Error: {e}")

def search_web():
    speak('What can I search for you?')
    search_term = myCommand()
    speak('Here are the top results from the web.')
    try:
        for j in search(search_term, tld="co.in", num=5, stop=5, pause=2):
            print(j)
    except Exception as e:
        speak(f"Sorry, I encountered an error while searching: {e}")

def tell_joke():
    jokes = ['Why did the scarecrow win an award? Because he was outstanding in his field!', 'Why don’t scientists trust atoms? Because they make up everything!']
    speak(random.choice(jokes))

def take_screenshot():
    speak('Under what name should I save the screenshot?')
    ssname = myCommand().replace(" ", "_")
    screenshot_dir = os.path.join(config.HOME_DIR, "Pictures", "Screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshot_dir, f"{ssname}.png")
    try:
        pyautogui.screenshot().save(screenshot_path)
        speak(f'Screenshot saved to {screenshot_path}')
    except Exception as e:
        speak(f"Sorry, I could not take a screenshot. Error: {e}")

def execute_ssh_command():
    if not all([config.SSH_HOST, config.SSH_USER, config.SSH_PASSWORD]):
        speak("SSH credentials are not configured. Please set them in config.ini")
        return
    speak('What command do you want to execute on the remote machine?')
    command = myCommand()
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(config.SSH_HOST, port=22, username=config.SSH_USER, password=config.SSH_PASSWORD, timeout=10)
        stdin, stdout, stderr = ssh.exec_command(command)
        lines = stdout.readlines()
        errors = stderr.readlines()
        ssh.close()
        if errors:
            print("--- SSH Errors ---")
            for error in errors:
                print(error.strip())
            speak("The command resulted in an error.")
        if lines:
            print("--- Command Output ---")
            for line in lines:
                print(line.strip())
            speak('The command has been executed.')
        if not lines and not errors:
            speak("The command executed successfully with no output.")
    except Exception as e:
        speak(f"Failed to execute SSH command. Error: {e}")

def write_note():
    speak('What would you like to write down?')
    note_content = myCommand()
    try:
        with open(config.NOTEPAD_FILE, "a") as file1:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file1.write(f"\n---\n{timestamp}\n{note_content}\n")
        speak("I've added that to your notes.")
    except Exception as e:
        speak(f"Sorry, I couldn't write to the notepad. Error: {e}")

def show_notes():
    try:
        with open(config.NOTEPAD_FILE, "r") as file1:
            speak('Here are your notes:')
            print(file1.read())
    except FileNotFoundError:
        speak("You don't seem to have any notes yet.")

def search_youtube():
    if not config.CHROME_DRIVER_PATH or not os.path.exists(config.CHROME_DRIVER_PATH):
        speak("The path to chromedriver is not configured or is invalid. Please set it in config.ini.")
        return
    speak('What do you want to search for on YouTube?')
    search_text = myCommand()
    try:
        service = webdriver.chrome.service.Service(executable_path=config.CHROME_DRIVER_PATH)
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.youtube.com/")
        wait = WebDriverWait(driver, 10)
        search_box = wait.until(EC.presence_of_element_located((By.NAME, "search_query")))
        search_box.send_keys(search_text)
        search_box.send_keys(Keys.RETURN)
        speak(f"I have opened YouTube and searched for {search_text}.")
    except Exception as e:
        speak(f"Sorry, I couldn't perform the YouTube search. Error: {e}")

def send_email():
    if not config.GMAIL_EMAIL or config.GMAIL_EMAIL == 'YOUR_EMAIL@gmail.com':
        speak("Gmail credentials are not configured in config.ini")
        return
    speak("Who is the recipient? Please provide their email address.")
    recipient = myCommand().lower().replace(" ", "")
    speak("What should the subject be?")
    subject = myCommand()
    speak("What should I say in the email?")
    content = myCommand()
    full_content = f"Subject: {subject}\n\n{content}"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    try:
        server.login(config.GMAIL_EMAIL, config.GMAIL_PASSWORD)
        server.sendmail(config.GMAIL_EMAIL, recipient, full_content)
        speak("Email has been sent!")
    except smtplib.SMTPAuthenticationError:
        speak("Failed to send email. Please check your Gmail credentials and ensure 'less secure app access' is enabled.")
    except Exception as e:
        speak(f"An error occurred while sending the email: {e}")
    finally:
        server.close()

def play_local_music():
    if os.path.exists(config.MUSIC_FOLDER_PATH):
        try:
            music_files = [f for f in os.listdir(config.MUSIC_FOLDER_PATH) if f.endswith(('.mp3', '.wav', '.flac'))]
            if not music_files:
                speak("I couldn't find any music in your music folder.")
                return
            random_music = os.path.join(config.MUSIC_FOLDER_PATH, random.choice(music_files))
            os.startfile(random_music)
            speak('Okay, here is your music! Enjoy!')
        except Exception as e:
            speak(f"An error occurred while trying to play music: {e}")
    else:
        speak("I couldn't find your music folder. Please check the path in config.ini.")

def open_vscode():
    if config.VSCODE_PATH and os.path.exists(config.VSCODE_PATH):
        try:
            subprocess.Popen(config.VSCODE_PATH)
            speak('Opening Visual Studio Code.')
        except Exception as e:
            speak(f"Sorry, I could not open VS Code. Error: {e}")
    else:
        speak("The path for VS Code is not configured or is invalid. Please set it in config.ini.")

def open_pycharm():
    if config.PYCHARM_PATH and os.path.exists(config.PYCHARM_PATH):
        try:
            subprocess.Popen(config.PYCHARM_PATH)
            speak("Opening PyCharm.")
        except Exception as e:
            speak(f"Sorry, I could not open PyCharm. Error: {e}")
    else:
        speak("The path for PyCharm is not configured or is invalid. Please set it in config.ini.")

def ask_wolframalpha(query, client):
    if not client:
        speak("WolframAlpha is not configured. Please add your App ID to config.ini.")
        return False
    try:
        res = client.query(query)
        results = next(res.results).text
        speak('WOLFRAM-ALPHA says - ')
        speak(results)
        return True
    except (StopIteration, AttributeError):
        return False # Indicate that WolframAlpha did not find an answer
    except Exception as e:
        speak(f"An error occurred with WolframAlpha: {e}")
        return False
