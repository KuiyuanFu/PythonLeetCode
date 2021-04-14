#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#
# https://leetcode.com/problems/permutation-sequence/description/
#
# algorithms
# Hard (39.54%)
# Likes:    2162
# Dislikes: 361
# Total Accepted:    223.5K
# Total Submissions: 564.8K
# Testcase Example:  '3\n3'
#
# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
# 
# By listing and labeling all of the permutations in order, we get the
# following sequence for n = 3:
# 
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 
# 
# Given n and k, return the k^th permutation sequence.
# 
# 
# Example 1:
# Input: n = 3, k = 3
# Output: "213"
# Example 2:
# Input: n = 4, k = 9
# Output: "2314"
# Example 3:
# Input: n = 3, k = 1
# Output: "123"
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 9
# 1 <= k <= n!
# 
# 
#
# 
#
# @lc idea=start
#
# 求前n个正整数的第k个排列。
# 递归，求1-n个数最多有多少个排列，这样可以计算每一位是第几个了。
#
# @lc idea=end

from typing import *
from collections import *


# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 第一个在计算机中索引为0
        k -=1
        times = [1] * n
        buf = list(range(1,n+1))
        result = ''
        for i in range(1 ,n):
            times[-1-i ] = times[-i] * (i+1)
        # 实际使用的是下一位的个数
        times .append(1)
        for i in range(1 , n+1):
            result+=str( buf.pop( k // times[i]))            
            k = k % times[i]

        return result 

        
# @lc code=end

if __name__ == '__main__':
    print(Solution().getPermutation(3,3))
    print(Solution().getPermutation(4,9))
    print(Solution().getPermutation(3,1))
