def canMakeWord(letters, word):
    for letters in word:
        if letters in word:
            return True
        if letters not in word:
            return False
print(canMakeWord("ladilmy", "daily"))
print(canMakeWord("riin", "eerie"))
    