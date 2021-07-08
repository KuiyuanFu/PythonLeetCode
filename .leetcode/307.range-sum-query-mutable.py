# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#
# https://leetcode.com/problems/range-sum-query-mutable/description/
#
# algorithms
# Medium (37.21%)
# Likes:    2152
# Dislikes: 120
# Total Accepted:    154.2K
# Total Submissions: 408.2K
# Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
#
# Given an integer array nums, handle multiple queries of the following
# types:
#
#
# Update the value of an element in nums.
# Calculate the sum of the elements of nums between indices left and right
# inclusive where left <= right.
#
#
# Implement the NumArray class:
#
#
# NumArray(int[] nums) Initializes the object with the integer array nums.
# void update(int index, int val) Updates the value of nums[index] to be
# val.
# int sumRange(int left, int right) Returns the sum of the elements of nums
# between indices left and right inclusive (i.e. nums[left] + nums[left + 1] +
# ... + nums[right]).
#
#
#
# Example 1:
#
#
# Input
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# Output
# [null, 9, null, 8]
#
# Explanation
# NumArray numArray = new NumArray([1, 3, 5]);
# numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
# numArray.update(1, 2);   // nums = [1, 2, 5]
# numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 3 * 10^4
# -100 <= nums[i] <= 100
# 0 <= index < nums.length
# -100 <= val <= 100
# 0 <= left <= right < nums.length
# At most 3 * 10^4 calls will be made to update and sumRange.
#
#
#

# @lc tags=binary-indexed-tree;segment-tree

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 给定数值数组，有更新操作，与求区间和的操作。
# 用线段树。保存指定范围内的和，若底层更新，依次向上传递。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Segment:
    def __init__(self, l, r, lp=None, rp=None, fp=None, value=0) -> None:
        self.l = l
        self.r = r
        self.lp = lp
        self.rp = rp
        self.fp = fp
        self.value = value


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = []

        def initSegment(l, r, fp):
            root = Segment(l, r, value=nums[l], fp=fp)
            if l == r:
                self.nums.append(root)
                return root
            m = (r + l) // 2
            root.lp = initSegment(l, m, root)
            root.rp = initSegment(m + 1, r, root)
            root.value = root.lp.value + root.rp.value
            return root

        self.root = initSegment(0, len(nums) - 1, None)

    def update(self, index: int, val: int) -> None:
        p = self.nums[index]
        t = val - p.value
        while p:
            p.value += t
            p = p.fp

    def sumRange(self, left: int, right: int) -> int:
        def rSumRange(p: Segment):
            if not p:
                return
            # full contain
            if left <= p.l and p.r <= right:
                return p.value
            # out range
            elif p.l > right or p.r < left:
                return 0
            else:
                return rSumRange(p.lp) + rSumRange(p.rp)

        return rSumRange(self.root)


# @lc code=end

# @lc main=start
if __name__ == '__main__':

    pass
# @lc main=end