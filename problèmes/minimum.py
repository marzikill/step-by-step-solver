import random
from problem_solver import Problème
from data_structures import Liste, Entier
from generate import alternate, mini_last, mini_first

problem_name = "minimum"
problem_type = "liste -> int" # Inutile à priori
problem_doc = "Étant donné une liste l non vide renvoyer le plus petit élément de l"
difficulté_type = "la longueur de la liste l"

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
             entrée_fun = alternate(mini_first, mini_last),
             input_types = [Entier],
             problem_mets = [],
             problem_funs = [Liste.divise, Liste.ajoute],
             solution_fun = minimum,
             rec_mode = len)
