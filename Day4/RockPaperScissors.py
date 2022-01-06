import random

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

#Write your code below this line 👇
items = [rock, paper, scissors]

choosing = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print(items[choosing])


rand = random.randint(0, 2)

print("Computer chose:")
print(items[rand])

if choosing == rand:
    print("You draw")
elif choosing == 0:
    if rand == 1:
        print("You lose")
    else:
        print("You win")
elif choosing == 1:
    if rand == 2:
        print("You lose")
    else:
        print("You win")
elif choosing == 2:
    if rand == 0:
        print("You lose")
    else:
        print("You win")