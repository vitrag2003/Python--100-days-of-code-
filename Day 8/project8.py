import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift,direction):
    if direction=="encode":
        cipher_text = ""
        for char in text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift
                cipher_text += alphabet[new_position]
            else:
                cipher_text+=char
        print(f"The encoded text is {cipher_text}")

    elif direction == "decode":
        plain_text = ""
        for char in text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position - shift
                plain_text += alphabet[new_position]
            else:
                plain_text+=char   
        print(f"The decoded text is {plain_text}")

    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    #SOLUTION- LINES(7-11 AND 19-22)

#TODO-1: Import and print the logo from art.py when the program starts.
print(art.logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

should_continue=True
while should_continue==True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
    #Hint: Think about how you can use the modulus (%).
    shift =shift%26 #(26 alphabets)

    caesar(text,shift,direction)

    choice=input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
    if choice=="no":
        should_continue=False
        print("Thank you. The code has ended")
