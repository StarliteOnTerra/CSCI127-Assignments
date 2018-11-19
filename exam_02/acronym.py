def makeacronym(w):
    words = w.split()
    letters = [word[0] for word in words]
    return "".join(letters)
print(makeacronym("Laugh Out Loud"))
print(makeacronym("Walking On Sunshine"))
print(makeacronym("this is me"))
        