scheduler = dict()

N = int(input())
for i in range(N):
    for j in range(4):
        schedule = input().split()
        for worker in schedule:
            if worker == '-':
                continue
            if j in [0, 2]:
                scheduler[worker] += 4
            elif j == 1:
                scheduler[worker] += 6
            else:
                scheduler[worker] += 10
print(scheduler)