from collections import defaultdict
import math
import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
        diff = d1 - d2
        return diff.day

    def validateBinaryTreeNodes(self, n: int, leftChild: [int], rightChild: [int]) -> bool:
        # something wrong with this problem
        pass
    def closestDivisors(self, num: int) -> [int]:
        s = int(math.sqrt(num+2))
        m = 0
        for i in range(1, s+1):
            if (num+2) % i == 0:
                m = i
        res1 = [m, (num+2)//m]

        s = int(math.sqrt(num+1))
        m = 0
        for i in range(1, s+1):
            if (num+1) % i == 0:
                m = i
        res2 = [m, (num+1)//m]
        if abs(res1[0]-res1[1]) > abs(res2[0]-res2[1]):
            return res2
        else:
            return res1

    def largestMultipleOfThree(self, digits: [int]) -> str:
        cnts = defaultdict(int)
        s = 0
        for d in digits:
            cnts[d] += 1
            s += d
        rem = s % 3

        def format_str():
            res = ""
            for i in range(9, -1, -1):
                res += str(i)*cnts[i]
            if res.startswith('0'):
                return '0'
            return res
        if rem == 0:
            return format_str()

        xs = [i for i in range(rem, rem+7, 3)]
        # 1 4 7 or 2 5 8 in cnts
        for i in xs:
            if cnts[i] > 0:
                cnts[i] -= 1
                return format_str()

        i = (rem+rem) % 3
        x, y, z = i, i+3, i+6  # (1, 4, 7) -> (2, 5, 8), (2, 5, 8) -> (1, 4, 7)
        # (1, 1), (1, 4), (4, 4), (1, 7), (4, 7), (7, 7)
        if cnts[x] >= 2:
            cnts[x] -= 2
        elif cnts[x] > 0 and cnts[y] > 0:
            cnts[x] -= 1
            cnts[y] -= 1
        elif cnts[y] > 1:
            cnts[y] -= 2
        elif cnts[x] > 0 and cnts[z] > 0:
            cnts[z] -= 1
            cnts[x] -= 1
        elif cnts[y] > 0 and cnts[z] > 0:
            cnts[z] -= 1
            cnts[y] -= 1
        elif cnts[z] > 1:
            cnts[z] -= 2
        else:
            return ""
        return format_str()


s = Solution()
print("res", s.largestMultipleOfThree([9, 8, 6, 8, 6]))
print("res", s.largestMultipleOfThree([1]))
print("res", s.largestMultipleOfThree([0, 0, 0]))
