# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#
# https://leetcode.com/problems/word-ladder-ii/description/
#
# algorithms
# Hard (23.87%)
# Likes:    2529
# Dislikes: 303
# Total Accepted:    229.6K
# Total Submissions: 954K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# A transformation sequence from word beginWord to word endWord using a
# dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk
# such that:
#
#
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to
# be in wordList.
# sk == endWord
#
#
# Given two words, beginWord and endWord, and a dictionary wordList, return all
# the shortest transformation sequences from beginWord to endWord, or an empty
# list if no such sequence exists. Each sequence should be returned as a list
# of the words [beginWord, s1, s2, ..., sk].
#
#
# Example 1:
#
#
# Input: beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log","cog"]
# Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
# Explanation: There are 2 shortest transformation sequences:
# "hit" -> "hot" -> "dot" -> "dog" -> "cog"
# "hit" -> "hot" -> "lot" -> "log" -> "cog"
#
#
# Example 2:
#
#
# Input: beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log"]
# Output: []
# Explanation: The endWord "cog" is not in wordList, therefore there is no
# valid transformation sequence.
#
#
#
# Constraints:
#
#
# 1 <= beginWord.length <= 5
# endWord.length == beginWord.length
# 1 <= wordList.length <= 1000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.
#
#
#

# @lc tags=array;string;backtracking;breadth-first-search

# @lc imports=start
from distutils.core import run_setup
from unittest import result
from imports import *

# @lc imports=end

# @lc idea=start
#
# 词梯。给定一组单词，与起始词，结束词。
# 求转换顺序。
# 使用双端，写的太复杂了。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findLadders(self, beginWord: str, endWord: str,
                    wordList: List[str]) -> List[List[str]]:

        beginSet = set([beginWord])
        endSet = set([endWord])
        # check endword is in wordList
        notReachedSet = set(wordList)
        if endWord not in notReachedSet:
            return []
        notReachedSet.remove(endWord)

        beginOldSets = [beginSet]
        endOldSets = [endSet]

        correspondings = []
        while beginSet and endSet:
            # find count smaller set
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
                beginOldSets, endOldSets = endOldSets, beginOldSets

            beginSetNew = set()
            for val in list(beginSet):
                # change char
                for i in range(len(val)):
                    vals = [val[:i], '', val[i + 1:]]
                    for c in 'qwertyuiopasdfghjklzxcvbnm':
                        vals[1] = c
                        v = ''.join(vals)
                        if v in endSet:
                            correspondings.append([val, v])
                        if v in notReachedSet:
                            notReachedSet.remove(v)
                            beginSetNew.add(v)
            if correspondings:
                break
            beginOldSets.append(beginSet)
            beginSet = beginSetNew
        beginValues = set()
        endValues = set()
        # find left sets
        flag = 0 if beginWord in beginOldSets[0] else 1
        if flag != 0:
            beginOldSets, endOldSets = endOldSets, beginOldSets
        for c in correspondings:
            beginValues.add(c[0 - flag])
            endValues.add(c[1 - flag])

        mem = {}

        # find path
        def recur(sets, index, val, flag):
            if val in mem:
                return mem[val]
            if index == 0:
                results = [[val]]
                mem.update({val: results})
                return results
            results = []

            for v in list(sets[index]):
                times = 0
                for i in range(len(val)):
                    if val[i] != v[i]:
                        times += 1
                if times == 1:
                    rs = recur(sets, index - 1, v, flag)
                    for r in rs:
                        if flag:
                            results.append(r + [val])
                        else:
                            results.append([val] + r)
            mem.update({val: results})
            return results

        for val in beginValues:
            recur(beginOldSets, len(beginOldSets) - 1, val, True)
        for val in endValues:
            recur(endOldSets, len(endOldSets) - 1, val, False)
        flag = flag == 0
        results = []
        for c in correspondings:

            ls, rs = mem[c[0]], mem[c[1]]
            if not flag:
                ls, rs = rs, ls
            for l in ls:
                for r in rs:
                    results.append(l + r)

        return results


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'beginWord = "hit", endWord = "cog", wordList =["hot","dot","dog","lot","log","cog"]'
    )
    print('Exception :')
    print('[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]')
    print('Output :')
    print(
        str(Solution().findLadders(
            "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'beginWord = "hit", endWord = "cog", wordList =["hot","dot","dog","lot","log"]'
    )
    print('Exception :')
    print('[]')
    print('Output :')
    print(
        str(Solution().findLadders("hit", "cog",
                                   ["hot", "dot", "dog", "lot", "log"])))
    print()

    pass
# @lc main=end