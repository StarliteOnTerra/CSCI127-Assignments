def addline(d, line):
    d = {}
    string = line.lower()
    newstring = string.split()
    first = newstring[0]
    for newstring in string:
        if first not in d:
            d[first] = newstring
        if first in string:
            d[newstring] = d[newstring] + 1
            
    return d
print(addline(d, "This Is Me"))
            
            
    