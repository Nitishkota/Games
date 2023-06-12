# from replit import clear
import os
clear = lambda: os.system('clear')
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program")
next_person = True
previous_bid = 0

bid_list = {}
  
while next_person:
  name = input("What is your name?").lower()
  currrent_bid = int(input("What is your bid?"))
  
  
  bid_list[name] = currrent_bid
  
  dec = input("Are their any others biders? Type Yes or No").lower()
  if previous_bid < currrent_bid:
    previous_bid = currrent_bid
    current_name = name

  if dec == "no":
    next_person = False
    clear()
    print(f"The winner for this auction is {current_name} with a bid of {previous_bid}")
    
  else:
    clear()
    continue
  
# print(bid_list)
    
    