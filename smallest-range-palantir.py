"""
Given a set of number ranges, e.g. [3,6],[5,9],[1,2],[10,15]
Develop an efficient algorithm to output the smallest number of ranges without losing any information. i.e. Output => [1,2],[3,9],[10,15] as [3,6] and [5,9] overlap so they can be merged to just be one range [3,9].

Extra info: If you had [2,5],[6,7] these would not merge as [2,7] would include all numbers between 5 and 6 which was not in the original subsets.
You should be able to come up with a solution that is better than O(N^2)
"""

def combine(a, b):
    """
    rtype: bool
    """
    if a[1] >= b[0]:
        return True

    return False

a = [[3,6],[3,9],[5,9],[1,2],[10,15]]
# a = [[1,3], [3,4], [4,6]]

a.sort() # [[1, 2], [3, 6], [3, 9], [5, 9], [10, 15]]
ret = {}
for i in range(len(a)):
    if i == 0:
        continue
    if (not(combine(a[i - 1], a[i])) and i == (len(a)-1)):
        ret[str(a[i])] = True
    if combine(a[i - 1], a[i]):
        interval = [a[i - 1][0], a[i][1]]
        if str(a[i - 1]) in ret:
            del ret[str(a[i - 1])]
        ret[str(interval)] = True
        a[i] = interval
    else:
        ret[str(a[i - 1])] = True

print(ret.keys())
