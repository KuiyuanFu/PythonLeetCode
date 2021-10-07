# @lc app=leetcode id=632 lang=python3
#
# [632] Smallest Range Covering Elements from K Lists
#
# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description/
#
# algorithms
# Hard (55.97%)
# Likes:    1702
# Dislikes: 28
# Total Accepted:    53.7K
# Total Submissions: 95.2K
# Testcase Example:  '[[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]'
#
# You have k lists of sorted integers in non-decreasing order. Find the
# smallest range that includes at least one number from each of the k lists.
#
# We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a
# < c if b - a == d - c.
#
#
# Example 1:
#
#
# Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
# Output: [20,24]
# Explanation:
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
#
#
# Example 2:
#
#
# Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
# Output: [1,1]
#
#
# Example 3:
#
#
# Input: nums = [[10,10],[11,11]]
# Output: [10,11]
#
#
# Example 4:
#
#
# Input: nums = [[10],[11]]
# Output: [10,11]
#
#
# Example 5:
#
#
# Input: nums = [[1],[2],[3],[4],[5],[6],[7]]
# Output: [1,7]
#
#
#
# Constraints:
#
#
# nums.length == k
# 1 <= k <= 3500
# 1 <= nums[i].length <= 50
# -10^5 <= nums[i][j] <= 10^5
# nums[i] is sorted in non-decreasing order.
#
#
#

# @lc tags=hash-table;two-pointers;string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求包含每个数组中至少一个元素的最短区域。
# 堆，优先队列，保证堆中存在所有数组中的元素，之后移除最小值，并添加对应数组中的下一个值。取最小范围。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        h = []

        maxi = -10000
        for idx, ns in enumerate(nums):
            n = ns[0]
            heappush(h, (n, idx, 0))
            maxi = max(maxi, n)
        mini = h[0][0]

        rmini, rmaxi = mini, maxi
        while True:
            n, idx, offset = heappop(h)
            offset += 1
            if offset == len(nums[idx]):
                break
            n = nums[idx][offset]
            heappush(h, (n, idx, offset))
            maxi = max(maxi, n)
            mini = h[0][0]
            if maxi - mini < rmaxi - rmini:
                rmini, rmaxi = mini, maxi

        return [rmini, rmaxi]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]')
    print('Exception :')
    print('[20,24]')
    print('Output :')
    print(
        str(Solution().smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20],
                                      [5, 18, 22, 30]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [[1,2,3],[1,2,3],[1,2,3]]')
    print('Exception :')
    print('[1,1]')
    print('Output :')
    print(str(Solution().smallestRange([[1, 2, 3], [1, 2, 3], [1, 2, 3]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [[10,10],[11,11]]')
    print('Exception :')
    print('[10,11]')
    print('Output :')
    print(str(Solution().smallestRange([[10, 10], [11, 11]])))
    print()

    print('Example 4:')
    print('Input : ')
    print('nums = [[10],[11]]')
    print('Exception :')
    print('[10,11]')
    print('Output :')
    print(str(Solution().smallestRange([[10], [11]])))
    print()

    print('Example 5:')
    print('Input : ')
    print('nums = [[1],[2],[3],[4],[5],[6],[7]]')
    print('Exception :')
    print('[1,7]')
    print('Output :')
    print(str(Solution().smallestRange([[1], [2], [3], [4], [5], [6], [7]])))
    print()

    pass
# @lc main=end