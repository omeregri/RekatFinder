__author__ = "omeregri"
import os
import time
while True:
    print("Namaz Rekatları")
    print("Sabah Namazı(1)")
    print("Öğle Namazı(2)")
    print("İkindi Namazı(3)")
    print("Akşam Namazı(4)")
    print("Yatsı Namazı(5)")
    print("Ek namazlar için (6) \n")

    vakit_secimi = int(input("Hangi namazın rekat sayısını öğrenmek istersiniz, 1'den 6'ya kadar yazabilirsiniz:"))
    if vakit_secimi == 1:
        print("\n2 Rekat sünnet, 2 Rekat farz \n")
        time.sleep(3)
        os.system("cls")
    elif vakit_secimi == 2:
        print("\n4 Rekat Sünnet, 4 Rekat Farz, 2 Rekat Son Sünnet \n")
        time.sleep(3)
        os.system("cls")
    elif vakit_secimi == 3:
        print("\n4 Rekat Sünnet, 4 Rekat Farz \n")
        time.sleep(3)
        os.system("cls")
    elif vakit_secimi == 4:
        print("\n3 Rekat Farz, 2 Rekat Sünnet \n")
        time.sleep(3)
        os.system("cls")
    elif vakit_secimi == 5:
        print("\n4 Rekat Sünnet, 4 Rekat Farz, 2 Rekat Son Sünnet, 3 Rekat Vitir \n")
        time.sleep(3)
        os.system("cls")
    elif vakit_secimi == 6:
        print("\nBayram Namazı: 2 Rekat")
        print("Teravih Namazı: Genellikle 20 Rekat \n")
        time.sleep(3)
        os.system("cls")
    else:
        print("Geçersiz Giriş, Program Sonlandırılıyor...")
        break
