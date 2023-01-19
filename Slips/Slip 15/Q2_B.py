def Mystring():
    Str=input("Enter any String: ")
    cnt=len(Str)
    newString=""
    for i in range(0,cnt):
        if 1%2 ==0:
            newString=newString + Str[i]

        print("New String with removed odd Index Character: ".newString)

Mystring()