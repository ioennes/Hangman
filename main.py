import random
import re

# Open movie_names.txt

fname = open("movie_names.txt", "r")
fname = fname.read().upper().splitlines()

# Define Game

def hangman(wrongGuess = 0):
    randomWord = random.choice(fname)                                                   # Random movie name
    randomList = []                                                                     
    for letter in randomWord:
        randomList.append(letter)
    hidden = re.sub("[ABCDEFGHIJKLMNOPQRSTUVWXYZ]", "_", randomWord)                    # Turn letters into underscores
    hiddenList = []
    stop = False
    for i in hidden:
        hiddenList.append(i)
    while wrongGuess != 14 and stop == False:      
        guess = input("Guess: ").upper()
        if guess in randomList:
            found = randomList.index(guess)
            hiddenList = hiddenList[:found] + [guess] + hiddenList[found+1:]            # Replace _ by guess
            randomList = randomList[:found] + ["FOUND"] + randomList[found+1:]          # Replace guess by "FOUND"
            hidden = "".join(hiddenList)                                                # Print out guessed words
            print(hidden)                                                                   

        else:
            print(f"Wrong! {hidden}")                                                   # Prints out wrong and shows current progress
            wrongGuess += 1
            if wrongGuess == 2:
                x = str("------\n"+                                                     # HANGMAN FIGURE
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
                print(f"Wrong! The correct word was {randomWord.capitalize()}")              
                stop = True
        if hidden.find("_") == -1:
            stop = True
            print("DONE!")

# Execute Game

hangman()