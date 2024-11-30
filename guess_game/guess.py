print('welcome to my computer quiz!') 
playing = input('Do you want to play? (y/n) ').lower()
if playing != 'y':
    quit()
score = 0
print('okay lets play')
answer_1 = input('Are you gay ?').lower()
if answer_1 != 'yes':
    print("wrong answer!!")
elif answer_1 == 'yes':
    print('correct')
    score +=1

answer_2 = input('Are you gay ?').lower()
if answer_2 != 'yes':
    print("wrong answer!!")
elif answer_2 == 'yes':
    print('correct')
    score +=1

answer_3 = input('Are you gay ?').lower()
if answer_3 != 'yes':
    print("wrong answer!!")
elif answer_3 == 'yes':
    print('correct')
    score +=1

answer_4 = input('Are you gay ?').lower()
if answer_4 != 'yes':
    print("wrong answer!!")
elif answer_4 == 'yes':
    print('correct')
    score +=1

print(f'you got {score} quetions correct')