# @lc app=leetcode id=556 lang=python3
#
# [556] Next Greater Element III
#
# https://leetcode.com/problems/next-greater-element-iii/description/
#
# algorithms
# Medium (33.40%)
# Likes:    1565
# Dislikes: 284
# Total Accepted:    76.9K
# Total Submissions: 230.3K
# Testcase Example:  '12'
#
# Given a positive integer n, find the smallest integer which has exactly the
# same digits existing in the integer n and is greater in value than n. If no
# such positive integer exists, return -1.
#
# Note that the returned integer should fit in 32-bit integer, if there is a
# valid answer but it does not fit in 32-bit integer, return -1.
#
#
# Example 1:
# Input: n = 12
# Output: 21
# Example 2:
# Input: n = 21
# Output: -1
#
#
# Constraints:
#
#
# 1 <= n <= 2^31 - 1
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将数字每一位的值重新排序成比其大的最小值。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        cl = [c for c in str(n)]

        l = []
        for i in range(len(cl) - 1, -1, -1):
            idx = bisect_right(l, cl[i])
            if idx == len(l):
                l.append(cl[i])
            else:
                cl[i], l[idx] = l[idx], cl[i]
                cl[i + 1:] = l[:]
                res = int(''.join(cl))
                if res > 2**31 - 1:
                    return -1
                else:
                    return res
        return -1
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 12')
    print('Exception :')
    print('21')
    print('Output :')
    print(str(Solution().nextGreaterElement(12)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 21')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().nextGreaterElement(21)))
    print()
    print(str(Solution().nextGreaterElement(2147483486)))
    pass
# @lc main=end