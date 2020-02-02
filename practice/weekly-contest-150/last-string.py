class Solution:
    def lastSubstring(self, s: str) -> str:
        s_len = len(s)
        c = max(s)
        xs = [i for i in range(s_len) if c == s[i]]
        if len(xs) == s_len:
            return s
        off = 1
        while len(xs) != 1:
            max_i = xs[0]
            for i in xs:
                max_i = i if i + \
                    off < s_len and s[i+off] > s[max_i+off] else max_i
            c = s[max_i+off]  # max char
            xs = [i for i in xs if i+off < s_len and s[i+off] == c]
            off += 1
        return s[xs[0]:]