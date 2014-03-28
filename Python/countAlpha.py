from collections import defaultdict    
def letterOccurrances(string):
    frequencies = defaultdict(lambda: 0)
    for character in string:
        frequencies[character.lower()] += 1
    return frequencies


test = letterOccurrances('intuitive, impeccable, proud, original, smart, progressive, responsible, sustainable, sensible')


print test['a']
print test['b']
