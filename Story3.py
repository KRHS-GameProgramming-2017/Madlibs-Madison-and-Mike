from Getter import *

def story3(sc=[0], debug= False):
    if debug: print "--In story3 function--"
    
    StarWarsVillain = getSWV("A Star Wars Villain:", debug)
    Adjective = getWord("A Adjective: ", debug)
    Noun = getWord("A Noun: ", debug)
    
    out = ""
    out += "You had been found in the middle of a galactic war between the Republic "
    out += "and the Empire. You had been caught on a spacecraft, on the way to the "
    out += "'Finalizer' for interrogation from the First Order. As the spacecraft came "
    out += "to a halt, " + StarWarsVillain + " came bursting through the door."
    out += " They were " + Adjective + " and highly irritated at " + Noun + "."
    out += " Some blasters came bursting through the door as some of the stormtroopers "
    out += "fell into the ship; and then you began to wonder what you had gotten yourself "
    out += "into."

    return out
