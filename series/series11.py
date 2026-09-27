N = int(input())
K = int(input())
a = False
for i in range(N):
    x = int(input())
    if x < K:
        a = True
print(a)