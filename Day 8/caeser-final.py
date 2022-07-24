alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

def caeser(caeser_direction, message, shift_amount):
  final_message=''
  if caeser_direction == 'decode':
    shift_amount *= 1
  for letter in message:
    position = alphabet.index(letter)
    new_position = position + shift
    final_message+=alphabet[new_position]
  print(f"The {caeser_direction}d message is {final_message}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caeser(caeser_direction = direction, message=text, shift_amount=shift)

 
      