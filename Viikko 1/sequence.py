def generate(n):
    indeksi = n
    lukujono = []
   
    for luku in range(10, 2500):
        str_luku = str(luku)
        luvut = {}
        määrä = 1
       
        for i in range(len(str_luku)):
            numero = str_luku[i]
            if str_luku[i] in luvut:
                määrä += 1
            else:
                luvut[numero] = 0

            if i == len(str_luku)-1 and määrä >= 2:
                lukujono.append(luku)

    print(lukujono[100])
               
    return lukujono[indeksi-1]
       

if __name__ == "__main__":
    print(generate(1)) # 11
    #print(generate(2)) # 22
    #print(generate(3)) # 33
    #print(generate(10)) # 100
    #print(generate(123)) # 505
    #print(generate(1000)) # 2425