# @lc app=leetcode id=826 lang=python3
#
# [826] Most Profit Assigning Work
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 不同工作难度对应不同的钱，求工人们最大的利润。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int],
                            worker: List[int]) -> int:
        pairs = [[difficulty[i], profit[i]] for i in range(len(difficulty))]
        pairs.sort()

        for i in range(1, len(difficulty)):
            pairs[i][1] = max(pairs[i][1], pairs[i - 1][1])

        profit = 0
        for d in worker:
            idx = bisect_right(pairs, [d + 1, 0]) - 1
            if idx >= 0:
                profit += pairs[idx][1]
            pass
        return profit
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker =[4,5,6,7]'
    )
    print('Exception :')
    print('100')
    print('Output :')
    print(
        str(Solution().maxProfitAssignment([2, 4, 6, 8, 10],
                                           [10, 20, 30, 40, 50],
                                           [4, 5, 6, 7])))
    print()

    print('Example 2:')
    print('Input : ')
    print('difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]')
    print('Exception :')
    print('0')
    print('Output :')
    print(
        str(Solution().maxProfitAssignment([85, 47, 57], [24, 66, 99],
                                           [40, 25, 25])))
    print()

    pass
# @lc main=end