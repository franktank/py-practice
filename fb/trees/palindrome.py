def pal(s):
    if not s or s == " ":
        return False

    i = 0
    j = len(s)-1

    while i <= j:
        if s[i] == " ":
            i += 1
            continue
        if s[j] == " ":
            j -= 1
            continue
        if s[i] == s[j]:
            i += 1
            j -= 1

        else:
            return False
    return True
