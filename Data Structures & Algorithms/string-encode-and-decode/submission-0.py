class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for s in strs:
            encoded_string += str(len(s)) + '#' + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            n = ''
            j = i
            while s[j] != '#':
                n += s[j]
                j += 1
            n = int(n) # len of word
            i = j + 1
            res.append(s[i: i + n])
            i =  i + n

        return res