def count(s, c):
    n = len(s)
    osajonot = 0

    s = s.replace(c, ' ')
    s = s.split(' ')

    for i in range(len(s)):
        määrä = len(s[i])
        osajonot += määrä * (määrä +1) // 2

    return osajonot

if __name__ == "__main__":
    print(count("abacabb", "b")) # 7
    print(count("abcdef", "g")) # 21
    print(count("xxxxxxxxx", "x")) # 0
    print(count("pupujussikainen", "u")) # 48
