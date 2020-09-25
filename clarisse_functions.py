import pygame  # install pygame
import tkinter as tkr
import docx  # install python-docx
import random
import calendar
import warnings
import datetime
import os
import wikipedia  # install wikipedia
from gtts import gTTS  # install gTTS
import speech_recognition as sr  # install SpeechRecognition
# Go on https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio, download the right version, pip install [file's directory]
import pyaudio
import smtplib  # install smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import webbrowser
import pyttsx3  # install pyttsx3
import time


warnings.filterwarnings("ignore")


# Records audio from microphone and returns as a string
def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please state response:")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        wrong_names = ["Clarice", "Larry's", "clary's", "fairies",
                       "Clary", "Reese", "Cleary's", "Aries",
                       "Solaris", "Tyrese", "series"]
        for wrong_name in wrong_names:
            if wrong_name in data:
                data = data.replace(wrong_name, "Clarisse")

        print(f"You said: {data}")
    except sr.UnknownValueError:  # Checks for unknown errors
        print("Google Speech Recognition could not understand the audio. Unknown error.")
    except sr.RequestError as e:
        print("Request results from Google Speech Recognition service error " + e)

    return data


# Gets virtual assistant's response
def assistantResponse(text):
    try:
        print(text)

        # Convert the text to speech
        myobj = gTTS(text=text, lang="en", slow=False)

        # Save the converted audio to a file
        myobj.save("assistant_response.mp3")

        # Play the converted file
        os.system("start assistant_response.mp3")

    except:
        assistantResponse(
            "I'm sorry, I did not catch that. Could you please repeat what you said?")
        main()


# Detects wakewords/phrases
def wakeWord(text):
    WAKE_WORDS = ["clarisse", "hey clarisse",
                  "okay clarisse", "yo clarisse",
                  "hi clarisse", "hello clarisse"]
    text = text.lower()
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
    return False


# Get date function
def getDate():

    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]

    days = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th",
            "11th", "12th", "13th", "14th", "15th", "16th", "17th", "18th", "19th", "20th",
            "21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th", "29th", "30th", "31st"]

    return "Today is " + weekday + ", " + months[monthNum - 1] + " the " + days[dayNum - 1] + "."


# Returns a random greeting response
def greeting(text):
    GREETING_INPUTS = ["hi", "hey", "yo", "hello",
                       "good", "morning", "afternoon", "evening"]
    GREETING_RESPONSES = ["Hey there!", "Hello!", "Greetings!"]
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
    return ""  # If no greeting was detected, then return an empty string


# Gets a person's first and last name from the text
def getPerson(text):
    wordList = text.split()  # Splitting the text into a list of words
    for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == "who" and wordList[i + 1].lower() == "is":
            return wordList[i + 2] + " " + wordList[i + 3]


# Calculator
def calculate(text):

    # Finds the key word (the operator) and uses that as a reference index for the numbers in the equation
    equation = text.split()
    operatorList = ["+", "-", "*", "/", "^"]
    for i in equation:
        if i in operatorList and isinstance(float(equation[equation.index(i) - 1]), float) == True and isinstance(float(equation[equation.index(i) + 1]), float) == True:
            operation = i
            num1 = equation[equation.index(i) - 1]
            num2 = equation[equation.index(i) + 1]

            num1 = float(num1)
            num2 = float(num2)

            if operation == "+":
                answer = num1 + num2
                return str(answer)

            elif operation == "-":
                answer = num1 - num2
                return str(answer)

            elif operation == "*":
                answer = num1 * num2
                return str(answer)

            elif operation == "/":
                answer = num1 / num2
                return str(answer)

            elif operation == "^":
                answer = pow(num1, num2)
                return str(answer)

            else:
                return ("Sorry, I cannot calculate that.")

        else:
            main()


# Makes notes based on what the user says
def makeNotes(text):
    doc = docx.Document("notes.docx")

    # Be able to add multiple lines, separate notes using "-"
    # However, it can only add one line (paragraph) at a time
    # But it keeps running until you tell it to stop
    words = text.split()
    for i in words:

        if i == "note" or i == "notes":
            unwantedWords = ["Clarisse", "note", "notes"]
            for i in unwantedWords:
                if i in words:
                    words.remove(i)
            words.insert(0, "-")
            str1 = " "
            words = (str1.join(words))
            doc.add_paragraph(words)

    doc.save("notes.docx")


# Detects hour and replies with "Good morning/afternoon/evening"
def salutations():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        assistantResponse("Good morning, sir.")

    elif hour >= 12 and hour < 18:
        assistantResponse("Good afternoon, sir.")

    else:
        assistantResponse("Good evening, sir.")


# Google search
def search(text):
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    textList = text.split()
    textList.remove("Clarisse")
    key_phrases = ["search for", "what is", "search up", "Clarisse Google"]

    for phrase in key_phrases:
        if phrase in text:
            if "search for" in text:
                textList.remove("search")
                textList.remove("for")

            if "what is" in text:
                textList.remove("what")
                textList.remove("is")

            if "search up" in text:
                textList.remove("search")
                textList.remove("up")

            if "Clarisse Google" in text:
                textList.remove("Google")

            textList.remove(phrase)
            str1 = " "
            query = (str1.join(textList))
            webbrowser.get(chrome_path).open(
                "http://www.google.com/?#q=" + query)
            quit()

        else:
            quit()


