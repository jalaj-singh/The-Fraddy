import sys
import wolframalpha

from src.assistant import greetMe, myCommand, speak
from src import features
from src import config

def main():
    """Main function to run the Fraddy assistant."""

    # Initialize WolframAlpha client
    try:
        client = wolframalpha.Client(config.WOLFRAMALPHA_APP_ID)
    except Exception:
        print("Warning: WolframAlpha App ID is not configured or is invalid. The 'ask' feature will be limited.")
        client = None

    greetMe()
    speak('Hello Sir, I am your digital assistant Fraddy!')
    speak('How may I help you?')

    # Command mapping
    command_map = {
        'open youtube': features.open_youtube,
        'open google': features.open_google,
        'play music': features.play_music_online,
        'open gmail': features.open_gmail,
        'the time': features.get_time,
        'search on wikipedia': features.search_wikipedia,
        'shutdown': features.system_shutdown,
        'power off': features.system_shutdown,
        'system information': features.get_system_info,
        'news': features.get_news,
        'headlines': features.get_news,
        'weather': features.get_weather,
        'search on web': features.search_web,
        'joke': features.tell_joke,
        'screenshot': features.take_screenshot,
        'ssh': features.execute_ssh_command,
        'linux': features.execute_ssh_command,
        'notepad': features.write_note,
        'write a note': features.write_note,
        'show notes': features.show_notes,
        'search on youtube': features.search_youtube,
        'email': features.send_email,
        'local music': features.play_local_music,
        'open visual studio': features.open_vscode,
        'open pycharm': features.open_pycharm,
    }

    while True:
        query = myCommand()

        if any(keyword in query for keyword in ['nothing', 'abort', 'stop', 'bye', 'thank you']):
            speak('Okay. Bye Sir, have a good day.')
            sys.exit()

        command_executed = False
        for keyword, function in command_map.items():
            if keyword in query:
                function()
                command_executed = True
                break

        if not command_executed:
            speak('I am not sure what you mean. Trying to find an answer...')
            # Fallback: Try WolframAlpha, then Wikipedia, then web search
            if not features.ask_wolframalpha(query, client):
                try:
                    speak("I didn't find anything on WolframAlpha, trying Wikipedia.")
                    features.search_wikipedia()
                except Exception:
                    speak("I couldn't find anything on Wikipedia either. Here are some web search results.")
                    features.search_web()

        speak('Next Command! Sir!')

if __name__ == '__main__':
    main()
