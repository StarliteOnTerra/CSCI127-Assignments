def happy2(s):
    if "_" not in s:
        for i in range(1,len(s)-1):
            if s[i] != s[i-1] and s[i] != s[i+1]:
                return False
            if s[0] != s[1] or s[len(s)-1] != s[len(s)-2]:
                return False
        return True
    else:
        s = s.replace("_","")
        s = sorted(s)
        for i in range(1,len(s)-1):
            if s[i] != s[i-1] and s[i] != s[i+1]:
                return False
        if s[0] != s[1] or s[len(s)-1] != s[len(s)-2]:
            return False
        return True


def happy(s):
    if '_' not in s:
        for i in range(1,len(s)-1):
            if s[i] != s[i-1] and s[i] != s[i+1]:
                return False
        return True
    else:
        s = s.replace("_","")
        counts = {}
        for bug in s:
            counts.setdefault(bug,0)
            counts[bug]=counts[bug]+1
    
        return 1 not in counts.values()

testcases = ["abcdea","abccde","aabbcccdd","abc_def","abc_ecdccdeba__","abc_abcd_abc_"]

for test in testcases:
    print(test)
    print(happy(test))
    print(happy2(test))
    print("------------")