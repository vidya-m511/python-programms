
#ask the user to make a choice
# if choice is not valid print error
# let comp make a choice
#print choice emojis 
# determine the winner
# ask the user if they want to contiue the game
#if not terminate
import random 

emojis = {'r':'🪨' , 's':'✂️','p':'📃'}
choices = ('r','p','s')

while True:
  user_choice = input ('Rock, paper, or scissor? (r/p/s):') .lower()
  if user_choice not in choices:
    print('invalid choice')
    continue

  computer_choice = random.choice(choices)

  print (f'you chose {emojis [user_choice]}')
  print (f'computer chose {emojis [computer_choice]}')

  if user_choice == computer_choice:
     print('tie!')
  elif(
    (user_choice == 'r' and computer_choice == 's') or
    (user_choice == 'p' and computer_choice == 'r') or 
    (user_choice == 's' and computer_choice == 'p')):
    print("you win")
  else:
    print('you lose')

  should_continue = input ('conntinue? (y/n)').lower()
  if should_continue == 'n':
    break






