from random import *
from math import *
from string import ascii_lowercase, ascii_uppercase
from xmlrpc.client import Boolean

def initialize():
    global alphabet_dict,alphabet_low,alphabet_upp
    alphabet_low,alphabet_upp = list(ascii_lowercase),list(ascii_uppercase)
    alphabet_dict = {"lower":alphabet_low,"upper":alphabet_upp}

def alphabet_randomizer(boolvar:bool, num = None, text = None):
    if num is None and text is None: return alphabet_dict
    if text is None: 
        if num == 0: 
            return alphabet_dict
        num = abs(num)
        rand = num*sqrt(randint(1,500))+num**3
        while rand > len(alphabet_low): 
            rand = (rand/sqrt(randint(1,2)*rand))+sqrt(rand//randint(1,20))
    if num is None:
        val = 0
        for caractere in text:
            val += ord(caractere)
        return alphabet_randomizer(val)
    if bool
    pass

initialize()
alphabet_randomizer(True, None, "Bonjour")