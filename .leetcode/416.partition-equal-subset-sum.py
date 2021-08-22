# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (45.48%)
# Likes:    5174
# Dislikes: 97
# Total Accepted:    320.9K
# Total Submissions: 705.7K
# Testcase Example:  '[1,5,11,5]'
#
# Given a non-empty array nums containing only positive integers, find if the
# array can be partitioned into two subsets such that the sum of elements in
# both subsets is equal.
#
#
# Example 1:
#
#
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#
#
# Example 2:
#
#
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将数组分为两部分，满足两部分的和相等，判断是否可行。
# 总和为奇数一定不可以；目标为总和的一半，之后统计每个数值的个数，对于每个数值，执行个数次迭代，第一个迭代的输入为之前的所有结果，之后加上数值，得到值，判断是否出现过，没出现过的新值进入下一次迭代。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        t = s // 2

        d = defaultdict(int)
        for n in nums:
            d[n] += 1

        s = set([0])
        for k in d.keys():
            sn = list(s)
            for _ in range(d[k]):
                so, sn = sn, []
                for o in so:
                    n = o + k
                    if n <= t and n not in s:
                        s.add(n)
                        sn.append(n)
            if t in s:
                return True
        return False


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(
        str(Solution().canPartition([
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
            100, 100, 100, 99, 97
        ])))
    print('Example 1:')
    print('Input : ')
    print('nums = [1,5,11,5]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().canPartition([1, 5, 11, 5])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3,5]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().canPartition([1, 2, 3, 5])))
    print()

    pass
# @lc main=end