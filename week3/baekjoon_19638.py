import sys
import heapq

# 입력 처리
N, H, T = map(int, sys.stdin.readline().split())
heap = []

# 최대 힙 구성 (음수로 저장하여 최대 힙처럼 사용)
for _ in range(N):
    heapq.heappush(heap, -int(sys.stdin.readline()))

trial = 0
success = False

while heap and trial < T:
    # 가장 큰 키를 가져옴
    tallest = -heapq.heappop(heap)
    if tallest < H:
        success = True  # 가장 큰 키가 H 미만이라면 성공
        break

    # 키가 H 이상이고, 더 나눌 수 있다면 뿅망치 사용
    if tallest > 1:
        tallest //= 2
        heapq.heappush(heap, -tallest)  # 다시 힙에 삽입
        trial += 1
    else:
        # 키가 1이면 더 이상 나눌 수 없음
        heapq.heappush(heap, -tallest)
        break

# 결과 확인
if success or (heap and -heap[0] < H):
    print(f"YES\n{trial}")
else:
    print(f"NO\n{-heap[0]}")
