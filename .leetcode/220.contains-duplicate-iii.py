# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#
# https://leetcode.com/problems/contains-duplicate-iii/description/
#
# algorithms
# Medium (21.41%)
# Likes:    1668
# Dislikes: 1733
# Total Accepted:    174.1K
# Total Submissions: 812.5K
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
# Given an integer array nums and two integers k and t, return true if there
# are two distinct indices i and j in the array such that abs(nums[i] -
# nums[j]) <= t and abs(i - j) <= k.
#
#
# Example 1:
# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
# Example 2:
# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true
# Example 3:
# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false
#
#
# Constraints:
#
#
# 0 <= nums.length <= 2 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# 0 <= k <= 10^4
# 0 <= t <= 2^31 - 1
#
#
#

# @lc tags=sort;ordered-map

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个整数序列，给定一个长度k，一个距离t，判断是否在k长的子序列中存在相差至多t的元素对。
# bucket。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int,
                                      t: int) -> bool:

        if k < 1:
            return False
        from collections import defaultdict
        buckets = defaultdict(set)
        s = set()
        bl = 1 if t == 0 else t
        for i in range(len(nums)):
            n = nums[i]
            bucket = (n + 2**31) // bl
            for b in [bucket - 1, bucket, bucket + 1]:
                for nt in buckets[b]:
                    if abs(nt - n) <= t:
                        return True
            if i - k >= 0:
                buckets[(nums[i - k] + 2**31) // bl].remove(nums[i - k])
            buckets[bucket].add(n)
        return False
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3,1], k = 3, t = 0')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,0,1,1], k = 1, t = 2')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2)))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1,5,9,1,5,9], k = 2, t = 3')
    print('Exception :')
    print('false')
    print('Output :')
    print(
        str(Solution().containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2,
                                                     3)))
    print()

    pass
# @lc main=end