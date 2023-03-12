import random
from data_structures import Liste, Entier

problem_name = "minimum"
problem_type = "liste -> int"
problem_args = 1
problem_doc = "Étant donné une liste l non vide renvoyer le plus petit élément de l"
difficulté_type = "la longueur de la liste l"

def génère_entrée(difficulté, type_element = [0]):
    """ int -> Liste """
    if difficulté <= 1:
        return Liste([Entier(random.randint(-10, 10))])

    res = [Entier(random.randint(-10, 10))
                          for _ in range(difficulté - 1)]
    if type_element[0] == 0:
        # le minimum est le dernier élément de la liste
        type_element[0] = 1
        res =  res + [Entier(min(res).n - random.randint(1, 5))]
    else:
        # le minimum est le premier élément de la liste
        type_element[0] = 0
        res =  [Entier(min(res).n - random.randint(1, 5))] + res

    return Liste(res,
                 name = "l"),

def minimum(l):
    """ Liste -> Liste """
    # Les Listes héritent de ce qu'il faut :
    m = min(l)
    return Entier(m,
                  name = f"minimum({l.name})"),

# print(génère_entrée(5))
# print(génère_entrée(5))
# n = 2
# print(tri_insertion(*génère_entrée(n)))
# print(type(tri_insertion(*génère_entrée(n))))

problème_desc = {
    "name": problem_name,
    "type": problem_type,
    "args_num": problem_args,
    "doc": problem_doc,
    "entrée_fun": génère_entrée,
    "problem_mets": [("divise", 0)],
    "problem_funs": [],
    "solution_fun": (minimum, "minimum", 1)
}
