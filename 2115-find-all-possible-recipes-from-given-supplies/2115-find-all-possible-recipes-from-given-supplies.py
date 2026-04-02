from collections import deque, defaultdict
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
        recipes ingredients

        recipes + ingredients -> new recipe -> can be a ingredient for another recipe
        
        yeast, flour -> bread
        bread, meat -> sandwitch

        directed acyclic graph -> kahn's topological sort
        
        check which recipe needs ingredients from recipes
        check which recipe can make by initiated supplies -> starting points

        we start from bread because it needs only initial ingredients

        graph
        bread -> sandwitch, burger

        indegree
        sandwitch = 1
        burger = 1

        -> indegree is based on idx
        indegree[i]
        sandwitch-> sandwitch_idx -> indegree[sandwitch_idx] -= 1
        """
        n = len(recipes)
        set_supplies = set(supplies)
        
        graph = defaultdict(list)
        indegree = [0] * n
        for i in range(n):
            curr_recipe = recipes[i]
            for ingredient in ingredients[i]:
                if ingredient not in set_supplies:
                    indegree[i] += 1
                    graph[ingredient].append(recipes[i])

        # indegree [0, 1]
        # initial recipe if indegree 0
        pq = deque()
        for i, count in enumerate(indegree):
            if count == 0:
                pq.append(i)

        recipe_to_idx = {}
        for i, recipe in enumerate(recipes):
            recipe_to_idx[recipe] = i

        res = []
        while pq:
            recipe_idx = pq.popleft()
            complete_recipe = recipes[recipe_idx]            
            res.append(complete_recipe)

            # check other ingredients to use this new recipe
            for next_recipe in graph[complete_recipe]:
                # i need the idx from recipe name
                indegree[recipe_to_idx[next_recipe]] -= 1
                if indegree[recipe_to_idx[next_recipe]] == 0:
                    pq.append(recipe_to_idx[next_recipe])
        return res


        from collections import deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
        bread, sandwich

        yeast, flour -> bread

        bread, meat -> sandwich

        bread -> sandwich,burger..

        """
        set_sup = set(supplies)
        n = len(recipes)
        
        graph = defaultdict(list)
        indegree = [0] * n
        for i in range(n):
            recipe = recipes[i]
            for ingre in ingredients[i]:
                if ingre not in set_sup:
                    graph[ingre].append(recipe)
                    indegree[i] += 1

        pq = deque()
        for i, cnt in enumerate(indegree):
            if cnt == 0:
                pq.append(i)
        
        recipe_idx = {}
        for i, recipe in enumerate(recipes):
            recipe_idx[recipe] = i

        res = []
        while pq:
            curr_idx = pq.popleft()
            recipe = recipes[curr_idx]
            res.append(recipe)

            for neighbor in graph[recipe]:
                idx = recipe_idx[neighbor]
                indegree[idx] -= 1
                if indegree[idx] == 0:
                    pq.append(idx)
        return res