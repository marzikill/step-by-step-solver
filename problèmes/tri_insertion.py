import random
from problem_solver import Problème
from data_structures import Liste, Entier
from problèmes.insere_triée import insère_triée

problem_name = "tri_insertion"
problem_type = "liste -> liste"
problem_args = 1
problem_doc = "Étant donné une liste l renvoyer la liste des éléments de l triés par ordre croissant."
difficulté_type = "la longueur de la liste l"

def génère_entrée(difficulté):
    """ int -> Liste """
    if difficulté == 0:
        return Liste([])
    res = [Entier(random.randint(-10, 10))
                          for _ in range(difficulté - 1)]
    # la tête est à insérer vers la fin de la liste
    res = [Entier(max(res).n - random.randint(1, 5))] + res
    return Liste(res, name = "l")

def tri_insertion(l):
    """ Liste -> Liste """
    # Les Listes héritent de ce qu'il faut :
    L = Liste(sorted(l))
    return L

if not __name__:
    Problème(name = problem_name,
            type = problem_type,
            doc = problem_doc,
            entrée_fun = génère_entrée,
            problem_mets = ["divise"],
            problem_funs = [(insère_triée, "insère_triée")],
            solution_fun = (tri_insertion, "tri_insertion"),
            rec_mode = len)
