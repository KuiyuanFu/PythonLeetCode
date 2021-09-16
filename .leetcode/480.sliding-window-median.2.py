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
from sys import float_repr_style
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求滑动窗口的中位数。
# 使用两个优先队列，分别存放中值以上，及以下。
# 使用来回穿插，求中值。
#
# @lc idea=end

# @lc group=sliding-window

# @lc rank=10

# @lc code=start


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if len(nums) < k:
            return []
        if k == 1:
            return [float(n) for n in nums]
        res = []
        # big: min heap, small: max heap
        bi, sm = [], []
        # is bi
        flags = [True] * len(nums)
        for i in range(k - 1):
            t = [nums[i], i]
            # 插入大堆中，取出最小值
            flags[t[1]] = True
            t = heappushpop(bi, t)
            # 插入小堆中
            t[0] = -t[0]
            flags[t[1]] = False
            heappush(sm, t)
            # 大堆数量小于小堆，那么再插回去
            if len(bi) < len(sm):
                t = heappop(sm)
                t[0] = -t[0]
                flags[t[1]] = True
                heappush(bi, t)

        # 如果k是奇数，那么之前两者的数量相等；总之，大堆数量少一。
        isOdd = k % 2 == 1
        f = isOdd
        for i in range(k - 1, len(nums)):
            l = i - k + 1

            t = [nums[i], i]

            heappush(bi, t)
            flags[t[1]] = True
            # 找到大堆可用的最小值
            while bi and bi[0][1] < l:
                heappop(bi)
            t = heappop(bi)
            while bi and bi[0][1] < l:
                heappop(bi)

            # 插入小堆中
            t[0] = -t[0]
            heappush(sm, t)
            flags[t[1]] = False
            while sm and sm[0][1] < l:
                heappop(sm)

            # 如果是大堆少数量，那么就再插回去
            if f:
                t = heappop(sm)
                while sm and sm[0][1] < l:
                    heappop(sm)
                t[0] = -t[0]
                heappush(bi, t)
                flags[t[1]] = True

            if isOdd:
                res.append(float(bi[0][0]))
            else:
                res.append((bi[0][0] - sm[0][0]) / 2)

            f = flags[l]
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