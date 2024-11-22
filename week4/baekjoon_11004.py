import sys

def solution(N, K, arr):
    answer = 0
    arr.sort()
    answer = arr[K-1]
    return answer

def main():
    N, K = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    print(solution(N, K, arr))

if __name__ == '__main__':
    main()
