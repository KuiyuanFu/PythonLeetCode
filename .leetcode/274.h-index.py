# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#
# https://leetcode.com/problems/h-index/description/
#
# algorithms
# Medium (36.54%)
# Likes:    940
# Dislikes: 1539
# Total Accepted:    205.8K
# Total Submissions: 562.3K
# Testcase Example:  '[3,0,6,1,5]'
#
# Given an array of integers citations where citations[i] is the number of
# citations a researcher received for their i^th paper, return compute the
# researcher's h-index.
#
# According to the definition of h-index on Wikipedia: A scientist has an index
# h if h of their n papers have at least h citations each, and the other n − h
# papers have no more than h citations each.
#
# If there are several possible values for h, the maximum one is taken as the
# h-index.
#
#
# Example 1:
#
#
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each
# of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the
# remaining two with no more than 3 citations each, their h-index is 3.
#
#
# Example 2:
#
#
# Input: citations = [1,3,1]
# Output: 1
#
#
#
# Constraints:
#
#
# n == citations.length
# 1 <= n <= 5000
# 0 <= citations[i] <= 1000
#
#
#

# @lc tags=hash-table;sort

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求作者的h指数，即有h篇文章有至少h个引用。
# 直接排序，判断。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h = 0
        for i, n in enumerate(reversed(citations)):
            if n > i:
                h = i + 1
            else:
                break
        return h

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('citations = [3,0,6,1,5]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().hIndex([3, 0, 6, 1, 5])))
    print()

    print('Example 2:')
    print('Input : ')
    print('citations = [1,3,1]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().hIndex([1, 3, 1])))
    print()

    pass
# @lc main=end