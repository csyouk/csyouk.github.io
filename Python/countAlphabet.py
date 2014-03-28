from collections import defaultdict    
def letterOccurrances(string):
    frequencies = defaultdict(lambda: 0)
    for character in string:
        frequencies[character.lower()] += 1
    return frequencies


test = letterOccurrances('responsible, sustainable, sensible')


print test['a']
print test['b']
print test['c']
print test['c']
print test['e']
print test['f']
print test['g']
print test['h']
print test['i']
print test['j']
print test['k']
print test['l']
print test['m']
print test['n']
print test['o']
print test['p']
print test['q']
print test['r']
print test['s']
print test['t']
print test['u']
print test['v']
print test['w']
print test['x']
print test['y']
print test['z']
