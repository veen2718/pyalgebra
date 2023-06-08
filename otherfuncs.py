from listfuncs import *

def pascalTriangle(n): #Make a Pascal Triangle of size n
    k = [1,1]
    for i in range(n):
        k1 = []
        for j in range(len(k)-1):
            k1.append(k[j]+k[j+1])
        k = [1]+k1+[1]
    return(k)