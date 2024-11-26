import random  

top_of_range = input('type a number: ')
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print('Please type a number larger than 0 next time')
        quit()
else:
    print("enter a number next time")
    quit( )
random_number = random.randint(0, top_of_range)
guess = 0
while True: 
    guess = guess + 1
    make_guess = input('Guess the number: ')
    if make_guess.isdigit():
        make_guess = int(make_guess)
    
    else:
        print("enter a number next time")
        continue
    if make_guess == random_number:
        print('You got it!')
        break
    else:
        if make_guess > random_number:
            print('you where above the number')
        else: 
            print("you are below")
        
print("you got it in", guess, "guesses")
        