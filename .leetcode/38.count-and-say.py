# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say/description/
#
# algorithms
# Medium (46.25%)
# Likes:    374
# Dislikes: 1332
# Total Accepted:    494.1K
# Total Submissions: 1.1M
# Testcase Example:  '1'
#
# The count-and-say sequence is a sequence of digit strings defined by the
# recursive formula:
#
#
# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from
# countAndSay(n-1), which is then converted into a different digit string.
#
#
# To determine how you "say" a digit string, split it into the minimal number
# of groups so that each group is a contiguous section all of the same
# character. Then for each group, say the number of characters, then say the
# character. To convert the saying into a digit string, replace the counts with
# a number and concatenate every saying.
#
# For example, the saying and conversion for digit string "3322251":
#
# Given a positive integer n, return the n^th term of the count-and-say
# sequence.
#
#
# Example 1:
#
#
# Input: n = 1
# Output: "1"
# Explanation: This is the base case.
#
#
# Example 2:
#
#
# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
#
#
#
# Constraints:
#
#
# 1 <= n <= 30
#
#
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 读数字，每次遇到连续的数字时，读作n个x，记作nx，作为下一轮需要读的字符串。
# 就是简单递归。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        nPre = 0
        cPre = ''
        res = ''
        for c in (self.countAndSay(n - 1) + ' '):
            if c == cPre:
                nPre += 1
            else:
                res = res + (str(nPre) if nPre != 0 else '') + cPre
                cPre = c
                nPre = 1
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 1')
    print('Output :')
    print(str(Solution().countAndSay(1)))
    print('Exception :')
    print('"1"')
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 4')
    print('Output :')
    print(str(Solution().countAndSay(4)))
    print('Exception :')
    print('"1211"')
    print()

    pass
# @lc main=end