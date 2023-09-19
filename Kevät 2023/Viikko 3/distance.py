def find(t, k):    
    jono = sorted(t)
    jono = list(dict.fromkeys(jono))
    n = len(jono)
    suurin = 0
    arvot = []

    for i in range(1, n):
        etäisyys = jono[i]-jono[i-1]
        if etäisyys > suurin:
            suurin = etäisyys
            if len(arvot) == 0:
                arvot.append([jono[i-1], jono[i]])
            else:
                arvot = []
                arvot.append([jono[i-1], jono[i]])
                
    if 1 not in jono:
        if suurin//2 < jono[0]-1: 
            suurin = (jono[0]-1)*2
        
    if k not in jono:
        if suurin//2 < k-jono[-1]:
            suurin = (k-jono[-1])*2
           
    return suurin // 2
    
if __name__ == "__main__":
    print(find([2], 15)) # 13
    print(find([15, 9, 12, 6, 10], 15)) # 5
    print(find([1, 2, 9], 11)) # 3
    print(find([2, 1, 3], 3)) # 0
    print(find([7, 4, 10, 4], 10)) # 3
    print(find([15, 2, 6, 4, 18], 20)) # 4
    print(find([41222388, 392676742, 307110407, 775934683, 25076911], 809136843)) # 191628970
    print(find([7, 12, 4], 15)) # 3