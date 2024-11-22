import sys

def solution(K, arr):
    answer = 0
    arr.sort()
    answer = arr[K-1]
    return answer

def main():
    _, K = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    print(solution(K, arr))

if __name__ == '__main__':
    main()
