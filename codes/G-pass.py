# Standard Input
# 输入只有一行，有一个字符串str和一个非负整数x，字符串str形如YYYYMMDD，表示今年某一天的年份、月份和日期，以及说这句话的同学人数。
# 输入保证题目给出的日期不早于今天（20221126），但早于2023年元旦，即YYYY=2022，若MM=11则26<=DD<=30,否则MM=12且1<=DD<=31,具体请见样例。
# 另外还保证0<=x<=50
#
# Standard Output
# 一行一个整数，表示Redcrown会给出去多少钱。

w = input().split(' ')
date = int(w[0])
people = int(w[1])
thusday = False
if (date-20221201) % 7 == 0 and date >= 20221200:
    thusday = True
if thusday:
    print(50 * people)
else:
    print(0)
