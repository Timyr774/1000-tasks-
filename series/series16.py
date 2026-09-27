K = int(input())
N = 0
A = 0
while True:
    x = int(input())
    if x == 0:
        break
    N += 1
    if x < K:
        A = N

print(A)