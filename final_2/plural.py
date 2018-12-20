def countPlurals(line):
    string = line.split()
    for words in string:
        if words.endswith('s') == True:
            result = string.count(words)
            return result
print(countPlurals("she sells seashells"))
print(countPlurals("cookies in a glass"))

def notPossesive(line):
    string = line.split()
    for words in string:
        if words.endswith('s') == True:
            result = string.count(words)
            return result
        if words.endswith("'s") == True:
            pass
print(countPlurals("she's sells seashells"))

            
    
    
    
        