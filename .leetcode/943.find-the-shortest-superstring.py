# @lc app=leetcode id=943 lang=python3
#
# [943] Find the Shortest Superstring
#
# https://leetcode.com/problems/find-the-shortest-superstring/description/
#
# algorithms
# Hard (45.11%)
# Likes:    1146
# Dislikes: 131
# Total Accepted:    24.6K
# Total Submissions: 54.5K
# Testcase Example:  '["alex","loves","leetcode"]'
#
# Given an array of strings words, return the smallest string that contains
# each string in words as a substring. If there are multiple valid strings of
# the smallest length, return any of them.
#
# You may assume that no string in words is a substring of another string in
# words.
#
#
# Example 1:
#
#
# Input: words = ["alex","loves","leetcode"]
# Output: "alexlovesleetcode"
# Explanation: All permutations of "alex","loves","leetcode" would also be
# accepted.
#
#
# Example 2:
#
#
# Input: words = ["catg","ctaagt","gcta","ttca","atgcatc"]
# Output: "gctaagttcatgcatc"
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 12
# 1 <= words[i].length <= 20
# words[i] consists of lowercase English letters.
# All the strings of words are unique.
#
#
#

# @lc tags=array;stack

# @lc imports=start

from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定字符串数组，求最短的字符串，使数组中所有字符串都是其的子字符串。
# 递归，需要缓存才能不超时。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def shortestSuperstring(self, A):

        @lru_cache(None)
        def suff(s1, s2):
            for length in range(len(s2), 0, -1):
                if s1[-length:] == s2[:length]:
                    return s2[length:]
            return s2

        @lru_cache(None)
        def dp(mask, l):
            if mask + 1 == 1 << N: return ""
            return min([
                suff(A[l], A[i]) + dp(mask | 1 << i, i)
                for i in range(N) if not mask & 1 << i
            ],
                       key=len)

        N = len(A)
        return min([A[i] + dp(1 << i, i) for i in range(N)], key=len)


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('words = ["alex","loves","leetcode"]')
    print('Exception :')
    print('"alexlovesleetcode"')
    print('Output :')
    print(str(Solution().shortestSuperstring(["alex", "loves", "leetcode"])))
    print()

    print('Example 2:')
    print('Input : ')
    print('words = ["catg","ctaagt","gcta","ttca","atgcatc"]')
    print('Exception :')
    print('"gctaagttcatgcatc"')
    print('Output :')
    print(
        str(Solution().shortestSuperstring(
            ["catg", "ctaagt", "gcta", "ttca", "atgcatc"])))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'words = ["txvteggrtmylrxxknwub","lipgamrjnsfcqizch","teggrtmylrxxknwubv","uogduurswxthftx","akwnbruogduursw","uurswxthftxvteg","mylrxxknwubvlipga","ggrtmylrxxknwubvl","gzeindakwnbruogdu","thftxvteggrtmylrx"]'
    )
    print('Exception :')
    print('"gzeindakwnbruogduurswxthftxvteggrtmylrxxknwubvlipgamrjnsfcqizch"')
    print('Output :')
    print(
        str(Solution().shortestSuperstring([
            "txvteggrtmylrxxknwub", "lipgamrjnsfcqizch", "teggrtmylrxxknwubv",
            "uogduurswxthftx", "akwnbruogduursw", "uurswxthftxvteg",
            "mylrxxknwubvlipga", "ggrtmylrxxknwubvl", "gzeindakwnbruogdu",
            "thftxvteggrtmylrx"
        ])))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'words = ["vgrikrnwezryimj","umwgwvzpsfpmctzt","pjourlpgeemdjor","urlpgeemdjorpzbkbz","jorpzbkbzcqyewih","xuwkzvoczozhhvf","ihbumoogibirbsvch","nwezryimjivvpjourlp","kzvoczozhhvfwgeplv","ezryimjivvpjourlpgee","zhhvfwgeplvqngglu","rikrnwezryimjivvp"]'
    )
    print('Exception :')
    print(
        '"vgrikrnwezryimjivvpjourlpgeemdjorpzbkbzcqyewihbumoogibirbsvchxuwkzvoczozhhvfwgeplvqngglumwgwvzpsfpmctzt"'
    )
    print('Output :')
    print(
        str(Solution().shortestSuperstring([
            "vgrikrnwezryimj", "umwgwvzpsfpmctzt", "pjourlpgeemdjor",
            "urlpgeemdjorpzbkbz", "jorpzbkbzcqyewih", "xuwkzvoczozhhvf",
            "ihbumoogibirbsvch", "nwezryimjivvpjourlp", "kzvoczozhhvfwgeplv",
            "ezryimjivvpjourlpgee", "zhhvfwgeplvqngglu", "rikrnwezryimjivvp"
        ])))
    print()

    pass
# @lc main=end