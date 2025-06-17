# Definition for a street.
# class Street:
#     def openDoor(self):
#         pass
#     def closeDoor(self):
#         pass
#     def isDoorOpen(self):
#         pass
#     def moveRight(self):
#         pass
#     def moveLeft(self):
#         pass
class Solution:
    def houseCount(self, street: Optional['Street'], k: int) -> int:
        # circular street, k = maximum bound
        # Houses' doors could be open or closed initially.
        
        for i in range(k):
            street.closeDoor()
            street.moveRight()
        
        count = 0
        for i in range(k):
            if not street.isDoorOpen():
                street.openDoor()
                street.moveRight()
                count += 1
            else:
                break

        return count