def is_prime(n):
    """Vérifie si un nombre est premier."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Vérifier les diviseurs impairs jusqu'à la racine carrée
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_generator():
    """Générateur infini de nombres premiers."""
    yield 2  # Premier nombre premier
    
    n = 3  # Commencer par 3
    while True:
        if is_prime(n):
            yield n
        n += 2  # Ne vérifier que les nombres impairs

# Exemple d'utilisation
if __name__ == "__main__":
    primes = prime_generator()
    
    # Afficher les 20 premiers nombres premiers
    print("Les 20 premiers nombres premiers:")
    for i, prime in enumerate(primes):
        if i >= 20:
            break
        print(prime, end=" ")
    print()
