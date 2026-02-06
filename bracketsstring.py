
def isValid( s):
        stack = []
        
        for i in s:
            if s[0] == "]" or s[0] == ")" or s[0] == "}":
                return False
            if i == "(" or i =="{" or i == "[":
                stack.append(i)
            if not stack: 
                return False
            
            if i == "]" and stack[-1] != "[":
                return False
            if i == "}" and stack[-1] != "{":
                return False
            if i == ")" and stack[-1] != "(":
                return False
            
            if i == "}" and stack[-1] == "{":
                stack.pop()
            if i == "]" and stack[-1] == "[":
                stack.pop()
            if i == ")" and stack[-1] == "(":
                stack.pop()
            
            

            print(stack)
        if not stack:
            return True
        return False

print(isValid("[(){}]"))
            

        