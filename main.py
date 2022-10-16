import random
import re

fname = open("movie_names.txt", "r")
fname = fname.read().upper().splitlines()

def hangman(wrongGuess = 0):
    randomWord = random.choice(fname)   # Random movie name
    randomList = []
    for letter in randomWord:
        randomList.append(letter)
    hidden = re.sub("[ABCDEFGHIJKLMNOPQRSTUVWXYZ]", "_", randomWord)
    hiddenList = []
    stop = False
    for i in hidden:
        hiddenList.append(i)
    while wrongGuess != 14 and stop == False:      
        guess = input("Guess: ").upper()
        if guess in randomList:
            found = randomList.index(guess)
            hiddenList = hiddenList[:found] + [guess] + hiddenList[found+1:]
            randomList = randomList[:found] + ["FOUND"] + randomList[found+1:]
            hidden = "".join(hiddenList)
            print(hidden)

        else:
            print(f"Wrong! {hidden}")
            wrongGuess += 1
            if wrongGuess == 2:
                x = str("------\n"+
                        " |   |\n"+
                        "     |\n"+
                        "     |\n"+
                        "     |\n"+
                        "     |\n"+
                        "    ---")   
            elif wrongGuess == 2:
                x = str("------\n"+
                        " |   |\n"+
                        " 0   |\n"+
                        "     |\n"+
                        "     |\n"+
                        "     |\n"+
                        "    ---")
                print(x)
            elif wrongGuess == 4:
                x = str("------\n"+
                        " |   |\n"+
                        " 0   |\n"+
                        " |   |\n"+
                        "     |\n"+
                        "     |\n"+
                        "    ---")
                print(x)   
            elif wrongGuess == 6:
                x = str("------\n"+
                        " |   |\n"+
                        " 0   |\n"+
                        "/|   |\n"+
                        "     |\n"+
                        "     |\n"+
                        "    ---")
                print(x)          
            elif wrongGuess == 8:
                x = str("------\n"+
                        " |   |\n"+
                        " 0   |\n"+
                        "/|\  |\n"+
                        "     |\n"+
                        "     |\n"+
                        "    ---")
                print(x)     
            elif wrongGuess == 10:
                x = str("------\n"+
                        " |   |\n"+
                        " 0   |\n"+
                        "/|\  |\n"+
                        " |   |\n"+
                        "     |\n"+
                        "    ---")
                print(x)   
            elif wrongGuess == 12:
                x = str("------\n"+
                        " |   |\n"+
                        " 0   |\n"+
                        "/|\  |\n"+
                        " |   |\n"+
                        "/    |\n"+
                        "    ---")
                print(x)
            elif wrongGuess == 14:
                x = str("------\n"+
                        " |   |\n"+
                        " 0   |\n"+
                        "/|\  |\n"+
                        " |   |\n"+
                        "/ \  |\n"+
                        "    ---")
                print(x)
                print(f"Wrong! The correct word was {randomWord}")
                stop = True
        if hidden.find("_") == -1:
            stop = True
            print("DONE!")
hangman()