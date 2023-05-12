import random
from generate import random_liste, alternate
from problem_solver import Problème
from data_structures import Liste, Entier


def del_first(level):
    liste = random_liste(level)
    e = liste[0]
    e.name = 'e'
    return liste, e

def del_last(level):
    liste = random_liste(level)
    e = liste[max(0, level - random.randint(1, 2))]
    e.name = 'e'
    return liste, e

def supprime(l, e):
    """ Liste, Entier -> Liste
    l est une liste supposée non vide et e appartient à l
    Supprime de l une occurrence de e. """
    if l.est_singleton():
        return Liste([])
    else:
        t, q = l.divise()
        if e == t:
            return q
        else:
            res = supprime(q, e)
            res = res.ajoute(t)
            return res
            
if not __name__:
    Problème(name = "Supprimer",
             generating_fun = alternate(del_first, del_last),
             problem_funs = [Liste.divise, Liste.ajoute],
             solution_fun = supprime, 
             rec_mode = lambda l, e: len(l))
