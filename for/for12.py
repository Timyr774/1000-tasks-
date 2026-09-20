N = int(input())
sum = 1
for i in range(N):
    sum *= 1 + ((i + 1) / 10)
print(sum)