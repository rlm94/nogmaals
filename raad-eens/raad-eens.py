import random


roundLimit = 21
rounds = 1
score = 0
triesLimit = 11

while rounds < roundLimit:

    number = random.randrange(1, 1000)
    print(f"This is the {rounds}th round")
    print(number)
    rounds += 1
    tries = 1
    

    while tries < triesLimit:

        guess = input(f"**********TYPE QUIT TO STOP**********\ntries: {tries}\nscore: {score}\nGuess the number between 1 and 1000\n : ")
        
        if guess.isdigit()==True:
            if int(guess) == number:
                score += 1
                print("!!!!!You\'ve guessed the right number!!!!! your score is:", score)
                tries = 11
            

            else:
                tries += 1
                print("wrong number guess again")
        if guess.isdigit()==True:
    
            difference = number - int(guess)
            difference = abs(difference)       
            if difference < 20:
                print("warmer")
            elif difference < 50 and difference > 20:
                print("warm")

        elif guess == "quit":
                rounds = 21
                tries = 11
        else:
            print("put a valid character in or quit")