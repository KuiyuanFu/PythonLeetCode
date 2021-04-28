# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (49.77%)
# Likes:    2885
# Dislikes: 78
# Total Accepted:    447.5K
# Total Submissions: 897.9K
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers, nums, that might contain duplicates, return
# all possible unique permutations in any order.
#
#
# Example 1:
#
#
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
# ⁠[1,2,1],
# ⁠[2,1,1]]
#
#
# Example 2:
#
#
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10
#
#
#
#
#

# @lc tags=backtracking

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数组，返回所有排列，可能有重复数字。
# 只能按照指定第一位的思想来进行求排列，因为这样可以控制每一次使用相同数字的个数。而插入的思想，当有重复数字时，会产生相同的排列，错误。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        dic = self.getDict(nums)
        return self.permuteUniqueRecur(dic)

    def permuteUniqueRecur(self, dic: Dict) -> List[List[int]]:
        nums = list(dic.keys())
        if len(nums) == 1 and dic[nums[0]] == 1:
            return [nums]
        results = []
        for n in nums:
            dicCopy = dic.copy()
            dicCopy[n] -= 1
            if (dicCopy[n] == 0):
                dicCopy.pop(n)
            ls = self.permuteUniqueRecur(dicCopy)
            for l in ls:
                results.append([n] + l)
        return results

    # 获得字典，内容是每个词出现的次数
    def getDict(self, words):
        d = {}
        for w in words:
            d[w] = d.get(w, 0) + 1
        return d
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,1,2]')
    print('Output :')
    print(str(Solution().permuteUnique([1, 1, 2])))
    print('Exception :')
    print('[[1,1,2],⁠[1,2,1],⁠[2,1,1]]')
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,2,3]')
    print('Output :')
    print(str(Solution().permuteUnique([1, 2, 3])))
    print('Exception :')
    print('[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]')
    print()

    pass
# @lc main=end