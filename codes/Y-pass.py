n = int(input())
a = input().split(' ')
b = input().split(' ')
# a = [int(a[i]) for i in range(len(a))]
# b = [int(b[i]) for i in range(len(b))]

c = [[int(b[i]) -int(a[i]), int(a[i]), int(b[i])] for i in range(n)]
c = sorted(c, reverse=True)

res = 0
for i in range(n//2):
    res += c[i][1]
for i in range(n//2, n):
    res += c[i][2]
print(res)
