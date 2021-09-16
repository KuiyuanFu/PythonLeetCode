# @lc app=leetcode id=480 lang=python3
#
# [480] Sliding Window Median
#
# https://leetcode.com/problems/sliding-window-median/description/
#
# algorithms
# Hard (39.91%)
# Likes:    1721
# Dislikes: 111
# Total Accepted:    86.9K
# Total Submissions: 217.5K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# The median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value. So the median is the mean of the two
# middle values.
#
#
# For examples, if arr = [2,3,4], the median is 3.
# For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
#
#
# You are given an integer array nums and an integer k. There is a sliding
# window of size k which is moving from the very left of the array to the very
# right. You can only see the k numbers in the window. Each time the sliding
# window moves right by one position.
#
# Return the median array for each window in the original array. Answers within
# 10^-5 of the actual value will be accepted.
#
#
# Example 1:
#
#
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
# Explanation:
# Window position                Median
# ---------------                -----
# [1  3  -1] -3  5  3  6  7        1
# ⁠1 [3  -1  -3] 5  3  6  7       -1
# ⁠1  3 [-1  -3  5] 3  6  7       -1
# ⁠1  3  -1 [-3  5  3] 6  7        3
# ⁠1  3  -1  -3 [5  3  6] 7        5
# ⁠1  3  -1  -3  5 [3  6  7]       6
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
# Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
#
#
#
# Constraints:
#
#
# 1 <= k <= nums.length <= 10^5
# 2^31 <= nums[i] <= 2^31 - 1
#
#
#

# @lc tags=sliding-window

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求滑动窗口的中位数。
# 二叉搜索树。叶子存放值，与值的个数。
#
# @lc idea=end

# @lc group=sliding-window

# @lc rank=10


# @lc code=start
class Node:
    def __init__(self, l=None, r=None, f=None, v=0, c=0) -> None:
        self.l = l
        self.r = r
        self.f = f
        self.v = v
        self.c = c
        pass


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:

        if len(nums) < k:
            return []
        if k == 1:
            return [float(n) for n in nums]
        root = Node(v=nums[0], c=1)

        def addValue(v):
            p = root
            # not leaf
            while p.l:
                p.c += 1
                p = p.l if v <= p.v else p.r
            # leaf - value same
            if p.v == v:
                p.c += 1
            else:

                if v <= p.v:
                    p.l = Node(c=1, v=v, f=p)
                    p.r = Node(c=p.c, v=p.v, f=p)
                    p.v = v
                else:
                    p.r = Node(c=1, v=v, f=p)
                    p.l = Node(c=p.c, v=p.v, f=p)
                p.c += 1

        def searchIndex(idx):
            p = root
            while p.l:
                # in left
                if p.l.c >= idx:
                    p = p.l
                # right minus left count
                else:
                    idx -= p.l.c
                    p = p.r
            return p.v

        def deleteValue(v):
            p = root
            while p.l:
                p.c -= 1
                if v <= p.v:
                    p = p.l
                else:
                    p = p.r

            p.c -= 1
            if p.c == 0:
                pf = p.f
                pb = pf.r if pf.l == p else pf.l
                pf.l = pb.l
                pf.r = pb.r
                pf.v = pb.v
                pf.c = pb.c
                if pf.l:
                    pf.l.f = pf
                if pf.r:
                    pf.r.f = pf

        for i in range(1, k - 1):
            addValue(nums[i])
        isOdd = k % 2 == 1
        half = (k + 1) // 2
        res = []
        for i in range(k - 1, len(nums)):
            addValue(nums[i])
            if isOdd:
                res.append(float(searchIndex(half)))
            else:
                l = searchIndex(half)
                r = searchIndex(half + 1)
                res.append((l + r) / 2)
            deleteValue(nums[i - k + 1])
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,3,-1,-3,5,3,6,7], k = 3')
    print('Exception :')
    print('[1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]')
    print('Output :')
    print(str(Solution().medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3,4,2,3,1,4,2], k = 3')
    print('Exception :')
    print('[2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]')
    print('Output :')
    print(str(Solution().medianSlidingWindow([1, 2, 3, 4, 2, 3, 1, 4, 2], 3)))
    print()
    # print(str(Solution().medianSlidingWindow([1, 4, 2, 3], 4)))
    print(
        str(Solution().medianSlidingWindow([5, 5, 8, 1, 4, 7, 1, 3, 8, 4], 8)))
    pass
# @lc main=end