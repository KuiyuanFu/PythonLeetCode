# @lc app=leetcode id=591 lang=python3
#
# [591] Tag Validator
#
# https://leetcode.com/problems/tag-validator/description/
#
# algorithms
# Hard (35.55%)
# Likes:    117
# Dislikes: 510
# Total Accepted:    9.8K
# Total Submissions: 27.6K
# Testcase Example:  '"<DIV>This is the first line <![CDATA[<div>]]></DIV>"'
#
# Given a string representing a code snippet, implement a tag validator to
# parse the code and return whether it is valid.
#
# A code snippet is valid if all the following rules hold:
#
#
# The code must be wrapped in a valid closed tag. Otherwise, the code is
# invalid.
# A closed tag (not necessarily valid) has exactly the following format :
# <TAG_NAME>TAG_CONTENT</TAG_NAME>. Among them, <TAG_NAME> is the start tag,
# and </TAG_NAME> is the end tag. The TAG_NAME in start and end tags should be
# the same. A closed tag is valid if and only if the TAG_NAME and TAG_CONTENT
# are valid.
# A valid TAG_NAME only contain upper-case letters, and has length in range
# [1,9]. Otherwise, the TAG_NAME is invalid.
# A valid TAG_CONTENT may contain other valid closed tags, cdata and any
# characters (see note1) EXCEPT unmatched <, unmatched start and end tag, and
# unmatched or closed tags with invalid TAG_NAME. Otherwise, the TAG_CONTENT is
# invalid.
# A start tag is unmatched if no end tag exists with the same TAG_NAME, and
# vice versa. However, you also need to consider the issue of unbalanced when
# tags are nested.
# A < is unmatched if you cannot find a subsequent >. And when you find a < or
# </, all the subsequent characters until the next > should be parsed as
# TAG_NAME (not necessarily valid).
# The cdata has the following format : <![CDATA[CDATA_CONTENT]]>. The range of
# CDATA_CONTENT is defined as the characters between <![CDATA[ and the first
# subsequent ]]>.
# CDATA_CONTENT may contain any characters. The function of cdata is to forbid
# the validator to parse CDATA_CONTENT, so even it has some characters that can
# be parsed as tag (no matter valid or invalid), you should treat it as regular
# characters.
#
#
#
# Example 1:
#
#
# Input: code = "<DIV>This is the first line <![CDATA[<div>]]></DIV>"
# Output: true
# Explanation:
# The code is wrapped in a closed tag : <DIV> and </DIV>.
# The TAG_NAME is valid, the TAG_CONTENT consists of some characters and
# cdata.
# Although CDATA_CONTENT has an unmatched start tag with invalid TAG_NAME, it
# should be considered as plain text, not parsed as a tag.
# So TAG_CONTENT is valid, and then the code is valid. Thus return true.
#
#
# Example 2:
#
#
# Input: code = "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"
# Output: true
# Explanation:
# We first separate the code into : start_tag|tag_content|end_tag.
# start_tag -> "<DIV>"
# end_tag -> "</DIV>"
# tag_content could also be separated into : text1|cdata|text2.
# text1 -> ">>  ![cdata[]] "
# cdata -> "<![CDATA[<div>]>]]>", where the CDATA_CONTENT is "<div>]>"
# text2 -> "]]>>]"
# The reason why start_tag is NOT "<DIV>>>" is because of the rule 6.
# The reason why cdata is NOT "<![CDATA[<div>]>]]>]]>" is because of the rule
# 7.
#
#
# Example 3:
#
#
# Input: code = "<A>  <B> </A>   </B>"
# Output: false
# Explanation: Unbalanced. If "<A>" is closed, then "<B>" must be unmatched,
# and vice versa.
#
#
# Example 4:
#
#
# Input: code = "<DIV>  div tag is not closed  <DIV>"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= code.length <= 500
# code consists of English letters, digits, '<', '>', '/', '!', '[', ']', '.',
# and ' '.
#
#
#

