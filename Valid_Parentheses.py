class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        top=-1
        for i in s:
            if i == "[" or i == "(" or i == "{":
                stack.append(i)
                top +=1
            elif (i in [")","}","]"] ) and top==-1 :
                return False  
            elif i == "]":
                if stack[top] == "[":
                    stack.pop()
                    top-=1
                else:
                    return False        
            elif i == ")":
                if stack[top] == "(":
                    stack.pop()
                    top-=1
                else:
                    return False
            elif i == "}":
                if stack[top] == "{":
                    stack.pop()
                    top-=1
                else:
                    return False           
        if len(stack)==0: 
            return True 
