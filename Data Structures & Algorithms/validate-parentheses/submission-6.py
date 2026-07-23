class Solution:
    def isValid(self, s: str) -> bool:
        # The stack method:
        stack = deque([])
        if len(s)%2 != 0:
            return False
        
        for ch in s:
            if ch == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                    continue
                else:
                    return False
            if ch == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                    continue
                else:
                    return False
            if ch == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(ch)
        return True if not stack else False

        