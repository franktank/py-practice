def  countPairs(k, a):
    res = 0
    d = {}
    for i in range(len(a)):
        if k - a[i] in d:
            res += 1
        d[a[i]] = i
    return res

    # OR

    a.sort()
    res = 0
    for i in range((len(a)-1)):
        # bool
        found = False
        start = i+1
        end = len(a)-1
        while start<end:
            mid = (start+end)/2
            if a[mid] == k - a[i]:
                res += 1
                found = True
                break
            elif a[mid] > k-a[i]:
                end = mid-1
            else:
                start = mid + 1
        if (a[i] + a[start] == k or a[i] + a[end] == k) and not found:
            if not(i == start or i == end):
                res += 1
        print("i: {0} start: {1} end: {2}".format(a[i],a[start],a[end]))
    return res
