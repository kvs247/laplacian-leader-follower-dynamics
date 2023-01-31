# Laplacian Leader Follower Dynamics

K. Schneider

## matrixMath.py

Provides functions for determining matrix controllability using linear algebra.

## matrixGeneration.py

Provides functions for generating Laplacian matrices

## Algorithm progress

### Starting point 

The first version of the algorithm was at a point where it would take well over 12 hours to categorize all 7 dimensional Laplacian matrices. It seems a long way from categorizing all matrices with dimensions in the double-dgits. This version would first generate the set of Laplacian matrices for the given dimension. I quickly realized this may create a memory problem, but would also be problematic as there would be no way to pause the calculation and continue later without repeating many computations.

### Different Approach

The second iteration reorganized the process so that a matrix is generated, controllability is determined, and data is saved before moving on to the next matrix. This allows the program to pause and resume later, giving the potential to break up calculations into many sessions. I also found this algorithm to be must faster. This method categorized all 7 dimensional Laplacian matrices within 3 hours.
