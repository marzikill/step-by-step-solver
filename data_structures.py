import typing

class BaseObject:
    def __init__(self, c, n):
        self.content = c
        self.name = n

    @property
    def id(self):
        return id(self)
    
    @property
    def doc(self):
        return self.__class__.__doc__.strip()

    def __repr__(self):
        return f"{self.content}" 

    def get_content(self):
        return self.content

class Entier(BaseObject):
    """ Un entier """
    def __init__(self, n, name = ''):
        super().__init__(n, name)

    # On peut comparer les Entiers 
    def __eq__(self, o): return self.content == o.content
    def __gt__(self, o): return self.content >= o.content
    def __lt__(self, o): return self.content <= o.content

class Function(BaseObject):
    """ Représente une fonction sans arguments nommés """
    def __init__(self, f, rec_mode=None, max_size=float('inf')):
        super().__init__(f, f.__name__)
        def default_rec_mode(*args):
            return None
        self.rec = rec_mode is not None
        self.rec_mode = default_rec_mode if not rec_mode else rec_mode
        self.max_size = max_size

    def check_args(self, args):
        # Vérification du nombre d'arguments
        if not len(args) == len(self.signature['in']):
            raise ValueError(f"{len(args)} arguments passés à la fonction {self.name}, {len(self.signature['in'])} arguments attendus", self.signature['in'])
        # Tous les arguments doivent être de bon type (exact, pas d'héritage)
        # Le type 'I/O' n'est pas pris en compte
        if not all([o.__class__.__name__ == T
                    for o, T in zip(args, self.signature['in'])
                    if T != "I/O"]):
            raise TypeError(f"Les arguments sélectionnés n'ont pas le bon type")

    def apply_return_tuple(self, res):
        """ La valeur renvoyée par une fonction est un tuple """
        res = self.content(*res)
        if res is None:
            return ()
        if not isinstance(res, tuple):
            return res,
        return res
        
    def __call__(self, *args):
        if not self.signature:
            return self.apply_return_tuple(args)
        if self.rec and self.rec_mode(*args) >= self.max_size:
            raise RecursionError("Le problème est trop dur")

        self.check_args(args)
        res = self.apply_return_tuple(args)
        # Rename output 
        for i, o in enumerate(res):
            index_pos_str = '' if len(res) == 1 else f"[{i}]"
            if not o.name or self.rec:
                o.name = f"{self.name}(" + ", ".join(a.name for a in args) + ")" + index_pos_str 
        return res
        
    @property
    def signature(self):
        # signature via type annotations
        signature = typing.get_type_hints(self.content)
        if signature:
            out_args = [t.__name__ for t in signature.pop('return')]
            in_args = [t.__name__ for t in signature.values()]
            return {'in':in_args,
                    'out':out_args}

        # signature via docstring
        doc = self.content.__doc__
        if not doc or doc.find('->') < 0:
            return dict()
        sig = doc.split('->')
        left_args = sig[0].split(',')
        sig = sig[1].split('\n')
        right_args = sig[0].split(',')
        return {'in':[t.strip() for t in left_args],
                'out':[t.strip() for t in right_args]}

    @property
    def signature_str(self):
        if not self.signature:
            return ''
        return ", ".join(self.signature['in']) + ' -> ' + ", ".join(self.signature['out']) + "\n"

    @property
    def doc(self):
        if not self.signature:
            return self.content.__doc__
        doc = self.content.__doc__.split('\n')
        if len(doc) == 1:
            return ''
        return "\n".join(l.strip() for l in doc[1:])

# class Entier:
#     def __init__(self, n, name = ""):
#         self.n = n
#         self.name = name
#         interface = {}

#     def get_content(self):
#         return self.n

#     # On peut comparer les Entiers 
#     def __repr__(self): return str(self.n)
#     def __eq__(self, o): return self.n == o.n
#     def __gt__(self, o): return self.n >= o.n
#     def __lt__(self, o): return self.n <= o.n



class Liste(BaseObject):
    """ Une liste d'Entiers. """
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
    def __eq__(self, o): return self.content == o.content
    def __len__(self): return len(self.content)
    def __getitem__(self, item): return self.content[item]
    def __setitem__(self, item, val): self.content[item] = val

    # Interface d'une liste
    def est_vide(self):
        """ Liste -> bool
        Détermine si la liste est vide. """
        return self.content == []

    def est_singleton(self):
        """ Liste -> bool 
        Détermine si la liste ne contient qu'un élément. """
        return len(self.content) == 1

    def tete(self):
        """ Liste -> Entier 
        Renvoie le premier élément de la liste. """
        return Entier(self.content[0].content,
                      name = f"tete({self.name})")

    def queue(self):
        """ Liste -> Liste
        Renvoie la queue de la liste. """
        return Liste(self.content[1:],
                     name = f"queue({self.name})")

    def ajoute(self, e):
        """ Liste, Entier -> Liste
        Étant donné une liste l et un élément e, ajoute l'élément e en tête de la liste l """
        # assert isinstance(e, Entier)
        return Liste([e] + self.content,
                     f"ajoute({self.name}, {e.name})")

    def divise(self):
        """ Liste -> Entier, Liste
        Étant donné une liste l non vide, la découpe en deux morceaux tete(l) et queue(l)
        Exemples :
        l = [3] -> tete(l) = 3, queue(l) = [] 
        l = [24, 42] -> tete(l) = 24, queue(l) = [42] 
        l = [2, 5, 6] -> tete(l) = 2, queue(l) = [5, 6] """
        return self.tete(), self.queue()
        # return [self.tete(), self.queue()]
