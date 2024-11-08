import math
def isprime(p):
    """ 
    Revoie la valeur de vérité de l'affirmation p est premier
    """
    if p==1:
        return False
    sqrt=int(math.sqrt(p))
    for i in range (2,sqrt+1) :
        if p%i==0:
            return False
    return True
#### Fonction principale
def main():
    """
    Appel principal de la méthode isprime
    """
    # vos appels à la fonction secondaire ici
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()

if __name__ == "__main__":
    main()