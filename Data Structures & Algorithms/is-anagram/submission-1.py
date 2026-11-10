class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {char:0 for char in s }
        for char in s:
            if char in dict1:
                dict1[char] += 1
        dict2 = {char:0 for char in t }
        for char in t:
            if char in dict2:
                dict2[char] += 1
        if dict2 == dict1:
            return True
        else:
            return False

       

