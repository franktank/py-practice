import sys
def cut_rod(p, n):
    """
    p -> array of prices
    n -> length of rod
    """

    r = [None for _ in range(n + 1)]
    r[0] = 0 # cost is 0 for 0 length
    soln = [None for _ in range(n + 1)]
    soln[0] = 0
    for i in range(1, n + 1):
        profit = -sys.maxint - 1
        for j in range(1, j):
            if p[j] + r[i - j] > profit:
                profit = p[j] + r[i - j]
                soln[i] = j
        r[i] = profit

    solnstr = ''
    while n > 0:
        solnstr += str(soln[n])
        n -= soln[n]
    return r[n], solnstr
