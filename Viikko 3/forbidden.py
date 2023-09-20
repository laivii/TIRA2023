def count(s):
    merkkijono = s
    pituus = len(merkkijono)
    osajonot = 0
    peräkkäin = 0
    kolmioluku = 0

    for i in range(pituus):
        if merkkijono[i] == "a":
            osajonot += kolmioluku
            peräkkäin = 0
            kolmioluku = 0
        else:
            peräkkäin += 1
            kolmioluku = (peräkkäin*(peräkkäin+1))//2
    
    osajonot += kolmioluku
    return osajonot

if __name__ == "__main__":
    print(count("aybabtu")) # 9
    print(count("aaa")) # 0
    print(count("saippuakauppias")) # 23
    print(count("x")) # 1