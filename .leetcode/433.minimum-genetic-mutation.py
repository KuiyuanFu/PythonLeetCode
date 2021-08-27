# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#
# https://leetcode.com/problems/minimum-genetic-mutation/description/
#
# algorithms
# Medium (44.32%)
# Likes:    638
# Dislikes: 79
# Total Accepted:    42.8K
# Total Submissions: 96.4K
# Testcase Example:  '"AACCGGTT"\n"AACCGGTA"\n["AACCGGTA"]'
#
# A gene string can be represented by an 8-character long string, with choices
# from 'A', 'C', 'G', and 'T'.
#
# Suppose we need to investigate a mutation from a gene string start to a gene
# string end where one mutation is defined as one single character changed in
# the gene string.
#
#
# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
#
#
# There is also a gene bank bank that records all the valid gene mutations. A
# gene must be in bank to make it a valid gene string.
#
# Given the two gene strings start and end and the gene bank bank, return the
# minimum number of mutations needed to mutate from start to end. If there is
# no such a mutation, return -1.
#
# Note that the starting point is assumed to be valid, so it might not be
# included in the bank.
#
#
# Example 1:
#
#
# Input: start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
# Output: 1
#
#
# Example 2:
#
#
# Input: start = "AACCGGTT", end = "AAACGGTA", bank =
# ["AACCGGTA","AACCGCTA","AAACGGTA"]
# Output: 2
#
#
# Example 3:
#
#
# Input: start = "AAAAACCC", end = "AACCCCCC", bank =
# ["AAAACCCC","AAACCCCC","AACCCCCC"]
# Output: 3
#
#
#
# Constraints:
#
#
# start.length == 8
# end.length == 8
# 0 <= bank.length <= 10
# bank[i].length == 8
# start, end, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定基因序列，与一个可能的突变集合，每次只能突变一个位置，求从开始到最后的最小突变次数。
# 图，广度优先遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0
        if end not in bank:
            return -1
        if start not in bank:
            bank.append(start)
        adj = defaultdict(list)
        l = len(bank)
        kr = range(8)
        for i in range(l):
            si = bank[i]
            for j in range(i + 1, l):
                sj = bank[j]
                if [si[k] == sj[k] for k in kr].count(True) == 7:
                    adj[si].append(sj)
                    adj[sj].append(si)
        adjs = [start]
        n = 0
        visited = set(adjs)
        while adjs:
            adjsn = []
            n += 1
            for ad in adjs:
                for a in adj[ad]:
                    if a == end:
                        return n
                    if a not in visited:
                        visited.add(a)
                        adjsn.append(a)
            adjs = adjsn
        return -1

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"])))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'start = "AACCGGTT", end = "AAACGGTA", bank =["AACCGGTA","AACCGCTA","AAACGGTA"]'
    )
    print('Exception :')
    print('2')
    print('Output :')
    print(
        str(Solution().minMutation("AACCGGTT", "AAACGGTA",
                                   ["AACCGGTA", "AACCGCTA", "AAACGGTA"])))
    print()

    print('Example 3:')
    print('Input : ')
    print(
        'start = "AAAAACCC", end = "AACCCCCC", bank =["AAAACCCC","AAACCCCC","AACCCCCC"]'
    )
    print('Exception :')
    print('3')
    print('Output :')
    print(
        str(Solution().minMutation("AAAAACCC", "AACCCCCC",
                                   ["AAAACCCC", "AAACCCCC", "AACCCCCC"])))
    print()

    pass
# @lc main=end