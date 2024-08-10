class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]  # Start with the first string as the potential prefix
        for i in range(1, len(strs)):
            j = 0
            while j < len(res) and j < len(strs[i]) and res[j] == strs[i][j]:  # Corrected condition
                j += 1
            res = res[:j]  # Truncate res to the common prefix length found so far
            if res == "":  # Early exit if no common prefix
                break
        return res
