def splash(debug = False):
	if debug: print "--In splash function--"
	output = ""
	output += "***************************************\n"
	output += "*                                     *\n"
	output += "*        Welcome to Madlibs           *\n"
	output += "*           Written by                *\n"
	output += "*         Chris Spooner               *\n"
	output += "*                                     *\n"
	output += "***************************************\n"
	return output

def menu(debug = False):
	if debug: print "--In menu function--"
	output = ""
	output += "***************************************\n"
	output += "*Main menu                            *\n"
	output += "*1) A story                           *\n"
	output += "*2)                                   *\n"
	output += "*3)                                   *\n"
	output += "*Q) Exit                              *\n"
	output += "***************************************\n"
	return output
