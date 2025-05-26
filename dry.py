#CTRL +D provides cursor where we can change any variable at a time with multiple of them
import random 

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

emojis = {'ROCK':'🪨' , 'SCISSOR':'✂️','PAPER':'📃'}
choices = tuple(emojis.keys)
choices = ('ROCK','PAPER','SCISSOR')

while True:
  user_choice = input ('Rock, paper, or scissor? (ROCK/PAPER/SCISSOR):') .lower()
  if user_choice not in choices:
    print('invalid choice')
    continue

  computer_choice = random.choice(choices)

  print (f'you chose {emojis [user_choice]}')
  print (f'computer chose {emojis [computer_choice]}')

  if user_choice == computer_choice:
     print('tie!')
  elif(
    (user_choice == 'ROCK' and computer_choice == 'SCISSOR') or
    (user_choice == 'PAPER' and computer_choice == 'ROCK') or 
    (user_choice == 'SCISSOR' and computer_choice == 'PAPER')):
    print("you win")
  else:
    print('you lose')

  should_continue = input ('conntinue? (y/n)').lower()
  if should_continue == 'n':
    break






