import filter, sys, os
import speech_recognition as sr
import pyttsx3, time, threading
userInput = ""
gotTheData = False

def SpeechToText():
    global userInput, gotTheData
    r = sr.Recognizer()
    while not gotTheData:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                myText = r.recognize_google(audio2)
                myText = myText.lower()
                if not gotTheData:
                    userInput = myText
                    gotTheData = True
                elif gotTheData:
                    return -1
        except sr.RequestError as e:
            print("Could not request results: {}".format(e))
        except sr.UnknownValueError:
            pass
            #print("Unknown errror occured with speech recognition.")


def KeyBoardInput():
    global userInput, gotTheData
    myText = input("")
    if not gotTheData:
        userInput = myText
        gotTheData = True
    else:
        return -1

def usrInput():
    global userInput, gotTheData
    speekThread = threading.Thread(target = SpeechToText, daemon=True)
    keyBThread = threading.Thread(target = KeyBoardInput, daemon = True)
    speekThread.start()
    keyBThread.start()
    while not gotTheData:
        #userInput = str(input("Application name: "))
        time.sleep(0.5)
    gotTheData = False
    return userInput


if __name__ == "__main__":
    while True:
        print("Application name: ", end = "")
        uInput = usrInput()
        print(userInput)
        if uInput.lower() == "q":
            sys.exit(-1)
            break

        filter.inputFromUser(uInput)
        #os.system("cls")
        print('To quit this program press \"q\"')
