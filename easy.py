def fibonacci(i): return (i<=1 and 1) or fibonacci(i-1) + fibonacci(i-2)

def pascals(i, j): return ((j==0 or i==j+1) and 1) or pascals(i-1, j-1) + pascals(i-1, j)


''' Test function for pascal '''
def test_pascal():
    for i in range(10):
        for j in range(i):
            print pascals(i, j),
        print 
