class SnapshotArray:
    def __init__(self, length: int):
        self.id = 0
        self.history_records = [[[0, 0]] for _ in range(length)]
        
    def set(self, index: int, val: int) -> None:
        self.history_records[index].append([self.id, val])

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        snap_index = bisect.bisect_right(self.history_records[index], [snap_id, 10 ** 9])
        return self.history_records[index][snap_index - 1][1]

    # MLE
    # def __init__(self, length: int):
    #     self.array_like = [0] * length
    #     self.snaps = []
    #     self.snap_id = 0
        
    # def set(self, index: int, val: int) -> None:
    #     self.array_like[index] = val
        

    # def snap(self) -> int:
    #     self.snaps.append(self.array_like[:])
    #     self.snap_id += 1
    #     return self.snap_id - 1

    # def get(self, index: int, snap_id: int) -> int:
    #     return self.snaps[snap_id][index]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)