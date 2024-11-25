class Solution:
    def __init__(self):
        self.answer = 0

    def largestInteger(self, num: int) -> int:
        nums = list(map(int, str(num)))
        odds, evens = [], []

        for n in nums:
            if n % 2 == 0:
                evens.append(n)
            else:
                odds.append(n)

        odds.sort(reverse=True)
        evens.sort(reverse=True)

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = evens.pop(0)  # 가장 큰 짝수로 교체
            else:
                nums[i] = odds.pop(0)  # 가장 큰 홀수로 교체

        self.answer = int(''.join(map(str, nums)))
        return self.answer

def main():
    print(Solution().largestInteger(1234))
    print(Solution().largestInteger(65875))
    print(Solution().largestInteger(266))

if __name__ == '__main__':
    main()
