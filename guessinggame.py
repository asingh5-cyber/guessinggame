import random
# generate a random number between 1-10
random_number = random.randint(1,10)
#track the user's previous guess to prevent duplicates
previous_guess=[]
while True:
    user_guess=int(input("Enter a number between 1-10 "))
    if user_guess <1 or user_guess >10:
        print ("Invalid Guess")
#check if the user has already guess this number before
    elif user_guess in previous_guess:
        for old_guess in previous_guess:
            if user_guess == old_guess:
                is_duplicate = True
        if is_duplicate:
            print("you alreay guess")
            print("Chosse a differnet number")
            print("preivous guess")
    else:
        print("Valid new guess")
    if 1 <=user_guess <=10 and user_guess not in previous_guess:
        previous_guess.append(user_guess)
    if user_guess == random_number:
        print("you guess correctly")
        break
    #End the game
    elif user_guess > random_number:
        print("try again the random number is lower")
    else:
        print("try again the random number is higher")
