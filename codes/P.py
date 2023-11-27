w = input()
n = int(w.split(' ')[0])
bag = int(w.split(' ')[1])
value = input().split(' ')
weight = input().split(' ')
value = [int(value[i]) for i in range(n)]
weight = [int(weight[i]) for i in range(n)]

dp = [0 for _ in range(bag + 1)]
for i in range(n):
    for j in range(bag, weight[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
print(dp[-1])
