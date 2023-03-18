import random
from problem_solver import Problème
from data_structures import Liste, Entier

problem_name = "insere_trie"
problem_type = "liste, int -> liste"
problem_doc = "Étant donné une liste l triée par ordre croissant et un élément e, renvoyer la liste où l'élément e a été inséré dans l de telle sorte que la liste, résultante soit triée"
difficulté_type = "la longueur de la liste l"

def génère_entrée(difficulté, type_element = [0]):
    """ int -> Liste, Entier """
    # Lors des appels successifs, la fonction génère une fois sur deux :
    # - une liste et un élément à insérer dont la position se trouve
    # en début de liste (insertion directe)
    # - une liste et un élément à insérer dont la position se trouve
    # en fin de liste (insertion récursive)
    if difficulté == 0:
        return Liste([]), Entier(random.randint(-10, 10))

    liste = sorted([Entier(random.randint(-10, 10))
                    for _ in range(difficulté)])
    if type_element[0] == 0:
        type_element[0] = 1
        return (Liste(liste, name = "l"),
                Entier(liste[0].n - random.randint(1, 5), name = "e"))
    else:
        type_element[0] = 0
        return (Liste(liste, name = "l"),
                Entier(liste[-1].n - random.randint(1, 5), name = "e"))

def insère_triée(l, e):
    """ Liste, Entier -> Liste """
    # Les Listes héritent de ce qu'il faut :
    l = l.ajoute(e)
    l = sorted(l)
    # L = Liste(sorted(l.ajoute(e)[0]),
    #           name = f"insère_triée({l.name}, {e.name})")
    return Liste(l)

if not __name__:
    Problème(name = problem_name,
            type = problem_type,
            doc = problem_doc,
            entrée_fun = génère_entrée,
            problem_mets = ["divise", "ajoute"],
            problem_funs = [],
            solution_fun = (insère_triée, "insère_triée"),
            rec_mode = lambda l, e: len(l))
