

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
they write function, because they have to "propose" (e.g. return) a
solution to the program.

The project has been inspired by [Insertion Sort Game](https://www.advanced-ict.info/interactive/insertion_sort.html), where the user
has to sort an array using only two buttons `Left`, and `Stick`. The
problem `tri_insertion_iter` tries to mimic this behavior and show how
the teacher can use its owns data structures to virtually implement
any problem. The interface is inspired by the proof assistant program
Coq, where is displayed the current set of hypothesis on which to
operate at any given time.

This program also helps to explain how to solve problems using
recursion, as it is explained in [the recursion case](#org274b67e).


# Defining a problem

Every problem is defined in the folder `./problèmes/` or one of their
subfolder. The problem is automatically available if any variable of
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


## Defining the solution

In order to verify student's answers, one has to provide a way of
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


## Exporting the problem


### Defining a `Problem` variable

The `Problem` class has various attributes :

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Attribute</th>
<th scope="col" class="org-left">Description</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left"><code>name</code></td>
<td class="org-left">A string describing the problem name</td>
</tr>


<tr>
<td class="org-left"><code>type</code></td>
<td class="org-left">A string describing the solution function signature</td>
</tr>


<tr>
<td class="org-left"><code>doc</code></td>
<td class="org-left">A string explaining the problem</td>
</tr>


<tr>
<td class="org-left"><code>entrée_fun</code></td>
<td class="org-left">A function to use in order to generate problem entries</td>
</tr>


<tr>
<td class="org-left"><code>problem_mets</code></td>
<td class="org-left">A list of strings. The user will be able to use corresponding method to solve the problem.</td>
</tr>


<tr>
<td class="org-left"><code>problem_funs</code></td>
<td class="org-left">A list of tuples, the first element being a function, the second being a string (the function name)</td>
</tr>


<tr>
<td class="org-left"><code>solution_fun</code></td>
<td class="org-left">A tuple, the first element being a function, the second being a string (the function name)</td>
</tr>


<tr>
<td class="org-left"><code>rec_mode</code></td>
<td class="org-left">Optional (function) : whether to allow recursion to solve the problem</td>
</tr>
</tbody>
</table>


### Usable interface

When solving the problem, the user is proposed :

-   the methods of `problem_mets`
-   the functions of `problem_funs`
-   the `solution_fun` if `rec_mode` is defined. `rec_mode` is a function
    having the same arguments than the solution function. It outputs an
    int representing the data "complexity". When this variable is set,
    the user might use the solution function only if the data it is
    applied to has a "complexity" strictly lower than the problem
    current difficulty. 
    
    For instance, `rec_mode` might be set at `len` when solving the minimum
    problem, but at `lambda l1, l2: len(l1) + len(l2)` when solving the
    problem of fusion of two sorted list.


### Using other problems

It is possible to use already defined functions. For example, if
trying to implement the selection sort algorithm, one can first import
the function `minimum` and make it usable by setting `problem_funs` to
`[(minimum, "minimum")]`. Of course any number of functions might be
added this way.


## Custom data structures

In addition to the already defined data structures, one can add its
own data structures when creating new problems. An attribute `interface`
has to be defined, linking to exposed methods. Exposed methods **has to
return an object** (or a list of objects) : they will be added to the
environment whereas the old object to which the method was added will
be popped out from the environment. 

`__eq__` and `__repr__` also has to be defined for verifing the solution and
displaying objects. 

For an example of the implementation of [Insertion Sort Game](https://www.advanced-ict.info/interactive/insertion_sort.html) with our
program, see `tri_insertion_iter.py`.


# Implemented data structures


## Entiers


## Listes


## TODO Trees

