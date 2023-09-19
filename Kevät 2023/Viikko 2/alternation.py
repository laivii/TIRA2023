def count(t):
    n = len(t)
    laskuri = 0
    pituus = 0
    isompi = False
    pienempi = False

    for i in range(n):
        print(t[i-1], t[i])
        if i != 0 and t[i-1] < t[i]:  # jos pienempi
            isompi = False
            if pienempi != False:
                pituus = 1
            else:
                pienempi = True
            pituus += 1
        elif i != 0 and t[i-1] > t[i]: # jos isompi
            pienempi = False
            if isompi != False:
                pituus = 1
            else:
                isompi = True
            pituus += 1
        else:
            pituus = 1
        laskuri += pituus
        print("kohtaan", i, "päättyy", pituus, "osajonoa")
        
    return laskuri

if __name__ == "__main__":
    print(count([1, 3, 4, 2, 5])) # 12 (?)
    print(count([1,2,3,4])) # 7
    print(count([1,4,2,5,3])) # 15
    print(count([7,2,1,3,5,4,6])) # 17