# @lc app=leetcode id=335 lang=python3
#
# [335] Self Crossing
#
# https://leetcode.com/problems/self-crossing/description/
#
# algorithms
# Hard (28.85%)
# Likes:    194
# Dislikes: 421
# Total Accepted:    25.8K
# Total Submissions: 89.6K
# Testcase Example:  '[2,1,1,2]'
#
# You are given an array of integers distance.
#
# You start at point (0,0) on an X-Y plane and you move distance[0] meters to
# the north, then distance[1] meters to the west, distance[2] meters to the
# south, distance[3] meters to the east, and so on. In other words, after each
# move, your direction changes counter-clockwise.
#
# Return true if your path crosses itself, and false if it does not.
#
#
# Example 1:
#
#
# Input: distance = [2,1,1,2]
# Output: true
#
#
# Example 2:
#
#
# Input: distance = [1,2,3,4]
# Output: false
#
#
# Example 3:
#
#
# Input: distance = [1,1,1,1]
# Output: true
#
#
#
# Constraints:
#
#
# 1 <= distance.length <= 10^5
# 1 <= distance[i] <= 10^5
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一系列正整数，依次按照逆时针次序移动，判断路径是否交叉。
# 每新添加一根线，与之前线交叉的情况是固定的。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        d = distance
        for i in range(len(d)):
            # 4 line
            if i >= 3 and d[i] >= d[i - 2] and d[i - 1] <= d[i - 3]:
                return True
            # 5 line
            if i >= 4 and d[i - 1] == d[i - 3] and d[i] + d[i - 4] >= d[i - 2]:
                return True
            # 6 line
            if i >= 5 and d[i - 4] < d[i - 2] and d[i] + d[i - 4] >= d[i - 2]\
                 and d[i - 1] < d[i - 3] and d[i - 1] + d[i - 5] >= d[i - 3]:
                return True
        return False
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('distance = [2,1,1,2]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isSelfCrossing([2, 1, 1, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('distance = [1,2,3,4]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isSelfCrossing([1, 2, 3, 4])))
    print()

    print('Example 3:')
    print('Input : ')
    print('distance = [1,1,1,1]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isSelfCrossing([1, 1, 1, 1])))
    print()

    pass
# @lc main=end