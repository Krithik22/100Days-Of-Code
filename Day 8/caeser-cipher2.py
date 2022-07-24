alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

last_index_of_list=len(alphabet)-1
def encrypt(plain_text, shift_amount):
  encrypted_message=''
  for letter in text:
    position=alphabet.index(letter)
    new_position = position + shift
    if new_position > last_index_of_list:
      diff=new_position - last_index_of_list
      diff=shift-diff
      if diff == 0:
        new_position = shift-1
      else:
        new_position = diff
    encrypted_message+=alphabet[new_position]
  print(f"The encrypted message is {encrypted_message}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

def decrypt(encoded_text,shift_amount):
  decoded_message=''
  for letter in encoded_text:
    position = alphabet.index(letter)
    if position == (shift_amount-1):
      new_position = last_index_of_list
    elif position < shift_amount:
      diff = shift_amount - position
      new_position = last_index_of_list - (diff - 1)
    else:
      new_position = position - shift_amount
    decoded_message += alphabet[new_position]
  print(f"The decrypted message is {decoded_message}")

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

if direction == 'encode':
  encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
  decrypt(encoded_text=text, shift_amount=shift)