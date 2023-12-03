"""
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.
Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation
is defined as one single character changed in the gene string.
For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a
valid gene string.
Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations
needed to mutate from startGene to endGene. If there is no such a mutation, return -1.
Note that the starting point is assumed to be valid, so it might not be included in the bank.

Example:
Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2

Tag: 96/150
Tag: 433/2927, R1250/2936 (overall frequency ranking)
"""
from collections import deque


def min_mutation_bfs(start_gene: str, end_gene: str, bank: list[str]) -> int:
    bank = set(bank)
    dq = deque([(start_gene, 0)])

    while dq:
        st0, cnt = dq.popleft()
        if st0 == end_gene:
            return cnt
        for i, ch0 in enumerate(st0):
            for ch1 in "ACGT":
                if ch0 != ch1 and (st1 := st0[:i] + ch1 + st0[i+1:]) in bank:
                    bank.remove(st1)
                    dq.append((st1, cnt + 1))
    return -1


def min_mutation_dfs(start_gene: str, end_gene: str, bank: list[str]) -> int:
    bank = set(bank) | {start_gene}

    def dfs(st0, cnt):
        if st0 == end_gene:
            return cnt

        bank.remove(st0)
        for i, ch0 in enumerate(st0):
            for ch1 in "ACGT":
                if (
                    ch0 != ch1
                    and (st1 := st0[:i] + ch1 + st0[i+1:]) in bank
                    and (res := dfs(st1, cnt + 1)) != -1
                ):
                    return res
        return -1
    return dfs(start_gene, 0)


def main():
    start_gene = "AACCGGTT"
    end_gene = "AAACGGTA"
    bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    print(min_mutation_dfs(start_gene, end_gene, bank))


if __name__ == "__main__":
    main()
