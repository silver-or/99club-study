import heapq
import math

class Solution:
    def __init__(self):
        self.heap = []
        self.sum = 0

    def pick_gifts(self, gifts: [int], k: int) -> int:
        for gift in gifts:
            heapq.heappush(self.heap, -gift)

        for i in range(0, k):
            max_gift = -heapq.heappop(self.heap)
            max_gift = math.floor(math.sqrt(max_gift))
            heapq.heappush(self.heap, -max_gift)

        for e in self.heap:
            self.sum += e

        return -self.sum

print(Solution().pick_gifts([25,64,9,4,100], 4))
print(Solution().pick_gifts([1,1,1,1], 4))