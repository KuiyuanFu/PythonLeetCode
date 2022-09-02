# @lc app=leetcode id=954 lang=python3
#
# [954] Array of Doubled Pairs
#
# https://leetcode.com/problems/array-of-doubled-pairs/description/
#
# algorithms
# Medium (38.84%)
# Likes:    1180
# Dislikes: 129
# Total Accepted:    74.4K
# Total Submissions: 191.6K
# Testcase Example:  '[3,1,3,6]'
#
# Given an integer array of even length arr, return true if it is possible to
# reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i <
# len(arr) / 2, or false otherwise.
#
#
# Example 1:
#
#
# Input: arr = [3,1,3,6]
# Output: false
#
#
# Example 2:
#
#
# Input: arr = [2,1,2,6]
# Output: false
#
#
# Example 3:
#
#
# Input: arr = [4,-2,2,-4]
# Output: true
# Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or
# [2,4,-2,-4].
#
#
#
# Constraints:
#
#
# 2 <= arr.length <= 3 * 10^4
# arr.length is even.
# -10^5 <= arr[i] <= 10^5
#
#
#

# @lc tags=array

# @lc imports=start

from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数组，判断是否可以分成两两一组，每组一个元素是另一个元素的二倍。
# 直接计数，之后按绝对值排序。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def canReorderDoubled(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        if counter[0] % 2 != 0:
            return False
        keys = list(counter.keys())
        keys.sort(key=abs)

        for k in keys:
            n = counter[k]
            if n == 0:
                continue
            t = k * 2
            nt = counter[t]
            if nt < n:
                return False
            counter[t] = nt - n
        return True
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('arr = [3,1,3,6]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().canReorderDoubled([3, 1, 3, 6])))
    print()

    print('Example 2:')
    print('Input : ')
    print('arr = [2,1,2,6]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().canReorderDoubled([2, 1, 2, 6])))
    print()

    print('Example 3:')
    print('Input : ')
    print('arr = [4,-2,2,-4]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().canReorderDoubled([4, -2, 2, -4])))
    print()

    pass
# @lc main=end