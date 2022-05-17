# @lc app=leetcode id=923 lang=python3
#
# [923] 3Sum With Multiplicity
#
# https://leetcode.com/problems/3sum-with-multiplicity/description/
#
# algorithms
# Medium (45.43%)
# Likes:    2223
# Dislikes: 267
# Total Accepted:    87K
# Total Submissions: 191.3K
# Testcase Example:  '[1,1,2,2,3,3,4,4,5,5]\n8'
#
# Given an integer array arr, and an integer target, return the number of
# tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.
#
# As the answer can be very large, return it modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
# Output: 20
# Explanation:
# Enumerating by the values (arr[i], arr[j], arr[k]):
# (1, 2, 5) occurs 8 times;
# (1, 3, 4) occurs 8 times;
# (2, 2, 4) occurs 2 times;
# (2, 3, 3) occurs 2 times.
#
#
# Example 2:
#
#
# Input: arr = [1,1,2,2,2,2], target = 5
# Output: 12
# Explanation:
# arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
# We choose one 1 from [1,1] in 2 ways,
# and two 2s from [2,2,2,2] in 6 ways.
#
#
# Example 3:
#
#
# Input: arr = [2,1,3], target = 6
# Output: 1
# Explanation: (1, 2, 3) occured one time in the array so we return 1.
#
#
#
# Constraints:
#
#
# 3 <= arr.length <= 3000
# 0 <= arr[i] <= 100
# 0 <= target <= 300
#
#
#

# @lc tags=math;binary-search;dynamic-programming

# @lc imports=start
import math
from imports import *

# @lc imports=end

# @lc idea=start
#
# 三数和为给定值的个数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def threeSumMulti(self, arr: List[int], target: int) -> int:

        res = 0
        counter = Counter(arr)
        keys = sorted(list(counter.keys()))
        if target % 3 == 0 and target // 3 in keys:
            res += math.comb(counter[target // 3], 3)
        for idx1 in range(len(keys)):
            n1 = keys[idx1]
            c1 = counter[n1]

            n3 = target - 2 * n1
            if n3 in counter and n3 != n1:
                res += c1 * (c1 - 1) // 2 * counter[n3]

            for idx2 in range(idx1 + 1, len(keys)):
                n2 = keys[idx2]
                n3 = target - (n1 + n2)
                if n3 > n2 and n3 in counter:
                    res += c1 * counter[n2] * counter[n3]
        return res % 1000000007
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('arr = [1,1,2,2,3,3,4,4,5,5], target = 8')
    print('Exception :')
    print('20')
    print('Output :')
    print(str(Solution().threeSumMulti([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8)))
    print()

    print('Example 2:')
    print('Input : ')
    print('arr = [1,1,2,2,2,2], target = 5')
    print('Exception :')
    print('12')
    print('Output :')
    print(str(Solution().threeSumMulti([1, 1, 2, 2, 2, 2], 5)))
    print()

    print('Example 3:')
    print('Input : ')
    print('arr = [2,1,3], target = 6')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().threeSumMulti([2, 1, 3], 6)))
    print()

    pass
# @lc main=end