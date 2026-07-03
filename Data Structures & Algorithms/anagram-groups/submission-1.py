class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for w in strs:
            anagram = [0]*26
            for c in w:
                anagram[ord(c) - ord("a")] += 1
            anagrams[tuple(anagram)].append(w)

        return list(anagrams.values())