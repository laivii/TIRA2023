def encrypt(s):
    letters = "abcdefghijklmnopqrstuvwxyz"
    new_str = ""

    for i in range(len(s)):
        letter = letters.index(s[i])
        index = letter+i+1

        if index >= len(letters) or len(s)>len(letters):
            letters += letters
        
        new_str += letters[index]

    return new_str

if __name__ == "__main__":
    print(encrypt("abc")) # bdf
    print(encrypt("xz")) # yb
    print(encrypt("kkkkkkkk")) # lmnopqrs
    print(encrypt("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")) # bcdefghijklmnopqrstuvwxyzabcde