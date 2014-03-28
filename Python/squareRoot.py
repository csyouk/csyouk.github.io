def sqrt(x):
    ans = 0
    if x >= 0:
        while ans*ans<x: ans = ans + 1
        if ans*ans != x:
            print x, 'is not a perfect square'
            return None
        else: return ans
    else :
        print x, 'is negative number'
        return None


def f(x):
    x = x + 1
    return x


def solve(numLegs, numHeads):
    for numChicks in range(0, numHeads + 1):
        numPigs = numHeads - numChicks
        totLegs = 4*numPigs + 2*numChicks
        if totLegs == numLegs:
            return [numPigs, numChicks]
    print 'Maybe there are some mutants. Dude.'
    return [None, None]

def barnYard():
    heads = int(raw_input('Enter number of heads: '))
    legs = int(raw_input('Enter number of legs: '))
    pigs, chickens = solve(legs, heads)
    if pigs == None:
        print 'There is no solution'
    else:
        print 'Number of pigs:', pigs
        print 'Number of chickens: ', chickens



def isPalindrome(s):
    if len(s) <= 1: return True
    else: return s[0] == s[-1] and isPalindrome(s[1:-1])

def isPalindromel(s, indent):
    print indent, 'isPalindromel called with', s
    if len(s) <= 1:
        print indent, 'About to return True frome this case'
        return True
    else:
        ans * s[0] == s[-1] and isPalindromel(s[1:-1], indent + indent)
        print indent, 'About to return', ans
        return ans


def fib(x):
    if x == 0 or x == 1: return 1
    else: return fib(x-1) + fib(x-2)
