from random import shuffle
position = ["","X",""]


# Take in list, and returned shuffle versioned
def shuffle_position(a):
    shuffle(a)
    return  a

# Guess the position
def player_guess():
    guess = ""
    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0, 1, or 2:  ")
    return int(guess)
 
# Check the Guess
def check_guess(position,guess):
    if position[guess] == "X":
        print('You won!')
    else:
        print('Sorry! Better luck next time')
        print(position)

#Let's Play
random_position = shuffle_position(position)
guess = player_guess()
check_guess(random_position,guess)
