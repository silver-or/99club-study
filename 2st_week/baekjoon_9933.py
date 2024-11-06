N = int(input())
words = []
answer = ''
for _ in range(N):
    words.append(input())

for word in words:
    rWord = word[::-1]
    if rWord in words:
        answer = rWord
        break

mIndex = len(answer) // 2
print(len(answer), answer[mIndex])