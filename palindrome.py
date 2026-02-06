
def isPalindrome(x: int) -> bool:
    if x < 0: return False
    num = x
    rev = 0 
    while x > 0:
        last_digit = x%10
        rev = (rev*10) + last_digit
        x = x//10
    if rev == num:
        return True
    else:
        return False
    
print(isPalindrome(17701))      