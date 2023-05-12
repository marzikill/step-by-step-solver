from problem_solver import Problème
from generate import random_liste
from problèmes.minimum import minimum
from problèmes.supprime import supprime
from data_structures import Liste, Entier

def tri_sélection(l):
    """ Liste -> Liste """
    L = Liste(sorted(l))
    return L
            
if not __name__:
    Problème(name = "Tri par sélection (récursif)",
             entrée_fun = random_liste,
             problem_funs = [Liste.ajoute, supprime, minimum],
             solution_fun = tri_sélection, 
             rec_mode = len)
