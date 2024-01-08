"""
A scenic location is represented by its name and attractiveness score, where name is a unique string among all
locations and score is an integer. Locations can be ranked from the best to the worst. The higher the score,
the better the location. If the scores of two locations are equal, then the location with the lexicographically
smaller name is better.

You are building a system that tracks the ranking of locations with the system initially starting with no locations.
It supports:
- Adding scenic locations, one at a time.
- Querying the ith best location of all locations already added, where i is the number of times the system has been
queried (including the current query).
For example, when the system is queried for the 4th time, it returns the 4th best location of all locations
already added.

Note that the test data are generated so that at any time, the number of queries does not exceed the number of
locations added to the system.

Implement the SORTracker class:
- SORTracker() Initializes the tracker system.
- void add(string name, int score) Adds a scenic location with name and score to the system.
- string get() Queries and returns the ith best location, where i is the number of times this method has been
invoked (including this invocation).

Example:
Input
["SORTracker", "add", "add", "get", "add", "get", "add", "get", "add", "get", "add", "get", "get"]
[[], ["bradford", 2], ["branford", 3], [], ["alps", 2], [], ["orland", 2], [], ["orlando", 3], [], ["alpine", 2], [],
[]]
Output
[null, null, null, "branford", null, "alps", null, "bradford", null, "bradford", null, "bradford", "orland"]

Explanation: (After the program below)

Tag: 2102/2927 , R2636/2935 , R48/50 (amz)
"""
import heapq


class CString:
    def __init__(self, word):
        self.word = word

    def __lt__(self, other):
        return self.word > other.word

    def __eq__(self, other):
        return self.word == other.word


class SORTTracker:
    def __init__(self):
        self.upper_part = []  # minHeap
        self.lower_part = []  # maxHeap

    def add(self, name: str, score: int) -> None:
        name = CString(name)
        # first check if there is any element in minHeap
        if self.upper_part:
            upper_score, upper_name = self.upper_part[0]
            # check if we got a better location than the i-1th location
            if upper_score < score or upper_score == score and upper_name.word > name.word:
                heapq.heappop(self.upper_part)
                heapq.heappush(self.upper_part, (score, name))
                # negative score used below because it is a maxheap
                heapq.heappush(self.lower_part, (-upper_score, upper_name.word))
            else:
                # if not we just add the new location to lower part
                heapq.heappush(self.lower_part, (-score, name.word))
        else:
            # if not we just add the new location to lower part
            heapq.heappush(self.lower_part, (-score, name.word))

    def get(self) -> str:
        # remove from the ith position
        score, name = heapq.heappop(self.lower_part)
        # add to the upper part of hte tracker or minHeap
        heapq.heappush(self.upper_part, (-score, CString(name)))
        return name


def main():
    sort_tracker = SORTTracker()
    sort_tracker.add("bradford", 2)
    sort_tracker.add("branford", 3)
    print(sort_tracker.get())
    sort_tracker.add("alps", 2)
    print(sort_tracker.get())
    sort_tracker.add("orland", 2)
    print(sort_tracker.get())
    sort_tracker.add("orlando", 3)
    print(sort_tracker.get())
    sort_tracker.add("alpine", 2)
    print(sort_tracker.get())
    print(sort_tracker.get())


if __name__ == "__main__":
    main()


"""
Explanation of Example:
Input
["SORTracker", "add", "add", "get", "add", "get", "add", "get", "add", "get", "add", "get", "get"]
[[], ["bradford", 2], ["branford", 3], [], ["alps", 2], [], ["orland", 2], [], ["orlando", 3], [], ["alpine", 2], [], 
[]]
Output
[null, null, null, "branford", null, "alps", null, "bradford", null, "bradford", null, "bradford", "orland"]

Explanation
SORTracker tracker = new SORTracker(); // Initialize the tracker system.
tracker.add("bradford", 2); // Add location with name="bradford" and score=2 to the system.
tracker.add("branford", 3); // Add location with name="branford" and score=3 to the system.
tracker.get();              // The sorted locations, from best to worst, are: branford, bradford.
                            // Note that branford precedes bradford due to its higher score (3 > 2).
                            // This is the 1st time get() is called, so return the best location: "branford".
tracker.add("alps", 2);     // Add location with name="alps" and score=2 to the system.
tracker.get();              // Sorted locations: branford, alps, bradford.
                            // Note that alps precedes bradford even though they have the same score (2).
                            // This is because "alps" is lexicographically smaller than "bradford".
                            // Return the 2nd best location "alps", as it is the 2nd time get() is called.
tracker.add("orland", 2);   // Add location with name="orland" and score=2 to the system.
tracker.get();              // Sorted locations: branford, alps, bradford, orland.
                            // Return "bradford", as it is the 3rd time get() is called.
tracker.add("orlando", 3);  // Add location with name="orlando" and score=3 to the system.
tracker.get();              // Sorted locations: branford, orlando, alps, bradford, orland.
                            // Return "bradford".
tracker.add("alpine", 2);   // Add location with name="alpine" and score=2 to the system.
tracker.get();              // Sorted locations: branford, orlando, alpine, alps, bradford, orland.
                            // Return "bradford".
tracker.get();              // Sorted locations: branford, orlando, alpine, alps, bradford, orland.
                            // Return "orland".
                            
"""