import random
from generate import random_liste, alternate
from problem_solver import Problème
from data_structures import Liste, Entier

def insert_first(level):
    liste = sorted(random_liste(level))
    val = liste[0].content - random.randint(1, 5)
    return Liste(liste, name = "l"), Entier(val, name = "e")

def insert_last(level):
    liste = sorted(random_liste(level))
    val = liste[-1].content - random.randint(1, 5)
    return Liste(liste, name = "l"), Entier(val, name = "e")

def insère_triée(l, e):
    """ Liste, Entier -> Liste
    l est une liste supposée triée par ordre croissant.
    Renvoie une liste constituée des éléments de l et de e
    triés par ordre croissant. """
    # Les Listes héritent de ce qu'il faut :
    l = l.ajoute(e)
    l = sorted(l)
    return Liste(l)

if not __name__:
    Problème(name = "Insérer (liste triée)",
             generating_fun = alternate(insert_first, insert_last),
             problem_funs = [Liste.divise, Liste.ajoute],
             solution_fun = insère_triée, 
             rec_mode = lambda l, e: len(l))
