# Given a string s, return the longest 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

# Take 1
# if len(s) == 1 or len(set(s)) == 1: return s
#         stack = []
#         for index, c in enumerate(s):
#             # init
#             if not stack:
#                 stack.append(index)
#                 continue
#             # branch
#             if s[stack[-1]] == c:
#                 stack = stack[:-1]
#                 continue
#             if len(stack) >= 2 and s[stack[-2]] == c:
#                 stack = stack[:-2]
#                 continue
#             if c not in stack:
#                 stack.append(index)
#         return self.getResult(s, stack) if stack else s
    
#     def addChar(self, string:str, char: str) -> str:
#         return string + char
    
#     def getResult(self, s:str, stack:list) -> str:
#         if len(stack) == len(s): return s[0]
#         for idx in stack:
#             s = s[:idx] + "!" + s[idx + 1 :]
#         return s.replace("!", "") 



class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        result = []
        string = ""
        for i in range(len(s) - 1):
            init = True
            stack = []
            string = ""
            for j in range(i, len(s)):
                
                string += s[j]
                if not stack:
                    stack.append(s[j])
                    init = False
                    continue
                
                if s[j] == stack[-1]:
                    stack = stack[:-1]
                    continue
                
                if len(stack) >= 2 and s[j] == stack[-2]:
                    stack = stack[:-2]
                    continue
                
                stack.append(s[j])
                
            if not init and not stack:
                result.append(string)
                continue
        if len(stack) == len(s): return s[0]
        
        return sorted(result, reverse=True)[0]
        
    

s = Solution();
TC = ["aacabdkacaa"]
for _ in TC:
    print(s.longestPalindrome(_))
