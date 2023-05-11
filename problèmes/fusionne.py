from problem_solver import Problème
from generate import random_liste
from data_structures import Liste, Entier

def génère_entrée(difficulté):
    l1 = random_liste(difficulté//2)
    l1.name = "l1"
    l2 = random_liste(difficulté//2 + difficulté%2)
    l2.name = "l2"
    return l1, l2

def fusionne(l1, l2):
    """ Liste, Liste -> Liste """
    if l1.est_vide() and l2.est_vide():
        return Liste([])
    elif l1.est_vide():
        return l2
    elif l2.est_vide():
        return l1
    else:
        x1, xs1 = l1.divise()
        x2, xs2 = l2.divise()
        if x1 < x2:
            reste = fusionne(xs1, l2)
            return reste.ajoute(x1)
        else:
            reste = fusionne(l1, xs2)
            return reste.ajoute(x2)

if not __name__:
    Problème(name = "Fusionner", 
            entrée_fun = génère_entrée,
            problem_funs = [Liste.divise, Liste.ajoute],
            solution_fun = fusionne, 
            rec_mode = lambda l1, l2: len(l1) + len(l2))

