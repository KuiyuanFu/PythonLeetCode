# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (44.96%)
# Likes:    6250
# Dislikes: 243
# Total Accepted:    414.4K
# Total Submissions: 918.6K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# You are given an array of integers nums, there is a sliding window of size k
# which is moving from the very left of the array to the very right. You can
# only see the k numbers in the window. Each time the sliding window moves
# right by one position.
#
# Return the max sliding window.
#
#
# Example 1:
#
#
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
#
#
# Example 2:
#
#
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Example 3:
#
#
# Input: nums = [1,-1], k = 1
# Output: [1,-1]
#
#
# Example 4:
#
#
# Input: nums = [9,11], k = 2
# Output: [11]
#
#
# Example 5:
#
#
# Input: nums = [4,-2], k = 2
# Output: [4]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
#
#
#

# @lc tags=heap;sliding-window

# @lc imports=start

from imports import *
# @lc imports=end

# @lc idea=start
#
# 活动窗口，求每一个窗口的最大值。
# 使用一个双向队列，存储区域内的最大值的序列。这个队列中的每一个元素，满足在当前窗口中，在次元素后面的元素都小于其，也就是每滑动一次窗口，那么就会得到一个新的元素，从此队列的右侧依次判断队列中的元素是否小于这个元素，如果小于，就说明队列中的元素不可能成为窗口中的最大元素了，可以删掉。
#
# @lc idea=end

# @lc group=heap;sliding-window

# @lc rank=10

# @lc code=start


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import collections
        deq = collections.deque()
        ret = []
        for i, n in enumerate(nums):
            while deq and nums[deq[-1]] < n:
                deq.pop()
            deq += i,
            if deq[0] == i - k:
                deq.popleft()
            if i >= k - 1:
                ret += nums[deq[0]],
        return ret


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,3,-1,-3,5,3,6,7], k = 3')
    print('Exception :')
    print('[3,3,5,5,6,7]')
    print('Output :')
    print(str(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1], k = 1')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().maxSlidingWindow([1], 1)))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [1,-1], k = 1')
    print('Exception :')
    print('[1,-1]')
    print('Output :')
    print(str(Solution().maxSlidingWindow([1, -1], 1)))
    print()

    print('Example 4:')
    print('Input : ')
    print('nums = [9,11], k = 2')
    print('Exception :')
    print('[11]')
    print('Output :')
    print(str(Solution().maxSlidingWindow([9, 11], 2)))
    print()

    print('Example 5:')
    print('Input : ')
    print('nums = [4,-2], k = 2')
    print('Exception :')
    print('[4]')
    print('Output :')
    print(str(Solution().maxSlidingWindow([4, -2], 2)))
    print()

    pass
# @lc main=end