# TODO
- [ ] popup input utilisateur
- [ ] nettoyer le code :
  Problèmes de design :
  généraliser ce qui a été fait pour le problème minimum (cf commentaires)
  - que pense-t-on de "ne pas faire la distinction entre fonction/méthode -> ne manipuler que des fonctions" ?
  - que pense-t-on de "les méthodes mutent l'objet sur lequel elles s'appliquent ?"
	- certaines méthodes mutent les objets (genre ajoute)
	- d'autre non (genre divise)
	- la plupart du temps les fonctions manipulées ne mutent pas les objets
  -> tout est fonction mais certaines fonctions mutent les objets auxquelles elles s'appliquent, d'autres non. Utiliser le mécanisme `id` de python comme identificateur dans le World ?
  - que pense-t-on de "input est une méthode du type" vs "étant donné un type, le pb construit une fonction d'input" ?
- [ ] implémenter un objet fonction : gestion des signatures etc
- [ ] cli : historique des actions : 
  l.divise()
  minimum(l)


- [~] ajouter une fonctionnalité de destruction d'objet
- +afficher les docstring dans Problème_minimum.apply_operation+
  -> ajouter une méthode info
- [X] une fois le problème de difficulté n résolu, enchaîner avec n + 1
- [X] rendre la classe Problème plus générale
- [X] rendre la classe Monde plus générale et supporter d'autres structures de données 
- [X] ajout de fonctions arbitraires à l'interface de manipulation
- [X] self.supported_opérations : pas très beau. À déplacer dans World
- [X] rendre indépendant le processus de sélection et d'action ?
- [X] se cantoner aux fonction qui ne renvoient q'un élément
-> plus besoin de mettre des , partout
-> plus facile de construire le nom des nouveaux éléments
-> supprimer la composante fun_name : fun.__name__ suffit ?
- [X] reprendre l'interface du type liste pour virer les q, = sortie(l)
- [X] reprendre la méthode résoudre de la classe solveur : à réécrire
- [X] ajouter un mécanisme de calcul de la complexité de l'entrée (mode récursif)
- [X] régler le décompte des commits sur github
- [X] reprendre les anciens problèmes avec la nouvelle interface
- [X] interface terminal
- [X] écrire la documentation et présenter le projet
- [X] tester les problèmes 
	- [X] tri_fusion.py
	- [X] tri_insertion.py
	- [X] divise.y
	- [X] minimum.py
	- [X] fusionne.py 
	- [X] supprime.py 
	- [X] insere_triée.py 
	- [X] tri_selection.py 
	- [X] tri_insertion_iter.py
