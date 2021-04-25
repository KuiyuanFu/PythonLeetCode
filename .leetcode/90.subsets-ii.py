# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (49.21%)
# Likes:    2447
# Dislikes: 105
# Total Accepted:    339.4K
# Total Submissions: 688.9K
# Testcase Example:  '[1,2,2]'
#
# Given an integer array nums that may contain duplicates, return all possible
# subsets (the power set).
# 
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
# 
# 
# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# 
# 
#


# @lc tags=array;backtracking

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
# 
# 给定一个整数数组，可能有重复值，求幂集。
# 还是分治法，求左右两侧的幂集后，做笛卡尔积，只不过遇到重复值，需要保证每一次个数都是不同的。
# 
# @lc idea=end

# @lc group=backtracking

# @lc rank=10

# @lc code=start
import bisect
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.nums= nums
        return self.recur(0,len(nums)-1)
        pass

    def recur(self, l,r) -> List[List[int]]:
        if l > r:
            return [[]]
        if l ==r :
            return [[],[self.nums[l]]]

        # 中间的值
        n = self.nums[ (l+r) //2]
        # 左侧位置，即第一个n出现的索引
        nl = bisect.bisect_left(self.nums,n,l,r+1)
        # 右侧位置，即在n后的第一个索引
        nr = bisect.bisect_right(self.nums,n,l,r+1)
        # 递归左右两侧
        ls = self.recur(l,nl-1)
        rs = self.recur(nr,r)
        # 得到其他的结构
        resultR = [ll + rr for ll in ls for rr in rs]
        result=[]
        # 对于当前值，分别取不同长度，进行拼接
        for nt in range(nl-1,nr):
            ns = self.nums[nl:nt+1]
            for rr in resultR:
                result.append(ns +rr)
        return result
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,2]')
    print('Output :')
    print(str(Solution().subsetsWithDup([1,2,2])))
    print('Exception :')
    print('[[],[1],[1,2],[1,2,2],[2],[2,2]]')
    print()
    print('Example 2:')
    print('Input : ')
    print('nums = [0]')
    print('Output :')
    print(str(Solution().subsetsWithDup([0])))
    print('Exception :')
    print('[[],[0]]')
    print()
    
    pass
# @lc main=end