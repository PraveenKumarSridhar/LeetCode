class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if not s:
            return 0
        st, end = 0, 0
        max_sub = 0
        
        char_map = {}
        
        while end< n:
            # print(st, end, s[end])
            if s[end] in char_map:
                st = max(char_map[s[end]], st)
                # char_map = {}
            
            char_map[s[end]] = end + 1
            # print(st, end)
            max_sub = max(max_sub, end - st + 1)
            end +=1
            # print(char_map, max_sub)
        return max_sub