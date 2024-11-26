import sys

def solution(T):
    for _ in range(T):
        sys.stdin.readline()
        N, M = map(int, sys.stdin.readline().split())
        sejun = sorted(list(map(int, sys.stdin.readline().split())))
        sebi = sorted(list(map(int, sys.stdin.readline().split())))

        while sejun and sebi:
            if sejun[0] < sebi[0]:
                sejun.pop(0)
            else: # sejun[0] >= sebi[0]
                sebi.pop(0)

        if sejun:
            print('S')
        elif sebi:
            print('B')
        else:
            print('C')

def main():
    solution(int(sys.stdin.readline()))

if __name__ == '__main__':
    main()
