from listfuncs import *
from display.superscript import *

class term:
    def __init__(self,x,deg=1,c=1):
        self.sortval = 0
        self.deg = deg
        self.const = c
        self.var = x
    def f(self,a):
        return self.const * a**self.deg
    def nc(self):
        return term(self.var,self.deg)
    def display(self):
        s = str(self.const)
        if self.const == 1:
            s = ""
        return (s+self.var+sup(self.deg))


class compound:
    def __init__ (self, con,*args):
        terms = [k for k in args if type(k) == term] #arguments given that are univariate
        compounds = [k for k in args if k not in terms]#arguments that are declared as compounds
        constGlobal = con #global constant will become self.const
        for t in compounds: 
            if len(t.terms) == 1:
                terms.append(t.toterm(True))#objects that are of type compound but only consist of one term are converted to terms
                constGlobal *= t.terms[0].const
                compounds.remove(t)
        
        terms2 = []
        for c in compounds:
            constGlobal *= c.const  #global constant multiplied by constants of all compounds given
            terms2 += c.terms
        terms += terms2
        vars = [] #will hold all variables in terms
        terms2 = { #will hold all variables in terms and their degrees

        }
        for obj in terms: #for loop through all terms, if variable is same, add degrees together
            if obj.var not in vars:
                vars.append(obj.var)
                terms2[obj.var] = obj.deg
            else:
                terms2[obj.var] += obj.deg
            constGlobal *= obj.const
        
        self.const = constGlobal
        self.terms = []
        for obj in terms2:
            self.terms.append(term(obj,terms2[obj]))
        self.deg = max([i.deg for i in self.terms])
    def toterm(self,noConst=False): #Converts compounds with one term to just a term
        x = self.terms[0]
        x1 = x.var
        x2 = x.deg
        c = self.const
        if noConst:
            c=1
        return term(x1,x2,c)
    def f(self,a):
        product = self.const
        for t in self.terms:
            product *= t.f(a)
        return product
    def display(self):
        n = [str(k.var)+sup(k.deg) for k in self.terms]
        c = str(self.const)
        if self.const == 1:
            c = ""
        return c+"".join(n)
    def nc(self):
        return self.terms


class polynomial:
    def __init__(self, *args,c=0,sortval="deg"):
        self.terms = args
        self.const = c
        self.sortval = sortval
        t1 = []
        t2 = []
        for obj in self.terms:
            if (type(obj) == term): #performs operation only if the object is a term, not compound
                simplified = False 
                for obj2 in t1:
                    if obj2.var == obj.var and obj2.deg == obj.deg: #checks for like terms
                        t1.remove(obj2)
                        t1.append(term(obj.var,obj.deg,obj.const+obj2.const))
                        simplified = True
                if not simplified:
                    t1.append(obj)
                
            elif (type(obj) == compound):
                simplified = False 
                for obj2 in t2:
                    if not simplified:
                        c1 = [[i.deg,i.var] for i in obj.terms]#returns list contains sublists of degree and variable of each variable
                        c2 = [[i.deg,i.var] for i in obj2.terms]
                        
                        isSame = True
                        for obj3 in c1: #Checks if the contents of both lists are identical
                            if obj3 not in c2:
                                isSame = False
                        if isSame:
                            t2.remove(obj2)
                            t2.append(compound(obj.const+obj2.const,*obj.terms))
                            simplified = True
                if not simplified:
                    t2.append(obj)
        self.terms = t1+t2
        if self.sortval == "deg":
            self.terms.sort(key=lambda x: x.deg)
        elif self.sortval == "const":
            self.terms.sort(key=lambda x: x.const)
        

    def f(self,a):
        sum = 0
        for t in self.terms:
            sum += t.f(a)
        return sum+self.const
    def display(self):
        if self.const == 0:
            c = ""
        else:
            c = " + "+str(self.const)
        return " + ".join([n.display() for n in self.terms]) + c
    def arrange(self,sval="deg",rev=False):
        if sval == "deg":
            self.terms.sort(key=lambda x: x.deg)
        elif sval == "const":
            self.terms.sort(key=lambda x: x.const,reverse=rev)

class fraction: #Just started, do not use, work in progress
    def __init__ (self,top,bottom):
        self.top = top
        self.bottom = bottom
        