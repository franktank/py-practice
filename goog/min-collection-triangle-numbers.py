"""
Write a function that given a target number, finds a minimal collection of triangle numbers that sum to the target

2 -> {1,1}
10 -> {10}
11 -> {10,1}
12 -> {6,6} not {10,1,1}
"""

def min_collect(target):
    dp = {}
    return helper(target,dp)

def helper(target,dp):
    if target == 0:
        return []
    if target in dp:
        return dp[target]
    i = 1 # index of triangle number
    n = 1 # first triangle number
    while n <= target:
        cur = list(helper(target-n, dp))
        cur.append(n) # Add current triangle number
        if target in dp:
            prev_entry = dp[target]
            if len(prev_entry) > len(cur):
                dp[target] = cur
        else:
            dp[target] = cur
        i += 1
        n = i*(i+1)//2
    return dp[target]
