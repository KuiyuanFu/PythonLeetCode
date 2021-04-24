class Solution:
    # 获得字典，内容是每个词出现的次数
    def getDict(self, words: List[str]):
        d = {}
        for w in words:
            i = self.toInt(w)
            d[i] = d.get(i, 0) + 1
        return d