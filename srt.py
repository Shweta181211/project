import speech_recognition as sr

recognizer= sr.Recognizer()

with sr.Microphone() as source:
    print("Adjusting for ambient nooise please wait")
    recognizer.adjust_for_ambient_noise(source, duration=2)
    print("listening please speak something")
    audio_data=recognizer.listen(source)

    try:

        text=recognizer.recognize_google(audio_data)
        print("you said",text)

        commands=["hello","bye","text","open","close"]
        if text.lower() in commands:
            print("command recognized:",text)
        else:
            print("nomatching comment found")

    except sr.UnknownValueError:
        print("could not understand audio. Please try again")
    except sr.RequestError:
        print("could not connect to speech recognition service")
                  















