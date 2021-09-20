# @lc app=leetcode id=517 lang=python3
#
# [517] Super Washing Machines
#
# https://leetcode.com/problems/super-washing-machines/description/
#
# algorithms
# Hard (38.87%)
# Likes:    467
# Dislikes: 171
# Total Accepted:    20.1K
# Total Submissions: 51.7K
# Testcase Example:  '[1,0,5]'
#
# You have n super washing machines on a line. Initially, each washing machine
# has some dresses or is empty.
#
# For each move, you could choose any m (1 <= m <= n) washing machines, and
# pass one dress of each washing machine to one of its adjacent washing
# machines at the same time.
#
# Given an integer array machines representing the number of dresses in each
# washing machine from left to right on the line, return the minimum number of
# moves to make all the washing machines have the same number of dresses. If it
# is not possible to do it, return -1.
#
#
# Example 1:
#
#
# Input: machines = [1,0,5]
# Output: 3
# Explanation:
# 1st move:    1     0 <-- 5    =>    1     1     4
# 2nd move:    1 <-- 1 <-- 4    =>    2     1     3
# 3rd move:    2     1 <-- 3    =>    2     2     2
#
#
# Example 2:
#
#
# Input: machines = [0,3,0]
# Output: 2
# Explanation:
# 1st move:    0 <-- 3     0    =>    1     2     0
# 2nd move:    1     2 --> 0    =>    1     1     1
#
#
# Example 3:
#
#
# Input: machines = [0,2,0]
# Output: -1
# Explanation:
# It's impossible to make all three washing machines have the same number of
# dresses.
#
#
#
# Constraints:
#
#
# n == machines.length
# 1 <= n <= 10^4
# 0 <= machines[i] <= 10^5
#
#
#

# @lc tags=math;dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 一列洗衣机，每次可以向左或右移动一件衣服。问最少多少次，可以使所有洗衣机的衣服数相等。
# 从左向右遍历，根据已访问过的数量，确定此节点的流向。
#
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        s = sum(machines)
        if s % len(machines) != 0:
            return -1
        # target
        t = s // len(machines)
        #
        mt = 0
        le, re = 0, s
        ls, rs = 0, s
        for c in machines:
            re -= t
            rs -= c
            mt = max(mt, max(le - ls, 0) + max(re - rs, 0))
            le += t
            ls += c
        return mt


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('machines = [1,0,5]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().findMinMoves([1, 0, 5])))
    print()

    print('Example 2:')
    print('Input : ')
    print('machines = [0,3,0]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().findMinMoves([0, 3, 0])))
    print()

    print('Example 3:')
    print('Input : ')
    print('machines = [0,2,0]')
    print('Exception :')
    print('-1')
    print('Output :')
    print(str(Solution().findMinMoves([0, 2, 0])))
    print()
    print('Exception :')
    print('8')
    print('Output :')
    print(str(Solution().findMinMoves([0, 4, 12, 0])))
    print()
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().findMinMoves([1, 2, 3, 4, 5, 6, 7])))
    print()
    pass
# @lc main=end