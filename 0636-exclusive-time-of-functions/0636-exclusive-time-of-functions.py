class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """
        keep the latest id and prev time in stack
        """
        stack = []
        prev_time = 0
        
        exclusive_time = [0] * n
        for log in logs:
            fid, typ, time = log.split(":")
            fid = int(fid)
            time = int(time)

            if typ == "start":
                if stack:
                    exclusive_time[stack[-1]] += time - prev_time
                stack.append(fid)
                prev_time = time
            else:
                exclusive_time[stack[-1]] += time - prev_time + 1
                stack.pop()
                prev_time = time + 1

        return exclusive_time