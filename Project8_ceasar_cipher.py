from extra_files import art

print(art.logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']




#
# # TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
#
# # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# # e.g.
# # plain_text = "hello"
# # shift = 5
# # cipher_text = "mjqqt"
# # print output: "The encoded text is mjqqt"
#
# ##HINT: How do you get the index of an item in a list:
# # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
#
# ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
# def encrypt(text, shift):
#     # text = list(text)
#     cipher_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position + shift
#         if new_position>25:
#            new_position=new_position-26
#         cipher_text += alphabet[new_position]
#     print(f" The encoded text : {cipher_text}")
#
#
# #TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
#
#   #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
#   #e.g.
#   #cipher_text = "mjqqt"
#   #shift = 5
#   #plain_text = "hello"
#   #print output: "The decoded text is hello"
#
# def decrypt(cipher_text, shift):
#     text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift
#         text += alphabet[new_position]
#     print(f" The decoded text : {text}")
#
#
#
#
#
#
#
# #TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message
#
#
# if direction.lower() == "encode":
#     encrypt(text, shift)
# elif direction.lower() == "decode":
#     decrypt(text,shift)
# else :
#     print("Please select encode or decode")
#

# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.




def ceasar(text, shift, direction):
    end_text = ""
    #if shift > 26:
        #shift = shift%26
    if direction.lower() == "decode":
        shift *= -1

    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)

            new_position = position + shift
            if new_position > 25:
                new_position = new_position - 26
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f" The {direction}d text : {end_text}")

#restart = "yes"
should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    ceasar(text, shift, direction)
    restart = input(". Type 'yes' if you want to go again. Otherwise type 'no' ")
    if restart.lower() == "no":
        should_end = True
        print("Goodbye")
