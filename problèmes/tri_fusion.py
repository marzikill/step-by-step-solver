from generate import random_liste
from problem_solver import Problème
from data_structures import Liste, Entier
from problèmes.divise import divise_en_2
from problèmes.fusionne import fusionne

def tri_fusion(l):
    """ Liste -> Liste
    Implémente l'algorithme du tri fusion. """
    if l.est_vide() or l.est_singleton():
        return l
    else:
        l1, l2 = divise_en_2(l)
        l1, l2 = tri_fusion(l1), tri_fusion(l2)
        return fusionne(l1, l2)

if not __name__:
    Problème(name = "Tri fusion",
             generating_fun = random_liste,
             problem_funs = [divise_en_2, fusionne],
             solution_fun = tri_fusion, 
             rec_mode = len)
