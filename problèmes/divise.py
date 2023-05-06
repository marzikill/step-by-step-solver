import random
from problem_solver import Problème
from data_structures import Liste, Entier

problem_name = "divise_en_2"
problem_type = "liste -> (liste, liste)"
problem_doc = "Étant donné une liste l, renvoie deux listes l1 et l2 construites avec les éléments de l et dont la longueur diffère au plus d'un."
difficulté_type = "la longueur de la liste l"

def génère_entrée(difficulté):
    """ int -> Liste """
    if difficulté == 0:
        return Liste([], name = "l")
    res = [Entier(random.randint(-10, 10))
                          for _ in range(difficulté)]
    return Liste(res, name = "l")

def divise_en_2(l):
    """ Liste -> Liste, Liste """
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
    Problème(name = problem_name,
            type = problem_type,
            doc = problem_doc,
            entrée_fun = génère_entrée,
            problem_mets = ["divise", "ajoute"],
            problem_funs = [],
             solution_fun = (divise_en_2, "divise_en_2"),
             rec_mode=len)
