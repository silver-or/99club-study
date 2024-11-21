import heapq

def solution(scoville, K):
    heap = scoville
    answer = 0
    heapq.heapify(heap)

    while heap[0] < K and len(heap) >= 2:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        mixed = n1 + (n2 * 2)
        heapq.heappush(heap, mixed)
        answer += 1

    if heap[0] < K:
        return -1

    return answer

def main():
    print(solution([1, 2, 3, 9, 10, 12], 7))
    print(solution([1, 1, 1], 10))

if __name__ == '__main__':
    main()


