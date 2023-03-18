import random
from problem_solver import Problème
from data_structures import Liste, Entier
from problèmes.divise import divise_en_2
from problèmes.fusionne import fusionne

problem_name = "tri_fusion"
problem_type = "liste -> liste"
problem_doc = "Trie la liste l à l'aide de l'algorithme du tri fusion"
difficulté_type = "la longueur de la liste l"

def génère_entrée(difficulté):
    """ int -> Liste, Entier """
    l  = [Entier(random.randint(-10, 10))
                    for _ in range(difficulté)]
    return Liste(l, name = "l")

def tri_fusion(l):
    """ Liste, Liste -> Liste """
    if l.est_vide() or l.est_singleton():
        return l
    else:
        l1, l2 = divise(l)
        l1, l2 = tri_fusion(l1), tri_fusion(l2)
        return fusionne(l1, l2)

if not __name__:
    Problème(name = problem_name,
            type = problem_type,
            doc = problem_doc,
            entrée_fun = génère_entrée,
            problem_mets = [],
            problem_funs = [(divise_en_2, "divise_en_2"), (fusionne, "fusionne")],
            solution_fun = (tri_fusion, "tri_fusion"),
            rec_mode = len)
