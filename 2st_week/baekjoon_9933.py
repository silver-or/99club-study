N = int(input())
words = []
answer = ''
for _ in range(N):
    words.append(input())
# print(words) # ['las', 'god', 'psala', 'sal']
for word in words:
    rWord = word[::-1]
    if rWord in words:
        answer = rWord
mIndex = int(len(answer)/2)
print(len(answer), answer[mIndex])
