from world import World
from dataclasses import dataclass
from data_structures import Function

from importlib import util
from os import path
from glob import glob


ProblemIndex = dict()
@dataclass
class Problème:
    name: str = "Problem name"
    generating_fun: 'typing.Any' = "fonction"
    input_types: list = ()
    problem_funs: list = ()
    solution_fun: tuple = ()
    rec_mode: 'typing.Any' = None

    def __post_init__(self):
        if ProblemIndex.get(self.name):
            print(f"Problème {self.name} déjà enregistré !")
            return 
        ProblemIndex[self.name] = self

    @property
    def doc(self):
        return Function(self.solution_fun).doc
             
class OutputException(Exception):
    pass

class InputException(Exception):
    pass

class ProblemInstance:
    def __init__(self, n, problem):
        self.problem = problem
        self.in_fun = Function(self.problem.generating_fun)
        self.sol_fun = Function(problem.solution_fun)
        self.signature = self.sol_fun.signature
        self.level = n
        self.monde = World()
        self.available_funs = dict() # dict(f_name: str, F: Function)
        self.generate_problem_data()

        # Ajout des fonctions et méthodes du problème
        for type in problem.input_types:
            def ask_input():
                raise InputException(type)
            ask_input.__name__ = type.__name__
            ask_input.__doc__ = f" I/O -> {type.__name__}\n" + "Saisir un entier."
            self.add_function(ask_input)

        for fun in problem.problem_funs:
            self.add_function(fun)

        self.add_function(self.propose_solution())
        self.add_function(self.info)


    def add_function(self, fun, rec_mode=None, max_size=float('inf')):
        """ Lorsque rec_mode est défini, il est possible d'appeler 
        la fonction solution du problème lorsque celle-ci opère sur 
        des objets de taille inférieure à la level du problème. """

        F = Function(fun, rec_mode=rec_mode, max_size=max_size)
        self.available_funs[F.name] = F
        self.monde.add_function(F)

    def objects(self):
        return [(o_name, '')
                for o_name in self.monde.object_names()]

    def functions(self):
        return [(f_name, self.monde.docs[f_name])
                for f_name in self.monde.fun_names()]

    def fun(self, fun_name):
        return self.available_funs[fun_name]

    def generate_problem_data(self):
        # Lorsque l'on régénère le problème il faut également
        # mettre à jour la fonction solution seuillée (dépend de level).
        if self.problem.rec_mode:
            self.add_function(self.problem.solution_fun,
                                    rec_mode = self.problem.rec_mode,
                                    max_size = self.level)

        self.entrée = self.in_fun(self.level)
        self.monde.objects = {}
        for o in self.entrée:
            self.monde.add_object(o)
        self.sol = self.sol_fun(*self.entrée)

    def info(self, *args):
        """ Énoncé du problème """
        doc = f"PROBLÈME {self.problem.name} (level {self.level}) :\n"
        doc += self.sol_fun.signature_str
        doc += self.sol_fun.doc
        raise OutputException(doc)

    def vérifie_solution(self, *data):
        return all(data[i] == self.sol[i] for i in range(len(self.sol)))

    def propose_solution(self):
        def propose(*args):
            """ Vérifie que les objets sélectionnés sont solution. """
            if self.vérifie_solution(*args):
                # Dans le cas où l'élève trouve la solution, on régénère
                # un problème de difficulté supérieure. 
                self.level += 1
                self.generate_problem_data()
                raise OutputException("Bravo vous avez résolu le problème.")
            else:
                raise OutputException("Ça n'est pas la bonne réponse, il faut continuer.")
        # Les fonctions ont une documentation du type :
        # Type1, Type2, Type3 -> Type1', Type2'
        # Description de la fonction.
        propose.__doc__ = ", ".join(self.signature['out']) + " -> I/O\n" + propose.__doc__
        return propose

    def make_input(self, exception, data):
        """ Ajoute au monde un objet lors d'une exception entrée """
        type, = exception.args
        self.monde.add_object(type(*data))

    def select_apply_operation(self, op_name, data_names):
        op = self.monde.functions[op_name]
        self.monde.active_data = data_names
        op()


# Récupérer tous les fichiers pythons présents dans ./problèmes
# https://stackoverflow.com/questions/57878744/how-do-i-dynamically-import-all-py-files-from-a-given-directory-and-all-sub-di
def import_submodules(start_path, include_start_directory=True):
    start_path = path.abspath(start_path)
    pattern = '**/*.py' if include_start_directory else '*/**/*.py'
    py_files = [f for f in glob(path.join(start_path, pattern), recursive=True) if not f.endswith('__.py')]

    for py_file in py_files:
        spec = util.spec_from_file_location('', py_file)
        module = util.module_from_spec(spec)
        spec.loader.exec_module(module)

import_submodules("problèmes")
