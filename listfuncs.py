def clone(arr):
    r = []
    for i in arr:
        r.append(i)
    return r

def sameContents(arr1,arr2):
    l = True
    for i in arr1:
        if arr2.count(i) != arr1.count(i):
            l = False
    return l

def hasdupes(a, disordered=True):
    if not sameContents(tuple(a),tuple(set(a))):
        return True
    return False

def hasdupes2(a):
    a = tuple(a)
    b = tuple(a)
    for i,v1 in enumerate(a):
        for j,v2 in enumerate(b):
            if i!= j:
                if sameContents(v1,v2):
                    return True
    return False