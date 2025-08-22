from collections import deque
from typing import Iterator, Iterable, Tuple, Any

class FenetreGlissante:
    """Itérateur qui renvoie des fenêtres glissantes de taille fixe."""
    
    def __init__(self, iterable: Iterable, taille: int):
        if taille <= 0:
            raise ValueError("La taille doit être positive")
        
        self.iterator = iter(iterable)
        self.taille = taille
        self.window = deque(maxlen=taille)
        self._first_window = True
    
    def __iter__(self) -> Iterator[Tuple[Any, ...]]:
        return self
    
    def __next__(self) -> Tuple[Any, ...]:
        if self._first_window:
            # Remplir la première fenêtre
            try:
                for _ in range(self.taille):
                    self.window.append(next(self.iterator))
                self._first_window = False
                return tuple(self.window)
            except StopIteration:
                raise StopIteration("Pas assez d'éléments pour créer une fenêtre")
        
        # Fenêtres suivantes: ajouter un nouvel élément
        try:
            nouvel_element = next(self.iterator)
            self.window.append(nouvel_element)
            return tuple(self.window)
        except StopIteration:
            raise StopIteration

# Exemple d'utilisation
if __name__ == "__main__":
    # Test avec une liste
    data = [1, 2, 3, 4, 5, 6, 7]
    print("Fenêtres de taille 3:")
    for fenetre in FenetreGlissante(data, 3):
        print(fenetre)
    
    print("\nFenêtres de taille 2:")
    for fenetre in FenetreGlissante("abcdef", 2):
        print(fenetre)
