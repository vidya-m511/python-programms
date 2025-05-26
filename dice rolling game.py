import random

while True:
  choice = input("roll the dice? (y/n):").lower()
  if choice == "y" :
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print(f"({die1},{die2})")
  elif choice == "n" :
    print ("thanks for playing!")
    break
  else:
    print("invalid choice!")
  


   #ask : roll the dice
# if users enters y
# generate two random numbers
# print them
#if users enters n 
# print thank you message and terminate
#else 
# print error