# KMP

# next[i] is the max k that makes p[0:k] == p[ i+1-k:i+1], p is pattern string

def getNext(s):
    # get next for string s
    next = [0]*len(s)
    for i in range(1, len(s)):
        k = i
        while k > 0:
            if s[0:k] == s[i+1-k:i+1]:
                next[i] = k
                break
            k -= 1
    return next

# reference https://www.zhihu.com/question/21923021


def fastGetNext(p):
    # O(N)
    # p -> pattern string
    next = [0]*len(p)
    for j in range(1, len(p)):
        now = next[j-1]
        if p[j] == p[now]:
            next[j] = now + 1  # we can extend same part
        else:  # decrease now till p[j] == p[now] or now = 0
            while now > 0:
                if p[j] == p[now]:
                    next[j] = next[now-1]
                    break
                now = next[now-1]
            if now == 0:
                if p[j] == p[0]:
                    next[j] = 1
    return next


def buildNext(p):
    next = [0]
    j = 1
    now = 0
    while j < len(p):
        if p[j] == p[now]:
            j += 1
            now += 1
            next.append(now)
        elif now != 0:
            now = next[now-1]
        else:
            next.append(0)
            j += 1
    return next


def kmp(s, p):
    # O(M+N)
    # find first index in s that makes s[i:i+len(p)] = p
    # s  is main string
    # p is pattern string
    next = fastGetNext(p)
    i = 0
    j = 0
    while i < len(s):
        if s[i] == p[j]:
            i += 1
            j += 1
        else:  # s[i] != p[j]
            if j == 0:
                i += 1
            else:
                # move j forward
                j = next[j-1]
        if j == len(p):
            print(i-j)
            j = next[j-1]


s = "ababaabaabac"
p = "abaabac"
print(getNext(p))
print(fastGetNext(p))
print(buildNext(p))
kmp(s, p)
