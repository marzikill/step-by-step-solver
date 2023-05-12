from problem_solver import Problème
from generate import random_liste
from data_structures import Liste, Entier
from problèmes.insere_triée import insère_triée

def tri_insertion(l):
    """ Liste -> Liste
    Implémente l'algorithme du tri par insertion. """
    # Les Listes héritent de ce qu'il faut :
    L = Liste(sorted(l))
    return L

if not __name__:
    Problème(name = "Tri par insertion (récursif)",
             generating_fun = random_liste,
             problem_funs = [Liste.divise, insère_triée],
             solution_fun = tri_insertion, 
             rec_mode = len)
