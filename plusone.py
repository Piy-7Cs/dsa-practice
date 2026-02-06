#Leetcode 66, 
#Time Complexity O(n)


digits = [0, 0]

last_index = len(digits)-1


if digits[-1] == 9:
    for i in range(last_index, -1, -1):
        if digits[i] == 9:
            digits[i] = 0

        if digits[i] != 0 and digits[i+1] == 0:
            digits[i] += 1
            break
        
        if digits[0] == 0:
            digits.insert(0, 1)

elif digits[-1] != 9:
    digits[-1]+=1



print(digits)