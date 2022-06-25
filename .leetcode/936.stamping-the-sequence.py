# @lc app=leetcode id=936 lang=python3
#
# [936] Stamping The Sequence
#
# https://leetcode.com/problems/stamping-the-sequence/description/
#
# algorithms
# Hard (53.69%)
# Likes:    552
# Dislikes: 126
# Total Accepted:    24.3K
# Total Submissions: 45.3K
# Testcase Example:  '"abc"\n"ababc"'
#
# You are given two strings stamp and target. Initially, there is a string s of
# length target.length with all s[i] == '?'.
#
# In one turn, you can place stamp over s and replace every letter in the s
# with the corresponding letter from stamp.
#
#
# For example, if stamp = "abc" and target = "abcba", then s is "?????"
# initially. In one turn you can:
#
#
# place stamp at index 0 of s to obtain "abc??",
# place stamp at index 1 of s to obtain "?abc?", or
# place stamp at index 2 of s to obtain "??abc".
#
# Note that stamp must be fully contained in the boundaries of s in order to
# stamp (i.e., you cannot place stamp at index 3 of s).
#
#
# We want to convert s to target using at most 10 * target.length turns.
#
# Return an array of the index of the left-most letter being stamped at each
# turn. If we cannot obtain target from s within 10 * target.length turns,
# return an empty array.
#
#
# Example 1:
#
#
# Input: stamp = "abc", target = "ababc"
# Output: [0,2]
# Explanation: Initially s = "?????".
# - Place stamp at index 0 to get "abc??".
# - Place stamp at index 2 to get "ababc".
# [1,0,2] would also be accepted as an answer, as well as some other answers.
#
#
# Example 2:
#
#
# Input: stamp = "abca", target = "aabcaca"
# Output: [3,0,1]
# Explanation: Initially s = "???????".
# - Place stamp at index 3 to get "???abca".
# - Place stamp at index 0 to get "abcabca".
# - Place stamp at index 1 to get "aabcaca".
#
#
#
# Constraints:
#
#
# 1 <= stamp.length <= target.length <= 1000
# stamp and target consist of lowercase English letters.
#
#
#

# @lc tags=array

# @lc imports=start

from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个stamp，每次在初始值为空的s上覆盖，使其变成target，最多10*len(target)次。求覆盖序列。
# 首先可以确定，target中完整的stamp是最后放置的，那么就可以分成多段，之后左右两侧遍历。
# 就是挺麻烦。
#
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def movesToStamp(self, stamp: str, target: str) -> List[int]:

        # find stamp idx
        stampStartIndeices = []
        idx = 0
        while True:
            idx = target.find(stamp, idx)
            if idx == -1:
                break
            stampStartIndeices.append(idx)
            idx += len(stamp)

        # validation
        if len(stampStartIndeices) == 0:
            return []

        # right to left
        def rtl(l, r):
            res = []
            rt = r + 1
            for lt in reversed(range(l, r + 1)):
                s = target[lt:rt]
                length = len(s)
                if length > len(stamp):
                    break
                if s == stamp[:length]:
                    res.append(lt)
                    rt = lt

            return rt - 1, list(reversed(res))

        # left to right
        def ltr(l, r):
            res = []
            lt = l
            for rt in range(l + 1, r + 2):
                s = target[lt:rt]
                length = len(s)
                if length > len(stamp):
                    break
                if s == stamp[-length:]:
                    res.append(rt - len(stamp))
                    lt = rt
            return lt, list(reversed(res))

        res = []
        # first
        t, r = rtl(0, stampStartIndeices[0] - 1)
        if t != -1:
            return []
        res += r
        # last
        t, r = ltr(stampStartIndeices[-1] + len(stamp), len(target) - 1)
        if t != len(target):
            return []
        res += r
        # middle
        for idx in range(len(stampStartIndeices) - 1):
            l = stampStartIndeices[idx] + len(stamp)
            r = stampStartIndeices[idx + 1] - 1
            lt, lr = ltr(l, r)
            rt, rr = rtl(lt, r)
            if lt == rt + 1:
                al = lr + rr
                res += al
            elif target[lt:rt + 1] in stamp:
                i = stamp.index(target[lt:rt + 1])
                al = [lt - i] + lr + rr
                res += al
            else:
                return []
        res += stampStartIndeices

        tb = [None] * len(target)
        for idx in res:
            tb[idx:idx + len(stamp)] = stamp[:]
        print(target)
        print(''.join(tb))

        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('stamp = "xkaw", target = "xkxxkawxkxkawkxkxxkaxkaww"')
    print('Exception :')
    print('[13,11,10,15,12,14,1,19,18,16,6,5,4,8,0,21,17,7,2,20,9,3]')
    print('Output :')
    print(str(Solution().movesToStamp("xkaw", "xkxxkawxkxkawkxkxxkaxkaww")))
    print()
    print('Example 1:')
    print('Input : ')
    print('stamp = "zbs", target = "zbzbsbszbssbzbszbsss"')
    print('Exception :')
    print('[11,9,17,10,6,5,3,1,16,14,13,8,4,0,15,12,7,2]')
    print('Output :')
    print(str(Solution().movesToStamp("zbs", "zbzbsbszbssbzbszbsss")))
    print()

    # print('Example 1:')
    # print('Input : ')
    # print('stamp = "abc", target = "ababc"')
    # print('Exception :')
    # print('[0,2]')
    # print('Output :')
    # print(str(Solution().movesToStamp("abc", "ababc")))
    # print()

    # print('Example 2:')
    # print('Input : ')
    # print('stamp = "abca", target = "aabcaca"')
    # print('Exception :')
    # print('[3,0,1]')
    # print('Output :')
    # print(str(Solution().movesToStamp("abca", "aabcaca")))
    # print()

    # print(str(Solution().movesToStamp("ab", "abbbabbbab")))
    # print(str(Solution().movesToStamp("ab", "abbbabbbaa")))

    pass
# @lc main=end