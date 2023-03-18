import random
from problem_solver import Problème
from data_structures import Liste, Entier

problem_name = "supprime"
problem_type = "liste, int -> liste"
problem_args = 2
problem_doc = "Étant donné une liste l non vide et un élément e supposé présent dans la liste l, renvoyer la liste des éléments de l où une occurrence de e a été supprimée"
difficulté_type = "la longueur de la liste l"

def génère_entrée(difficulté, type_element = [0]):
    """ int -> Liste """
    if difficulté <= 2:
        return Liste([Entier(random.randint(-10, 10))])

    res = [Entier(random.randint(-10, 10))
                          for _ in range(difficulté)]
    if type_element[0] == 0:
        # l'élément à supprimer est en tête de liste
        type_element[0] = 1
        élément = res[0]
        élément.name = "e"
    else:
        # l'élément à supprimer est en fin de liste
        type_element[0] = 0
        élément = res[random.randint(2, difficulté - 1)]
        élément.name = "e"

    return Liste(res, name = "l"), élément

def supprime(l, e):
    """ Liste, Entier -> Liste """
    if l.est_singleton():
        return Liste([]),
    else:
        t, q = l.divise()
        if e == t:
            return q,
        else:
            res, = supprime(q, e)
            res, = res.ajoute(t)
            res.name = f"supprime({l.name}, {e.name})"
            return res,
            
Problème(name = problem_name,
         type = problem_type,
         doc = problem_doc,
         entrée_fun = génère_entrée,
         problem_mets = ["divise", "ajoute"],
         problem_funs = [],
         solution_fun = (supprime, "supprime"),
         rec_mode = len)
