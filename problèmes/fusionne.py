from problem_solver import Problème
from generate import random_liste
from data_structures import Liste, Entier

def génère_entrée(level):
    l1 = random_liste(level//2)
    l1.name = "l1"
    l2 = random_liste(level//2 + level%2)
    l2.name = "l2"
    return l1, l2

@Problème.recursive(lambda l1, l2: len(l1) + len(l2))
def fusionne(l1, l2):
    """ Liste, Liste -> Liste
    Étant donné deux listes l1 et l2 supposées triées toutes les deux,
    renvoyer une liste constituée des éléments de l1 et de l2 triés
    par ordre croissant. """
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
            generating_fun = génère_entrée,
            problem_funs = [Liste.divise, Liste.ajoute],
            solution_fun = fusionne)

