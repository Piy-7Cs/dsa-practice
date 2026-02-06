
def longestCommonPrefix(strs):
    
    res = []

    minlength = len(strs[0])

    for s in strs:
        minlength = min(minlength, len(s))

    print(minlength)

    for i in range(minlength):

        char = strs[0][i]

        for s in strs:
            if s[i] != char:
                return "".join(res)
        
        res.append(char)

    return "".join(res)

    

if __name__ == "__main__":
    arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
    print(longestCommonPrefix(arr))