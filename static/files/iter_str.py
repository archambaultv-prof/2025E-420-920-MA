class IterateurUnSurDeux:
    """Itérateur qui parcourt une chaîne en ne renvoyant qu'un caractère sur
    deux."""
    
    def __init__(self, chaine):
        self.chaine = chaine
        self.position = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.position >= len(self.chaine):
            raise StopIteration
        
        caractere = self.chaine[self.position]
        self.position += 2  # Passer au caractère suivant (un sur deux)
        return caractere


# Exemple d'utilisation
if __name__ == "__main__":
    texte = "Bonjour le monde!"
    iterateur = IterateurUnSurDeux(texte)
    
    print("Caractères un sur deux:")
    for char in iterateur:
        print(f"'{char}'", end=" ")
    print()
    
    # Démonstration avec une autre chaîne
    print("\nAvec '0123456789':")
    for char in IterateurUnSurDeux("0123456789"):
        print(char, end="")
    print()
