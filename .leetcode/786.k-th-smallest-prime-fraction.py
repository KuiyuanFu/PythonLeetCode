# @lc app=leetcode id=786 lang=python3
#
# [786] K-th Smallest Prime Fraction
#
# https://leetcode.com/problems/k-th-smallest-prime-fraction/description/
#
# algorithms
# Hard (46.03%)
# Likes:    664
# Dislikes: 34
# Total Accepted:    23.6K
# Total Submissions: 50.1K
# Testcase Example:  '[1,2,3,5]\n3'
#
# You are given a sorted integer array arr containing 1 and prime numbers,
# where all the integers of arr are unique. You are also given an integer k.
#
# For every i and j where 0 <= i < j < arr.length, we consider the fraction
# arr[i] / arr[j].
#
# Return the k^th smallest fraction considered. Return your answer as an array
# of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].
#
#
# Example 1:
#
#
# Input: arr = [1,2,3,5], k = 3
# Output: [2,5]
# Explanation: The fractions to be considered in sorted order are:
# 1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
# The third fraction is 2/5.
#
#
# Example 2:
#
#
# Input: arr = [1,7], k = 1
# Output: [1,7]
#
#
#
# Constraints:
#
#
# 2 <= arr.length <= 1000
# 1 <= arr[i] <= 3 * 10^4
# arr[0] == 1
# arr[i] is a prime number for i > 0.
# All the numbers of arr are unique and sorted in strictly increasing
# order.
# 1 <= k <= arr.length * (arr.length - 1) / 2
#
#
#

# @lc tags=binary-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 优先队列，要想使商最小，范围需要最大，弹出最小值，再将除数向前移动。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:

        tail, idxTail = arr[-1], len(arr) - 1
        h = [(n / tail, n, idxTail) for i, n in enumerate(arr)]
        heapify(h)
        for _ in range(k - 1):
            _, n, idxJ = heappop(h)
            idxJ -= 1
            heappush(h, (n / arr[idxJ], n, idxJ))
        _, n, idxJ = heappop(h)
        return [n, arr[idxJ]]

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('arr = [1,2,3,5], k = 3')
    print('Exception :')
    print('[2,5]')
    print('Output :')
    print(str(Solution().kthSmallestPrimeFraction([1, 2, 3, 5], 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('arr = [1,7], k = 1')
    print('Exception :')
    print('[1,7]')
    print('Output :')
    print(str(Solution().kthSmallestPrimeFraction([1, 7], 1)))
    print()

    pass
# @lc main=end