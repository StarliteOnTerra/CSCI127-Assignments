#Jadeja Baptiste

import random

def build_random_list(size,max_value):
    """
    Parameters:
      size : the number of elements in the list
      max_value : the max random value to put in the list
    """
    l = [] 

    i = 0
    while i < size:
        l.append(random.randrange(0,max_value))
        i = i + 1
    return l
print(build_random_list(13,62))

def locate(l,value):
    l = [5, 3, 10, 21, 8, 34, 18, 56]
    if value in l:
        print(l.index(value))
    else:
        return -1
print(locate(0,35))

def count(l,value):
    l = [5, 3, 10, 21, 8, 3, 18, 56, 89, 21, 45, 3]
    if value in l:
        print(l.count(value))
print(count(1,21))

def reverse(l):
    l = [1, 2, 4, 5, 8,]
    l = l[::-1]
    print(l)
print(reverse(1))

def isIncreasing(l):
    Increasing = True
    i = 0
    while i < len(l)- 1:
        if l[i] >= l[i+1]:
            return True
            
    

        
