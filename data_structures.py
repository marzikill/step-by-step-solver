class UnsupportedOperation(Exception):
    pass


class Entier:
    def __init__(self, n, name = ""):
        self.n = n
        self.name = name
        interface = {}

    def get_content(self):
        return self.n

    # On peut comparer les Entiers 
    def __repr__(self): return str(self.n)
    def __eq__(self, o): return self.n == o.n
    def __gt__(self, o): return self.n >= o.n
    def __lt__(self, o): return self.n <= o.n



class Liste:
    def __init__(self, content, name = ""):
        self.name = name
        self.content = content
        self.interface = {
            "est_vide": self.est_vide,
            "tete": self.tete,
            "queue": self.queue,
            "divise": self.divise,
            "ajoute": self.ajoute
        }

    # Une Liste est une liste
    # Les Listes d'Entiers supportent sorted(l)
    def get_content(self): return self.content
    def __repr__(self): return str(self.content)
    def __eq__(self, o): return self.content == o.content
    def __len__(self): return len(self.content)
    def __getitem__(self, item): return self.content[item]
    def __setitem__(self, item, val): self.content[item] = val

    # Interface d'une liste
    def est_vide(self):
        return self.content == []

    def est_singleton(self):
        return len(self.content) == 1

    def tete(self):
        return Entier(self.content[0].n,
                      name = f"tete({self.name})")

    def queue(self):
        return Liste(self.content[1:],
                     name = f"queue({self.name})")

    def ajoute(self, e):
        """ liste, int -> liste
        Étant donné une liste l et un élément e, ajoute l'élément e en tête de la liste l """
        # assert isinstance(e, Entier)
        return Liste([e] + self.content,
                     f"ajoute({self.name}, {e.name})")

    def divise(self):
        """ liste -> int, liste
        Étant donné une liste l non vide, la découpe en deux morceaux tete(l) et queue(l)
        Exemples :
        l = [3] -> tete(l) = 3, queue(l) = [] 
        l = [24, 42] -> tete(l) = 24, queue(l) = [42] 
        l = [2, 5, 6] -> tete(l) = 2, queue(l) = [5, 6] """
        return self.tete(), self.queue()
        # return [self.tete(), self.queue()]
