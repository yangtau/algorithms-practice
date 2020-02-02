class SnapshotArray:

    def __init__(self, length: int):
        self._snap={}
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self._snap.setdefault(self.snap_id, {})
        self._snap[self.snap_id][index] = val

    def snap(self) -> int:
        _snap_id = self.snap_id
        self.snap_id += 1
        return _snap_id

    def get(self, index: int, snap_id: int) -> int:
        for i in range(snap_id, -1, -1):
            if i in self._snap and index in self._snap[i]:
                    return self._snap[i][index]
        return 0
