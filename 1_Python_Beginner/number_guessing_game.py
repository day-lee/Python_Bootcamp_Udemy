logo = """


  _   _                 _                  _____                     _                _____                      
 | \ | |               | |                / ____|                   (_)              / ____|                     
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _  | |  __  __ _ _ __ ___   ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` | | | |_ |/ _` | '_ ` _ \ / _ \
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| | | |__| | (_| | | | | | |  __/
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |  \_____|\__,_|_| |_| |_|\___|
                                                                              __/ |                              
                                                                             |___/                               
"""
# from art import logo
import random

answer = random.randint(1, 100)

EASY = 10
HARD = 5
attempt = 0

def guessing():
    answer = random.randint(0, 100)
    # print(f"\n pssst answer is {answer}")
    
    print(logo)
    print("I'm thinking of a number between 1 and 100.")
    
    level = input("Choose a difficulty level 'easy' or 'hard'? ")
    
    if level == 'easy':
        attempt = EASY
    else:
        attempt = HARD

    while attempt > 0:
        guess = int(input("Make a guess: "))
        if guess == answer:
            return print("\n Congrats. You guessed it! \n")
        elif guess > answer:
            attempt -= 1
            print(f"Too high. You have {attempt}  attempts left")
        elif guess < answer:
            attempt -= 1
            print(f"Too low. You have {attempt} attempts left")

    if attempt == 0:
        print("\n Out of attempts. You lose. \n")
    if input("Restart? y or n: ") == "y":
        guessing()

guessing()
