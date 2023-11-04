from random import *
from math import *
from string import ascii_lowercase, ascii_uppercase
from xmlrpc.client import Boolean

def initialize():
    global alphabet_dict,alphabet_low,alphabet_upp
    alphabet_low,alphabet_upp = list(ascii_lowercase),list(ascii_uppercase)
    alphabet_dict = {"lower":alphabet_low,"upper":alphabet_upp}

def num_alphabet_randomizer(boolvar:bool, num = None, text = None):
    if num is None and text is None: return alphabet_dict
    
    if boolvar == True and num is not None: 
        if num <= len(alphabet_low): return num
    
    if text is None:   
        if num == 0: return alphabet_dict
        num = abs(num)
        rand = num*sqrt(randint(1,500))+num**3
        while rand > len(alphabet_low)+500: rand = (rand/sqrt(randint(1,2)*rand))+sqrt(rand//randint(1,20))
    
    if (num is None) or (num != None and text != None):
        val = 0
        if num != None and text != None: val += num
        for caractere in text: val += ord(caractere)
        return num_alphabet_randomizer(False, val)
    
    return round(rand)

def new_alphabet(num):
    place, new_alphabet = [], []
    for i in range(len(alphabet_low)):
        val = -i**3/sqrt(num)+randint(5,100)-i/9
        val = round(val)
        val = abs(val)
        while val > len(alphabet_low): 
            val -= len(alphabet_low)
        place.append(val-1)
    print(place)
    for i in range(len(place)): 
        new_alphabet.append(alphabet_low[place[i]])
        
    return {"cle":place,"new_alphabet":new_alphabet}


initialize()
#print(num_alphabet_randomizer(False, 12, "Bonjour"))
print(new_alphabet(num_alphabet_randomizer(False, None, "Bonjour")))
