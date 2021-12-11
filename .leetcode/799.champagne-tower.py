# @lc app=leetcode id=799 lang=python3
#
# [799] Champagne Tower
#
# https://leetcode.com/problems/champagne-tower/description/
#
# algorithms
# Medium (44.34%)
# Likes:    935
# Dislikes: 67
# Total Accepted:    37.7K
# Total Submissions: 84.6K
# Testcase Example:  '1\n1\n1'
#
# We stack glasses in a pyramid, where the first row has 1 glass, the second
# row has 2 glasses, and so on until the 100^th row.  Each glass holds one cup
# of champagne.
#
# Then, some champagne is poured into the first glass at the top.  When the
# topmost glass is full, any excess liquid poured will fall equally to the
# glass immediately to the left and right of it.  When those glasses become
# full, any excess champagne will fall equally to the left and right of those
# glasses, and so on.  (A glass at the bottom row has its excess champagne fall
# on the floor.)
#
# For example, after one cup of champagne is poured, the top most glass is
# full.  After two cups of champagne are poured, the two glasses on the second
# row are half full.  After three cups of champagne are poured, those two cups
# become full - there are 3 full glasses total now.  After four cups of
# champagne are poured, the third row has the middle glass half full, and the
# two outside glasses are a quarter full, as pictured below.
#
#
#
# Now after pouring some non-negative integer cups of champagne, return how
# full the j^th glass in the i^th row is (both i and j are 0-indexed.)
#
#
# Example 1:
#
#
# Input: poured = 1, query_row = 1, query_glass = 1
# Output: 0.00000
# Explanation: We poured 1 cup of champange to the top glass of the tower
# (which is indexed as (0, 0)). There will be no excess liquid so all the
# glasses under the top glass will remain empty.
#
#
# Example 2:
#
#
# Input: poured = 2, query_row = 1, query_glass = 1
# Output: 0.50000
# Explanation: We poured 2 cups of champange to the top glass of the tower
# (which is indexed as (0, 0)). There is one cup of excess liquid. The glass
# indexed as (1, 0) and the glass indexed as (1, 1) will share the excess
# liquid equally, and each will get half cup of champange.
#
#
# Example 3:
#
#
# Input: poured = 100000009, query_row = 33, query_glass = 17
# Output: 1.00000
#
#
#
# Constraints:
#
#
# 0 <= poured <= 10^9
# 0 <= query_glass <= query_row < 100
#
#

# @lc tags=tree;recursion

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 香槟金字塔，问倒n杯后，指定位置的酒杯内酒占比。
# 直接计算。全倒在第一个上，之后计算流向。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def champagneTower(self, poured: int, query_row: int,
                       query_glass: int) -> float:

        d = [[poured * 1.0]]
        for i in range(100):
            d.append([0 for _ in range(i + 2)])
            for j in range(i + 1):

                if i == query_row and j == query_glass:
                    return min(1.0, d[i][j])
                else:
                    t = max(0, d[i][j] - 1) / 2
                    d[i + 1][j] += t
                    d[i + 1][j + 1] += t


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('poured = 1, query_row = 1, query_glass = 1')
    print('Exception :')
    print('0.00000')
    print('Output :')
    print(str(Solution().champagneTower(1, 1, 1)))
    print()

    print('Example 2:')
    print('Input : ')
    print('poured = 2, query_row = 1, query_glass = 1')
    print('Exception :')
    print('0.50000')
    print('Output :')
    print(str(Solution().champagneTower(2, 1, 1)))
    print()

    print('Example 3:')
    print('Input : ')
    print('poured = 100000009, query_row = 33, query_glass = 17')
    print('Exception :')
    print('1.00000')
    print('Output :')
    print(str(Solution().champagneTower(100000009, 33, 17)))
    print()

    pass
# @lc main=end