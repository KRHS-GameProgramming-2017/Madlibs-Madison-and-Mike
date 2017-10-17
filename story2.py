from Getter import *

def story2(debug= False):
    if debug: print "--In story2 function--"
    
    FantasyCreature = getWord("A Fantasy Creature: ", debug)
    Animal = getWord("A Animal: ", debug)
    VerbEd1 = getEd("A verb(ed): ", debug)
    Verbing1 = getIng("A Verb(ing): ", debug)
    Place = getWord("A Place: ", debug)
    
    
    out = ""
    out += "The " + FantasyCreature + " was roaming in the woods when it came acrossed a wild "
    out += Animal + ", it " + VerbEd1 + " when they made eye contact. They stood staring at each other for a long "
    out += "time until the " + Animal + " suddenly began " + Verbing1 + ". The " + FantasyCreature + " began to follow the animal "
    out += "wherever it went. They went all the way to the " + Place  

    return out
