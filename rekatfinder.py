from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title('RekatFinder+')
root.geometry('400x200')
root.maxsize(400,200)
root.minsize(400,200)

def rekatsayi():
    rekat_girisi = rekat_giris.get()

    if rekat_girisi == "1":
        rekat_yazi_2.configure(text="2 Rekat sünnet, 2 Rekat farz")
    elif rekat_girisi == "2":
        rekat_yazi_2.configure(text="4 Rekat Sünnet, 4 Rekat Farz, 2 Rekat Son Sünnet")
    elif rekat_girisi == "3":
        rekat_yazi_2.configure(text="4 Rekat Sünnet, 4 Rekat Farz")
    elif rekat_girisi == "4":
        rekat_yazi_2.configure(text="3 Rekat Farz, 2 Rekat Sünnet")
    elif rekat_girisi == "5":
        rekat_yazi_2.configure(text="4 Rekat Sünnet, 4 Rekat Farz, 2 Rekat Son Sünnet, 3 Rekat Vitir")
    else:
        rekat_yazi_2.configure(text="Lütfen geçerli bir değer giriniz")

baslik = tk.Label(root, text="RekatFinder+", fg="black", font=('verdana', 10, 'bold')).place(x=120, y=5)

rekat_soru_yazi_2 = tk.Label(root, text="""
Hangi Vakit?:
Sabah Namazı: 1
Öğle Namazı: 2
İkindi Namazı: 3
Akşam Namazı: 4
Yatsı Namazı: 5
""", font = ('verdana', 10, 'bold')).place(x = 6, y = 30)


rekat_giris = tk.Entry(root, text = "Öğrenmek İstediğiniz Vakit")
rekat_giris.place(x=180, y=60, height=80)
rekat_yazi = tk.Label(root, text = "Rekat Sayısı:")
rekat_yazi.place(x = 40, y = 170)
rekat_yazi_2 = tk.Label(root, text = "")
rekat_yazi_2.place(x = 120, y = 170)
rekat_getir  = tk.Button(root, text = "Bul", command=rekatsayi).place(x = 180, y = 140, width=125)

root.mainloop()
