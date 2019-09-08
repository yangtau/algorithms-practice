class Solution:

    def numSmallerByFrequency(self, queries: [str], words: [str]) -> [int]:
        def f(s: str):
            return s.count(min(s))
        words_f = [f(w) for w in words]
        words_f.sort(reverse=True)
        # print(words_f)
        def count(q):
            fq = f(q)
            # print(fq)
            cnt = 0
            for i in words_f:
                if i <= fq:
                    break
                cnt += 1
            return cnt
        return [count(s) for s in queries]

["cbd"]
["zaaaz"]
queries = ["cbd"]
words = ["zaaaz"]
print(Solution().numSmallerByFrequency(queries, words))
