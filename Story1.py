from Getter import *


def story1(debug= False):
    if debug: print "--In story1 function--"
    
    MaleName = getWord("A Name: ", debug)
    Verbing1 = getWord("A Verb(ing): ", debug) + getIng(debug) 
    Noun1 = getWord("A Noun: ", debug)
    Noun2 = getWord("A Noun: ", debug)
    Verbing2 = getWord("A Verb(ing):", debug)
    Adjective1 = getWord("A Adjective:", debug)
    
    
    
    out = ""
    out += MaleName + " was " + Verbing1 + " when he saw a(n) " + Noun1 + " falling from the sky. "
    out += " There was a huge impact as the " + Noun1 + " crashed into a(n) " + Noun2 + ". "
    out += MaleName + " ran to the site of the impact wondering what he had just witnessed. "
    out += " He saw the " + Noun1 + " at the " + Noun2 + " and noticed that the " + Noun1 + " was " + Verbing2 + ". "
    out += " The " + Noun1 + " started to expand until it exploded in a " + Adjective1 + " plume of smoke. "
    out += " Not sure of what to do, " + MaleName + " returned to his house to resume " + Verbing1 + ". "
    
    
    return out
