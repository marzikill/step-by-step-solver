import random
from data_structures import BaseObject
from problem_solver import Problème

problem_name = "tri_insertion_iter"
problem_type = "tableau -> tableau"
problem_args = 1
problem_doc = "Trier un tableau tab"
level_type = "la longueur de la liste l"

# Exemple : Avec une structure de donnée maison :
# on cherche à implémenter l'activité qui se trouve à :
# https://www.advanced-ict.info/interactive/insertion_sort.html
class Tableau(BaseObject):
    def __init__(self, content, name = ""):
        super().__init__(content, name)
        self.indice_courant = 0
        self.indice_insérer = 0

    def échange_gauche(self):
        """ Tableau -> None
        Échange l'élément actif du tableau avec celui d'avant """
        i = self.indice_courant
        if i >= 1 and self.content[i - 1] > self.content[i]:
            self.content[i], self.content[i - 1] = self.content[i - 1], self.content[i]
            self.indice_courant -= 1
        else:
            # print(f"Non, {self.content[i]} était à la bonne place")
            self.dépose()


    def dépose(self):
        """ Tableau -> None
        Change l'élément actif """
        self.indice_insérer += 1
        self.indice_courant = self.indice_insérer
    

    def __repr__(self):
        tab_str = [str(i).rjust(3) for i in self.content]
        if self.indice_insérer == len(self.content):
            return ', '.join(tab_str) + '|'
        tab_str[self.indice_insérer] = "|" + tab_str[self.indice_insérer]
        curseur_str = ' '*(4*self.indice_courant + 2) + "^"
        return f"\n{','.join(tab_str)}\n{curseur_str}"

    def __eq__(self, o): return self.content == o.content
        

def génère_entrée(level):
    return Tableau([random.randint(-10, 10) for _ in range(level)],
                   name = "tab")

def tri_insertion(tab):
    """ Tableau -> Tableau
    Implémente l'algorithme du tri par insertion. """
    tab = Tableau(sorted(tab.content))
    tab.indice_insérer = len(tab.content)
    return tab


if not __name__:
    Problème(name = "Tri par insertion (itératif)",
             generating_fun = génère_entrée,
             problem_funs = [Tableau.échange_gauche, Tableau.dépose],
             solution_fun = tri_insertion)
