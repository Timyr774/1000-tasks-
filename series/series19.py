N = int(input())
B = int(input())
K = int(input())
for i in range(N-1):
    C = int(input())
    if C < B:
        print(C)
        K += 1
    B = C
print(K)