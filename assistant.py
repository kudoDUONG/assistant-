import speech_recognition
import pyttsx3
from datetime import date,datetime

robort_mouth = pyttsx3.init()
robort_ear=speech_recognition.Recognizer()
robort_brain=" "

while True:
    with speech_recognition.Microphone() as mic:
        print('robort!, I am listening...')
        audio=robort_ear.listen(mic)
    print("Robort:...")

    try:
     you= robort_ear.recognize_google(audio)
    except:
     you= "don't say anything"

    print('you:',you)


    if you=="":
        robort_brain="i can't hear you "
    elif "hello" in you:
        robort_brain="Hello Minh"
    elif "how are you" in you:
        robort_brain="I'm fine thank you and you"
    elif "today" in you:
        today = date.today()
        robort_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now=datetime.now()
        robort_brain=now.strftime("%I:%M:%S")
    elif "bye" in you:
        robort_brain="Bye MINH"
        print("Robort brain:", robort_brain)
        robort_mouth.say(robort_brain)
        robort_mouth.runAndWait()
        break
    else:
        robort_brain="I don't understand"

    print("Robort brain:", robort_brain)
    robort_mouth.say(robort_brain)
    robort_mouth.runAndWait()
