K = int(input())
N = 0
while True:
    x = int(input())
    if x == 0:
        break
    if x < K:
        N += 1
print(N)