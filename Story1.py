from Getter import *

#mike waz heeerr

def story1(debug= False):
    if debug: print "--In story1 function--"
    
    MaleName = getWord("A Name: ", debug)
    
    
    out = ""
    out += MaleName + "was" + Verbing1 + "when he saw a(n)" + noun1 + "falling from the sky."
    out += "There was a huge impact as the" + noun1 + "crashed into a(n)" + noun2 + "."
    out += MaleName + "ran to the site of the impact wondering what he had just witnessed."
    out += "He saw the" + noun1 + "at the" + noun2 + "and noticed that the" + noun1 + "was" + verbing2 + "."
    out += "The" + noun1 + "started to expand until it exploded in a" + adjective1 + "plume of smoke."
    out += "Not sure of what to do," + MaleName + "returned to his house to resume" + verbing1 + "."
    
    
    return out
