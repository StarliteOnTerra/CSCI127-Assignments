
def compress_word(word):
    vowels = "aeiouAEIOU"
    first = word[0]
    rest = word[1:]
    new_rest = ""
    for letter in rest:
        if letter not in vowels:
            new_rest = new_rest + letter
            
    return first + new_rest

print(compress_word("apple"))
print(compress_word("banana"))
print(compress_word("hello"))
print(compress_word("arm"))
print(compress_word("ear"))
print(compress_word("nice"))
