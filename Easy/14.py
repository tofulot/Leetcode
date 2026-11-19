class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        longest = ''
        for letterindex in range(len(strs[0])):
            shared = ''
            for s in strs:
                if letterindex >= len(s):
                    return longest
                if shared == '':
                    shared = s[letterindex]
                    continue
                if s[letterindex]!=shared:
                    return longest
            longest += shared
        return longest
                
        