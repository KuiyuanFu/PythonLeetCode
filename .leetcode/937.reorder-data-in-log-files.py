# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Data in Log Files
#
# https://leetcode.com/problems/reorder-data-in-log-files/description/
#
# algorithms
# Easy (56.07%)
# Likes:    1781
# Dislikes: 4090
# Total Accepted:    316.4K
# Total Submissions: 562.5K
# Testcase Example:  '["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]'
#
# You are given an array of logs. Each log is a space-delimited string of
# words, where the first word is the identifier.
#
# There are two types of logs:
#
#
# Letter-logs: All words (except the identifier) consist of lowercase English
# letters.
# Digit-logs: All words (except the identifier) consist of digits.
#
#
# Reorder these logs so that:
#
#
# The letter-logs come before all digit-logs.
# The letter-logs are sorted lexicographically by their contents. If their
# contents are the same, then sort them lexicographically by their
# identifiers.
# The digit-logs maintain their relative ordering.
#
#
# Return the final order of the logs.
#
#
# Example 1:
#
#
# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit
# dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5
# 1","dig2 3 6"]
# Explanation:
# The letter-log contents are all different, so their ordering is "art can",
# "art zero", "own kit dig".
# The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
#
#
# Example 2:
#
#
# Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act
# zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4
# 7"]
#
#
#
# Constraints:
#
#
# 1 <= logs.length <= 100
# 3 <= logs[i].length <= 100
# All the tokens of logs[i] are separated by a single space.
# logs[i] is guaranteed to have an identifier and at least one word after the
# identifier.
#
#
#

# @lc tags=stack

# @lc imports=start

from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定日志类型，排序。字符型在前，数字型在后，其中字符型按照字典序，数字型按先后顺序。
# 直接分类排序。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        lets = []
        digs = []

        for log in logs:
            strs = log.split(' ')

            t = ''.join(strs[1:])
            if t.isdigit():
                digs.append(log)
            else:
                lets.append((log[log.index(' '):], log))

        lets.sort()
        r = [let[1] for let in lets] + digs
        return r

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kitdig","let3 art zero"]'
    )
    print('Exception :')
    print(
        '["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 51","dig2 3 6"]'
    )
    print('Output :')
    print(
        str(Solution().reorderLogFiles([
            "dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kitdig",
            "let3 art zero"
        ])))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]'
    )
    print('Exception :')
    print(
        '["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 47"]')
    print('Output :')
    print(
        str(Solution().reorderLogFiles([
            "a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog",
            "a8 actzoo"
        ])))
    print()

    pass
# @lc main=end