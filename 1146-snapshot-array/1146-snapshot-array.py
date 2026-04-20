class SnapshotArray:
    def __init__(self, length: int):
        self.snap_id = 0
        self.histories = [[[0,0]] for _ in range(length)]
        
    def set(self, index: int, val: int) -> None:
        self.histories[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        snap_index = bisect.bisect_right(self.histories[index], [snap_id, 10 ** 9])
        # self.history_records[index] = [[0,5], [1, 10]]... this type of form.
        # so need to make the same form to compare them [0,5][1,10] then 0, 1 compare first and then second element
        # put maximum possible value 10**9 so we can get always last updated value
        return self.histories[index][snap_index - 1][1]

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