#!/usr/bin/env python3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = []
        letterPos = 0
        if s != "":
            for letterPos in range(len(s)):
                if s[letterPos] not in letters:
                    letters.append(s[letterPos])
                
                else:
                    break
            
            if letterPos + 1 == len(s):
                return len(letters)
            else:
                otherLen = self.lengthOfLongestSubstring(s[1:])
                if len(letters) > otherLen:
                    return len(letters)
                else:
                    return otherLen

        else:
            return 0

            
if __name__ == "__main__":
    test1 = "abcabcbb"
    test2 = "bbbbb"
    test3 = "pwwkew"
    
    solucion = Solution()
    print(solucion.lengthOfLongestSubstring(test1))
    print(solucion.lengthOfLongestSubstring(test2))
    print(solucion.lengthOfLongestSubstring(test3))