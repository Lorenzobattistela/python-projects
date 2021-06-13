import random

def main():
    print("Hello! Let's play ROCK PAPER SCISSORS!")
    user_choice = 'rock' #input("Rock, paper or scissors? ").lower()
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    compare_choices(user_choice, computer_choice)

def compare_choices(user, computer):
    if user == computer:
        print('It is a tie!')
    elif user == 'rock' and computer == 'paper' or user == 'paper' and computer == 'scissors' or user == 'scissors' and computer == 'rock':
        print('Computer won!')
    elif user == 'rock' and computer == 'scissors' or user == 'paper' and computer == 'rock' or user == 'rock' and computer == 'scissors':
        print('User won!')
    else:
        print('Option not included in the game. Be sure to type it correctly.')


if __name__ == '__main__':
    main()
