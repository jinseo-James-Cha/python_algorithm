class StringIterator:

    def __init__(self, compressedString: str):
        self._str = ""
        self.cur_index = 0
        index = 0
        letter = ""
        times = 0
        while index < len(compressedString):
            if compressedString[index].isalpha():
                self._str += letter * times
                letter = compressedString[index]
                times = 0
            else: # if its number
                times *= 10
                times += int(compressedString[index])
            index += 1
        # for the last letter and times
        self._str += letter * times     

    def next(self) -> str:
        if not self.hasNext():
            return " "
        cur_index = self.cur_index
        self.cur_index += 1
        return self._str[cur_index]

    def hasNext(self) -> bool:
        if self.cur_index + 1 > len(self._str): # 7 8
            return False
        return True
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()