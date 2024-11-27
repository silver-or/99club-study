import sys

def solution(M, N):
    num_dict = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }

    alpha_dict = {v:k for k,v in num_dict.items()}

    nums = [i for i in range(M, N+1)]
    alphas = []
    for num in nums:
        a = ""
        for i in str(num):
            a += num_dict[i] + " "
        alphas.append(a.rstrip())

    sorted_alphas = sorted(alphas) # 문자열 정렬
    i = 0
    for sorted_alpha in sorted_alphas:
        for a in sorted_alpha.split():
            print(alpha_dict.get(a), end="")
        print(end=" ")
        i += 1
        if i % 10 == 0: print()

def main():
    M, N = map(int, sys.stdin.readline().split())
    solution(M, N)

if __name__ == '__main__':
    main()