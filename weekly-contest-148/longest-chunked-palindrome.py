class Solution:
    def longestDecomposition(self, text: str) -> int:
        if len(text) < 2:
            return len(text)
        for i in range(1, len(text)//2+1):
            if text[:i] == text[-i:]:
                return 2 + self.longestDecomposition(text[i:-i])
        return 1
