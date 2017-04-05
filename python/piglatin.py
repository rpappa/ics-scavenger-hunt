def englishfcn(): 
    
    engword = raw_input("Enter an English word: ") # an english word will be prompted
    pig = 'ay' #first variable that appends the letters 'ay' to a word
    word = engword.lower()
    first = word[0]
    newword = word + first + pig # creates the pig latin word by moving the first letter to end and appending 'ay'
    newword = newword[1:]
    
    if len(engword) > 0 and engword.isalpha(): # checks if word is a valid input and has no spaces or numbers etc
        print newword # prints the pig latin word to the console
        restart = raw_input("Would you like to enter another word? (y/n): ").lower()  # asks the user if they wish to restart
        if restart == "y":
            langfcn()
        elif restart == "n":
            print "Goodbye!"
        else: 
            print "You didn't choose an option!"
            restart = raw_input("Would you like to enter another word? (y/n): ").lower()
    else: # runs the following events if input is not valid such as numbers or spaces
        print "That's not a valid input!"
        restart = raw_input("Would you like to enter another word? (y/n): ").lower()  # asks the user if they wish to restart
        if restart == "y":
            langfcn()
        elif restart == "n":
            print "Goodbye!"
        else: 
            print "You didn't choose an option!"
            restart = raw_input("Would you like to enter another word? (y/n): ").lower()

def pigfcn():
    pigword = raw_input("Enter a Pig Latin word: ") # a pig latin word will be prompted
    word = pigword.lower()
    newword = word[:-2] # removes the 'ay' from the word
    firstletter = newword[-1:] # holds the value of the last letter
    newword = newword[:-1] # removes the last letter
    newword = firstletter + newword # adds the value of the last letter to the beginning instead of the end
    if pigword == "cavengersay":
        print newword
        print "Use the following question as your next clue..."
        print "Can war change a man?"
        return
    if len(pigword) > 0 and pigword.isalpha():
        print newword 
        restart = raw_input("Would you like to enter another word? (y/n): ").lower()
        if restart == "y":
            langfcn()
        elif restart == "n":
            print "Goodbye!"
        else: 
            print "You didn't choose an option!"
            restart = raw_input("Would you like to enter another word? (y/n): ").lower()
    else: # runs the following events if input is not valid such as numbers or spaces
        print "That's not a valid input!"
        restart = raw_input("Would you like to enter another word? (y/n): ").lower()  # asks the user if they wish to restart
        if restart == "y":
            langfcn()
        elif restart == "n":
            print "Goodbye!"
        else: 
            print "You didn't choose an option!"
            restart = raw_input("Would you like to enter another word? (y/n): ").lower()


print "Welcome to the Pig Latin and English translator!" # introduction phrase

def langfcn(): # defines the function 'langfcn' that allows for the translator to choose a language
        prompt = raw_input("Type your native language as either 'English' or 'Pig' to input a word for translation: ").lower() # allows for input of which language you will be translating from, the .lower() part makes sure that case does not matter in the input 
        if prompt == "english": # if the answer is english, it redirects you to engfcn
            print "You are now translating English to Pig Latin."
            englishfcn()
        elif prompt == "pig": # if the answer is pig it redirects you to pigfcn
            print "You are now translating Pig Latin to English."
            pigfcn()
        else:
            print "Invalid language!"
            langfcn()
langfcn()