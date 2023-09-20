def count(s):
    merkkijono = s
    osajonot = 0
    peräkkäin = 0
    kolmioluku = 0

    for i in range(len(merkkijono)):
        if merkkijono[i] != merkkijono[i-1]:
            osajonot += kolmioluku
            peräkkäin = 0
            kolmioluku = 0
        
        peräkkäin += 1
        kolmioluku = (peräkkäin*(peräkkäin+1))//2
    
    osajonot += kolmioluku
    return osajonot
            
if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abc")) # 3
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5
    print(count("aaaaa")) # 15