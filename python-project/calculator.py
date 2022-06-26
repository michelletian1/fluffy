#memanggil isi semua library dari tkinter/form
from tkinter import *
root = Tk()
root.title("Kalkulator")

#rumus tombol tambah
def tambah():
    nilaibil1=float(bil1.get())
    nilaibil2=float(bil2.get())
    nilaihasil.set(nilaibil1+nilaibil2)

#rumus tombol kurang
def kurang():
    nilaibil1=float(bil1.get())
    nilaibil2=float(bil2.get())
    nilaihasil.set(nilaibil1-nilaibil2)

#rumus tombol kali
def kali():
    nilaibil1=float(bil1.get())
    nilaibil2=float(bil2.get())
    nilaihasil.set(nilaibil1*nilaibil2)

#rumus tombol bagi
def bagi():
    nilaibil1=float(bil1.get())
    nilaibil2=float(bil2.get())
    nilaihasil.set(nilaibil1/nilaibil2)

#rumus tombol pangkat
def pangkat():
    nilaibil1=float(bil1.get())
    nilaibil2=float(bil2.get())
    nilaihasil.set(nilaibil1**nilaibil2)

#rumus tombol keluar
def keluar():
    exit()

#menangkap input dari form
bil1= Entry(root)
bil2= Entry(root)

#mengirim output ke form
nilaihasil= StringVar()
hasil= Entry(root, textvariable=nilaihasil)

#memberi nama label
teksbil1= Label(root, text="Masukkan Bilangan Pertama")
teksbil2= Label(root, text="Masukkan Bilangan Kedua")
tekshasil=Label(root, text="Hasil")

#memanggil rumus dari tombol
hitung= Button(root, text="+", command=tambah)
hitungkurang= Button(root, text="-", command=kurang)
hitungkali= Button(root, text="x", command=kali)
hitungbagi= Button(root, text=":", command=bagi)
hitungpangkat= Button(root, text="^", command=pangkat)
keluar= Button(root, text="Keluar", command=keluar)

#mengatur posisi kata
bil1.grid(row=1, column=2)
bil2.grid(row=2, column=2)
hasil.grid(row=3, column=2)

#mengatur posisi tombol
hitung.grid(row=1, column=3)
hitungkurang.grid(row=1, column=4)
hitungkali.grid(row=1, column=5)
hitungbagi.grid(row=2, column=3)
hitungpangkat.grid(row=2, column=4)
keluar.grid(row=3, column=4)

#mengatur posisi dari form
teksbil1.grid(row=1, column=1)
teksbil2.grid(row=2, column=1)
tekshasil.grid(row=3, column=1)

#munculin app
root = mainloop()
