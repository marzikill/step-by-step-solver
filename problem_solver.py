from world import World
from dataclasses import dataclass
from utils import encapsulate, listargs2str, count_args

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
        monde = f"\nObjets courants\n{self.monde}" 
        sol = f"Solution du problème\n{listargs2str(self.sol)}\n"
        return monde + sol


    def generate_problem_data(self):
        in_fun = encapsulate(self.problem.entrée_fun)
        self.entrée = in_fun(self.difficulté)
        self.monde.objects = {}
        for o in self.entrée:
            self.monde.add_object(o)

        out_fun = encapsulate(self.problem.solution_fun[0])
        self.sol = out_fun(*self.entrée)


    def info(self):
        doc = f""" PROBLÈME {self.problem.name} (difficulté {self.difficulté}) :
        {self.problem.type}
        {self.problem.doc}"""
        # print(doc)
        return doc


    def vérifie_solution(self, sel):
        # print(f"Vérifie : {self.sol} == {sel}")
        return all(sel[i] == self.sol[i] for i in range(len(sel)))
        

    def propose_solution(self, data_names):
        """ Vérifie que les objets de noms data_names sont 
        des solutions du problème. """
        self.monde.active_data = data_names
        sel = self.monde.sel_objects(len(self.sol))
        if self.vérifie_solution(sel):
            return "Bravo vous avez résolu le problème."
        else:
            return "Ça n'est pas la bonne réponse, il faut continuer."




        # sel = self.monde.
        # sel_str = ", ".join([o.name for o in sel])

        # print(f"Réponse proposée : {sel}\nRéponse attendue : {self.sol}")
        # if self.vérifie_solution(sel):
        #     print("Bravo vous avez résolu le problème !")
        #     print(f"Propose : {sel_str}")
        #     self.solved = True
        # else:
        #     print("Ça n'est pas la bonne réponse, il faut continuer...")
        # return None

    def select_apply_operation(self, op, data_names):
        self.monde.active_data = data_names
        op()
        # print(self)
        # op_name = self.monde.sel_function()
        # op = self.monde.functions[op_name]
        # op()

    def joue(self):
        self.generate_problem_data()
        self.solved = False
        while not self.solved:
            self.select_apply_operation()
        return self.solved


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
