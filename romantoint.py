
def roman(s: str):
    map = {
        "I" :1,
        "V" :5,
        "X" :10,
        "L" :50,
        "C" :100,
        "D" :500,
        "M" :1000
    }
    num = 0
    
    if len(s) == 1:
            num += map.get(s)

    for i in range(0, len(s)-1):
        print(num)
        
        if map.get(s[i]) <= map.get(s[i+1]):
            num -= map.get(s[i])
        else: 
            num += map.get(s[i])

        if i == len(s)-2:
            num += map.get(s[i+1])

    return num




print(roman("D"))