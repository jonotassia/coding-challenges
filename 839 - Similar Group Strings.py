from functools import cache

class Disjoint:
    def __init__(self, n: int):
        # Initialize a parent array, where the ith element is the parent of i
        # In clearer terms, when intitialized, each n terms in the strings array will be their own parents
        self.parent = list(range(n))
        # Set the rank of the tree to be an array where the ith index corresponds to the ith tree's rank
        self.rank = [1] * n
        # Initialize the count to n since it begins with n distinct groups
        self.group_count = n

    def find(self, n: int):
        # Find the parent of n.
        # This uses the assumption that the root of each tree points to themselves as the exit clause for recursion
        if self.parent[n] != n:
            return self.find(self.parent[n])
        else:
            return n

    def union(self, n1: int, n2: int) -> bool:
        if n1 == n2:
            return True

        # Find the root of each value's tree. This will be used to union each tree at the root and calculate their rank
        pn1, pn2 = self.find(n1), self.find(n2)

        # If already connected, return early as true
        if pn1 == pn2:
            return True

        # Use ranking to merge the smaller tree onto the larger tree's root node. The smaller ranked one should
        # always be added to the larger tree to minimize depth.
        if self.rank[pn1] >= self.rank[pn2]:
            self.parent[pn2] = pn1
            self.rank[pn1] += 1

        else:
            self.parent[pn1] = pn2
            self.rank[pn2] += 1

        # Decrement by 1 for every union since we are merging two groups
        self.group_count -= 1
        return True

    # @cache
    # def check_connected(self, n1, n2) -> bool:
    #     if n1 == n2:
    #         return True
    #
    #     # If the root of n1 and the root of n2 are the same, then they are connected
    #     if self.find(n1) == self.find(n2):
    #         return True
    #     else:
    #         return False


def numSimilarGroups(strs: list[str]) -> int:
    # Create the DSU for the list of strings
    string_dsu: Disjoint = Disjoint(len(strs))

    # Define function to check similarity
    def check_similar(string1: str, string2: str):
        mismatch_counter:int = 0

        # Leverages assumption that all strings are same size
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                mismatch_counter += 1

        # If more than one mismatched character, strings are not similar
        if mismatch_counter > 2:
            return False

        return True

    # Move through list of strs to identify similar items
    for i in range(len(strs)-1):
        for j in range(i+1, len(strs)):
            if not check_similar(strs[i], strs[j]):
                continue

            string_dsu.union(i, j)

    # Convert parent to a set to get number of unique values, then get its length
    return string_dsu.group_count


numSimilarGroups(["ajdidocuyh","djdyaohuic","ddjyhuicoa","djdhaoyuic","ddjoiuycha","ddhoiuycja","ajdydocuih","ddjiouycha","ajdydohuic","ddjyouicha"])
