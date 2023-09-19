def count(s):
    n = len(s)
    laskuri = 0
    pituus = 0

    for i in range(n):
        if i != 0 and s[i-1] == s[i]:
            pituus += 1
        else:
            pituus = 1

        laskuri += pituus
        
    return laskuri

if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5