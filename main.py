import filter, sys, os

def userInput():
    uInput = ""
    while True:
        uInput = str(input("Application name: "))
        if uInput != "":
            return uInput


if __name__ == "__main__":
    while True:
        uInput = userInput()
        if uInput.lower() == "q":
            sys.exit(-1)
            break

        filter.inputFromUser(uInput)
        #os.system("cls")
        print('To quit this program press \"q\"')