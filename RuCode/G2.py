def prefix_function(s):
    n = len(s)
    p = [0] * n
    for i in range(1, n):
        k = p[i-1]
        while (k > 0 and s[k] != s[i]):
            k = p[k - 1]
        if s[i] == s[k]:
            k += 1
        p[i] = k
    return p

s = input()

a = prefix_function(s)
b = prefix_function(s[::-1])
# print(a)
# print(b)
print(s[:min(a[-1],b[-1])+1])
