from listfuncs import *
from polynomials.polynomials import *

def pow(poly,n):
    i = n
    poly1 = polynomial(*poly.terms)
    while i > 1:
        a1 = poly1
        a2 = poly
        poly1 = multiply(poly1,poly)
        i -= 1
    return poly1


def multiply(poly1,poly2):
    newlist = []
    for t1 in poly1.terms:
        for t2 in poly2.terms:
            newlist.append(compound(1,t1,t2))
    return polynomial(*newlist)

def distribute(term,poly):
    newlist = []
    for i in poly.terms:
        newlist.append(compound(term.const*i.const,term,i))
    return polynomial(*newlist)