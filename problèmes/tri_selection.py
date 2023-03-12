import random
from problèmes.minimum import minimum
from problèmes.supprime import supprime
from data_structures import Liste, Entier

problem_name = "tri_sélection"
problem_type = "liste -> liste"
problem_args = 1
problem_doc = "Étant donné une liste l, renvoyer la liste des éléments de l triés par ordre croissant avec la méthode du tri par sélection"
difficulté_type = "la longueur de la liste l"

def génère_entrée(difficulté, type_element = [0]):
    """ int -> Liste """
    if difficulté <= 1:
        return Liste([Entier(random.randint(-10, 10))])

    res = [Entier(random.randint(-10, 10))
                          for _ in range(difficulté - 1)]
    res = res + [Entier(min(res).n - random.randint(1, 5))]

    return Liste(res, name = "l"), 

def tri_sélection(l):
    """ Liste -> Liste """
    L = Liste(sorted(l))
    return L,
            
problème_desc = {
    "name": problem_name,
    "type": problem_type,
    "args_num": problem_args,
    "doc": problem_doc,
    "entrée_fun": génère_entrée,
    "problem_mets": [("divise", 0), ("ajoute", 1)],
    "problem_funs": [(supprime, "supprime", 2), (minimum, "minimum", 1)],
    "solution_fun": (tri_sélection, "tri_sélection", 1)
}
