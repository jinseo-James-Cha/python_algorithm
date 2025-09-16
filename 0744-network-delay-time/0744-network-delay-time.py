class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for source, dest, travel_time in times:
            adj[source].append((travel_time, dest))  # (가중치, 목적지)
        
        # 
        signalReceivedAt = [float('inf')] * (n + 1)
        signalReceivedAt[k] = 0

        pq = [(0, k)]
        while pq:
            curr_time, curr_node = heapq.heappop(pq)

            # 이미 더 짧은 시간으로 방문한 적이 있으면 스킵
            if curr_time > signalReceivedAt[curr_node]:
                continue

            # 인접 노드 탐색
            for time, neighbor in adj[curr_node]:
                new_time = curr_time + time
                # Edge relaxation
                if new_time < signalReceivedAt[neighbor]:
                    signalReceivedAt[neighbor] = new_time
                    heapq.heappush(pq, (new_time, neighbor))

        # 4️⃣ 결과 계산
        answer = max(signalReceivedAt[1:])  # 1번부터 n번까지
        return -1 if answer == float('inf') else answer