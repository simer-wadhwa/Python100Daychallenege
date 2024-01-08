#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("../Mail Merge Project Start/Input/Names/invited_names.txt", mode="r") as file:
    data = file.readlines()

with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r") as file:
    letter = file.read()

for name in data:
    name = name.strip()
    file_name = f"../Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt"
    print(file_name)
    with open(file_name, mode="w") as file:
        # updated_letter = letter.replace("[name]" , name)
        updated_letter = letter.replace(PLACEHOLDER, name)
        file.write(updated_letter)


