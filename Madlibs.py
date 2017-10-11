# Written by Chris Spooner
from Screens import *
from Getter import *
from Story1 import *

def madlibs(debug = False):
	if debug: print "--Debugging Activated--"
	
	print splash(debug)
	raw_input("Press Enter to Continue")
	
	end = False
	while not end:
		print menu(debug)
		response = getMenuResponse(debug)
		
		if response == "q":
			exit()
		elif response == "1":
			print story1()
			raw_input("Press Enter to Continue")
			
	
	
madlibs(True)
