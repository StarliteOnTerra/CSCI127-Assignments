import random

adj = ["beautiful", "aggressive", "calm", "delightful", "silly"]
noun = ["tiger", "cat", "house", "banana", "music"]
verb = ["running", "jumping", "swimming", "laughing", "skating"]
pnoun = ["tigers", "cats", "houses", "bananas", "musics"]
game = ["Scrabble", "Twister", "Tag", "Digging"]
statement = "A vacation is when you take a trip to some <adj> place with your <adj> family. Usually you go to some place that is near a/an <noun> or up on a/an <noun> . A good vacation place is one where you can ride <pnoun> or play <game> or go hunting for <pnoun> . I like to spend my time <verb> or <verb> . When parents go on a vacation, they spend their time eating three <pnoun> a day, and fathers play golf and mothers <verb> ."

subs = ['<adj>', '<noun>', '<verb>', '<pnoun>', '<game>']
words = [adj, noun, verb, pnoun, game]

d = {}
d[0] = words


for i, l in zip(subs, words):
    d[i] = l

def madlibs(statement, d):
    list = []

    for i in statement.split():
        if i in d:
                list.append(random.choice(d[i]))
        else:
            list.append(i)
            
    return ' '.join(list)

    
print(madlibs(statement, d))