# Standard Input
# 输入包含三行，每行包含三个整数，描述了一个三阶矩阵。
#
# Standard Output
# 输出一行一个整数，表示行列式的值。

row1 = input().split(' ')
row2 = input().split(' ')
row3 = input().split(' ')
matrix = [row1, row2, row3]
res = 0
res = int(matrix[0][0]) * int(matrix[1][1]) * int(matrix[2][2]) + \
      int(matrix[0][1]) * int(matrix[1][2]) * int(matrix[2][0]) + \
      int(matrix[1][0]) * int(matrix[2][1]) * int(matrix[0][2]) - \
      int(matrix[0][2]) * int(matrix[1][1]) * int(matrix[2][0]) - \
      int(matrix[0][0]) * int(matrix[1][2]) * int(matrix[2][1]) - \
      int(matrix[0][1]) * int(matrix[1][0]) * int(matrix[2][2])
print(res)
