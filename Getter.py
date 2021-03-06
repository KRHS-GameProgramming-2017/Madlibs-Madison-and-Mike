

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
        if (response == "2" or
            response == "two" or
            response == "story 2"):
                goodInput = True
                response = "2"
        elif (response == "q" or 
              response == "quit" or 
              response == "exit"):
            goodInput = True
            response = "q"
        elif (response == "3" or
              response == "three" or
              response == "story 3"):
            goodInput = True
        elif (response == "secret"):
            goodInput = True
        else:
            print "Please enter a valid input!"
    return response
#Checks word against filters
def getWord(prompt, swearCounter=[0], debug=False):
    if debug: print "--In getWord function--"
    goodInput = False
    while not goodInput:
        #sets response equal to input
        response = raw_input(prompt)
        if isSwear(response):
            goodInput = False
            #Counts and displays messages
            if swearCounter[0] == 0: print "Don't go using that type of language here!"
            elif swearCounter[0] == 1: print "We have already asked you once to stop so please stop using that type of language."
            elif swearCounter[0] == 2: print "Can you even read? If you can, please scroll up a few lines."
            elif swearCounter[0] == 3: print "The program will terminate if you continue to ignore its wishes"
            elif swearCounter[0] == 4: exit()
            swearCounter[0] += 1
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
                 "porn",
                 "damn",
                 "fucking",
                 "shitting"]

    if word.lower() in swearList:
        return True
    else:
        return False
#Political Filter
def isPolitical(word):
    politicalList = ["donald",
                    "trump",
                    "obama",
                    "bernie",
                    "sanders",
                    "bush",
                    "9/11",
                    "hillary",
                    "clinton",
                    "election",
                    "republican",
                    "democrat",
                    "regan",
                    "immigrant"]
    if word.lower() in politicalList:
        return True
    else:
        return False
        
#def isPolitical(word)
    #politicalList = []
    
def getIng(prompt, debug):
    if debug: print "--In getIng function--"
    goodInput= False
    while not goodInput:
        response = raw_input(prompt)
        if len(response) < 3:
            print response + " is not long enough"
        elif response[-3:] == "ing":
            goodInput = True
        else:
            print response + " does not end in ing"
    return response
    
def getEd(prompt, debug):
    if debug: print "--In getEd function"
    goodInput = False
    while not goodInput:
        response = raw_input(prompt)
        if len(response) < 2:
            print response + " is not long enough"
        elif response[-2:] == "ed":
            goodInput = True
        else:
            print response + " dose not end in ed"
    return response

def getSWV(prompt, debug):
    if debug: print "--In getSWV function"
    goodInput = False
    SWV = ["Kylo Ren",
          "Darth Maul",
          "Darth Vader",
          "Count Dooku",
          "Boba Fett",
          "General Grievous",
          "Jabba the Hutt",
          "Darth Bane",
          "Asajj Ventress",
          "Cad Bane",
          "Supreme Leader Snoke",
          "General Hux",
          "The Inquisitor",
          "Darth Nihilus",
          "Sheev Palpatine",
          "Emporer Palpatine",
          "Captain Phasma"]
    while not goodInput:
        response = raw_input(prompt)
        goodInput = True    
        for letter in response:
            if letter not in SWV:
                goodInput = False
                print letter + " this is not a star wars villain"
