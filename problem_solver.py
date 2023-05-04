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
    solution_fun: tuple = ()
    problem_mets: list = ()
    problem_funs: list = ()
    rec_mode: 'typing.Any' = None

    def __post_init__(self):
        if ProblemIndex.get(self.name):
            print(f"Problème {self.name} déjà enregistré !")
            return 
        ProblemIndex[self.name] = self
             
class Problème_Solver:
    def __init__(self, n, problem):
        self.problem = problem
        self.difficulté = n
        self.solved = False
        self.monde = World()
        self.generate_problem_data()

        # Ajout des fonctions et méthodes du problème
        for fun_info in problem.problem_funs:
            self.monde.add_function(fun_info)
        for meth_info in problem.problem_mets:
            self.monde.add_method(meth_info)

        # Ajout des fonctions et méthodes du solveur
        if problem.rec_mode:
            self.monde.add_solfunction(problem.solution_fun,
                                       problem.rec_mode,
                                       self.difficulté)
        solver_funs = [(self.propose_solution, "propose"),
                       (self.info, "info")]
        for fun_info in solver_funs:
            self.monde.add_function(fun_info)


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
        {self.problem.type}
        {self.problem.doc}"""
        # print(doc)
        return doc

    def vérifie_solution(self, data):
        if not isinstance(data, list):
            return data == self.sol
        return all(data[i] == self.sol[i] for i in range(len(self.sol)))
        

    def propose_solution(self, data_names):
        """ Vérifie que les objets sélectionnés sont solution. """
        data = [self.monde.objects[k] for k in data_names]
        if self.vérifie_solution(data):
            return "Bravo vous avez résolu le problème."
        else:
            return "Ça n'est pas la bonne réponse, il faut continuer."


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
