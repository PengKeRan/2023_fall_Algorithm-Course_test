n = int(input())
a = input().split(' ')
a = [int(a[i]) for i in range(n)]

cnt = 0
nums = [0, 0, 0]
times3 = 0
for i in range(n):
    times = a[i] // 3
    a[i] -= times * 3
    cnt += times
    nums[a[i]] += 1

    times3 += times

num_1 = nums[1]
num_2 = nums[2]
temp = min(num_1, num_2)
cnt += temp
num_1 -= temp
num_2 -= temp
# 如果1剩得多
if num_1 != 0:
    while num_1 > 0 and times3 > 0:
        num_1 -= 3
        cnt = cnt - 1 + 2
        times3 -= 1
    if num_1 > 0:
        cnt += (num_1 + 1) // 2
# 如果2剩得多
if num_2 != 0:
    times = num_2 // 3
    cnt += times * 2
    num_2 -= times * 3
    if num_2 == 1:
        cnt += 1
    if num_2 == 2:
        cnt += 2
print(cnt)
