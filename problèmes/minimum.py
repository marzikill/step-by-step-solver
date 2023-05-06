import random
from problem_solver import Problème
from data_structures import Liste, Entier

problem_name = "minimum"
problem_type = "liste -> int"
problem_doc = "Étant donné une liste l non vide renvoyer le plus petit élément de l"
difficulté_type = "la longueur de la liste l"

def génère_entrée(difficulté, case = [0]):
    """ int -> Liste """
    if difficulté <= 1:
        return Liste([Entier(random.randint(-10, 10))])

    res = [Entier(random.randint(-10, 10))
                          for _ in range(difficulté - 1)]
    if case[0] == 0:
        # le minimum est le dernier élément de la liste
        case[0] = 1
        res =  res + [Entier(min(res).n - random.randint(1, 5))]
    else:
        # le minimum est le premier élément de la liste
        case[0] = 0
        res =  [Entier(min(res).n - random.randint(1, 5))] + res
    return Liste(res, name = "l")

def minimum(l):
    """ Liste -> Entier 
    Étant donné une liste l non vide, renvoyer le plus petit élément de l """
    # Les Listes héritent de ce qu'il faut :
    m = min(l)
    return m
                  
if not __name__:
    Problème(name = problem_name,
            type = problem_type,
            doc = problem_doc,
            entrée_fun = génère_entrée,
            problem_mets = ["divise"],
            problem_funs = [],
            solution_fun = (minimum, "minimum"),
            rec_mode = len)
