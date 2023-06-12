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
game  = [rock, paper, scissors]
user = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors\n"))
num = game[user]
bot = random.choice(game)
if bot == num:
  print(f"{num} Game is tie")
  print(f"user choice\n {num}\n bot choice\n {bot}")
  
elif num == game[0] and bot == game[2]:
  print("You won")
  print(f"user choice\n {num}\n bot choice\n {bot}")
elif num == game[2] and bot == game[1]:
  print("You won")
  print(f"user choice\n {num}\n bot choice\n {bot}")
elif num == game[1] and bot == game[0]:
  print("You won")
  print(f"user choice\n {num}\n bot choice\n {bot}")
else:
  print("You lose")
  print(f"user choice\n {num}\n bot choice\n {bot}")
  
