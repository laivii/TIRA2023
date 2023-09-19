def find(s):
    n = len(s)
    merkit = 0
    osajono = True
    
    for i in range(n):
        if i != 0:
            if s[0:i]*s.count(s[0:i]) == s:
                merkit += len(s[0:i])
                osajono = True
                break
            else:
                osajono = False
        else:
            if n == 1:
                merkit = 1

    if osajono == False:
        merkit = n
            
    return merkit 

if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7