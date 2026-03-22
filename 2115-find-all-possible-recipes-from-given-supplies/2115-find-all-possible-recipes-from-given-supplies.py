class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
        I have n recipes
        recipe[i] -> ingredients[i] are all in supplies? -> then return recipe[i]
        """
        # kahn's topological sort
        set_sup = set(supplies)
        recipe_to_index = {recipe: idx for idx, recipe in enumerate(recipes)}

        graph = defaultdict(list)
        indegree = [0] * len(recipes)

        for recipe_idx, ingredient_list in enumerate(ingredients):
            for ingredient in ingredient_list:
                if ingredient not in set_sup:
                    graph[ingredient].append(recipes[recipe_idx])
                    indegree[recipe_idx] += 1
        
        queue = deque()
        for idx, count in enumerate(indegree):
            if count == 0:
                queue.append(idx)

        created_recipes = []
        while queue:
            recipe_idx = queue.popleft()
            recipe = recipes[recipe_idx]
            created_recipes.append(recipe)

            for neighbor in graph[recipe]:
                indegree[recipe_to_index[neighbor]] -= 1
                if indegree[recipe_to_index[neighbor]] == 0:
                    queue.append(recipe_to_index[neighbor])

        return created_recipes















        # brute force
        # check each each ingredients in supplies
        # it is not working cuz of order matters in this solution..
        n = len(recipes)
        set_supplies = set(supplies)
        res = []

        for i in range(n):
            curr_recipe = recipes[i]
            curr_ingredients = ingredients[i]

            all_pass = True
            for ing in curr_ingredients:
                if ing not in set_supplies:
                    all_pass = False
                    break
            
            if all_pass:
                set_supplies.add(curr_recipe)
                res.append(curr_recipe)
        return res