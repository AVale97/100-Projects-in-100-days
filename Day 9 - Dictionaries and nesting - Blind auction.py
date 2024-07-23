from replit import clear
from art import logo

print (logo)
print("Welcome to the secret auction program")

auction_names = {}
x = True

while x: #loops until there are no more bidders and adds name and bid to dictionary
  name = input("What is your name?")
  bid = int(input("What's your bid? $"))
  auction_names[name] = bid
  more_bids = input ("Are there other users who want to bid?")
  if more_bids.lower() == "no":
    x = False
  else:
    clear() #clear the output in the console

highest_bid = 0
winner = ""

for name, bid in auction_names.items(): #checks highest bid
  if bid > highest_bid:
    highest_bid = bid
    winner = name

print(f"The person with the highest bid is {winner} with a bid of {highest_bid}$")
