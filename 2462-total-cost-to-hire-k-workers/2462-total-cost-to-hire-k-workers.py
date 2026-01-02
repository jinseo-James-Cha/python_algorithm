import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # i worker costs[i] => 0 ~ n-1
        # K workers will be hired
        
        # hiring
        # run k sessions and hire one worker on each session.
        # hiring session, lowest cost worker from either the FIRST CANDIDATES or the LAST CANDIDATES
        # if the cost is the same, hire lower index
        """
        first session
        costs = [3,2,7,7,1,2] and candidates = 2
        first3,2 ..... 1, 2last -> 1 is the lowest -> 4th

        second session
        [3, 2, 7, 7, 2]
        first 3, 2, ... 7, 2 -> 2 is the lowest and 1th and 4th, but we choose lower index one
        """
        left_heap = []
        right_heap = []
        left, right = 0, len(costs) - 1
        
        for _ in range(candidates):
            if left <= right:
                heapq.heappush(left_heap, (costs[left], left))
                left += 1
        
        for _ in range(candidates):
            if left <= right:
                heapq.heappush(right_heap, (costs[right], right))
                right -= 1
        
        total_cost = 0
        for _ in range(k):
            if left_heap and right_heap:
                if left_heap[0] <= right_heap[0]:
                    cost, idx = heapq.heappop(left_heap)
                    total_cost += cost
                    if left <= right:
                        heapq.heappush(left_heap, (costs[left], left))
                        left += 1
                else:
                    cost, idx = heapq.heappop(right_heap)
                    total_cost += cost
                    if left <= right:
                        heapq.heappush(right_heap, (costs[right], right))
                        right -= 1
            elif left_heap:
                cost, idx = heapq.heappop(left_heap)
                total_cost += cost
                if left <= right:
                    heapq.heappush(left_heap, (costs[left], left))
                    left += 1
            else:
                cost, idx = heapq.heappop(right_heap)
                total_cost += cost
                if left <= right:
                    heapq.heappush(right_heap, (cost[right], right))
                    right -= 1
        return total_cost


        # queue = deque()
        # for i, cost in enumerate(costs):
        #     queue.append((cost, i))

        # total_cost = 0
        # session = 0
        # while session < k:
        #     session_candidates = []
        #     # front and back
        #     for i in range(candidates):
        #         if queue:
        #             session_candidates.append(queue.popleft())
                
        #         if queue:
        #             session_candidates.append(queue.pop())
                
        #         if not queue:
        #             break
        #     heapq.heapify(session_candidates)
        #     # [17,12,10,2,7,2,11,20,8] k = 3, candidates = 4
        #     # 17 12 10 "2" / 2 11 20 8

        #     cost, i = heapq.heappop(session_candidates)
        #     total_cost += cost

        #     # return back
        #     queue.extend(session_candidates[:])
        #     queue.sort(key=lambda x:x[1])
            
        #     session += 1
        # return total_cost