magic_responses = ["It is certain","It is decidedly so","Without a doubt","Yes definitely","You may rely on it","As I see it yes","Outlook good",
"Yes","Signs point to yes","Reply hazy try again","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again",
"Don't count on it","My reply is no","My sources say no","Outlook not so good","Very doubtful", ]; #This is to assign the variable magic_responses to all the possible outcomes in a list

import random #This imports a random phrase from the list

def question(): #this makes question a function-defining the function
    original = raw_input('Ask the Magic 8-Ball a yes or no question: ') #This asks the person to ask a question (asking for an input)
    if original == "Can war change a man?":
        print "Use the following sentence as your next clue:"
        print "No, it can, as it is, it is a war. Raw as it is, it is an action."
        return
    if len(original) > 0: #If the person did not ask a question, this will print 'empty'. If the person did ask a question, it will give a response.
        print(random.choice(magic_responses)) #This prints to the console a random phrase from the list when a question is asked
        restart = raw_input('Do you want to ask the Magic 8-Ball another yes or no question? (Please input yes or no)').lower() #asks the person if they want to ask another question
        if restart == "yes": #if they answer yes, it will ask the original raw input
            question()
        elif restart == "no": #if they answer no, it will send a parting message
            print "The Magic 8-Ball will always be here to guide you."
        else: #if the person entered neither and was being unfunny, it will tell the person they didnt answer
            print "You did not tell the Magic 8-Ball yes or no."
            restart = raw_input('Do you want to ask the Magic 8-Ball another yes or no question? (Please input yes or no)').lower() #asks the person if they want to ask another question
            question()
    
    else:
        print'You did not ask a question.' #if the person puts in nothing, it will say this
        restart = raw_input('Do you want to ask the Magic 8-Ball another yes or no question? (Please input yes or no)').lower() #asks the person if they want to ask another question
        if restart == "yes": #if they say yes it will ask the original raw output
            question()
        elif restart == "no": #if they answer no, it will send a parting message
            print "The Magic 8-Ball will always be here to guide you."
        else: #if the person entered neither and was being unfunny , it will tell the person they didnt answer
            print "You did not tell the Magic 8-Ball yes or no."
            restart = raw_input('Do you want to ask the Magic 8-Ball another yes or no question? (Please input yes or no)').lower()
            question()
question()

