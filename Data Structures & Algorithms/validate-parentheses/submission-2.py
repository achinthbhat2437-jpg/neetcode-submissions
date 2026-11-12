class Solution:
    def isValid(self, s: str) -> bool:
        def matches(m,n):
            if(m=='{'and n=='}'):
                return True
            elif(m == '[' and n == ']'):
                return True
            elif(m =='(' and n == ')'):
                return True
            else:
                return False

        t = []
        for i in range(0,len(s)):
            t.append(s[i])
            if(len(t)>1):
                if(matches(t[len(t)-2],t[len(t)-1])):
                    t.pop()
                    t.pop()
        if(len(t)==0):
            return True
        else:
            return False