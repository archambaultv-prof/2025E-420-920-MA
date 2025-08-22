import math
import itertools

def main():
	# Étape 1 : utiliser un itérateur au lieu d'une liste
	numbers = range(50_000_000)

	# Étape 2 : filtrer les multiples de 7 avec un générateur
	multiples_de_7 = (n for n in numbers if n % 7 == 0)

	# Étape 3 : sélectionner les carrés parfaits dont la racine est paire
	def est_carre_sqrt_pair(n):
		r = math.isqrt(n)
		return r * r == n and r % 2 == 0
	
	carres_sqrt_pair = filter(est_carre_sqrt_pair, multiples_de_7)

	# Étape 4 : transformer avec un générateur
	transformes = ((n // 7) ** 2 for n in carres_sqrt_pair)

	# Étape 5 & 6 combinées : ignorer les 100 premiers et prendre les 100 suivants
	selection_iter = itertools.islice(transformes, 100, 200)

	# Étape 7 : agrégations en une seule boucle
	total = 0
	mini = None
	maxi = None
	count = 0
	
	for n in selection_iter:
		total += n
		count += 1
		if mini is None or n < mini:
			mini = n
		if maxi is None or n > maxi:
			maxi = n
	
	moyenne = total / count if count > 0 else None

	print(f"Somme : {total}")
	print(f"Min/Max : {mini}/{maxi}")
	print(f"Moyenne : {moyenne}")

if __name__ == "__main__":
	main()