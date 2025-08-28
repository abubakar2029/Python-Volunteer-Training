class Solution:
    def isValid(self, s: str) -> bool:
      stack = []

      for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            top = stack.pop() 
            if ((ch==")" and top!="(") or (ch=="}" and top!="{") or    
            (ch=="]" and top!="[") ):
                return False


      return True

a = Solution()
a.isValid("(]")