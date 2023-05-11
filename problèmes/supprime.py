import random
from generate import random_liste, alternate
from problem_solver import Problème
from data_structures import Liste, Entier


def del_first(difficulté):
    liste = random_liste(difficulté)
    e = liste[0]
    e.name = 'e'
    return liste, e

def del_last(difficulté):
    liste = random_liste(difficulté)
    e = liste[max(0, difficulté - random.randint(1, 2))]
    e.name = 'e'
    return liste, e

def supprime(l, e):
    """ Liste, Entier -> Liste """
    if l.est_singleton():
        return Liste([])
    else:
        t, q = l.divise()
        if e == t:
            return q
        else:
            res = supprime(q, e)
            res = res.ajoute(t)
            res.name = f"supprime({l.name}, {e.name})"
            return res
            
if not __name__:
    Problème(name = "Supprimer",
             entrée_fun = alternate(del_first, del_last),
             problem_funs = [Liste.divise, Liste.ajoute],
             solution_fun = supprime, 
             rec_mode = lambda l, e: len(l))
