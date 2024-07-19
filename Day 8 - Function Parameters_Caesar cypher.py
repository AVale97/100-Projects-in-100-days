from art import logo
print (logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
  result = ""
  for letter in text:
    if letter in alphabet:
      index = alphabet.index(letter)
      if direction == "encode":
        new_index = (index + shift) % 26
      elif direction == "decode":
        new_index = (index - shift) % 26
      else:
        print ("Invalid direction")
        return
      new_letter = alphabet[new_index]
      result += new_letter
    else:
      result += letter  # Preserve non-alphabet characters
      
    
  print(f"Here's the {direction}d result: {result}")

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(text, shift, direction)

  again = input ("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if again == "no":
    should_continue = False
    print ("Goodbye")