# Email function
class Email_Recipient:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def sendEmail(self, recipient):
        if self.name == recipient:
            email_user = "[your email here]"
            email_send = self.email
            assistantResponse("What should I put as the subject, sir?")
            subject = recordAudio()
            subject = subject.capitalize()

            msg = MIMEMultipart()
            msg["From"] = email_user
            msg["To"] = email_send
            msg["Subject"] = subject

            assistantResponse("And what should I send, sir?")
            body = recordAudio()
            body = body.capitalize()
            body = body + \
                "\n\n\n ~~This email was sent by [your name]'s A.I. assistant, Clarisse. Have a nice day!~~"
            msg.attach(MIMEText(body, "plain"))

            text = msg.as_string()
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email_user, "[email password]")
            server.sendmail(email_user, email_send, text)
            server.quit()

            assistantResponse("Your email has been sent, sir.")
            quit()
        else:
            assistantResponse("Sorry, I cannot email that person.")
            quit()


# Add a list of everyone you wish to email here as instances of the class
Test_User = Email_Recipient("[your name]", "[your email]")
Test_Recipient = Email_Recipient("[recipient's name]", "[recipient email]")

email_list = [Test_User, Test_Recipient]


# Search Youtube videos
def youtube(text):
    video_search = text  # Modify this
    if("Clarisse play" in text):
        video_search = video_search.replace("Clarisse", "")
        video_search = video_search.replace("play", "")
        youtube_url = "https://www.youtube.com/results?search_query={}"
        search_url = youtube_url.format(video_search)

        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(search_url)
        quit()
    elif("Clarisse Youtube" in text):
        video_search = video_search.replace("Clarisse", "")
        video_search = video_search.replace("Youtube", "")
        youtube_url = "https://www.youtube.com/results?search_query={}"
        search_url = youtube_url.format(video_search)

        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(search_url)


# Play music directly from file
def play_music(file):
    player = tkr.Tk()
    player.title("Audio Player")
    player.geometry("340x340")
    os.chdir("[directory of your playlist]")
    songList = os.listdir()

    # Volume input
    VolumeLevel = tkr.Scale(player, from_=0.1, to_=1.0,
                            orient=tkr.HORIZONTAL, resolution=0.1)

    # Action Event
    def Play():
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(VolumeLevel.get())

    def ExitPlayer():
        pygame.mixer.music.stop()

    def Pause():
        pygame.mixer.music.pause()

    def UnPause():
        pygame.mixer.music.unpause()

    # Register buttons
    button1 = tkr.Button(player, width=5, height=3,
                         text="PLAY", command=Play)
    button2 = tkr.Button(player, width=5, height=3,
                         text="STOP", command=ExitPlayer)
    button3 = tkr.Button(player, width=5, height=3,
                         text="PAUSE", command=Pause)
    button4 = tkr.Button(player, width=5, height=3,
                         text="UNPAUSE", command=UnPause)
    label1 = tkr.LabelFrame(player, text=file)
    label1.pack(fill="both", expand="yes")
    contents1 = tkr.Label(label1)

    # Place Widgets
    button1.pack(fill="x")
    button2.pack(fill="x")
    button3.pack(fill="x")
    button4.pack(fill="x")
    VolumeLevel.pack(fill="x")
    contents1.pack()

    # Activate/Run the Code
    player.mainloop()


# Creates a Music Player
def music_player():

    # Create Window
    player = tkr.Tk()

    # Edit Window
    player.title("Audio Player")
    player.geometry("205x340")

    # Playlist register
    os.chdir("[directory of your playlist]")
    songList = os.listdir()

    # Volume input
    VolumeLevel = tkr.Scale(player, from_=0.1, to_=1.0,
                            orient=tkr.HORIZONTAL, resolution=0.1)

    # Playlist input
    # Only one song can be selected at a time - tkr.SINGLE
    playlist = tkr.Listbox(player, highlightcolor="blue",
                           selectmode=tkr.SINGLE)

    for item in songList:
        pos = 0
        playlist.insert(pos, item)
        pos = pos + 1

    # Pygame Inits
    pygame.init()
    pygame.mixer.init()

    # Action Event
    def ChooseSong():
        pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
        var.set(playlist.get(tkr.ACTIVE))
        pygame.mixer.music.play()  # Plays song until it ends
        pygame.mixer.music.set_volume(VolumeLevel.get())

    def ExitPlayer():
        pygame.mixer.music.stop()

    def Pause():
        pygame.mixer.music.pause()

    def UnPause():
        pygame.mixer.music.unpause()

    # Register buttons
    button1 = tkr.Button(player, width=5, height=3,
                         text="PLAY", command=ChooseSong)
    button2 = tkr.Button(player, width=5, height=3,
                         text="STOP", command=ExitPlayer)
    button3 = tkr.Button(player, width=5, height=3,
                         text="PAUSE", command=Pause)
    button4 = tkr.Button(player, width=5, height=3,
                         text="UNPAUSE", command=UnPause)

    # Song Name
    var = tkr.StringVar()
    songtitle = tkr.Label(player, textvariable=var)

    # Place Widgets
    songtitle.pack()
    button1.pack(fill="x")
    button2.pack(fill="x")
    button3.pack(fill="x")
    button4.pack(fill="x")
    VolumeLevel.pack(fill="x")
    playlist.pack(fill="both", expand="yes")

    # Activate/Run the Code
    player.mainloop()
