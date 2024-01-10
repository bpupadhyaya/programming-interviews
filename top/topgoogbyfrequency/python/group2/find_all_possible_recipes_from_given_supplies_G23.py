"""
You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients.
 The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients
 from ingredients[i]. Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i]
  may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, and you have
 an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.

Example 1:
Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
Output: ["bread"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".

Constraints:

n == recipes.length == ingredients.length
1 <= n <= 100
1 <= ingredients[i].length, supplies.length <= 100
1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.
All the values of recipes and supplies combined are unique.
Each ingredients[i] does not contain any duplicate values.

Tag: G23/50
"""
from collections import defaultdict, Counter, deque


def find_all_recipes0(recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
    # Brute force, just to help understand the problem
    ans = []
    seen = set(supplies)
    dq = deque([(r, ing) for r, ing in zip(recipes, ingredients)])

    # dummy value for prev_size, just to make sure
    # the initial value of prev_size < len(seen)
    prev_size = len(seen) - 1

    # Keep searching if we have any new finding(s).
    while len(seen) > prev_size:
        prev_size = len(seen)
        for _ in range(len(dq)):
            r, ing = dq.popleft()
            if all(i in seen for i in ing):
                ans.append(r)
                seen.add(r)
            else:
                dq.append((r, ing))
    return ans


def find_all_recipes(recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
    # Topological sorting
    # Construct directed graph and count the in-degrees
    ingredient_to_recipe, in_degree = defaultdict(set), Counter()
    for rcp, ingredient in zip(recipes, ingredients):
        for ing in ingredient:
            ingredient_to_recipe[ing].add(rcp)
        in_degree[rcp] = len(ingredient)
    # Topological sort.
    ans = []
    for ing in supplies:
        for rcp in ingredient_to_recipe.pop(ing, set()):
            in_degree[rcp] -= 1
            if in_degree[rcp] == 0:
                supplies.append(rcp)
                ans.append(rcp)

    return ans


def main():
    recipes = ["bread"]
    ingredients = [["yeast", "flour"]]
    supplies = ["yeast", "flour", "corn"]
    print(find_all_recipes(recipes, ingredients, supplies))


if __name__ == "__main__":
    main()
