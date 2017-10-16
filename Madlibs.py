from Screens import *
from Getter import *
from Story1 import *
from story2 import *

def madlibs(debug = False):
    if debug: print "--Debugging Activated--"
    
    print splash(debug)
    raw_input("Press Enter to Continue")
    
    end = False
    swearCounter = [0]
    while not end:
        print menu(debug)
        response = getMenuResponse(debug)
        
        if response == "q":
            exit()
        elif response == "1":
            print story1(swearCounter, debug)
            raw_input("Press Enter to Continue")
        elif response == "2":
            print story2()
            raw_input("Press Enter to Continue")
            
    
    
madlibs(True)
