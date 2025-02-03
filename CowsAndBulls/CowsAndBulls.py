import random
import sys
import numpy as NumPy

print("Hello and a big Welcome!")
print("Let's play Cows and Bulls!\n")
print("Enter a valid 4-digit number or Enter [Give up] or [quit] : ")


#global data needed
current_random_int = int
trials_so_far = NumPy.array([], dtype=int)
cows = 0
bulls = 0

def generate_current_selection():
    global current_random_int 
    current_random_int = random.randint(1000, 9999)
    current_random_int_as_str = str(current_random_int)
    if len(str(current_random_int)) != len(set(current_random_int_as_str)):
        generate_current_selection()

def input_trial():
    global trials_so_far
        
    #input a 4 digit trial number to guess
    current_trial = input("Input: ")
    if len(current_trial) == 4 and current_trial.isdigit():
        current_trial = int(current_trial)
        if current_trial not in trials_so_far:
            trials_so_far = NumPy.append(trials_so_far, current_trial)
            calculate_cows_and_bulls(current_trial)
    elif current_trial == "quit" or current_trial == "Give up":
        print("The number chosen was - "+ str(current_random_int))
        sys.exit()
    else:
        print("Invalid input. Please enter a 4-digit number.")

def start_game():
    generate_current_selection()
    input_trial()

def calculate_cows_and_bulls(number):
    global cows, bulls, current_random_int 
    current_random_int = str(current_random_int)
    number = str(number)

    if (number == current_random_int):
        print("You won!")
    else:                
        for i in range(4):
            if current_random_int[i] == number[i]:
                bulls += 1
            elif current_random_int[i] in number:
                cows += 1

        print("Cows: " + str(cows))
        print("Bulls: " + str(bulls))
        if (bulls == 4):
            print("You won!")
        else:
            input_trial()


start_game()




