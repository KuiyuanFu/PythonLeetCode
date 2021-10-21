# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#
# https://leetcode.com/problems/top-k-frequent-words/description/
#
# algorithms
# Medium (53.69%)
# Likes:    3676
# Dislikes: 225
# Total Accepted:    323K
# Total Submissions: 599.9K
# Testcase Example:  '["i","love","leetcode","i","love","coding"]\n2'
#
# Given an array of strings words and an integer k, return the k most frequent
# strings.
#
# Return the answer sorted by the frequency from highest to lowest. Sort the
# words with the same frequency by their lexicographical order.
#
#
# Example 1:
#
#
# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.
#
#
# Example 2:
#
#
# Input: words =
# ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
# Output: ["the","is","sunny","day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
# with the number of occurrence being 4, 3, 2 and 1 respectively.
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 500
# 1 <= words[i] <= 10
# words[i] consists of lowercase English letters.
# k is in the range [1, The number of unique words[i]]
#
#
#
# Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
#
#

# @lc tags=hash-table;heap;trie

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 频数最高的k的单词。
# 字典，堆，排序。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], kf: int) -> List[str]:
        length = max(len(w) for w in words)

        def getFres():
            d = defaultdict(int)
            for w in words:
                d[w] += 1
            return d

        d = getFres()

        def generateKeys(d):
            def reversedLexi(s):
                res = [26 - (ord(c) - ord("a")) for c in s]
                for _ in range(length - len(res)):
                    res.append(27)
                return res

            return [(d[key], reversedLexi(key), key) for key in d]

        keys = generateKeys(d)

        def getKF(keys):

            h = []
            for key in keys:

                if len(h) < kf:
                    heappush(h, key)
                elif key > h[0]:
                    heappushpop(h, key)
            res = []
            while h:
                res.append(heappop(h)[2])
            return list(reversed(res))

        res = getKF(keys)
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('words = ["i","love","leetcode","i","love","coding"], k = 2')
    print('Exception :')
    print('["i","love"]')
    print('Output :')
    print(
        str(Solution().topKFrequent(
            ["i", "love", "leetcode", "i", "love", "coding"], 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'words =["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4'
    )
    print('Exception :')
    print('["the","is","sunny","day"]')
    print('Output :')
    print(
        str(Solution().topKFrequent([
            "the", "day", "is", "sunny", "the", "the", "the", "sunny", "is",
            "is"
        ], 4)))
    print()

    pass
# @lc main=end