from collections import deque

N = int(input())
arr = deque([i + 1 for i in range(N)])
discard = []

while arr:
    # 1. 맨 앞의 요소를 제거하고 discard에 추가
    discard.append(arr.popleft())

    # 2. arr에 요소가 남아 있으면 맨 앞 요소를 뒤로 보냄
    if arr:
        arr.append(arr.popleft())

print(*discard)