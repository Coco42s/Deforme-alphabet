from random import *
from math import *
from string import ascii_lowercase, ascii_uppercase

alphabet_low,alphabet_upp = list(ascii_lowercase),list(ascii_uppercase)

def val_alea_mail():
    num = randint(2,4800)
    rand = num*sqrt(randint(1,5000))+num**3
    val = round(rand)
    val = abs(val)
    while val > 999999 or val < 100000:
        toto = randint(9000,1200000)
        if  val > 9999: val -= toto
        if  val < 1000: val += toto
    return val
