"""
Write a function that given a target number, finds a minimal collection of triangle numbers that sum to the target

2 -> {1,1}
10 -> {10}
11 -> {10,1}
12 -> {6,6} not {10,1,1}
"""

# Triangle number can be generated from
# make calculations with all triangle numbers smaller than target


def min_collect(target):
    d = {}
    helper(d, target)

def helper(d, target):
    if target == 0:
        # Found a possible combination
        return [] # WTF
    if target in d:
        return d[target]
    i = 1
    n = 1
    while n <= target:
        cur = list(helper(d, target-n))
        cur.append(n) # MONUMENTAL STEP
        if target in d:
            if len(cur) < len(d[target]):
                d[target] = cur
        else:
            d[target] = cur
        i += 1
        n = i*(i+1)//2
    return d[target]
