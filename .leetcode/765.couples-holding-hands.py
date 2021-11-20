# @lc app=leetcode id=765 lang=python3
#
# [765] Couples Holding Hands
#
# https://leetcode.com/problems/couples-holding-hands/description/
#
# algorithms
# Hard (56.05%)
# Likes:    1401
# Dislikes: 79
# Total Accepted:    39.5K
# Total Submissions: 70.4K
# Testcase Example:  '[0,2,1,3]'
#
# There are n couples sitting in 2n seats arranged in a row and want to hold
# hands.
#
# The people and seats are represented by an integer array row where row[i] is
# the ID of the person sitting in the i^th seat. The couples are numbered in
# order, the first couple being (0, 1), the second couple being (2, 3), and so
# on with the last couple being (2n - 2, 2n - 1).
#
# Return the minimum number of swaps so that every couple is sitting side by
# side. A swap consists of choosing any two people, then they stand up and
# switch seats.
#
#
# Example 1:
#
#
# Input: row = [0,2,1,3]
# Output: 1
# Explanation: We only need to swap the second (row[1]) and third (row[2])
# person.
#
#
# Example 2:
#
#
# Input: row = [3,2,0,1]
# Output: 0
# Explanation: All couples are already seated side by side.
#
#
#
# Constraints:
#
#
# 2n == row.length
# 2 <= n <= 30
# n is even.
# 0 <= row[i] < 2n
# All the elements of row are unique.
#
#
#

# @lc tags=tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 交换坐位，使所有 (2n - 2, 2n - 1)的对相邻。
# 与相对位置无关了。
# 直接交换。
#
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def minSwapsCouples(self, seatToId: List[int]) -> int:

        idToSeat = [0] * len(seatToId)
        for seat, id in enumerate(seatToId):
            idToSeat[id] = seat

        res = 0
        for seat in range(len(seatToId) // 2):
            id1, id2 = seatToId[seat * 2], seatToId[seat * 2 + 1]
            if id1 // 2 == id2 // 2:
                continue
            else:
                res += 1
                id1Com = id1 // 2 * 4 + 1 - id1
                id1ComSeat = idToSeat[id1Com]
                seatToId[id1ComSeat] = id2
                idToSeat[id2] = id1ComSeat
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('row = [0,2,1,3]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().minSwapsCouples([0, 2, 1, 3])))
    print()

    print('Example 2:')
    print('Input : ')
    print('row = [3,2,0,1]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().minSwapsCouples([3, 2, 0, 1])))
    print()
    print('Example 2:')
    print('Input : ')
    print('row =[2,0,5,4,3,1]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().minSwapsCouples([2, 0, 5, 4, 3, 1])))
    print()

    pass
# @lc main=end