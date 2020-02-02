from queue import Queue


class Solution:
    def minFlips(self, mat) -> int:
        m, n = len(mat), len(mat[0])
        target = tuple([tuple([0]*n)]*m)
        mat = tuple(tuple(row) for row in mat)
        que = Queue()
        s = set()
        que.put((0, target))
        s.add(target)
        while not que.empty():
            step, front = que.get()
            if front == mat:
                return step

            for i in range(m):
                for j in range(n):
                    tmp = [list(t) for t in front]
                    tmp[i][j] = 1 - tmp[i][j]
                    if i > 0:
                        tmp[i-1][j] = 1 - tmp[i-1][j]
                    if j > 0:
                        tmp[i][j-1] = 1 - tmp[i][j-1]
                    if i < m-1:
                        tmp[i+1][j] = 1 - tmp[i+1][j]
                    if j < n-1:
                        tmp[i][j+1] = 1 - tmp[i][j+1]
                    tmp = tuple(tuple(row) for row in tmp)
                    if tmp not in s:
                        print(tmp)
                        s.add(tmp)
                        que.put((step+1, tmp))
        return -1


if __name__ == '__main__':
    s = Solution()
    m = [[1, 1, 1], [1, 0, 1], [0, 0, 0]]
    m = [[1, 0, 0], [1, 0, 0]]
    res = s.minFlips(m)
    print(res)
