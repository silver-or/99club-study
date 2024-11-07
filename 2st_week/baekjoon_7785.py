from collections import defaultdict

n = int(input())
d = defaultdict(str)

for _ in range(n):
    person, status = input().split()
    d[person] = status

sorted_dict = dict(sorted(d.items(), key=lambda x: x[0], reverse=True))

for k, v in sorted_dict.items():
    if v == 'enter':
        print(k)
