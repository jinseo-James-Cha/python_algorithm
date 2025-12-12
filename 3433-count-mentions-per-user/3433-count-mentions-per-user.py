class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        # 1. message event -> ["MESSAGE", "time", ALL or HERE or id0 id1]
        # 2. offline event -> ["OFFLINE", "time", "id1"] -> time+60 -> online

        events.sort(key=lambda x: (int(x[1]), x[0] == "MESSAGE")) # OFFLINE FIRST

        users_timestamp = [0] * numberOfUsers
        res = [0] * numberOfUsers
        for event, timestamp, mentions_string in events:
            # message
            if event == "MESSAGE":
                if mentions_string == "ALL":
                    for i in range(numberOfUsers):
                        res[i] += 1
                elif mentions_string == "HERE":
                    for i in range(numberOfUsers):
                        if users_timestamp[i] <= int(timestamp):
                            res[i] += 1
                else:
                    ids = mentions_string.replace("id", "").split(" ")
                    for id in ids:
                        res[int(id)] += 1
            # offline
            else:
                users_timestamp[int(mentions_string)] = int(timestamp) + 60
        return res

        """
        [["MESSAGE","2","HERE"],
        ["OFFLINE","2","1"],
        ["OFFLINE","1","0"],
        ["MESSAGE","61","HERE"]]

        [0, 0, 0]
        [0, 0 ,0]
        """