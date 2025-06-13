# at most every 10 seconds
# t + 10 < next message
# Several messages may arrive at the same timestamp.

# time : O(1) -> hashtable / dictionary
# space : O(M)
class Logger:

    def __init__(self):
        self.message_timestamp = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if not message in self.message_timestamp:
            self.message_timestamp[message] = timestamp + 10
        
        elif self.message_timestamp[message] > timestamp:
            return False

        else:
            self.message_timestamp[message] = timestamp + 10

        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)