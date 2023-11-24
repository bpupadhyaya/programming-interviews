"""
You are given two string arrays username and website and an integer array timestamp. All the given arrays are of
the same length and the tuple [username[i], website[i], timestamp[i]] indicates that the user username[i] visited
the website website[i] at time timestamp[i].

A pattern is a list of three websites (not necessarily distinct).
- For example, ["home", "away", "love"], ["leetcode", "love", "leetcode"], and ["luffy", "luffy", "luffy"] are
all patterns.

The score of a pattern is the number of users that visited all the websites in the pattern in the same order they
appeared in the pattern.
- For example, if the pattern is ["home", "away", "love"], the score is the number of users x such that x visited
"home" then visited "away" and visited "love" after that.
- Similarly, if the pattern is ["leetcode", "love", "leetcode"], the score is the number of users x such that x
visited "leetcode" then visited "love" and visited "leetcode" one more time after that.
- Also, if the pattern is ["luffy", "luffy", "luffy"], the score is the number of users x such that x
visited "luffy" three different times at different timestamps.

Return the pattern with the largest score. If there is more than one pattern with the same largest score,
return the lexicographically smallest such pattern.

Example:
Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"],
timestamp = [1,2,3,4,5,6,7,8,9,10],
website = ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]
Explanation: The tuples in this example are:
["joe","home",1],["joe","about",2],["joe","career",3],["james","home",4],["james","cart",5],["james","maps",6],
["james","home",7],["mary","home",8],["mary","about",9], and ["mary","career",10].
The pattern ("home", "about", "career") has score 2 (joe and mary).
The pattern ("home", "cart", "maps") has score 1 (james).
The pattern ("home", "cart", "home") has score 1 (james).
The pattern ("home", "maps", "home") has score 1 (james).
The pattern ("cart", "maps", "home") has score 1 (james).
The pattern ("home", "home", "home") has score 0 (no user visited home 3 times).


Tag: 1152/2927 , R498/2935 , R24/50 (amz)
"""
from collections import defaultdict
from itertools import combinations
from typing import List


def most_visited_pattern(username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
    # Sort the website info based on the timestamp
    web_info = []
    for time, usr, web in zip(timestamp, username, website):
        web_info.append((time, usr, web))
    web_info.sort(key=lambda x: x[0])

    # Find the websites visited by particular user
    website_visit = defaultdict(list)
    for _, usr, web in web_info:
        website_visit[usr].append(web)

    # Find the routes in the form of tuples of 3
    possible_tuples = defaultdict(int)
    for usr in website_visit:
        web_routes = set(combinations(website_visit[usr], 3))
        for web_route in web_routes:
            possible_tuples[web_route] += 1

    # Find max value of users visited
    max_val, routes = max(possible_tuples.values()), []
    for r, val in possible_tuples.items():
        if val == max_val:
            routes.append(r)

    if len(routes) > 1:
        # Sort lexicographically
        routes.sort()

    return routes[0]


def main():
    username = ["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"]
    timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    website = ["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"]
    print(most_visited_pattern(username, timestamp, website))


if __name__ == "__main__":
    main()
