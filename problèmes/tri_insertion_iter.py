import random
from problem_solver import Problème

problem_name = "tri_insertion_iter"
problem_type = "tableau -> tableau"
problem_args = 1
problem_doc = "Trier un tableau tab"
difficulté_type = "la longueur de la liste l"

# Exemple : Avec une structure de donnée maison :
# on cherche à implémenter l'activité qui se trouve à :
# https://www.advanced-ict.info/interactive/insertion_sort.html
class Tableau:
    def __init__(self, content, name = ""):
        self.name = name
        self.content = content
        self.indice_courant = 0
        self.indice_insérer = 0
        self.interface = {
            "échange_gauche": self.échange_gauche,
            "dépose": self.dépose
        }


    def échange_gauche(self):
        i = self.indice_courant
        if i >= 1 and self.content[i - 1] > self.content[i]:
            self.content[i], self.content[i - 1] = self.content[i - 1], self.content[i]
            self.indice_courant -= 1
        else:
            print(f"Non, {self.content[i]} était à la bonne place")
            self.dépose()
        return self


    def dépose(self):
        self.indice_insérer += 1
        self.indice_courant = self.indice_insérer
        return self
    

    def __repr__(self):
        tab_str = [str(i).rjust(3) for i in self.content]
        if self.indice_insérer == len(self.content):
            return ', '.join(tab_str) + '|'
        tab_str[self.indice_insérer] = "|" + tab_str[self.indice_insérer]
        curseur_str = ' '*(4*self.indice_courant + 2) + "^"
        return f"\n{','.join(tab_str)}\n{curseur_str}"

    def __eq__(self, o): return self.content == o.content
        

def génère_entrée(difficulté):
    """ int -> Tableau """
    return Tableau([random.randint(-10, 10) for _ in range(difficulté)],
                   name = "tab")


def tri_insertion(tab):
    """ Tableau -> Tableau """
    tab =  Tableau(sorted(tab.content))
    tab.indice_insérer = len(tab.content)
    return tab


Problème(name = problem_name,
         type = problem_type,
         doc = problem_doc,
         entrée_fun = génère_entrée,
         problem_mets = ["échange_gauche", "dépose"],
         problem_funs = [],
         solution_fun = (tri_insertion, "tri_insertion"))
