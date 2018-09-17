def capitalize(name):
   name_1 = name
   x = name_1.title()
   print(x)
       
capitalize("chris evans")
capitalize("bucky barnes")

def init(name):
    name_1 = name
    new = name_1[0]
    new_2 = name_1[-8:]
    x = new.title()
    y = new_2.title()
    return x + "." + " " + y
    
print(init("jadeja baptiste"))

def part_pig_latin(name):
    x = name[1:]
    return x + name[0] + "ay"

print(part_pig_latin("jadeja"))
    
    

