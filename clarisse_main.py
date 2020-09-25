# Clarisse ver. 0.4.5
import random
import datetime
import os
import wikipedia  # install wikipedia
import webbrowser
from clarisse_functions import recordAudio, assistantResponse, wakeWord, getDate, greeting, getPerson, calculate, makeNotes, salutations, search, youtube, play_music, music_player, Email_Recipient

salutations()
assistantResponse("How may I help you?")

while True:
    def main():
        # Record the audio
        text = recordAudio()
        response = ""

        # Check for the wake word/phrase
        if(wakeWord(text) == True):

            # Check for greetings by the user
            greeting_words = ["hi,", "hello", "yo", "hey", "good",
                              "morning", "afternoon", "evening"]
            textList = text.split()
            if textList[0] in greeting_words:
                response = greeting(text)

            # Check if you asked Clarisse how she's doing
            elif("how are you" in text):
                statusList = [
                    "I am fine, sir.", "I am happy now that you are here, sir.", "I am doing good, sir."]
                response = random.choice(statusList)

            # Check to see if the user said anything having to do with the date
            elif("date" in text):
                get_date = getDate()
                response = get_date

            # Check to see if the user said anything having to do with the time
            elif("time" in text):
                now = datetime.datetime.now()
                meridiem = ""
                if now.hour >= 12:
                    meridiem = "p.m."  # Post Meridiem, after midday
                    hour = now.hour - 12
                else:
                    meridiem = "a.m."  # Ante Meridiem, before midday
                    hour = now.hour

                # Convert minute into a proper string
                if now.minute < 10:
                    minute = "0" + str(now.minute)
                else:
                    minute = str(now.minute)

                response = "It is " + str(hour) + ":" + \
                    minute + " " + meridiem + "."

            # Check to see if the user said "who is"
            elif("who is" in text):
                person = getPerson(text)
                wiki = wikipedia.summary(person, sentences=2)
                response = wiki

            # Checks if user needs calculator
            elif("+" in text or "-" in text or "*" in text or "/" in text or "^" in text):
                answer = calculate(text)
                response = answer

            elif("note" in text or "notes" in text):
                makeNotes(text)
                MESSAGES = ["Noted, sir.", "Understood, sir.", "Yes, sir."]
                response = random.choice(MESSAGES)

            elif("open Google" in text):
                response = "Understood, sir."
                chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open("google.com")
                quit()

            elif("open Youtube" in text):
                response = "Understood, sir."
                chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open("youtube.com")
                quit()

            elif("check my email" in text or "open email" in text or "open gmail" in text or "check my gmail" in text or "check gmail" in text or "check email" in text):
                response = "Right away, sir."
                chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                webbrowser.get(chrome_path).open("gmail.com")
                quit()

            elif("search for" in text or "what is" in text or "search up" in text or "Google" in text):
                assistantResponse("Understood, sir.")
                search(text)

            elif("Clarisse play" in text and "tic-tac-toe" not in text and "Tic-tac-toe" not in text):
                text = text.replace("Clarisse play", "")
                text = text.lower()
                file = text

                # This searches for the song in the playlist and plays it
                os.chdir(
                    "[directory of your playlist]")
                songList = os.listdir()
                for song in songList:
                    music = song.replace("- ", "")
                    music = music.lower()
                    if file in music:
                        file = song
                        play_music(file)
                    else:
                        pass

                if "music" in text:
                    music_player()
                quit()

            elif("Clarisse Youtube" in text):
                youtube(text)
                quit()

            elif("email" in text):
                text_list = text.split()
                recipient = str(text_list[2])
                for person in email_list:
                    if person.name == recipient:
                        Email_Recipient.sendEmail(person, recipient)
                        quit()

            elif("chat" in text or "talk" in text or "conversation" in text):
                assistantResponse("Okay, one moment please.")
                import clarisse_chatbot
                from clarisse_chatbot import chatbot_response
                print("Clarisse is now conversing; say stop, quit, or bye to exit.")
                assistantResponse("Okay, let's talk.")

                def chatting():
                    while True:
                        inp = recordAudio()
                        inp = inp.lower()
                        if inp == "quit" or inp == "stop" or inp == "bye":
                            break

                        else:
                            try:
                                res = chatbot_response(inp)
                                assistantResponse(res)
                                # A delay is required because the recordAudio() doesn't work that fast
                                time.sleep(1)
                            except:
                                assistantResponse(
                                    "I'm sorry, I didn't catch that.")
                                chatting()
                    quit()
                chatting()

            elif("stop Clarisse" in text or "Clarisse stop" in text or "mute Clarisse" in text or "Clarisse mute" in text or "shut up Clarisse" in text or "Clarisse shut up" in text or "Clarisse be quiet" in text or "be quiet Clarisse" in text):
                quit()

            else:
                response = "I'm sorry, I don't understand."

            # Have the assistant respond back using audio and the text from response
            assistantResponse(response)

    main()
