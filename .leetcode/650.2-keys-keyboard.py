# @lc app=leetcode id=650 lang=python3
#
# [650] 2 Keys Keyboard
#
# https://leetcode.com/problems/2-keys-keyboard/description/
#
# algorithms
# Medium (51.16%)
# Likes:    2124
# Dislikes: 152
# Total Accepted:    87.7K
# Total Submissions: 170.7K
# Testcase Example:  '3'
#
# There is only one character 'A' on the screen of a notepad. You can perform
# two operations on this notepad for each step:
#
#
# Copy All: You can copy all the characters present on the screen (a partial
# copy is not allowed).
# Paste: You can paste the characters which are copied last time.
#
#
# Given an integer n, return the minimum number of operations to get the
# character 'A' exactly n times on the screen.
#
#
# Example 1:
#
#
# Input: n = 3
# Output: 3
# Explanation: Intitally, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= n <= 1000
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 复制粘贴到指定位数。
# 动态规划。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0, 0]
        for i in range(2, n + 1):
            r = i
            for j in range(2, i // 2 + 1):
                if i % j == 0:
                    r = min(r, dp[j] + (i // j))
            dp.append(r)

        return dp[-1]

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().minSteps(6)))
    print('Example 1:')
    print('Input : ')
    print('n = 3')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().minSteps(3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().minSteps(1)))
    print()

    pass
# @lc main=end
