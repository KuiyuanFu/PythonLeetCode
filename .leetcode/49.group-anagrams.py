# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (59.68%)
# Likes:    5224
# Dislikes: 228
# Total Accepted:    896K
# Total Submissions: 1.5M
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
# 
# 
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
# Input: strs = [""]
# Output: [[""]]
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lower-case English letters.
# 
# 
#
# 
#

# @lc tags=hash-table;string

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 组字谜，就是把具有相同字符不同顺序的字符串放在一起。
# 对每个词进行排序，得到关键字，字典存储关键字与词数组。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}
        for w in strs:
            k = ''.join(sorted(w)) 
            l = d.get(k, [])
            l.append(w)
            d[k] =  l
        return list(d.values())
        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('strs = ["eat","tea","tan","ate","nat","bat"]')
    print('Output :')
    print(str(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])))
    print('Exception :')
    print('[["bat"],["nat","tan"],["ate","eat","tea"]]')
    print()
    
    print('Example 2:')
    print('Input : ')
    print('strs = [""]')
    print('Output :')
    print(str(Solution().groupAnagrams([""])))
    print('Exception :')
    print('[[""]]')
    print()
    
    print('Example 3:')
    print('Input : ')
    print('strs = ["a"]')
    print('Output :')
    print(str(Solution().groupAnagrams(["a"])))
    print('Exception :')
    print('[["a"]]')
    print()
    
    pass
# @lc main=end