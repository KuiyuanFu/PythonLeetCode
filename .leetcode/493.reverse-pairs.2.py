# @lc app=leetcode id=493 lang=python3
#
# [493] Reverse Pairs
#
# https://leetcode.com/problems/reverse-pairs/description/
#
# algorithms
# Hard (28.43%)
# Likes:    1947
# Dislikes: 161
# Total Accepted:    65.1K
# Total Submissions: 228.1K
# Testcase Example:  '[1,3,2,3,1]'
#
# Given an integer array nums, return the number of reverse pairs in the
# array.
#
# A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] >
# 2 * nums[j].
#
#
# Example 1:
# Input: nums = [1,3,2,3,1]
# Output: 2
# Example 2:
# Input: nums = [2,4,3,5,1]
# Output: 3
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
#
#
#

# @lc tags=binary-search;divide-and-conquer;sort;binary-indexed-tree;segment-tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求翻转对数。
# 分治法，因为前面的顺序不重要了。
#
# @lc idea=end

# @lc group=binary-search;divide-and-conquer;sort;

# @lc rank=10

# @lc code=start


class Solution:
    def recur(self, l, r):
        if l == r:
            return
        m = (l + r) // 2
        m1 = m + 1
        # 递归
        self.recur(l, m)
        self.recur(m1, r)

        # 计数
        for i in range(m1, r + 1):
            n = self.nums[i] * 2 + 1
            idxSmall = bisect_left(self.nums, n, l, m1)
            self.res += m1 - idxSmall

        # 合并
        self.buffer[l:r + 1] = self.nums[l:r + 1]
        i, j = l, m + 1
        k = l
        while i <= m and j <= r:
            if self.buffer[i] < self.buffer[j]:
                self.nums[k] = self.buffer[i]
                i += 1
            else:
                self.nums[k] = self.buffer[j]
                j += 1
            k += 1
        if i <= m:
            self.nums[k:k + m1 - i] = self.buffer[i:m1]
        else:
            self.nums[k:k + r + 1 - j] = self.buffer[j:r + 1]

    def reversePairs(self, nums: List[int]) -> int:

        self.res = 0
        self.buffer = nums.copy()
        self.nums = nums
        self.recur(0, len(nums) - 1)
        return self.res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,3,2,3,1]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().reversePairs([1, 3, 2, 3, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [2,4,3,5,1]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().reversePairs([2, 4, 3, 5, 1])))
    print()
    print('4')
    print(str(Solution().reversePairs([5, 4, 3, 2, 1])))

    pass
# @lc main=end