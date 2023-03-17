from problem_solver import Problème_Solver, Problème
from problèmes.insere_triée import problème_desc as pb1
from problèmes.tri_insertion import problème_desc as pb2
from problèmes.minimum import problème_desc as pb3
from problèmes.supprime import problème_desc as pb4
from problèmes.tri_selection import problème_desc as pb5
from problèmes.divise import problème_desc as pb6
from problèmes.fusionne import problème_desc as pb7
from problèmes.tri_fusion import problème_desc as pb8
from problèmes.tri_insertion_iter import problème_desc as pb9

# Insère triée
# P = Problème_Solver(5, Problème(**pb1))
# P.joue()
# P.joue()

# Tri insertion
# P = Problème_Solver(5, Problème(**pb2))
# P.joue()

# minimum
# P = Problème_Solver(5, Problème(**pb3))
# P.joue()
# P.joue()

# supprime
# P = Problème_Solver(5, pb4)
# P.joue()
# P.joue()

# tri_sélection
# P = Problème_Solver(5, pb5)
# P.joue()
# P.joue()

# divise
# P = Problème_Solver(5, pb6)
# P.joue()
# P.joue()

# fusionne
# P = Problème_Solver(5, Problème(**pb7))
# P.joue()
# P.joue()

# tri fusion
# P = Problème_Solver(5, pb8)
# P.joue()
# P.joue()

# tri insertion
P = Problème_Solver(5, Problème(**pb9))
P.joue()
