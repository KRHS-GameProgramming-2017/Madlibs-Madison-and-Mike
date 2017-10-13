

swearCounter = 0

#Handles Menues
def getMenuResponse(debug = False):
    if debug: print "--In getMenuResponse function--"
    goodInput = False
    while not goodInput:
        response = raw_input("Make a selection please: ")
        if (response == "1" or 
            response == "one" or 
            response == "story 1"):
                goodInput = True
                response = "1"
        elif (response == "q" or 
              response == "quit" or 
              response == "exit"):
            goodInput = True
            response = "q"
        else:
            print "Please enter a valid input!"
    return response
#Checks word against filters
def getWord(prompt, debug):
    if debug: print "--In getWord function--"
    goodInput = False
    while not goodInput:
        #sets response equal to input
        response = raw_input(prompt)
        if isSwear(response):
            goodInput = False
            #Counts and displays messages
            if swearCounter == 0: print "Don't go using that type of language here!"
            elif swearCounter == 1: print "We have already asked you once to stop so please stop using that type of language."
            elif swearCounter == 2: print "Can you even read? If you can, please scroll up a few lines."
            elif swearCounter == 3: print "The program will terminate if you continue to ignore its wishes"
            elif swearCounter == 4: exit()
            swearCounter += 1
        #Tests for no input
        elif response == "":
            goodInput = False
            print "Type something"
        #Test for politics
        elif isPolitical(response):
            goodInput = False
            print "Leave politics out of it."
        #Makes it good input
        else:
            goodInput = True
    return response
#Makes sure  input is a number
def getNumber(prompt, debug):
    if debug: print "--In getWord function--"
    goodInput = False
    numbers = "1234567890."
    while not goodInput:
        response = raw_input(prompt)
        goodInput = True    
        for letter in response:
            if letter not in numbers:
                goodInput = False
                print letter + " is not a number"
    return response 
#Swear Filter
def isSwear(word):
    swearList = ["poop",
                 "dumb",
                 "stupid",
                 "fuck",
                 "shit",
                 "crap",
                 "bitch",
                 "cunt",
                 "slut",
                 "ass",
                 "nigger",
                 "fucker",
                 "sex",
                 "porn"]

    if word.lower() in swearList:
        return True
    else:
        return False
#Political Filter
def isPolitical(word):
    politicalList = ["Donald", "Trump", "Obama", "Bernie", "Sanders", "Bush", "9/11", "Hillary", "Clinton", "Election", "republican", "democrat", "Regan", ]
    

    if word.lower() in politicalList:
        return True
    else:
        return False
        
#def isPolitical(word)
    #politicalList = []
    
def getIng(prompt, debug):
    if debug: print "--In getIng function--"
    goodInput= False
    ing= "ing"
    while not goodInput:
        response = raw_input(prompt)
        goodInput = True
        for letter in response:
            if letter not in ing:
                goodInput = False
                print letter + " does not end in ing"
    return response
    
	

