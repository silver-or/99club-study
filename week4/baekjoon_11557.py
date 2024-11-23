import sys

def solution(T, d):
    for _ in range(T):
        N = int(sys.stdin.readline())
        for _ in range(N):
            school, amount = sys.stdin.readline().split()
            d[school] = int(amount)
        print(max(d, key=d.get))
        d.clear()

def main():
    T = int(sys.stdin.readline())
    d = dict()
    solution(T, d)

if __name__ == '__main__':
    main()
