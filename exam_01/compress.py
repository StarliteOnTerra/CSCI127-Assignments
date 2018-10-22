def compress_word(w):
    vowels = ["a", "e", "i", "o", "u"]
    for vowels in w:
        if vowels == "e":
            x = w.replace(vowels, " ")
            return x
print(compress_word("apple"))
print(compress_word("arm"))