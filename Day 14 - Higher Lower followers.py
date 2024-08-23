import random
from art import logo, vs
from game_data import data



def higherlower():
  print (logo)
  score = 0
  continue_game = True

#First round
  celeb_a = random.choice(data)
  celeb_b = random.choice(data)

  while continue_game:
    # Ensure celeb_b is different from celeb_a
    while celeb_b == celeb_a:
        celeb_b = random.choice(data)

    #Celebs information
    print (f"Compare A: {celeb_a['name']}, a {celeb_a['description']}, from {celeb_a['country']}")
    print (vs)
    print (f"Compare B: {celeb_b['name']}, a {celeb_b['description']}, from {celeb_b['country']}")
    
    celeb_a_followers = celeb_a["follower_count"]
    celeb_b_followers = celeb_b["follower_count"]

    userchoice = input ("Who has more followers? type a or b").lower()

    #Clear screen
    print("\n" * 20)
    print(logo)

    #Check if user is correct
    if (
        (userchoice == "a" and celeb_a_followers > celeb_b_followers) or 
        (userchoice == "b" and celeb_b_followers > celeb_a_followers)
    ):
      
      #If user is correct
      score += 1
      print (f"You're right!, Current score: {score}")
      
      # Update celebrities for the next round
      celeb_a = celeb_b
      celeb_b = random.choice(data)
      # Ensure celeb_b is different from celeb_a
      while celeb_b == celeb_a:
          celeb_b = random.choice(data)
        
    else: #if user is wrong
      continue_game = False
      print (f"You lost, your final score is {score}")

higherlower()
  
    
    
  