# @lc tags=string;stack

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断是否是合法的代码。
# 确定有穷自动机。就是太麻烦了。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def isValid(self, code: str) -> bool:
        dfa = [
            # 0 1 2 3 4 5 678910  11   12       13        14
            # < / ! [ ] > CDATA Captical Other  >Empty >Illegal

            # 0   1   2   3   4   5   6    7   8  9  10   11  12  13  14
            # 0 初始状态，接下来必须是左括号。
            [5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            # 1 左尖括号，根据下一个字符，判断是开始、结束、还是数据。
            [-1, 3, 4, -1, -1, -1, 2, 2, 2, 2, 2, 2, -1, -1, -1],
            # 2 标签开始，开始读数据  todo
            [-1, -1, -1, -1, -1, 6, 2, 2, 2, 2, 2, 2, -1, -1, -1],
            # 3 标签结束，开始读数据 todo
            [-1, -1, -1, -1, -1, 6, 3, 3, 3, 3, 3, 3, -1, -2, -1],
            # 4 数据开始<!，开始读数据
            [-1, -1, -1, 15, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            # 5 初始状态的左尖括号，下一个字符必定是大写字母。
            [-1, -1, -1, -1, -1, -1, 2, 2, 2, 2, 2, 2, -1, -1, -1],
            # 6 标签内部。
            [1, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
            # 7 数据开始<![C
            [-1, -1, -1, -1, -1, -1, -1, 8, -1, -1, -1, -1, -1, -1, -1],
            # 8 数据开始<![CD
            [-1, -1, -1, -1, -1, -1, -1, -1, 9, -1, -1, -1, -1, -1, -1],
            # 9 数据开始<![CDA
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, 10, -1, -1, -1, -1, -1],
            # 10 数据开始<![CDAT
            [-1, -1, -1, -1, -1, -1, -1, -1, 11, -1, -1, -1, -1, -1, -1],
            # 11 数据开始<![CDATA
            [-1, -1, -1, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            # 12 数据开始<![CDATA[
            [12, 12, 12, 12, 13, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
            # 13 数据结束<![CDATA[...]
            [12, 12, 12, 12, 14, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
            # 14 数据结束<![CDATA[...]]
            [12, 12, 12, 12, 12, 6, 12, 12, 12, 12, 12, 12, 12, 12, 12],
            # 15 数据结束<![
            [-1, -1, -1, -1, -1, -1, 7, -1, -1, -1, -1, -1, -1, -1, -1],

            # -2 标签栈没有数据了，接下来任意字符都不行。
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            # -1 GG 出错。todo
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
            # 0   1   2   3   4   5   6   7   8  9  10   11  12  13  14
        ]
        stack = []
        state = 0
        symbols = '</![]>CDATA'
        ss = []
        for c in code:
            symbol = 12
            if c in symbols:
                symbol = symbols.index(c)
            elif c.isupper():
                symbol = 11
            if (state == 1 or state == 5) and 6 <= symbol <= 11:
                ss.append(c)
            # do >
            if state == 2 or state == 3:
                if 6 <= symbol <= 11:
                    ss.append(c)
                # >
                if symbol == 5:
                    if not 1 <= len(ss) <= 9:
                        symbol = 14
                    else:
                        s = ''.join(ss)
                        ss = []
                        # 开始
                        if state == 2:
                            stack.append(s)
                        else:
                            if len(stack) == 0 or s != stack[-1]:
                                symbol = 14
                            else:
                                stack.pop()
                                if len(stack) == 0:
                                    symbol = 13
            state = dfa[state][symbol]
            if state == -1:
                break

        return state == -2

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('code = "<DIV>This is the first line <![CDATA[<div>]]></DIV>"')
    print('Exception :')
    print('true')
    print('Output :')
    print(
        str(Solution().isValid(
            "<DIV>This is the first line <![CDATA[<div>]]></DIV>")))
    print()

    print('Example 2:')
    print('Input : ')
    print('code = "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"')
    print('Exception :')
    print('true')
    print('Output :')
    print(
        str(Solution().isValid(
            "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>")))
    print()

    print('Example 3:')
    print('Input : ')
    print('code = "<A>  <B> </A>   </B>"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isValid("<A>  <B> </A>   </B>")))
    print()

    print('Example 4:')
    print('Input : ')
    print('code = "<DIV>  div tag is not closed  <DIV>"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isValid("<DIV>  div tag is not closed  <DIV>")))
    print()

    pass
# @lc main=end