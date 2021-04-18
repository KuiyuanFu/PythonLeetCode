# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (26.36%)
# Likes:    1212
# Dislikes: 1460
# Total Accepted:    203.4K
# Total Submissions: 771K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# You are given a string s and an array of strings words of the same length.
# Return all starting indices of substring(s) in s that is a concatenation of
# each word in words exactly once, in any order, and without any intervening
# characters.
#
# You can return the answer in any order.
#
#
# Example 1:
#
#
# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar"
# respectively.
# The output order does not matter, returning [9,0] is fine too.
#
#
# Example 2:
#
#
# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# Output: []
#
#
# Example 3:
#
#
# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# Output: [6,9,12]
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s consists of lower-case English letters.
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# words[i] consists of lower-case English letters.
#
#
#
#
#

# @lc tags=hash-table;two-pointers;string

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 返回一个字符串中 用一系列相同长度的词组成的字符串的首字符索引值。
# 想法是获得词的特征码，之后用一个字典存储这些特征码，以计算个数。之后再计算字符串中每个同样长度的子字符串的码。
# 之后遍历次数为词的长度。每一次遍历时的间隔为词的长度，根据词的数量，确定滑动窗口的大小，若所有的词出现的个数都匹配，则匹配成功。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
class Solution:
    mod = 67108863
    mod26 = mod * 26
    assciA = 97

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        length = len(words[0])
        # 不够位数
        if len(s) < len(words) * len(words[0]):
            return result

        self.setNum(length)
        d = self.getDict(words)
        ints = self.getInts(s, length)

        target = len(d)
        # 子字符串的首位索引与最后一个词的首字符索引的差值
        lengthSum = (len(words) - 1) * len(words[0])
        for i in range(length):
            dCopy = d.copy()
            j = i
            now = 0
            while j < len(ints):
                # 在内且等于0，说明这一个词在这正好满足个数了，计数器加一
                if ints[j] in dCopy:
                    dCopy[ints[j]] -= 1
                    if dCopy[ints[j]] == 0:
                        now += 1
                if now == target:
                    result.append(j-lengthSum)
                # 在内且等于1，说明这一个词在这正好不满足个数了，计数器减一
                if j-lengthSum >=0 and ints[j-lengthSum] in dCopy:
                    dCopy[ints[j-lengthSum]] += 1
                    if dCopy[ints[j-lengthSum]] == 1:
                        now -= 1
                j += length

        return result
    # 获得首位的乘数
    def setNum(self, length):
        self.num = 1
        for _ in range(length):
            self.num = (self.num * 26) % self.mod
    # 获得当前索引下的同样长度的子字符串的码
    def getInts(self, s: str, length):
        re = [0] * (len(s) - length + 1)
        now = 0
        for n in s[:length-1]:
            now = (now + ord(n) - self.assciA) * 26 % self. mod

        for i in range(len(s) - length+1):
            now = (now + ord(s[i+length-1]) - self.assciA) * 26 % self.mod
            re[i] = now
            now = (now + self.mod26 -
                   (ord(s[i]) - self.assciA)*self.num) % self.mod
        return re
    # 获得字典，内容是每个词出现的次数
    def getDict(self, words: List[str]):
        d = {}
        for w in words:
            i = self.toInt(w)
            d[i] = d.get(i, 0) + 1
        return d

    def toInt(self, s):
        target = 0
        for n in s:
            target = (target + ord(n) - self. assciA) * 26 % self.mod
        return target


        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "barfoothefoobarman", words = ["foo","bar"]')
    print('Output :')
    print(str(Solution().findSubstring("barfoothefoobarman",["foo","bar"])))
    print('Exception :')
    print('[0,9]')
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]')
    print('Output :')
    print(str(Solution().findSubstring("wordgoodgoodgoodbestword",["word","good","best","word"])))
    print('Exception :')
    print('[]')
    print()
    
    print('Example 3:')
    print('Input : ')
    print('s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]')
    print('Output :')
    print(str(Solution().findSubstring("barfoofoobarthefoobarman",["bar","foo","the"])))
    print('Exception :')
    print('[6,9,12]')
    print()
    
    pass
# @lc main=end