s1 = input()
s2 = input()


# s1 = 'abababaabababaabababaabababaabababa'
# s2 = 'abcd'

def getNext(s1, s2):
    next = [0 for _ in range(len(s2))]
    next[0] = -1
    j = 0
    i = next[0]
    while j < len(s2) - 1:
        if i == -1 or s2[i] == s2[j]:
            i += 1
            j += 1
            next[j] = i
        else:
            i = next[i]
    return next


def kmp(s1, s2):
    if len(s2) == 1:
        cnt = 0
        for i in range(len(s1)):
            if s1[i] == s2:
                cnt += 1
        return cnt
    next = getNext(s1, s2)

    i = 0
    j = 0
    cnt = 0
    while i < len(s1):
        while i < len(s1) and j < len(s2):
            if j == -1 or s1[i] == s2[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == len(s2):
            cnt += 1
            j = 0
            i -= 1
    return cnt


cnt = kmp(s1, s2)
print(cnt)
