# The-Fraddy
Fraddy is a Python Module which is able to perform task like Chatbot, Assistant etc. It provides the basic functionality for any assistant application. This Fraddy is built using Python, Pytorch, and other open-source libraries and frameworks.  This project is created for those, who want to make, heavy tasks easier in their day-to-day life. Generally, it took lots of time to write code from scratch to build Virtual Assistant. So, we have used pre-installed libraries, which gives you easy functionality to build your own Virtual Assistant.

## Problem Statement
In our daily busy schedule, we forget to call or drop a text to our favorite ones. Let's make their life easier by introducing our project called “theFraddy”. 
No matter how busy you’re, just wake up Fraddy, tell him to perform a task for you and it will execute your command within a second. You’ll not just able to make call or drop messages, but can also send email, ask to book your flight, or appointment, or just to entertain your mood by some random jokes.

## Purpose-
This Program aims at developing a personal assistant for windows-based systems. The main purpose of the software is to perform the tasks of the user at certain commands, provided in either of the ways, speech or text. It will ease most of the work of the user as a complete task can be done on a single command. Fraddy draws its inspiration from Virtual assistants like Google Assistant for Android, Siri for iOS etc. Users can interact with the assistant either through voice commands or keyboard input.


## Requirements
- Python 3.8+
- A working microphone

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-repo/The-Fraddy.git
    cd The-Fraddy
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    **Note for Windows users:** The `pyttsx3` library uses the `SAPI5` engine, which may require the `pywin32` package. If you encounter errors, please install it manually:
    ```bash
    pip install pywin32
    ```

4.  **Configure the application:**
    - Rename `config.ini.example` to `config.ini`.
    - Open `config.ini` and add your API keys and credentials for the features you want to use.

## Running the Assistant
```bash
python src/main.py
```

## Technologies Used:
> Language - Python


> Framework - pyaudio, Sapi5 (it comes with windows10 OS)[voice id: 0 (male)]

## Features-
>It can do a lot of cool things, some of them being:

-	Greet user
-	Tell current time and date
-	Launch applications/software's
-	Open any website
-	Tells about weather of any city
-	Tells your current system status (RAM Usage, battery health, CPU usage)
-	Tells about any person (via Wikipedia)
-	Can search anything on Google
-	Can play any song on YouTube
-	Tells top headlines (via Times of India)
-	Plays music (via Local Folder)
-	Send email (with subject and content)
-	Calculate any basic mathematical expression
-	Answer any generic question
-	Take important note in notepad
-	Tells a random joke
-	Tells your IP address
-	Can switch off or reboot the system
-	Can take screenshot and save it with custom filename
-	Can hide all files in a folder and also make them visible again
-	Command line user interface
-	Get IP details 
-	Can search anything on YouTube
-	Can take command (via Keyboard)
-	Access Linux using remote connection

## Scope
>Fraddy can be used in Railway stations, Airports, Government agencies, Research Organizations, Hospitals, Hotels, Colleges and the most importantly at Home by each member for different purposes.
>Presently, Fraddy is being developed as an automation tool and virtual assistant. Among the Various roles played by Fraddy are: 
- Search Engine with voice interactions 
- Tells a random joke
- Tells your IP address with detail
- Plays music and send emails
- Answer any question
>***There shall be proper Documentation available on its Official GitHub repository for making further development easy, we aim to release our virtual assistant as an Open-Source Software where modifications and contributions by the community are warmly welcomed.***

## Conclusion:
Through this voice assistant, we have automated various services using a single line command. It eases most of the tasks of the user like searching the web, retrieving weather forecast details, vocabulary help and medical related queries. We aim to make this project a complete server assistant and make it smart enough to act as a replacement for a general server administration. The future plans include integrating Fraddy with mobile using React Native to provide a synchronized experience between the two connected devices. Further, in the long run, Fraddy is planned to feature auto deployment supporting elastic beanstalk, backup files, and all operations which a general Server Administrator does. The functionality would be seamless enough to replace the Server Administrator with Fraddy. We are planning to use Fraddy with Docker, so different people can have virtual space for Fraddy
