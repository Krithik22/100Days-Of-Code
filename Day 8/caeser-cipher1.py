alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
list_length=len(alphabet)-1
def encrypt(text, shift):
  encrypted_message=''
  for letter in text:
    position=alphabet.index(letter)
    new_position = position + shift
    #The below section is used to overcome the bug of letters that come last like word 'zulu'
    if new_position > list_length:
      diff=new_position - list_length
      diff=shift-diff
      if diff == 0:
        new_position = shift-1
      else:
        new_position = diff
    #The above section is used to overcome the bug of letters that come last like word 'zulu'
    encrypted_message+=alphabet[new_position]
  print(encrypted_message)
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"


#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(text, shift)

    ##ðBug alert: What happens if you try to encode the word 'civilization'?ð
