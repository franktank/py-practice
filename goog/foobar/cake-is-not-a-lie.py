"""
Test cases
==========

Inputs:
    (string) s = "abccbaabccba"
Output:
    (int) 2

Inputs:
    (string) s = "abcabcabcabc"
Output:
    (int) 4
"""

abcabc
a -> bcabc
ab


if substring reduced to nothing -> return
1 +
else if not part of substring
res = 0

def answer(s):
    res = 0
    for i in range(1, len(s)):
        if helper(s[:i], s[i:]):
            res = max(res, len(s)/i)
    return res

def helper(prev, cur):
    if not cur:
        return True
    if prev == cur[:len(prev)]:
        return helper(prev, cur[len(prev):])
    else:
        return False
