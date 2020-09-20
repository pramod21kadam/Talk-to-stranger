from random import *

def searchPartner(sid, rooms):
    for room in rooms:
        if sid in room:
            return room, True
    return None, False

def isprime(num):
    i = 2
    while( i**2 <= num):
        if(num%i == 0):
            return False
        else:
            i += 1
    return True

def generate(n1, n2):
    '''
        n1 - lower limit \n
        n2 - upper limit
    '''
    while(True):
        a = randint(n1, n2)
        if isprime(a):
            return a