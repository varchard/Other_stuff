# generate triangles
def triangle_at_n(n):
    '''accepts integer n, generates the 'triangle' value for n'''
    triangle = 0
    for i in range(n+1):
        triangle += i
    return triangle

# # test number of factors
def test_factors(triangle):
    '''accepts integer n, returns the number of factors of a given number, 
    also could be easily refactored to return list of factors'''
    factors = []
    for i in range(1,int(triangle**(1/2))+1):
        if triangle % i == 0:
            factors.append(i)
            if triangle / i != i:
                factors.append(triangle//i)
    # print(factors)
    return len(factors)