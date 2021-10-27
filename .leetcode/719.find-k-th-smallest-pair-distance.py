# @lc app=leetcode id=719 lang=python3
#
# [719] Find K-th Smallest Pair Distance
#
# https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/
#
# algorithms
# Hard (33.32%)
# Likes:    1653
# Dislikes: 56
# Total Accepted:    50.3K
# Total Submissions: 149.4K
# Testcase Example:  '[1,3,1]\n1'
#
# The distance of a pair of integers a and b is defined as the absolute
# difference between a and b.
#
# Given an integer array nums and an integer k, return the k^th smallest
# distance among all the pairs nums[i] and nums[j] where 0 <= i < j <
# nums.length.
#
#
# Example 1:
#
#
# Input: nums = [1,3,1], k = 1
# Output: 0
# Explanation: Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1^st smallest distance pair is (1,1), and its distance is 0.
#
#
# Example 2:
#
#
# Input: nums = [1,1,1], k = 2
# Output: 0
#
#
# Example 3:
#
#
# Input: nums = [1,6,1], k = 3
# Output: 5
#
#
#
# Constraints:
#
#
# n == nums.length
# 2 <= n <= 10^4
# 0 <= nums[i] <= 10^6
# 1 <= k <= n * (n - 1) / 2
#
#
#

# @lc tags=array;binary-search;heap

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 找距离的第k小。
# 顺序无关，可以排序。
# 以距离为目标，二分搜索。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        pre = -1
        unis = []
        idices = []
        counts = []
        for i, n in enumerate(nums):
            if n == pre:
                counts[-1] += 1
                idices[-1] = i
            else:
                idices.append(i)
                unis.append(n)
                counts.append(1)
                pre = n
        for c in counts:
            k -= ((c - 1) + 0) * c // 2
        l, r = 0, 1000000
        while l < r:
            c = 0
            m = (l + r) // 2
            for i, n in enumerate(unis):
                c += (bisect_right(nums, n + m) - idices[i] - 1) * counts[i]
            if c < k:
                l = m + 1
            else:
                r = m
        return l

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,3,1], k = 1')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().smallestDistancePair([1, 3, 1], 1)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,1,1], k = 2')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().smallestDistancePair([1, 1, 1], 2)))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1,6,1], k = 3')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().smallestDistancePair([1, 6, 1], 3)))
    print()

    pass
# @lc main=end