
def encode(s):
    lst = list(s)
    return lst
print(encode("abbbaaccddda"))


def count(lst):
    for letter in lst:
        letter_num = lst.count(letter)
        return letter_num
print(count("abbbaaccddda"))

def add(lst):
    d =[]
    let = list(lst)
    for i in range(len(lst)):
        if lst[i] in d:
            d[lst[i]].append(lst[i+1])
        return d
print(add("abbbaaccddda"))
        
    






    

    
    
    
    
    
    
        
        
        