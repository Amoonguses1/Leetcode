class SnapshotArray:
    def __init__(self, length: int):
        self.snapCalled = 0
        self.arr = [[] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        # Time: O(1)
        # Space: O(1)
        if self.arr[index] and self.arr[index][-1][0] == self.snapCalled:
            self.arr[index][-1][1] = val
        else:
            self.arr[index].append([self.snapCalled, val])

    def snap(self) -> int:
        # Time: O(1)
        # Space: O(1)
        self.snapCalled += 1
        return self.snapCalled - 1

    def get(self, index: int, snap_id: int) -> int:
        # Time: O(logN)
        # Space: O(1)
        # N = len(self.arr[index])
        return self.binarySearch(snap_id, self.arr[index])

    def binarySearch(self, id: int, arr: list[list[int]]) -> int:
        if len(arr) == 0 or arr[0][0] > id:
            return 0

        left = -1
        right = len(arr)
        while right - left > 1:
            mid = (left+right) // 2
            if arr[mid][0] == id:
                return arr[mid][1]

            elif arr[mid][0] > id:
                right = mid
            else:
                left = mid
        return arr[left][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
