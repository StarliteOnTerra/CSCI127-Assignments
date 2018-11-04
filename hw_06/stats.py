import random

def build_random_list(size, max_value):
     l = [] 
     i = 0
     while i < size:
        l.append(random.randrange(0,max_value))
        i = i + 1
     return l

def max(l):
    li = 0
    for i in range(1, len(l)):
        if l[i] > li[0]:
            li = i
    return li

def freq(l, item):
    count = 0
    for i in range(len(l)):
        if l[i] == item:
            count = count + 1
    return count

print(build_random_list(100,10))
print(freq(l, 5))
