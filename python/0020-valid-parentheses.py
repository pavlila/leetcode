# stack brute force O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        timezone = []
        
        for i in s:
            if i in ('(', '[', '{'):
                timezone.append(i)
            else:
                if i == ')':
                    if timezone and timezone[-1] == '(':
                        timezone.pop()
                    else:
                        return False
                elif i == ']':
                    if timezone and timezone[-1] == '[':
                        timezone.pop()
                    else:
                        return False
                else:
                    if timezone and timezone[-1] == '{':
                        timezone.pop()
                    else:
                        return False

        if len(timezone) != 0:
            return False
        else:
            return True