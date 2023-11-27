# w = input().split(' ')
# n = int(w[0])
# diamonds = int(w[1])
# arr = input().split(' ')
# arr = [int(arr[i]) for i in range(len(arr))]
# boxes = [0 for _ in range(n)]
# for i in range(len(arr)):
#     boxes[arr[i]-1] += 1
# print(boxes)
#
# def select(boxes):
#     if len(boxes) == 2:
#         return max(boxes)
#     return max(boxes[0]+select(boxes[1:-1]), boxes[-1]+select(boxes[0:-2]))
# print(select(boxes))

print('Win')
