#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#
# https://leetcode.com/problems/text-justification/description/
#
# algorithms
# Hard (30.13%)
# Likes:    995
# Dislikes: 1966
# Total Accepted:    168.2K
# Total Submissions: 556.2K
# Testcase Example:  '["This", "is", "an", "example", "of", "text", "justification."]\n16'
#
# Given an array of words and a width maxWidth, format the text such that each
# line has exactly maxWidth characters and is fully (left and right)
# justified.
#
# You should pack your words in a greedy approach; that is, pack as many words
# as you can in each line. Pad extra spaces ' ' when necessary so that each
# line has exactly maxWidth characters.
#
# Extra spaces between words should be distributed as evenly as possible. If
# the number of spaces on a line do not divide evenly between words, the empty
# slots on the left will be assigned more spaces than the slots on the right.
#
# For the last line of text, it should be left justified and no extra space is
# inserted between words.
#
# Note:
#
#
# A word is defined as a character sequence consisting of non-space characters
# only.
# Each word's length is guaranteed to be greater than 0 and not exceed
# maxWidth.
# The input array words contains at least one word.
#
#
#
# Example 1:
#
#
# Input: words = ["This", "is", "an", "example", "of", "text",
# "justification."], maxWidth = 16
# Output:
# [
# "This    is    an",
# "example  of text",
# "justification.  "
# ]
#
# Example 2:
#
#
# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth =
# 16
# Output:
# [
# "What   must   be",
# "acknowledgment  ",
# "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall
# be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified becase it contains only one
# word.
#
# Example 3:
#
#
# Input: words =
# ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],
# maxWidth = 20
# Output:
# [
# "Science  is  what we",
# ⁠ "understand      well",
# "enough to explain to",
# "a  computer.  Art is",
# "everything  else  we",
# "do                  "
# ]
#
#
# Constraints:
#
#
# 1 <= words.length <= 300
# 1 <= words[i].length <= 20
# words[i] consists of only English letters and symbols.
# 1 <= maxWidth <= 100
# words[i].length <= maxWidth
#
#
#
#
#
# @lc idea=start
#
# 文本适配。
# 占满宽度。
#
# @lc idea=end

from typing import *
from collections import *


# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        now = [words[0]]
        length = len(words[0])
        for word in words[1:]:
            if length + len(now) + len(word) > maxWidth:
                if len(now) == 1:
                    result .append(now[0] + ' '*(maxWidth - len(now[0])))
                else:
                    blankSpace = maxWidth - length
                    base = blankSpace // (len(now) - 1)
                    times = blankSpace % (len(now) - 1)
                    t = (' ' * (base + 1)).join(now[:times+1])
                    t = (' ' * (base)).join([t] + now[times+1:])
                    result .append(t)
                pass
                now = [word]
                length = len(word)
            else:
                length += len(word)
                now.append(word)
        if len(now) != 0:
            t = ' '.join(now)
            result .append(t + ' '*(maxWidth - len(t)))
        return result


# @lc code=end
if __name__ == '__main__':
    print(Solution().fullJustify(
        ["This", "is", "an", "example", "of", "text", "justification."], 16))
