import sys
import heapq

heap = []

N = int(sys.stdin.readline())

for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    elif num > 0:
        heapq.heappush(heap, num)