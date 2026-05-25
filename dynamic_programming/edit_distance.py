class Solution:
    def edit_min_distance(self, word1: str, word2: str) -> int:

        def dfs(w1: str, w1_idx, w2_idx):
            if w1 == word2:
                return 0

            if w1_idx < len(w1) and w2_idx == len(word2):
                return float("inf")

            # replace the current char in a w1 with current char in word2
            replaced = w1[0:w1_idx] + word2[w2_idx] + w1[w1_idx+1:]
            replace = dfs(replaced, w1_idx+1, w2_idx+1)

            # insert word2 current char at the curr index in w1
            inserted = w1[0:w1_idx] + word2[w2_idx] + w1[w1_idx:]
            insert = dfs(inserted, w1_idx+1, w2_idx+1)

            # remove current index char in w1
            removed = w1[0:w1_idx] + w1[w1_idx+1:]
            remove = dfs(removed, w1_idx, w2_idx)

            return 1 + min(remove, replace, insert)