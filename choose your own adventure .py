
name = input("type your name: ")
print("welcome", name, "to this adventure!")
answer = input("you are on a road, it has come to an end and you can either go left or right. which way you want to go?").lower()

if answer == "left":
    q2 = input("you have reached a den , you can pass through it or either not?type pass to pass through and not to not to pass(pass/not pass):")
    if q2 == "pass":
        print("you went into the den and got caught with the dragon and got incriminated.")
    elif q2 == "not pass":
        print("you just fell into the trap of a witch and just got sacrificed to her ritual")
    else:
        print ("not a valid option. you lose.")


elif answer=="right":
    q3 = input("you have reached a dense spirited foest, it has mythical creatures in it.do you wanna go inside or just stay out of it (go/stay) ?")
    if q3== "stay":
        print("you stayed and lost the game")
    elif q3 == "go":
      q3 = input("you have found a rare mythical creature called tyrain and befriended it. Do you want to continue or not (yes/no)?")
      if q3 == "yes":
          print("you have completed the journey by finding the tyrain and got yourself a power and became the strongest rider and YOU WIN!")
      elif q3== "no":
          print == ("you ignored the tyrain and LOST the game")
      else: 
          print ("not a valid option. you lose.") 
    else:
        print ("not a valid option. you lose.")            

    
else:
    print ("not a valid option. you lose.")


print ("THANK YOU FOR TRYING BETTER LUCK NEXT TIME", name) 