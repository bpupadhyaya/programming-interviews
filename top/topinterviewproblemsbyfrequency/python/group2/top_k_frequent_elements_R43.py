"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer
in any order.

Example:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Tag: R43/145
"""
from collections import Counter
from heapq import heappush, nlargest, heappop, heappushpop


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    # Using counter and most_common
    # Internally most_common() method is implemented by constructing a heap and using nlargest() function from the
    # heapq library
    freq_table = Counter(nums)
    ans_table = freq_table.most_common()
    ans = []
    for key, _ in ans_table:
        if k <= 0:
            break
        k -= 1
        ans.append(key)
    return ans


def top_k_frequent_1(nums: list[int], k: int) -> list[int]:
    # Using counter, heap, and nlargest
    freq_table = Counter(nums)
    heap = []
    for i in freq_table.keys():
        heappush(heap, (freq_table[i], i))
    freq_table = nlargest(k, heap)
    ans = []
    for i, j in freq_table:
        ans.append(j)
    return ans


def top_k_frequent_2(nums: list[int], k: int) -> list[int]:
    # Using counter and selecting manually
    freq_table = Counter(nums)
    heap = []
    for i in freq_table.keys():
        heappush(heap, (-freq_table[i], i))
    ans = []
    while k > 0:
        k -= 1
        ans.append(heappop(heap)[1])
    return ans


def top_k_frequent_3(nums: list[int], k: int) -> list[int]:
    # Manual
    freq_table = {}
    for i in nums:
        freq_table[i] = freq_table.get(i, 0) + 1
    heap = []
    for i in freq_table.keys():
        if len(heap) == k:  # If size is k then we don't want to increase the size further
            heappushpop(heap, (freq_table[i], i))
        else:  # Size is not k then freely push values
            heappush(heap, (freq_table[i], i))
    # After this operation the heap contains only k largest values of all the values in nums
    ans = []
    while k > 0:
        k -= 1
        ans.append(heappop(heap)[1])
    return ans


def main():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(top_k_frequent_3(nums, k))


if __name__ == "__main__":
    main()


"""
Note on manual method from internet:
During an interview using tons of library functions is generally not advisable. Especially when these things be 
replicated with relative ease without drastically increasing the size of your code or its complexity. However you 
can always ask the interviewer if you can use Library Functions as they might just want to see your apporach to 
the problem rather than your programming skills.

NOTE: heapq.heappushpop allows us to add element to the heap without changing its size. It basically does a push 
first then pop. So it is used in situations where you want to add values into the heap but dont want to change 
its size. This keeps the size fixed but keeps removing the min or max(as you may have used it) there by finally 
containing only largest or smallest of the added values.
"""
