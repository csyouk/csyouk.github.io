def squareRootBi(x, epsilon):
    """Assume x >= 0 and epsilon > 0
       Return y s.t. y*y is within epsilon of x"""
    assert x >= 0, 'x must be not non-negative, not' + str(x)
    assert epsilon > 0, 'epsilon must be positive, not' + str(epsilon)
    low = 0
    high = x
    guess = (low + high)/2.0
    ctr = 1
    while abs(guess**2 - x) > epsilon and ctr <= 100:
        #print 'low:', low, 'high:', high, 'guess:', guess
        if guess**2 < x:
            low = guess

        else:
            high = guess
        guess = ( low + high )/2.0
        ctr += 1
    assert ctr <= 100, 'Iteration count exceeded'
    print 'Bisection method. Num. Iterations:' , ctr, 'Estimate:', guess
    return guess


def testBi():
    print ' squareRootBi(4, 0.0001)'
    squareRootBi(4, 0.0001)
    print ' squareRootBi(9, 0.0001)'
    squareRootBi(9, 0.0001)
    print ' squareRootBi(2, 0.0001)'
    squareRootBi(2, 0.0001)
    print ' squareRootBi(0.25, 0.0001)'
    squareRootBi(0.25, 0.0001)
