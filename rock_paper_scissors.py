import random

userName = input("Please enter your username: ")
print(f"Welcome to myGame {userName}.")
print("Game is for 5 points.")
print(f"{userName}, you are now playing against me, try to win me.")

user_score = 0
computer_score = 0

options = ['rock','paper','scissors']

while True:
    user_input = input("Type Rock/Paper/Scissors or 'q' to quit: ").lower()
    
    if user_input == 'q':
        break
    
    if user_input not in options:
        print("Please type the valid option available.")
        continue
        
    random_number = random.randint(0,2)
    computer_input = options[random_number]
    print("Computer picked",computer_input.upper()+".")
    
    if user_input == 'rock' and computer_input == 'scissors':
        print(f"{userName}, you won this round.")
        user_score += 1
        
    elif user_input == 'paper' and computer_input == 'rock':
        print(f"{userName}, you won this round.")
        user_score += 1
        
    elif user_input == 'scissors' and computer_input == 'paper':
        print(f"{userName}, you won this round.")
        user_score += 1
        
    else:
        print(f"{userName}, you lost this round.")
        computer_score += 1
        
    if user_score + computer_score == 5:
        break
        
        
print("\nGame Over!")

if user_score > computer_score:
    print("Congratulations, you are the winner!")
elif user_score < computer_score:
    print("Better luck next time, computer is the winner.")
else:
    print("It's a tie!")
    
print(f"{userName}, you scored {user_score}.")
print(f"Computer scored {computer_score}.")

print("\nThanks for playing.")