import random
from data_structures import *

def alternate(f1, f2):
    """ Renvoie une fonction dont la sortie est alternativement 
    calculée avec f1 puis f2 lors de ses différents appels successifs. """
    def fun(*args, case = [0]):
        if case[0] == 0:
            case[0] = 1
            return f1(*args)
        else:
            case[0] = 0
            return f2(*args)
    return fun

def random_liste(level, name='l', minrange = -10, maxrange = 10):
    if level <= 1:
        return Liste([Entier(random.randint(minrange, maxrange))])
    return Liste([Entier(random.randint(minrange, maxrange))
                  for _ in range(level)],
                 name=name)

def mini_last(level, case = [0]):
    """ int -> Liste,
    Renvoie une Liste où le plus petit élément est le dernier. """    
    if level <= 1:
        return Liste([Entier(random.randint(-10, 10))])
    res = random_liste(level - 1)
    mini = Entier(min(res).content - random.randint(1, 5))
    res.content.append(mini)
    return res

def mini_first(level, case = [0]):
    """ int -> Liste,
    Renvoie une Liste où le plus petit élément est le premier. """    
    if level <= 1:
        return Liste([Entier(random.randint(-10, 10))])
    res = random_liste(level - 1)
    mini = Entier(min(res).content - random.randint(1, 5))
    res.content.insert(0, mini)
    return res
