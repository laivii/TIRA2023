def count(s):
    bittijono = s
    ykköset = 0
    nollat = 0
    tavat = 0

    for i in range(len(bittijono)):
        if bittijono[i] == "1":
            ykköset += 1
        else:
            nollat += 1

    kertoma_k = 2
    kertoma_ykköset = 1
    kertoma_nollat = 1
    kertoma_erotus1 = 1
    kertoma_erotus2 = 1

    if ykköset != 0:
        for i in range(2, ykköset+1):
            kertoma_ykköset = kertoma_ykköset * i
        
        erotus = ykköset - kertoma_k
        for i in range(2, erotus+1):
            kertoma_erotus1 = kertoma_erotus1 * i

        kombinaatiot_ykkösillä = kertoma_ykköset // (kertoma_k * kertoma_erotus1)
    
    if nollat != 0:
        for i in range(2, nollat+1):
            kertoma_nollat = kertoma_nollat * i
        
        erotus = nollat - kertoma_k
        for i in range(2, erotus+1):
            kertoma_erotus2 = kertoma_erotus2 * i

        kombinaatiot_nollilla = kertoma_nollat // (kertoma_k * kertoma_erotus2)

    if nollat != 0 and ykköset != 0:
        tavat = kombinaatiot_ykkösillä + kombinaatiot_nollilla
        return tavat
    elif nollat != 0 and ykköset == 0:
        return kombinaatiot_nollilla
    elif nollat == 0 and ykköset != 0:
        return kombinaatiot_ykkösillä

if __name__ == "__main__":
    print(count("0101")) # 2
    print(count("000000")) # 15
    print(count("000111")) # 6
    print(count("00100001101100")) # 46