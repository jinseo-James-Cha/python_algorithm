class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        n = len(rooms)
        all rooms are locked except 0
        visite all rooms with keys
        when I visit a room I find a key

        """
        # DFS
        def dfs(room_number):
            visited.add(room_number)

            for k in rooms[room_number]:
                if k not in visited and k < len(rooms):
                    dfs(k)
        
        n = len(rooms)
        visited = set()
        dfs(0) # initial
        return len(visited) == n