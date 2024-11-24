class Solution:
    def __init__(self):
        self.answer = list()

    def findRelativeRanks(self, score: [int]) -> [str]:
        rank = dict()
        score_copy = score.copy()
        score_copy.sort(reverse=True)
        for index, element in enumerate(score_copy):
            match index:
                case 0:
                    rank[element] = 'Gold Medal'
                case 1:
                    rank[element] = 'Silver Medal'
                case 2:
                    rank[element] = 'Bronze Medal'
                case _:
                    rank[element] = str(index+1)

        for s in score:
            self.answer.append(rank.get(s))

        return self.answer

def main():
    print(Solution().findRelativeRanks([5, 4, 3, 2, 1]))
    print(Solution().findRelativeRanks([10, 3, 8, 9, 4]))

if __name__ == '__main__':
    main()
