n = int(input())
cards = input().split(' ')
enemy = input().split(' ')
x = int(cards[0])
y = int(cards[1])
enemy = [int(enemy[i]) for i in range(n)]

ans = 10000
for i in range(max(enemy)):
    cnt = 0
    for j in range(0, n):
        cnt += max((enemy[j]-x*i+y-1)//y, 0)
    ans = min(ans, cnt+i)
print(ans)

# if fireball <= xf:
#     print((max(enemy) // xf) + 1)
#
# use_xf = False
# rounds = 0
# while sum(enemy) > 0:
#     xf_damage = 0
#     i = 0
#     while i < n:
#         if enemy[i] > xf:
#             xf_damage += xf
#         xf_damage += enemy[i]
#         if xf_damage >= fireball:
#             use_xf = True
#             break
#         i += 1
#     if use_xf:
#         rounds += 1
#         for i in range(n):
#             if enemy[i] > xf:
#                 enemy[i] -= xf
#             else:
#                 enemy[i] = 0
#     else:
#         for i in range(n):
#             if enemy[i] > 0:
#                 temp = enemy[i] // fireball
#                 rounds = rounds + temp + 1
#                 enemy[i] = 0
# print(rounds)



