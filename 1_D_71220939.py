print("\(^o^) selamat datang di kalkulator sederhana(^o^)/")
print("ketik 1 untuk menghitung penjumlahan")
print("ketik 2 untuk menghitung pengurangan")
print("ketik 3 untuk menghitung perkalian")
print("ketik 4 untuk menghitung pembagian")
print("ketik 5 untuk menghitung modulus")
print("ketik 6 untuk menghitung pemangkatan")



name=int(input("masukan pilihan anda:"))





if(name==1):
    a=int(input("bilangan pertama"))
    b=int(input("bilangan kedua"))
    print(a+b)

if(name==2):
    a=int(input("bilangan pertama"))
    b=int(input("bilangan kedua"))
    print(a-b)

if(name==3):
    a=int(input("bilangan pertama"))
    b=int(input("bilangan kedua"))
    print(a*b)

if(name==4):
    a=int(input("bilangan pertama"))
    b=int(input("bilangan kedua"))
    print(a/b)

if(name==6):
    a=int(input("bilangan pertama"))
    b=int(input("bilangan kedua"))
    print(a**b)

