"""
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed.
Suggested products should have common prefix with searchWord. If there are more than three products with a common
prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

Example 1:
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],
["mouse","mousepad"],["mouse","mousepad"]]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].

Example 2:
Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Explanation: The only word "havana" will be always suggested while typing the search word.


Tag: 1268/2927 , R342/2935 , R19/50 (amz)
"""
import bisect


def suggested_products_using_sort_and_list_comprehension(products: list[str], search_word: str) -> list[list[str]]:
    list_ = []
    products.sort()
    for i, c in enumerate(search_word):
        products = [p for p in products if len(p) > i and p[i] == c]
        list_.append(products[:3])
    return list_


def suggested_products_using_sort_and_filter(products: list[str], search_word: str) -> list[list[str]]:
    list_ = []
    products.sort()
    for i, c in enumerate(search_word):
        products = list(filter(lambda p: p[i] == c if len(p) > i else False, products))
        list_.append(products[:3])
    return list_


def suggested_products_using_sort_and_binary_search(products: list[str], search_word: str) -> list[list[str]]:
    # Steps:
    # 1. Search products
    # 2. For each prefix, do binary search
    # 3. Get  words fom the index and check if it matches the prefix

    products.sort()
    res, cur = [], ''
    for c in search_word:
        cur += c
        i = bisect.bisect_left(products, cur)
        res.append([w for w in products[i:i+3] if w.startswith(cur)])
    return res


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.words = list()
        self.n = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children: node.children[c] = TrieNode()
            node = node.children[c]
            if node.n < 3:
                node.words.append(word)
                node.n += 1

    def find_word_by_prefix(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children: return ''
            node = node.children[c]
        return node.words


def suggested_products_using_trie(products: list[str], search_word: str) -> list[list[str]]:
    # Standard Trie
    # 1. Add word to trie while maintaining a list of words of length 3 for each prefix
    # 2. Search each prefix and return

    products.sort()
    trie = Trie()
    for word in products: trie.add_word(word)
    ans, cur = [], ''
    for c in search_word:
        cur += c
        ans.append(trie.find_word_by_prefix(cur))
    return ans


# To sava some tme, it is not necessary to search prefix from the beginning. Use a static variable to search
# only current state.
class Trie1:
    def __init__(self):
        self.root = TrieNode()
        self.node = self.root

    def add_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            if node.n < 3:
                node.words.append(word)
                node.n += 1

    def find_word_by_prefix(self, c):
        if self.node and c in self.node.children:
            self.node = self.node.children[c]
            return self.node.words
        else:
            self.node = None
            return []


def suggested_products_using_trie_alt(products: list[str], search_word: str) -> list[list[str]]:
    products.sort()
    trie1 = Trie1()
    for word in products: trie1.add_word(word)
    return [trie1.find_word_by_prefix(c) for c in search_word]


def main():
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    search_word = "mouse"
    print(suggested_products_using_trie_alt(products, search_word))


if __name__ == "__main__":
    main()

"""
Analysis of first two methods (sort and list comprehension; sort and filter):
Complexity
Definition
N is the number of products.
M is the average length of product names.
L is the length of the search word.

Time
- Sorting: O(MN logN). (String comparison is O(M).)
- Loop and filter: O(LN). Loop L times in the outer loop(i.e. for-loop) and N times in the inner 
loop(i.e. list comprehension). Every filter condition completes in O(1).

The N times loop occurs when all products share the same prefixes of the search word. In this worst case, 
the 2-pointers approach can reduce the inner loop complexity. However, please notice that the time complexity of 
the sorting dominates the loop and filter.

Space
Sorting: O(MN). Python's built-in sort is Timsort.

Explanation:
The problem asks us to return a list of lists of suggested products, which means the list at index i contains 
products that have the same common prefix. So, we can generate results by filtering products based on the typing 
of the user in each iteration. For example

products =  ["mobile","moneypot","monitor","mouse","mousepad"] # Sorted
searchWord = "mouse"

# After typing ‘m’ (i=0, c=‘m’)
products =  ["mobile","moneypot","monitor","mouse","mousepad"]  # Common prefix = ‘m’
list_[0]=["mobile","moneypot","monitor"]

# After typing ‘o’ (i=1, c=‘o’)
products =  ["mobile","moneypot","monitor","mouse","mousepad"]  # Common prefix = ‘mo’
list_[1]=["mobile","moneypot","monitor"]

# After typing ‘u’ (i=2, c=‘u’)
products =  ["mouse","mousepad"]  # Common prefix = ‘mou’
list_[2]=["mouse","mousepad"]

# After typing ‘s’ (i=3, c=‘s’)
products =  ["mouse","mousepad"] # Common prefix = ‘mous’
list_[3]=["mouse","mousepad"]

# After typing ‘e’ (i=4, c=‘e’)
products =  ["mouse","mousepad"] # Common prefix = ‘mouse’
list_[4]=["mouse","mousepad"]

"""

