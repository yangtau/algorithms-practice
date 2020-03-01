'''
https://leetcode.com/problems/rank-teams-by-votes/
'''


class Solution:
    def rankTeams(self, votes: [str]) -> str:
        ranks = {c: [0]*len(votes[0])+[c] for c in votes[0]}
        for vote in votes:
            for i, c in enumerate(vote):
                ranks[c][i] -= 1
        return ''.join(sorted(ranks.keys(), key=ranks.get))

    def rankTeams0(self, votes: [str]) -> str:
        ranks = dict(map(lambda x: (x, [0]*len(votes[0])), votes[0]))
        for vote in votes:
            for i in range(len(vote)):
                ranks[vote[i]][i] += 1
        ranks = sorted(sorted(ranks.items()), reverse=True, key=lambda x: x[1])
        # print(ranks)
        return ''.join(k for k, v in ranks)


s = Solution()
# TEST CASE 1:
votes = ["ABC", "ACB", "ABC", "ACB", "ACB"]
res = "ACB"
print('expect:', res)
print('result:', s.rankTeams(votes))

# TEST CASE 2:
votes = ["WXYZ", "XYZW"]
res = "XWYZ"
print('expect:', res)
print('result:', s.rankTeams(votes))

# TEST CASE 3:
votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
res = "ZMNAGUEDSJYLBOPHRQICWFXTVK"
print('expect:', res)
print('result:', s.rankTeams(votes))

# TEST CASE 4:
votes = ["BCA", "CAB", "CBA", "ABC", "ACB", "BAC"]
res = "ABC"
print('expect:', res)
print('result:', s.rankTeams(votes))
