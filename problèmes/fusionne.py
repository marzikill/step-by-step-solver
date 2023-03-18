import random
from problem_solver import Problème
from data_structures import Liste, Entier

problem_name = "fusionne"
problem_type = "liste, liste -> liste"
problem_doc = "Étant donné deux listes l1 et l2, supposées triées par ordre croissant, renvoie la liste l constituée des éléments de l1 et l2 triés par ordre croissant."
difficulté_type = "la longueur de la liste l"

def génère_entrée(difficulté, type_element = [0]):
    """ int -> Liste, Entier """
    if difficulté == 0:
        return Liste([], name = "l1"), Liste([], name = "l2")

    n1 = int(difficulté*(50 + random.randint(-10, 10))/100)
    l1  = sorted([Entier(random.randint(-10, 10))
                    for _ in range(n1)])
    l2  = sorted([Entier(random.randint(-10, 10))
                    for _ in range(difficulté - n1)])
    return Liste(l1, name = "l1"), Liste(l2, name = "l2")

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
    Problème(name = problem_name,
            type = problem_type,
            doc = problem_doc,
            entrée_fun = génère_entrée,
            problem_mets = ["divise", "ajoute"],
            problem_funs = [],
            solution_fun = (fusionne, "fusionne"),
            rec_mode = lambda l1, l2: len(l1) + len(l2))

