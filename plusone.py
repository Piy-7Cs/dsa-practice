digits = [9, 9, 9, 9, 9, 9, 9]

for i in range(len(digits)-1 , 0 , -1):
    if digits[i] == 9:
        digits[i] = 0
        if digits[i-1] != 9 :
            digits[i-1] = digits[i-1]+ 1
        

print(digits)


    