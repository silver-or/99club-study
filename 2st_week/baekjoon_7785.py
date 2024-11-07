from collections import defaultdict

n = int(input())
d = defaultdict(str)
l = []
for _ in range(n):
    person = input().split()
    d[person[0]] = person[1]

sorted_dict = dict(sorted(d.items(), key=lambda x: x[0], reverse=True))

for k, v in sorted_dict.items():
    if v == 'enter':
        print(k)
