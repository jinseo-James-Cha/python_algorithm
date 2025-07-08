class Solution:
    def canWinNim(self, n: int) -> bool:
        # you go first
        # turn -> remove 1 to 3 stones from the heap
        # winner -> removed the last stone

        # my turn is n
        # your turn is n + 1
        # 1 2 3
        # 4 FALSE
        # 5 6 7 
        # 8 FALSE
        return n % 4 != 0