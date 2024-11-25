class Solution:
    def largestInteger(self, num: int) -> int:
        nums = list(map(int, str(num)))
        odds = [n for n in nums if n % 2 != 0]
        evens = [n for n in nums if n % 2 == 0]

        # 내림차순으로 정렬
        odds.sort(reverse=True)
        evens.sort(reverse=True)

        # 교환하며 리스트를 재구성
        for i in range(len(nums)):
            if nums[i] % 2 == 0:  # 짝수
                nums[i] = evens.pop(0)  # 가장 큰 짝수 사용
            else:  # 홀수
                nums[i] = odds.pop(0)  # 가장 큰 홀수 사용

        return int(''.join(map(str, nums)))

def main():
    print(Solution().largestInteger(1234))
    print(Solution().largestInteger(65875))
    print(Solution().largestInteger(266))

if __name__ == '__main__':
    main()
