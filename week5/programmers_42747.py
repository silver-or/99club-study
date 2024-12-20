def solution(citations):
    citations.sort(reverse=True)

    # H_index가 존재하고 H_index를 넘는 논문이 몇 개인지 구할때
    for i in range(len(citations)):
        if citations[i] < i+1:
            return i

    # 인용 횟수가 모두 같을때는 전체를 return
    return len(citations)

def main():
    print(solution([3, 0, 6, 1, 5]))
    print(solution([5, 5, 5, 5]))

if __name__ == '__main__':
    main()