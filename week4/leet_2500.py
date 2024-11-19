import heapq

class Solution:
    def __init__(self):
        self.answer = 0

    def deleteGreatestValue(self, grid: [[int]]) -> int:
        heap = [[-col for col in row] for row in grid]
        l = []

        for row in heap:
            heapq.heapify(row)
        for i in range(len(heap[0])):
            for row in heap:  # [1, 2, 4]
                l.append(-heapq.heappop(row))  # 4, 3
            self.answer += max(l)
            l.clear()
        return self.answer


print(Solution().deleteGreatestValue([[1,2,4],[3,3,1]]))
print(Solution().deleteGreatestValue([[10]]))
