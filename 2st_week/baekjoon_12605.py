import sys
N = int(sys.stdin.readline())
for i in range(N):
    case = sys.stdin.readline().split()
    case.reverse()
    print(f'Case #{i+1}:', end=' ')
    print(*case)