from random import random

from graph import Graphique

# Simulation écchantillonnage population de cistudes.
# Prob cistude femelle : 0.37
PROB_FEMELLE = 0.37
MALE = 1
FEMELLE = 0


def echantillonnage(taille_echantillon: int = 100):
	echantillon = []
	for i in range(taille_echantillon):
		if random() > PROB_FEMELLE:
			echantillon.append(MALE)
		else:
			echantillon.append(FEMELLE)
	return echantillon


def nombre_de_femelles(echantillon: list[int]):
	n_femelles = 0
	for resultat in echantillon:
		if resultat == FEMELLE:
			n_femelles += 1
	return n_femelles


def moyenne(nb_femelles: list[int]):
	total = 0
	taille = len(nb_femelles)
	for n in nb_femelles:
		total += n
	m = total / taille
	return m


def get_graph(taille_echantillon: int, nombre_echantillons_par_serie: int):
	Graphique(x_axis=[i + 1 for i in range(nombre_echantillons_par_serie)],
			  y_axis=[nombre_de_femelles(echantillonnage(taille_echantillon)) / taille_echantillon for _ in
					  range(nombre_echantillons_par_serie)],
			  xlabel='Echantillon',
			  ylabel='Proportion de femelles',
			  title=f"Proportion de femelles dans des échantillons de {taille_echantillon} individus")


get_graph(taille_echantillon=100, nombre_echantillons_par_serie=100)
get_graph(taille_echantillon=1000, nombre_echantillons_par_serie=100)
get_graph(taille_echantillon=10000, nombre_echantillons_par_serie=100)
Graphique.afficher()
