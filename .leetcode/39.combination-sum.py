# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (59.69%)
# Likes:    5744
# Dislikes: 150
# Total Accepted:    714.2K
# Total Submissions: 1.2M
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen
# numbers sum to target. You may return the combinations in any order.
#
# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen
# numbers is different.
#
# It is guaranteed that the number of unique combinations that sum up to target
# is less than 150 combinations for the given input.
#
#
# Example 1:
#
#
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple
# times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
#
#
# Example 2:
#
#
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
#
#
# Example 3:
#
#
# Input: candidates = [2], target = 1
# Output: []
#
#
# Example 4:
#
#
# Input: candidates = [1], target = 1
# Output: [[1]]
#
#
# Example 5:
#
#
# Input: candidates = [1], target = 2
# Output: [[1,1]]
#
#
#
# Constraints:
#
#
# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# All elements of candidates are distinct.
# 1 <= target <= 500
#
#
#
#
#

# @lc tags=array;backtracking

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 求数字和为target 的所有组合。递归，备忘录。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(True)
        self.candidates = candidates
        self.memo = {}
        return self.do(0, target)

    def do(self, index, target):

        if (index, target) in self.memo:
            return self.memo[(index, target)]
        n = target // self.candidates[index]
        result = []
        if target % self.candidates[index] == 0:
            result.append([self.candidates[index]]*n)
            n -= 1
        if index + 1 < len(self.candidates):
            for i in range(n+1):
                for t in self.do(index+1, target - self.candidates[index] * i):
                    result.append([self.candidates[index]]*i + t)
        return result


        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('candidates = [2,3,6,7], target = 7')
    print('Output :')
    print(str(Solution().combinationSum([2,3,6,7],7)))
    print('Exception :')
    print('[[2,2,3],[7]]')
    print()
    
    print('Example 2:')
    print('Input : ')
    print('candidates = [2,3,5], target = 8')
    print('Output :')
    print(str(Solution().combinationSum([2,3,5],8)))
    print('Exception :')
    print('[[2,2,2,2],[2,3,3],[3,5]]')
    print()
    
    print('Example 3:')
    print('Input : ')
    print('candidates = [2], target = 1')
    print('Output :')
    print(str(Solution().combinationSum([2],1)))
    print('Exception :')
    print('[]')
    print()
    
    print('Example 4:')
    print('Input : ')
    print('candidates = [1], target = 1')
    print('Output :')
    print(str(Solution().combinationSum([1],1)))
    print('Exception :')
    print('[[1]]')
    print()
    
    print('Example 5:')
    print('Input : ')
    print('candidates = [1], target = 2')
    print('Output :')
    print(str(Solution().combinationSum([1],2)))
    print('Exception :')
    print('[[1,1]]')
    print()
    
    pass
# @lc main=end