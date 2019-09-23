from queue import Queue
from collections import defaultdict


def topsort(items, beforeItems) -> list:
    afterItems = defaultdict(list)
    indge = dict()
    for it in items:
        indge.setdefault(it, 0)
        for before in beforeItems[it]:
            if before in items:
                afterItems[before].append(it)
                indge[it] += 1
    que = Queue()
    for k, v in indge.items():
        if v == 0:
            que.put(k)
    res = []
    while not que.empty():
        top = que.get()
        res.append(top)
        for after in afterItems[top]:
            indge[after] -= 1
            if indge[after] == 0:
                que.put(after)
    return [] if len(res) != len(items) else res


class Solution:
    def sortItems(self, n: int, m: int, group: [int], beforeItems: [[int]]) -> [int]:
        groups = [set() for _ in range(m)]
        group_cnt = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_cnt
                group_cnt += 1
                groups.append(set())
            groups[group[i]].add(i)
        sortGroups = []
        for i in range(group_cnt):
            if len(groups[i]) in (0, 1):
                sortGroups.append(list(groups[i]))
                continue
            sortGroups.append(topsort(groups[i], beforeItems))
            if sortGroups[i] == []:
                return []

        beforeGroup = [set() for _ in range(group_cnt)]
        for i in range(n):
            for before in beforeItems[i]:
                if before not in groups[group[i]]:
                    beforeGroup[group[i]].add(group[before])

        group_index_sort = topsort(set(range(group_cnt)), beforeGroup)
        if group_index_sort == []:
            return []
        return [it for i in group_index_sort for it in sortGroups[i]]


def test_topsort():
    items = [0, 1, 2, 3, 4, 5]
    beforeItems = [[2, 3], [1], [4, 6], [], [1], [4, 3]]
    print(topsort(items, beforeItems))


def test():
    n = 8
    m = 2
    group = [-1, -1, 1, 0, 0, 1, 0, -1]
    beforeItems = [[], [6], [5], [6], [3, 6], [], [], []]

    n = 8
    m = 2
    group = [-1, -1, 1, 0, 0, 1, 0, -1]
    beforeItems = [[], [6], [5], [6], [3], [], [4], []]

    n = 5
    m = 5
    group = [2, 0, -1, 3, 0]
    beforeItems = [[2, 1, 3], [2, 4], [], [], []]
    s = Solution()
    res = s.sortItems(n, m, group, beforeItems)
    print(res)


test()
