
#generate a random no
#ask the user to make a guss
#if not a valid number print error
#if no <guess print too low 
#  vicevers to > guess
# else print well done
import random
number_to_guess = random.randint(1 ,100)
while True:
  try:
    guess = int(input('guess  the number between 1 and 100: '))
    if guess <number_to_guess:
       print('To low!')
    elif guess > number_to_guess:
       print('too high!')
    else:
       print('congrats you guess the number')
       break
  except ValueError:
    print('please enter a valid number')



   

