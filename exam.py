def Function1(st, f):
    string_length = len(st)
    se = ""
    so = ""
    if f == 0:
        # Iterate through string at every even position
        for s in range(1,string_length,2):
            se = se + st[s];
        return se
    elif f == 1:
        # Iterate through string at every even position
        for s in range(0,string_length,2):
            so = so + st[s];
        return so


print (Function1("TRACXN",1))