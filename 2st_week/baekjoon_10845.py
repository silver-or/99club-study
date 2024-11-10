import sys
import queue

N = int(sys.stdin.readline())
q = queue.Queue()

for _ in range(N):
    command, *num = sys.stdin.readline().split()
    match command:
        case 'push':
            q.put(int(num[0]))
        case 'pop':
            print('-1') if q.empty() else print(q.get())
        case 'size':
            print(q.qsize())
        case 'empty':
            print('1') if q.empty() else print('0')
        case 'front':
            print('-1') if q.empty() else print(q.queue[0])
        case 'back':
            print('-1') if q.empty() else print(q.queue[-1])
