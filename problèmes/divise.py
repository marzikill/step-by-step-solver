import random
from problem_solver import Problème
from generate import random_liste
from data_structures import Liste, Entier

def divise_en_2(l):
    """ Liste -> Liste, Liste
    Étant donnée une liste, la divise en deux listes de
    longueur équivalentes. """
    # Les Listes héritent de ce qu'il faut :
    if l.est_vide():
        return l, l
    elif l.est_singleton():
        return l, l.queue()
    else:
        l1, l2 = divise_en_2(l.queue().queue())
        l1 = l1.ajoute(l.tete())
        l2 = l2.ajoute(l.queue().tete())
        return l1, l2

if not __name__:
    Problème(name = "Diviser",
             entrée_fun = random_liste,
             problem_funs = [Liste.divise, Liste.ajoute],
             solution_fun = divise_en_2, 
             rec_mode=len)
