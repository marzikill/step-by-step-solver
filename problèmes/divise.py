import random
from data_structures import Liste, Entier

problem_name = "divise"
problem_type = "liste -> (liste, liste)"
problem_args = 1
problem_doc = "Étant donné une liste l, renvoie deux listes l1 et l2 construites avec les éléments de l et dont la longueur diffère au plus d'un."
difficulté_type = "la longueur de la liste l"

def génère_entrée(difficulté):
    """ int -> Liste """
    if difficulté == 0:
        return Liste([], name = "l")
    res = [Entier(random.randint(-10, 10))
                          for _ in range(difficulté)]
    return Liste(res, name = "l")

def divise(l):
    """ Liste -> (Liste, Liste) """
    # Les Listes héritent de ce qu'il faut :
    if l.est_vide():
        return l, l
    elif l.est_singleton():
        return l, l.queue()
    else:
        l1, l2 = divise(l.queue().queue())
        l1 = l1.ajoute(l.tete())
        l2 = l2.ajoute(l.queue().tete())
        return l1, l2

# n = 0
# print(génère_entrée(5))
# print(génère_entrée(5))
# print(divise(génère_entrée(n)))
# print(type(divise(génère_entrée(n))))

problème_desc = {
    "name": problem_name,
    "type": problem_type,
    "args_num": problem_args,
    "doc": problem_doc,
    "entrée_fun": génère_entrée,
    "problem_mets": [("divise", 0), ("ajoute", 1)],
    "problem_funs": [],
    # "solution_fun": (minimum, "minimum", 1)
    "solution_fun": (divise, "divise_en_2", 1)
}
