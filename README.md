# pyalgebra
Several functions that help to do algebra

## Classes

### term
```python
term(variable, degree, constant)
```
The most basic unit in the program, and this can be given as arguments to other class constructors.
It is just something like 3x². Note only one variable can be used.

### compound
```python
compound(constant, *termsOrCompounds)
```
This can be something like 7y⁵z². Note multiple variables can be used. A constant is given as the first argument, and the rest of the arguments can be either terms or compounds.


