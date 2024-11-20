import sys
import heapq

N = int(sys.stdin.readline())
cnt = 0

# 첫 번째 입력은 다솜이의 득표수
dasom = int(sys.stdin.readline())

# 나머지 후보의 득표수는 최소 힙으로 관리
heap = []
for _ in range(N - 1):
    heapq.heappush(heap, -int(sys.stdin.readline()))  # 음수로 저장 (최대 힙처럼 사용)

while heap and -heap[0] >= dasom:
    # 가장 많은 득표수를 가진 후보를 가져오기
    max_votes = -heapq.heappop(heap)
    max_votes -= 1  # 한 표를 빼앗음
    dasom += 1      # 다솜이가 한 표를 얻음
    cnt += 1

    # 수정된 득표수를 다시 힙에 삽입
    heapq.heappush(heap, -max_votes)

print(cnt)
