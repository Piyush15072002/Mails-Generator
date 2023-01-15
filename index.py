# The mail merging project takes the names in the .txt file and generate emails for those people with their names


# Names
InvitedFighters = open("names.txt")

# Letter Template
letterTemplate = open("letterTemplate.txt")
letter = letterTemplate.read()

# readline() method will return a line from the file when called. 
# readlines() method will return all the lines in a file in the format of a list where each element is a line in the file.


# the list of names
listOfNames = InvitedFighters.readlines()

for name in listOfNames:
    
    # Removing the \n from each name
    fighterName = name.replace("\n", "")

    # To create a new mail for each name => Open in WRITE mode
    with open(f"lettersGenerated/Letter_for_{fighterName}.txt", mode="w") as mail:

        # To replace the [] symbols with fighterName in the letter template
        mail.write(letter.replace("[]", fighterName))

        print(f"Letter generated for {fighterName}")




# Closing files
InvitedFighters.close()
letterTemplate.close()




