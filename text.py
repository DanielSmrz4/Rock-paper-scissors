import random
import math

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''


scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, scissors, paper]

insert = int(input("Zadej 0 pro kámen, 1 pro nůžky, 2 pro papír: "))
user = options[insert]

output = random.randint(0, 2)
computer = options[output]

roll1 = print(f"Hráč\n{user}")
roll2 = print(f"Počítač\n{computer}")


if insert == output:
    print("Remíza hmm, zkus to znova")
elif(insert == 0 and output == 1):
    print("Dobře ty, vyhrál si")
elif (insert == 1 and output == 2):
    print("Dobře ty, vyhrál si")
elif (insert == 2 and output == 0):
    print("Dobře ty, vyhrál si")
else:
    print("Prohráls trapko")



