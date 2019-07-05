from random import randint

print('I selected a whole number between 1 and 100. Let\'s see if you can guess it!')

num = randint(1,100)

correct = False
n_guess = 0

while correct == False:
    guess = input('Enter your guess: ')
    guess = int(guess)
    n_guess += 1
    if guess == num:
        correct = True
    elif guess < num:
        print('Too low!')
    elif guess > num:
        print('Too high!')

print('Congratulations! The number was ' + str(num) + '. It took you ' + str(n_guess) + ' guesses to get it.')