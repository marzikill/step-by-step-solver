
# Table of Contents

1.  [Overview](#org5a3da6a)
2.  [Defining a problem](#orgcaad76e)
    1.  [Generating examples](#org19848e4)
    2.  [Defining the solution](#orgc46ea60)
    3.  [Exporting the problem](#orgf259c6d)
        1.  [Defining a `Problem` variable](#org4ff72a7)
        2.  [Usable interface](#org2218cb0)
        3.  [Using other problems](#org3b35803)
    4.  [The recursion case](#orgfd5a323)
    5.  [Custom data structures](#org1d55d44)
3.  [Implemented data structures](#org6fdb776)
    1.  [Entiers](#org815cc24)
    2.  [Listes](#orgfc84c83)
    3.  [Trees](#orgbeec270)



<a id="org5a3da6a"></a>

# Overview

This program aims at helping students to understand how algorithms
works. It also can help the teacher to explain some algorithms, since
it tries to mimic what can be done on a blackboard. The user is
proposed a problem from a set of problems, and it has to solve it
**using only some predefined functions**. The user selects one function
from the interface and some objects : the program then applies the
function to its selected arguments and waits for another
operation. When the correct object has been built, the user has to
propose its solution. The program verifies whether it's correct. 

By doing so, students may visualize step by step executions of
algorithms on actual data. By trial and errors, they may understand
the order in which operations has to be performed. This program can
also help students to write python programs by displaying at every
step the syntactically correct python expression corresponding to
their actions. It also accustom students to use `return` statements when
they write function, because they have to "propose" (e.g. return) a solution to the program.

The project has been inspired by [Insertion Sort Game](https://www.advanced-ict.info/interactive/insertion_sort.html), where the user
has to sort an array using only two buttons `Left`, and `Stick`. The
problem `tri_insertion_iter` tries to mimic this behavior and show how
the teacher can use its owns data structures to virtually implement
any problem. The interface is inspired by the proof assistant program
Coq, where is displayed the current set of hypothesis on which to
operate at any given time. 

This program also helps to explain how to solve problems using
recursion, as it is explained in [2.4](#orgfd5a323).


<a id="orgcaad76e"></a>

# Defining a problem

Every problem is defined in the folder `./problèmes/` or one of their
subfolder. The problem is automatically available  if any variable of
class `Problème` is defined in the file. For instance, let's explain how
to implement the problem of finding the minimum in a list `l`, using
recursion :

-   if the list `l` is of length 1 : return that element ;
-   in the general case :
    -   compute `m`, the minimum of `tail(l)`
    -   compare `m` with `head(l)` :
        -   if `m < head(l)`, then the minimum of the list is `m`
        -   else the minimum of `l` is `head(l)`.

When then start the code defining the problem by : 

    from problem_solver import Problème
    from data_structures import Liste, Entier


<a id="org19848e4"></a>

## Generating examples

When defining a new problem, one has to define a function generating
suitable input data for the problem. The same function is called each
time the problem is "played". It is especially usefull when
various cases can arise, as it is the case for minimum finding : in
the general case, the minimum can be the head of the list or else
belongs to the tail of the list.

According to current the `case` :

-   either generate `l`, a `Liste` of `Entiers`, `minimum(l)` is its first element ;
-   or generate `l`, a `Liste` of `Entiers`, `minimum(l)` is near its last
    element.


<a id="orgc46ea60"></a>

## Defining the solution

In order to verify students answer, one has to provide a way of
computing the solution of the given problem for any entry. It can be
done in various ways, either "manually" or using predefined python
functions. For instance it's possible to simply return `min(l)`, when `l`
is of type `Liste`. One can also give the "complete" recursive
implementation using the interface of type `Liste` :

    def minimum(l):
        if l.est_singleton():
    	return l.tete()
        else:
    	m = minimum(l.queue())
    	if m < l.tete():
    	    return m
    	else:
    	    return l.tete()


<a id="orgf259c6d"></a>

## Exporting the problem


<a id="org4ff72a7"></a>

### Defining a `Problem` variable


<a id="org2218cb0"></a>

### Usable interface


<a id="org3b35803"></a>

### Using other problems


<a id="orgfd5a323"></a>

## The recursion case


<a id="org1d55d44"></a>

## Custom data structures


<a id="org6fdb776"></a>

# Implemented data structures


<a id="org815cc24"></a>

## Entiers


<a id="orgfc84c83"></a>

## Listes


<a id="orgbeec270"></a>

## TODO Trees

