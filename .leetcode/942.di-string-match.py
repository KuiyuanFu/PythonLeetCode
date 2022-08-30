# @lc app=leetcode id=942 lang=python3
#
# [942] DI String Match
#
# https://leetcode.com/problems/di-string-match/description/
#
# algorithms
# Easy (76.37%)
# Likes:    1871
# Dislikes: 743
# Total Accepted:    115.5K
# Total Submissions: 151.2K
# Testcase Example:  '"IDID"'
#
# A permutation perm of n + 1 integers of all the integers in the range [0, n]
# can be represented as a string s of length n where:
#
#
# s[i] == 'I' if perm[i] < perm[i + 1], and
# s[i] == 'D' if perm[i] > perm[i + 1].
#
#
# Given a string s, reconstruct the permutation perm and return it. If there
# are multiple valid permutations perm, return any of them.
#
#
# Example 1:
# Input: s = "IDID"
# Output: [0,4,1,3,2]
# Example 2:
# Input: s = "III"
# Output: [0,1,2,3]
# Example 3:
# Input: s = "DDI"
# Output: [3,2,0,1]
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s[i] is either 'I' or 'D'.
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数组的相邻两元素的大小关系，求一个可能的排列。
# 直接从最大或最小开始，如果趋势上升，那么就添加最小值，否者添加最大值。这样每一步都是只会使范围缩小一个，大小关系不变。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def diStringMatch(self, s: str) -> List[int]:
        i, d = 0, len(s)
        res = []

        for c in s:
            if c == 'I':
                res.append(i)
                i += 1
            else:
                res.append(d)
                d -= 1
        res.append(i)
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "IDID"')
    print('Exception :')
    print('[0,4,1,3,2]')
    print('Output :')
    print(str(Solution().diStringMatch("IDID")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "III"')
    print('Exception :')
    print('[0,1,2,3]')
    print('Output :')
    print(str(Solution().diStringMatch("III")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "DDI"')
    print('Exception :')
    print('[3,2,0,1]')
    print('Output :')
    print(str(Solution().diStringMatch("DDI")))
    print()

    pass
# @lc main=end