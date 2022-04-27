# @lc app=leetcode id=898 lang=python3
#
# [898] Bitwise ORs of Subarrays
#
# https://leetcode.com/problems/bitwise-ors-of-subarrays/description/
#
# algorithms
# Medium (36.27%)
# Likes:    946
# Dislikes: 176
# Total Accepted:    26K
# Total Submissions: 71.6K
# Testcase Example:  '[0]'
#
# We have an array arr of non-negative integers.
#
# For every (contiguous) subarray sub = [arr[i], arr[i + 1], ..., arr[j]] (with
# i <= j), we take the bitwise OR of all the elements in sub, obtaining a
# result arr[i] | arr[i + 1] | ... | arr[j].
#
# Return the number of possible results. Results that occur more than once are
# only counted once in the final answer
#
#
# Example 1:
#
#
# Input: arr = [0]
# Output: 1
# Explanation: There is only one possible result: 0.
#
#
# Example 2:
#
#
# Input: arr = [1,1,2]
# Output: 3
# Explanation: The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1,
# 2].
# These yield the results 1, 1, 2, 1, 3, 3.
# There are 3 unique values, so the answer is 3.
#
#
# Example 3:
#
#
# Input: arr = [1,2,4]
# Output: 6
# Explanation: The possible results are 1, 2, 3, 4, 6, and 7.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5 * 10^4
# 0 <= nums[i] <= 10^9
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求所有连续子序列的或的集合的个数。
# 直接迭代。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        cur = set()

        for n in arr:
            cur = set(p | n for p in cur)
            cur.add(n)
            res.update(cur)
        return len(res)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('arr = [0]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().subarrayBitwiseORs([0])))
    print()

    print('Example 2:')
    print('Input : ')
    print('arr = [1,1,2]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().subarrayBitwiseORs([1, 1, 2])))
    print()

    print('Example 3:')
    print('Input : ')
    print('arr = [1,2,4]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().subarrayBitwiseORs([1, 2, 4])))
    print()

    pass
# @lc main=end