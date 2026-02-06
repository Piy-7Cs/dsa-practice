
def lastlen(string):

    count = 0
    
    for i in range(len(string)-1, -1, -1):
        
        if count == 0 and string[i] == " ":
            continue

        
        if string[i]== " ":
            return count
        
        count +=1 
    return count

string = "a"

print(lastlen(string))