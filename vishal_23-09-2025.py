class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        k=""
        
        for i in s:
            if i.isalnum():

                k+=i
        a=0
        b=len(k)-1
        while a<b:
            if k[a]==k[b]:
                a+=1
                b-=1
            else:
                return False
        return True
