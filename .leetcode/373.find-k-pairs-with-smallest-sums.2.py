# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
#
# algorithms
# Medium (39.02%)
# Likes:    2236
# Dislikes: 141
# Total Accepted:    139.6K
# Total Submissions: 357.8K
# Testcase Example:  '[1,7,11]\n[2,4,6]\n3'
#
# You are given two integer arrays nums1 and nums2 sorted in ascending order
# and an integer k.
#
# Define a pair (u, v) which consists of one element from the first array and
# one element from the second array.
#
# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest
# sums.
#
#
# Example 1:
#
#
# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]]
# Explanation: The first 3 pairs are returned from the sequence:
# [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
#
#
# Example 2:
#
#
# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [[1,1],[1,1]]
# Explanation: The first 2 pairs are returned from the sequence:
# [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
#
#
# Example 3:
#
#
# Input: nums1 = [1,2], nums2 = [3], k = 3
# Output: [[1,3],[2,3]]
# Explanation: All possible pairs are returned from the sequence:
# [1,3],[2,3]
#
#
#
# Constraints:
#
#
# 1 <= nums1.length, nums2.length <= 10^5
# -10^9 <= nums1[i], nums2[i] <= 10^9
# nums1 and nums2 both are sorted in ascending order.
# 1 <= k <= 1000
#
#
#

# @lc tags=heap

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定两个序列，求两个序列笛卡尔积中和最小的k个对。
# 优先队列。
# 当前最小的对，将左右两个元素索引分别后移，得到的更有可能是接下来最小的。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int],
                       k: int) -> List[List[int]]:

        l1, l2 = len(nums1), len(nums2)

        r = []
        h = []
        for i in range(min(k, l1)):
            heappush(h, (nums1[i] + nums2[0], nums1[i], 0))
        k = min(k, l1 * l2)
        while len(r) < k:
            _, n1, j = heappop(h)
            r.append([n1, nums2[j]])
            j += 1
            if j < l2:
                heappush(h, (n1 + nums2[j], n1, j))

        return r
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums1 = [1,7,11], nums2 = [2,4,6], k = 3')
    print('Exception :')
    print('[[1,2],[1,4],[1,6]]')
    print('Output :')
    print(str(Solution().kSmallestPairs([1, 7, 11], [2, 4, 6], 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums1 = [1,1,2], nums2 = [1,2,3], k = 2')
    print('Exception :')
    print('[[1,1],[1,1]]')
    print('Output :')
    print(str(Solution().kSmallestPairs([1, 1, 2], [1, 2, 3], 2)))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums1 = [1,2], nums2 = [3], k = 3')
    print('Exception :')
    print('[[1,3],[2,3]]')
    print('Output :')
    print(str(Solution().kSmallestPairs([1, 2], [3], 3)))
    print()

    pass
# @lc main=end