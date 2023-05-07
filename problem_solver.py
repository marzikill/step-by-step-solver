from world import World
from dataclasses import dataclass
from utils import encapsulate

from importlib import util
from os import path
from glob import glob


ProblemIndex = dict()
@dataclass
class Problème:
    name: str = "Problem name"
    type: str = "Problème type"
    doc: str = "Problème documentation"
    entrée_fun: 'typing.Any' = "fonction"
    input_types: list = ()
    solution_fun: tuple = ()
    problem_mets: list = ()
    problem_funs: list = ()
    rec_mode: 'typing.Any' = None

    def __post_init__(self):
        if ProblemIndex.get(self.name):
            print(f"Problème {self.name} déjà enregistré !")
            return 
        ProblemIndex[self.name] = self
             
class InputException(Exception):
    pass

class OutputException(Exception):
    pass

class Problème_Solver:
    def __init__(self, n, problem):
        self.problem = problem
        self.difficulté = n
        self.monde = World()
        self.generate_problem_data()

        # Ajout des fonctions et méthodes du problème
        for type in problem.input_types:
            def ask_input():
                raise InputException(type)
            ask_input.__doc__ = f" I/O -> {type.__name__}"
            self.monde.add_function((ask_input, type.__name__))

        # Cf commentaire problèmes/minimum.py
        # for fun in problem.problem_funs:
        #     self.monde.add_function((fun, fun.__name__))
        # for meth in problem.problem_mets:
        #     self.monde.add_method(meth.__name__)

        for fun_info in problem.problem_funs:
            self.monde.add_function(fun_info)
        for meth_info in problem.problem_mets:
            self.monde.add_method(meth_info)

        # Ajout des fonctions et méthodes du solveur
        if problem.rec_mode:
            self.monde.add_solfunction(problem.solution_fun,
                                       problem.rec_mode,
                                       self.difficulté)

        self.monde.add_function((self.propose_solution(), "propose"),
                                num_args=len(self.signature['out']))
        self.monde.add_function((self.info, "info"), num_args=0)

    @property
    def signature(self):
        doc = self.problem.solution_fun[0].__doc__
        if not doc.find('->'):
            return 
        sig = doc.split('->')
        left_args = sig[0].split(',')
        sig = sig[1].split('\n')
        right_args = sig[0].split(',')
        return {'in':left_args,
                'out':right_args}

    def objects(self):
        return [(o_name, '')
                for o_name in self.monde.object_names()]

    def functions(self):
        return [(f_name, self.monde.docs[f_name])
                for f_name in self.monde.fun_names()]

    def __str__(self):
        info = "\n".join([self.monde.docs[fname]
                          for fname in self.monde.fun_names()])
        return info

    def generate_problem_data(self):
        in_fun = encapsulate(self.problem.entrée_fun)
        self.entrée = in_fun(self.difficulté)
        self.monde.objects = {}
        for o in self.entrée:
            self.monde.add_object(o)

        out_fun = encapsulate(self.problem.solution_fun[0])
        self.sol = out_fun(*self.entrée)


    def info(self):
        """ Énoncé du problème """
        doc = f""" PROBLÈME {self.problem.name} (difficulté {self.difficulté}) :
        {", ".join(self.signature['in'])} -> {", ".join(self.signature['out'])}
        {self.problem.doc}"""
        return doc

    def vérifie_solution(self, *data):
        return all(data[i] == self.sol[i] for i in range(len(self.sol)))

    def propose_solution(self):
        """ Vérifie que les objets sélectionnés sont solution. """
        def propose(*args):
            if self.vérifie_solution(*args):
                raise OutputException("Bravo vous avez résolu le problème.")
            else:
                raise OutputException("Ça n'est pas la bonne réponse, il faut continuer.")
        # Les fonctions ont une documentation du type :
        # Type1, Type2, Type3 -> Type1', Type2'
        # Description de la fonction.
        sig = self.problem.solution_fun[0].__doc__.split('->')[1]
        sig = sig.split('\n')[0]
        propose.__doc__ = f"{sig} -> I/O"
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
