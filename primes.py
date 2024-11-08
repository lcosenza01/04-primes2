"""
module primes
"""
import math

def isprime(p):
    """
    fonction principale du module
    """
    sqrt=math.sqrt(p)
    sqrt=int(sqrt)

    for i in range (2,sqrt+1) :
        
        if p%i==0:
            return False
    else:
        return True
