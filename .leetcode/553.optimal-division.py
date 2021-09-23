# @lc app=leetcode id=553 lang=python3
#
# [553] Optimal Division
#
# https://leetcode.com/problems/optimal-division/description/
#
# algorithms
# Medium (58.12%)
# Likes:    226
# Dislikes: 1291
# Total Accepted:    29.4K
# Total Submissions: 50.5K
# Testcase Example:  '[1000,100,10,2]'
#
# You are given an integer array nums. The adjacent integers in nums will
# perform the float division.
#
#
# For example, for nums = [2,3,4], we will evaluate the expression "2/3/4".
#
#
# However, you can add any number of parenthesis at any position to change the
# priority of operations. You want to add these parentheses such the value of
# the expression after the evaluation is maximum.
#
# Return the corresponding expression that has the maximum value in string
# format.
#
# Note: your expression should not contain redundant parenthesis.
#
#
# Example 1:
#
#
# Input: nums = [1000,100,10,2]
# Output: "1000/(100/10/2)"
# Explanation:
# 1000/(100/10/2) = 1000/((100/10)/2) = 200
# However, the bold parenthesis in "1000/((100/10)/2)" are redundant, since
# they don't influence the operation priority. So you should return
# "1000/(100/10/2)".
# Other cases:
# 1000/(100/10)/2 = 50
# 1000/(100/(10/2)) = 50
# 1000/100/10/2 = 0.5
# 1000/100/(10/2) = 2
#
#
# Example 2:
#
#
# Input: nums = [2,3,4]
# Output: "2/(3/4)"
#
#
# Example 3:
#
#
# Input: nums = [2]
# Output: "2"
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10
# 2 <= nums[i] <= 1000
# There is only one optimal division for the given iput.
#
#
#

# @lc tags=math;string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将一个连除加括号，改变优先级，使结果最大。
# 动态规划。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        length = len(nums)
        dp = [[[[0, None], [1001, None]] for _ in range(length)]
              for _ in range(length)]
        for i in range(length):
            d = dp[i][i]
            d[0][0] = nums[i]
            d[1][0] = nums[i]
        for step in range(1, length):
            for l in range(0, length - step):
                r = l + step
                d = dp[l][r]
                for m in range(l, r):
                    maxi = dp[l][m][0][0] / dp[m + 1][r][1][0]
                    if maxi > d[0][0]:
                        d[0][0] = maxi
                        d[0][1] = m
                    mini = dp[l][m][1][0] / dp[m + 1][r][0][0]
                    if mini < d[1][0]:
                        d[1][0] = mini
                        d[1][1] = m

        def buildStr(l, r, flag):
            if l == r:
                return str(nums[l])
            m = dp[l][r][flag][1]
            leftStr = buildStr(l, m, flag)
            rightStr = buildStr(m + 1, r, flag ^ 1)
            if r > m + 1:
                rightStr = '(' + rightStr + ')'
            return leftStr + '/' + rightStr

        return buildStr(0, length - 1, 0)
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1000,100,10,2]')
    print('Exception :')
    print('"1000/(100/10/2)"')
    print('Output :')
    print(str(Solution().optimalDivision([1000, 100, 10, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [2,3,4]')
    print('Exception :')
    print('"2/(3/4)"')
    print('Output :')
    print(str(Solution().optimalDivision([2, 3, 4])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [2]')
    print('Exception :')
    print('"2"')
    print('Output :')
    print(str(Solution().optimalDivision([2])))
    print()

    pass
# @lc main=end