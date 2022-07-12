placeholder="[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names=names_file.readlines()  #https://www.w3schools.com/python/ref_file_readlines.asp

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents=letter_file.read()
    for name in names:
        stripped_name=name.strip()  #https://www.w3schools.com/python/ref_string_strip.asp
        new_letter=letter_contents.replace(placeholder,stripped_name)  #https://www.w3schools.com/python/ref_string_replace.asp
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt",mode="w") as completed_letter:
            completed_letter.write(new_letter)

