[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/KhRjEc-2)
# Introduction to Programming
## Winter Semester 2025/26 -- Assignment 9

1. (From GTG R-2.5.) The file `credit_card.py` contains the code of the credit card example from the book.  Revise the `charge` and `make_payment` methods to raise a `ValueError` if the caller does not send a number.

2. (From GTG R-2.9ff.) The file `vector.py` contains the code of the vector class from the book.  Add the following methods to the class: `__sub__` so that the expression `u-v` returns a new vector instance representing the difference between two vectors and `__neg__` so that the expression `-v` returns a new vector instance whose coordinates are all the negated values of the respective coordinates of `v`.  If the vectors do not have the same dimension, raise an error as for `__add__` in the example code.

3. Continuing Problem 2: Implement the `__mul__` method so that `u*v` returns a scalar that represents the dot product of the vectors `u` and `v`, i.e., $u_1 \, v_1 + \cdots + u_d \, v_d$, and that `u*a` results in scalar multiplication if `a` is a number.  Further, implement the `__rmul__` method to make sure that `a*v` is the same as `v*a` when `v` is a vector and `a` is a number.

4. Continuing Problem 3: Implement the method `cross` so that `u.cross(v)` gives the cross product of the vectors `u` and `v` if both of their length is 3.  Raise a value error otherwise.
   
