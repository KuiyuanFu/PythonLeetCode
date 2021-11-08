# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (65.78%)
# Likes:    5311
# Dislikes: 142
# Total Accepted:    298.1K
# Total Submissions: 450.7K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to
# wait after the i^th day to get a warmer temperature. If there is no future
# day for which this is possible, keep answer[i] == 0 instead.
#
#
# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
#
#
# Constraints:
#
#
# 1 <= temperatures.length <= 10^5
# 30 <= temperatures[i] <= 100
#
#
#

# @lc tags=hash-table;stack

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 找多久之后才会更热。
# 栈。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = []
        for i in reversed(range(len(temperatures))):
            t = temperatures[i]
            while s and s[-1][0] <= t:
                s.pop()
            if s:
                res[i] = s[-1][1] - i
            s.append((t, i))

        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('temperatures = [73,74,75,71,69,72,76,73]')
    print('Exception :')
    print('[1,1,4,2,1,1,0,0]')
    print('Output :')
    print(str(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])))
    print()

    print('Example 2:')
    print('Input : ')
    print('temperatures = [30,40,50,60]')
    print('Exception :')
    print('[1,1,1,0]')
    print('Output :')
    print(str(Solution().dailyTemperatures([30, 40, 50, 60])))
    print()

    print('Example 3:')
    print('Input : ')
    print('temperatures = [30,60,90]')
    print('Exception :')
    print('[1,1,0]')
    print('Output :')
    print(str(Solution().dailyTemperatures([30, 60, 90])))
    print()

    pass
# @lc main=end