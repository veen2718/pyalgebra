def sup(val):
    superscripts = "⁰¹²³⁴⁵⁶⁷⁸⁹"
    if val == 1:
        return ""
    if(val<10):
        return superscripts[val]
    v = str(val)
    r = []
    r[:0] = v
    q = [superscripts[int(k)] for k in r]
    return "".join(q)