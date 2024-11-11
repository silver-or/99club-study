import sys
N = int(sys.stdin.readline())
l = []

for _ in range(N):
    command, *num = sys.stdin.readline().split()
    match command:
        case 'push':
            l.append(num)
        case 'pop':
            print('-1') if len(l) == 0 else print(*l.pop())
        case 'size':
            print(len(l))
        case 'empty':
            print('1') if not l else print('0')
        case 'top':
            print('-1') if len(l) == 0 else print(*l[-1])
