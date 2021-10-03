# @lc app=leetcode id=611 lang=python3
#
# [611] Valid Triangle Number
#
# https://leetcode.com/problems/valid-triangle-number/description/
#
# algorithms
# Medium (49.08%)
# Likes:    2081
# Dislikes: 133
# Total Accepted:    119.9K
# Total Submissions: 243.9K
# Testcase Example:  '[2,2,3,4]'
#
# Given an integer array nums, return the number of triplets chosen from the
# array that can make triangles if we take them as side lengths of a
# triangle.
#
#
# Example 1:
#
#
# Input: nums = [2,2,3,4]
# Output: 3
# Explanation: Valid combinations are:
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
#
#
# Example 2:
#
#
# Input: nums = [4,2,3,4]
# Output: 4
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 三角形可能的组合数。
# 两边和大于第三边。
# 线段树。太慢了。
# 直接排序。二分搜索。
#
#
# @lc idea=end

# @lc group=array

# @lc rank=10


# @lc code=start
class Segment:
    def __init__(self, sl, sr, c, cl=None, cr=None) -> None:
        self.sl = sl
        self.sr = sr
        self.c = c
        self.cl = cl
        self.cr = cr

        pass


def add(p: Segment, l: int, r: int, c: int):
    if l > r:
        pass
    elif not p:
        p = Segment(l, r, c)
    elif l > p.sr:
        p.cr = add(p.cr, l, r, c)
    elif r < p.sl:
        p.cl = add(p.cl, l, r, c)
    else:
        nl = min(l, p.sl)
        nr = max(r, p.sr)
        ml = l + p.sl - nl
        mr = r + p.sr - nr
        lc = p.c if p.sl == nl else c
        rc = p.c if p.sr == nr else c
        p.sl, p.sr = ml, mr
        p.c += c
        p.cl = add(p.cl, nl, ml - 1, lc)
        p.cr = add(p.cr, mr + 1, nr, rc)

    return p


def search(p: Segment, idx: int):
    if not p:
        return 0
    if p.sl <= idx <= p.sr:
        return p.c
    if p.sl > idx:
        return search(p.cl, idx)
    if p.sr < idx:
        return search(p.cr, idx)


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        nums.sort()

        length = len(nums)
        if length < 3:
            return 0

        res = 0
        for i in range(length):
            ni = nums[i]
            for j in range(i):
                nj = nums[j]
                l, r = ni - nj + 1, ni + nj - 1
                il = bisect_left(nums, l, i + 1)
                ir = bisect_right(nums, r, i + 1)
                res += max(ir - il, 0)

        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,2,3,4]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().triangleNumber([2, 2, 3, 4])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [4,2,3,4]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().triangleNumber([4, 2, 3, 4])))
    print()
    print('Exception :')
    print('85630')
    print(
        str(Solution().triangleNumber([
            68, 80, 33, 1, 46, 50, 8, 99, 60, 10, 74, 93, 74, 70, 39, 91, 31,
            16, 63, 83, 19, 68, 63, 100, 69, 65, 45, 25, 34, 57, 44, 19, 78,
            26, 47, 64, 28, 38, 65, 42, 35, 72, 79, 6, 43, 9, 90, 73, 28, 36,
            2, 16, 48, 22, 48, 70, 25, 59, 71, 89, 12, 65, 98, 30, 56, 50, 85,
            50, 15, 87, 76, 34, 45, 45, 34, 10, 46, 10, 95, 0, 70, 28, 6, 70,
            58, 79, 40, 82, 91, 18, 76, 72, 71, 38, 34, 93, 16, 99, 93, 16
        ])))

    pass
# @lc main=end