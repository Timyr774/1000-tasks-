N =  int(input())
sum = 0
for i in range(1, N * 2):
    if i % 2 != 0:
        sum += i
        print(sum)