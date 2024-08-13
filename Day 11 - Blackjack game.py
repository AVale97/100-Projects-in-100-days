import random
from art import logo

# Draw card function
def deal_card(): 
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#Calculate total function
def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2: #Check for Blackjack
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

#Compare score function
def compare(user_total, dealer_total):
  if user_total == dealer_total:
      return "It's a draw."
  elif dealer_total == 0:
      return "The dealer has Blackjack, you lose."
  elif user_total == 0:
      return "You have Blackjack, you win!"
  elif user_total > 21:
      return "You bust, the dealer wins."
  elif dealer_total > 21:
      return "The dealer busts, you win!"
  elif user_total > dealer_total:
      return "You win!"
  else:
      return "The dealer wins."


def play_game():
  print (logo)
  #Variables
  player_cards = [] 
  dealer_cards = []
  is_game_over = False
  
  # Loop twice to deal two initial cards
  for _ in range(2):
    player_cards.append(deal_card())
    dealer_cards.append(deal_card())
  
  
  while not is_game_over: 
      #Initial score
      player_total = calculate_score(player_cards)
      dealer_total = calculate_score(dealer_cards)
      print(f"Dealer's 1st card: {dealer_cards[0]}")
      print(f"Player cards: {player_cards}, Score: {player_total}")
  
      #Checking if game is over
      if dealer_total == 0 or player_total == 0 or player_total > 21:
        is_game_over = True
      else:
      #Players turn
        hit = input("Do you want to draw another card? Y/N").lower()
        if hit == "y":
          player_cards.append(deal_card())
          player_total = calculate_score(player_cards)
        else:
          is_game_over = True
  
  #Dealer's turn
  if player_total <= 21:
    while dealer_total != 0 and dealer_total < 17:
      dealer_cards.append(deal_card())
      dealer_total = calculate_score(dealer_cards)
  print(f"Dealer's final hand: {dealer_cards}, Final score: {dealer_total}")
  
  # Compare scores and print the result
  print(compare(player_total, dealer_total))

while input("Do you want to play a game? Y/N").lower() == "y":
  print("\n" * 20)
  play_game()
