import re # imports regex --> string filtering

print "Welcome to the Palindrome tester!"
def strip(string):  # removes characters like numbers or spaces
    return re.sub('[^0-9a-zA-Z]+', '', string)  # this code from stackoverflow --> http://stackoverflow.com/questions/13748674/how-to-use-re-sub

def test(phrase): # fcn that tests if entered phrase is a palindrome
    
    phrase = strip(phrase.lower()) # returns the inputed phrase but lowercase and removing any invalid characters
    
    for i in range(0, int((len(phrase)/2.0))): # essentially divides string by 2, thanks to ryan for help with these 5 lines of code --> https://ide.c9.io/rpappa/ics-python-pappa
        # print phrase[i] + ", " + phrase[len(phrase)-1-i] # compares the letters of the phrase from beginning to end, separated by comma
        if not phrase[i] == phrase[len(phrase)-1-i]: # if the letters are ever not equal, it will be false
            return False
    return True


while True: # loops code indefinitely 
    input = raw_input("Enter a phrase or type 'exit' to terminate: ") # prompts user to enter a word or phrase or to exit
    
    if input == "exit": # code will terminate if exit is typed
        break
    
    pali = test(input); # true if palindrome, false if not
    
    if pali:
        print "Yes, \"" + input + "\" is a palindrome\n" # will confirm in the console that the input was in fact a palindrome
    if input == "No, it can, as it is, it is a war. Raw as it is, it is an action.":
        print "Congratulations. You have reached the end of this scavenger hunt!"
    else:
        print "No, \"" + input + "\" is not a palindrome\n" # will confirm in the console that the input was not a palindrome
