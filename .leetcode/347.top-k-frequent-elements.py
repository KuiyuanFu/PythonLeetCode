# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (63.12%)
# Likes:    5630
# Dislikes: 284
# Total Accepted:    638.2K
# Total Submissions: 1M
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
#
#
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#
#
#
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
#
#

# @lc tags=hash-table;heap

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求数组中，数量前k个的元素值。
# 朴素思想是直接排序。
# 可以优先队列。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        from heapq import heappush, heappushpop

        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        topK = []
        for v in counts:
            if len(topK) < k:
                heappush(topK, (counts[v], v))
            elif topK[0][0] < counts[v]:
                heappushpop(topK, (counts[v], v))
        return [v for c, v in topK]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,1,1,2,2,3], k = 2')
    print('Exception :')
    print('[1,2]')
    print('Output :')
    print(str(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1], k = 1')
    print('Exception :')
    print('[1]')
    print('Output :')
    print(str(Solution().topKFrequent([1], 1)))
    print()

    pass
# @lc main=end