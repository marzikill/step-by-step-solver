import random
from problem_solver import Problème, OutputException
from data_structures import Entier, Liste

class TableauCaché(Liste):
    def __init__(self, content, name = ""):
        super().__init__(content, name)
        self.indice_courant = 0

    def incr(self):
        """ TableauCaché -> None
        Incrémente le curseur """
        if self.indice_courant >= len(self.content) - 1:
            raise OutputException("Le curseur est à la fin du tableau")
        self.indice_courant += 1

    def get(self):
        return self.content[self.indice_courant]

    def store(self):
        """ TableauCaché -> Entier
        Sauvegarde l'élément sous le curseur """
        return Entier(self.get(), name = "mem")

    def __repr__(self):
        tab_str = [str(e).rjust(3) if i <= self.indice_courant
                   else " X "
                   for i, e in enumerate(self.content)]
        curseur_str = ' '*(4*self.indice_courant + 2) + "^"
        return f"\n{','.join(tab_str)}\n{curseur_str}"

def gen(difficulté):
    return TableauCaché([random.randint(-10, 10) for _ in range(difficulté)],
                        name= 'tab')

def minimum(l):
    """ TableauCaché -> Entier 
    Étant donné un tableau tab non vide, renvoyer le plus petit élément de l """
    # Les Listes héritent de ce qu'il faut :
    m = min(l)
    return Entier(m)

                  
if not __name__:
    Problème(name = "Minimum (itératif)",
             generating_fun = gen,
             input_types = [],
             problem_funs = [TableauCaché.incr, TableauCaché.store],
             solution_fun = minimum)
