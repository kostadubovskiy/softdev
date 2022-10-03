"""
Craig Chen, Aaron Gershkovich, Kosta Dubovskiy
SoftDev
04-krewes
-Dictionaries and Random- 
2022-09-22
time spent: 30 minutes
DISCO:
    * The key in the dictionary can be anything, and it's useful for categorization of many things
    * Need to import random with lowercase
    * Need to randint needs two arguments
    * randint is inclusive on both ends
    * random.choice(sequence) returns a random element
QCC:
    * Is there a way to generate a random item from an input list, with a built in random method
OPS SUMMARY:
    * We made a function, that given a dictionary with key:array pairs returns a random element of a random array
"""


krewes = {
           2:["NICHOLAS", "ANTHONY", "BRIAN", "SAMUEL", "JULIA", "YUSHA", "CRAIG", "FANG MIN", "JEFF", "KONSTANTIN", "AARON", "VIVIAN", "AYMAN", "TALIA", "FAIZA", "ZIYING", "YUK KWAN", "DANIEL", "WEICHEN", "MAYA", "ELIZABETH", "ANDREW", "VANSH", "JONATHAN", "ABID", "WILLIAM", "HUI", "ANSON", "KEVIN", "DANIEL", "IVAN", "JASMINE", "JEFFREY", "Ruiwen"], 
           7:["DIANA", "DAVID", "SAM", "PRATTAY", "ANNA", "JING YI", "ADEN", "EMERSON", "RUSSELL", "JACOB", "WILLIAM", "NADA", "SAMANTHA", "IAN", "MARC", "ANJINI", "JEREMY", "LAUREN", "KEVIN", "RAVINDRA", "SADI", "EMILY", "GITAE", "MAY", "MAHIR", "VIVIAN", "GABRIEL", "BRIANNA", "JUN HONG", "JOSEPH", "MATTHEW", "JAMES", "THOMAS", "NICOLE", "Karen"],
           8:["ALEKSANDRA", "NAKIB", "AMEER", "HENRY", "DONALD", "YAT LONG", "SEBASTIAN", "DAVID", "YUKI", "SHAFIUL", "DANIEL", "SELENA", "JOSEPH", "SHINJI", "RYAN", "APRIL", "ERICA", "JIAN HONG", "VERIT", "JOSHUA", "WILSON", "AAHAN", "GORDON", "JUSTIN", "MAYA", "FAIYAZ", "SHREYA", "ERIC", "JEFFERY", "BRIAN", "KEVIN", "SAMSON", "BRIAN", "HARRY", "CORINA", "Wanying", "Kevin"]
         }

import random

def get_devo(dictionary):
    randKey = random.choice(list(dictionary.keys()))
    randDevo = random.randint(0, len(dictionary[randKey]) - 1)
    return (randKey, dictionary[randKey][randDevo])

devo = get_devo(krewes)
print(str(devo[0]) + " " + devo[1])

