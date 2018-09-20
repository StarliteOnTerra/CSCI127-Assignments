# By Jadeja Baptiste & Stacy Li

def part_pig_latin(name):
    
    vowels = ('a', 'e', 'i', 'o', 'u',)
 
    x = name[0]
    
    if x.startswith(vowels):
            return name + "ay"
    else:
            return name[1:] + x + "ay"

print(part_pig_latin("owen"))
print(part_pig_latin("evan"))
print(part_pig_latin("kayla"))
print(part_pig_latin("john"))
print(part_pig_latin("twilight"))