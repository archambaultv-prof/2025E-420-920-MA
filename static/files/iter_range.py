class RangeIterator:
    def __init__(self, debut, fin, pas):
        self.debut = debut
        self.fin = fin
        self.pas = pas
        self.current = debut
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.pas > 0:
            if self.current >= self.fin:
                raise StopIteration
        else:
            if self.current <= self.fin:
                raise StopIteration
        
        valeur = self.current
        self.current += self.pas
        return valeur


class Range:
    def __init__(self, debut, fin, pas=1):
        if pas == 0:
            raise ValueError("Le pas ne peut pas être zéro")
        self.debut = debut
        self.fin = fin
        self.pas = pas
    
    def __iter__(self):
        return RangeIterator(self.debut, self.fin, self.pas)


# Exemples d'utilisation
if __name__ == "__main__":
    print("Range(0, 5):")
    for i in Range(0, 5):
        print(i, end=" ")
    print()
    
    print("Range(1, 10, 2):")
    for i in Range(1, 10, 2):
        print(i, end=" ")
    print()
    
    print("Range(10, 0, -1):")
    for i in Range(10, 0, -1):
        print(i, end=" ")
    print()
    
    print("Range(5, 1, -2):")
    for i in Range(5, 1, -2):
        print(i, end=" ")
    print()
