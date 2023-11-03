import random 

def start_game():
    goOn = 'yes'
    play_game(goOn)

def getSecretNumber():
    digits = list(range(10)) 
    while digits[0] == 0:
        random.shuffle(digits)
    return digits[:3]

def evaluateGuess(digits, guess):
    #give clues
    print('Here are your clues:')
    correctPlaces = 0
    incorrectPlaces = 0

    for index, c in enumerate(guess):
        if c == str(digits[index]):
            correctPlaces += 1
        elif c  in str(digits):
            incorrectPlaces += 1
    print('\033[2;31;43m You have {} digits in correct places and\n \033[0;0m'.format(correctPlaces))
    print('\033[2;31;43m You have {} digits in incorrect places!\n \033[0;0m'.format(incorrectPlaces))
    if correctPlaces == 0 and incorrectPlaces == 0:
        print("\033[2;31;43m Nothing matches! \033[0;0m")

def checkValidity():
        exceptionOccured = True
        while exceptionOccured:
            try:
                guess = input("Guess the number whose digits are unique(123)? ")
                guessNumber = int(guess)

                while len(guess) != 3 or guess[0] == guess[1] or guess[0] == guess[2] or guess[1] == guess[2]:
                    print('All digits are different and 3-digits number required!')
                    raise ValueError
            except ValueError as e:
                print("3-digits number required as a guess!")
                exceptionOccured = True
            else:
                exceptionOccured = False
                print("Your guess will be evaluated!")
        return guess

def play_game(goOn):
    '''
    simple guess game
    computer throws a 3-digit number between 102 and 987 whose digits are unique
    and you try to guess it with the given clues which are
    1.no match
    2.digits in correct places
    3.digits in incorrect places
    '''
    digits = getSecretNumber()
    while goOn[0].lower() == 'y':
        guess = checkValidity()

        if guess == ''.join(str(digit) for digit in digits):
            print('You guessed it correctly!')
            goOn = input('Do you want to play again(y)? : ')
            if goOn[0].lower() == 'y':
                digits = getSecretNumber()
        else:
            evaluateGuess(digits, guess)

def main():
    start_game()

if __name__ == '__main__':
    main()