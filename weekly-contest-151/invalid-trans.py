import itertools


class Solution:
    def invalidTransactions(self, transactions: [str]) -> [str]:
        transactions = [tuple(t.split(',')) for t in transactions]
        transactions.sort(key=lambda t: t[0])
        groupby_name = itertools.groupby(transactions, lambda t: t[0])
        res = set()
        # print(groupby_name)
        for name, trans in groupby_name:
            trans = list(trans)
            # print(name, trans)
            trans.sort(key=lambda s: int(s[1]))
            for i in range(len(trans)):
                if (int(trans[i][2]) > 1000):
                    res.add((',').join(trans[i]))
                    # continue
                for j in range(i-1, -1, -1):
                    if int(trans[i][1])-int(trans[j][1]) > 60:
                        break
                    if trans[i][-1] != trans[j][-1]:
                        res.add((',').join(trans[i]))
                        res.add((',').join(trans[j]))
                for j in range(i+1, len(trans), 1):
                    if int(trans[j][1])-int(trans[i][1]) > 60:
                        break
                    if trans[i][-1] != trans[j][-1]:
                        res.add((',').join(trans[i]))
                        res.add((',').join(trans[j]))
        return list(res)


s = Solution()
transactions = ["lee,886,1785,beijing", "alex,763,1157,amsterdam", "lee,277,129,amsterdam", "bob,770,105,amsterdam", "lee,603,926,amsterdam",
                "chalicefy,476,50,budapest", "lee,924,859,barcelona", "alex,302,590,amsterdam", "alex,397,1464,barcelona", "bob,412,1404,amsterdam", "lee,505,849,budapest"]
# transactions = ["lee,886,1785,beijing", "lee,277,129,amsterdam",
#                 "alice,20,800,mtv", "alice,50,100,beijing"]
res = s.invalidTransactions(transactions)
print(res)
