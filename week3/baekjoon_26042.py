import sys
import queue

N = int(sys.stdin.readline())
q = queue.Queue()
maxWaiting, minNum = 0, 0

for _ in range(N):
    info, *sNum = sys.stdin.readline().split()
    match info:
        case '1':
            num = int(sNum[0])
            q.put(num)
            if q.qsize() > maxWaiting:
                maxWaiting = q.qsize()
                minNum = num

            elif q.qsize() == maxWaiting and num < minNum:
                minNum = num
        case '2':
            q.get()

print(maxWaiting, minNum)

