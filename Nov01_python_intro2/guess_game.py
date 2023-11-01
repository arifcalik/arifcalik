import random 

def start_game():
    goOn = 'y'
    play_game(goOn)

def play_game(goOn):
    digits = list(range(10)) 
    while goOn[0].lower() == 'y':
        while digits[0] == 0:
            random.shuffle(digits)
        print(digits[:3])    
        
        guess = input("What is your guess? ") 

        while len(guess) != 3 or guess[0] == guess[1] or guess[0] == guess[2] or guess[1] == guess[2]:
            print('All digits are different and 3digits number required!')
            guess = input("What is your guess? ") 

        if guess == ''.join(str(digit) for digit in digits[:3]):
            print('You guessed it correctly!')
            goOn = input('Do you want to play again(y/n) : ')
            if goOn[0].lower() == 'y':
                digits = list(range(10))       
        else:
            #give clues
            print('Here are your clues:')
            correctPlaces = 0
            incorrectPlaces = 0

            for index, c in enumerate(guess):
                if c == str(digits[:3][index]):
                    correctPlaces += 1
                elif c  in str(digits[:3]):
                    incorrectPlaces += 1
            print('\033[2;31;43m You have {} digits in correct places and\n \033[0;0m'.format(correctPlaces))
            print('\033[2;31;43m You have {} digits in incorrect places!\n \033[0;0m'.format(incorrectPlaces))
            if correctPlaces == 0 and incorrectPlaces == 0:
                print("\033[2;31;43m Nothing matches! \033[0;0m")

start_game()