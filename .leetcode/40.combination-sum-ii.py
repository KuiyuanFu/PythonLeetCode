# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (50.39%)
# Likes:    2646
# Dislikes: 86
# Total Accepted:    400.8K
# Total Submissions: 794.7K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sum to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note: The solution set must not contain duplicate combinations.
#
#
# Example 1:
#
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,5,2,1,2], target = 5
# Output:
# [
# [1,2,2],
# [5]
# ]
#
#
#
# Constraints:
#
#
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
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
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        d = {}
        for w in candidates:
            d[w] = d.get(w, 0) + 1

        self.dic = d
        self.candidates = list(d.keys())
        self.memo = {}
        return self.do(0, target)

    def do(self, index, target):

        if (index, target) in self.memo:
            return self.memo[(index, target)]
        n = target // self.candidates[index]
        n = n if n < self.dic[self.candidates[index]
                              ] else self.dic[self.candidates[index]]
        result = []
        if target == self.candidates[index] * n:
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
    print('candidates = [10,1,2,7,6,1,5], target = 8')
    print('Output :')
    print(str(Solution().combinationSum2([10,1,2,7,6,1,5],8)))
    print('Exception :')
    print('[[1,1,6],[1,2,5],[1,7],[2,6]]')
    print()
    
    print('Example 2:')
    print('Input : ')
    print('candidates = [2,5,2,1,2], target = 5')
    print('Output :')
    print(str(Solution().combinationSum2([2,5,2,1,2],5)))
    print('Exception :')
    print('[[1,2,2],[5]]')
    print()
    
    pass
# @lc main=end