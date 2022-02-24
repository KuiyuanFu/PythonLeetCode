# @lc app=leetcode id=825 lang=python3
#
# [825] Friends Of Appropriate Ages
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 统计数量
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        total = 0
        for age in ages:
            la = age * 0.5 + 7
            if la < age:
                li = bisect_right(ages, la)
                ri = bisect_right(ages, age)
                total += ri - li - 1
        return total

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('ages = [16,16]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().numFriendRequests([16, 16])))
    print()

    print('Example 2:')
    print('Input : ')
    print('ages = [16,17,18]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().numFriendRequests([16, 17, 18])))
    print()

    print('Example 3:')
    print('Input : ')
    print('ages = [20,30,100,110,120]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().numFriendRequests([20, 30, 100, 110, 120])))
    print()

    pass
# @lc main=end