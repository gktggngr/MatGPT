from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox as mb
import math
import random
işlemler = []
pencereler = []
lis = ["Tamam!", "Peki!", "Pekala!"]
lis2 = ["Hemen", "Hızlıca"]
lis3 = ["yapabiliriz!", "yapabilirim!"]
lis4 = ["hesaplayabiliriz!", "hesaplayabilirim!"]
lis5 = ["gir.", "girin.", "giriniz.", "girebilir misin?", "girebilir misiniz?"]
lis6 = ["hesaplarsak", "bulursak", "hesaplayacak olursak", "bulacak olursak"]
lis7 = ["sonucunu", "sonucuna"]
lis8 = ["buluruz.", "bulmuş oluruz."]
lis9 = ["ulaşırız.", "ulaşmış oluruz."]
pencere = Tk()
pgen = 200
pyuks = 200
ekrangen = pencere.winfo_screenwidth()
ekranyuks = pencere.winfo_screenheight()
x = (ekrangen - pgen) // 2
y = (ekranyuks - pyuks) // 2
pencere.geometry(f"{pgen}x{pyuks}+{x}+{y}")
pencere.title("MatGPT")
pencere.state("zoomed")
etiket = Label(text="Merhaba! Hangi işlemi yapmak istiyorsunuz?")
etiket.place(relx=0, rely=0)
etiket2 = Label(text="İşleminiz:")
etiket2.place(relx=0, rely=0.026)
def toplama():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 155
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Toplama")
    top = random.choice(lis)
    top2 = random.choice(lis2)
    top3 = random.choice(["bir toplama işlemi", "iki sayıyı", "iki sayının", "bir sayı ile bir sayıyı", "bir sayı ile başka bir sayıyı", "bir sayı ile bir başka sayıyı", "bir sayıyla bir sayıyı", "bir sayıyla başka bir sayıyı", "bir sayıyla bir başka sayıyı"])
    if top3 == "bir toplama işlemi":
        top4 = random.choice(lis3)
    elif top3 == "iki sayının":
        top5 = "toplamını"
        top4 = random.choice([f"{top5} hesaplayabiliriz!", f"{top5} hesaplayabilirim!", f"{top5} bulabiliriz!", f"{top5} bulabilirim!"])
    else:
        top4 = random.choice(["toplayabiliriz!", "toplayabilirim!"])
    top6 = random.choice(lis5)
    etiket2.config(text=f"{top} {top2} {top3} {top4} Lütfen sayıları {top6}")
    etiket3 = Label(pencere2, text="Birinci toplanan:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    etiket4 = Label(pencere2, text="İkinci toplanan:")
    etiket4.pack()
    entry2 = ttk.Entry(pencere2)
    entry2.pack()
    def gönder():
        try:
            if not entry.get() or not entry2.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
                    entry2.delete(0, END)
            else:
                a = float(entry.get())
                b = float(entry2.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                if isinstance(b, float):
                    if b.is_integer():
                        b = int(b)
                son = a + b
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"{a} + {b} = {son}")
                etiket5.config(text="\n".join(işlemler))
                top7 = random.choice(["sayısı ile", "sayısıyla"])
                top8 = random.choice(["sayısını", "sayısının"])
                if top8 == "sayısını":
                    top9 = random.choice(["toplarsak", "toplayacak olursak"])
                else:
                    top12 = "toplamını"
                    top9 = random.choice([f"{top12} hesaplarsak", f"{top12} hesaplayacak olursak", f"{top12} bulursak", f"{top12} bulacak olursak"])
                top10 = random.choice(lis7)
                if top10 == "sonucunu":
                    top11 = random.choice(lis8)
                else:
                    top11 = random.choice(lis9)
                mb.showinfo("Bilgi", f"{a} {top7} {b} {top8} {top9} {son} {top10} {top11}")
                etiket2.config(text=f"{a} {top7} {b} {top8} {top9} {son} {top10} {top11}")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
                entry2.delete(0, END)
    def temizle1():
        entry.delete(0, END)
        entry2.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def çıkarma():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 155
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Çıkarma")
    cık = random.choice(lis)
    cık2 = random.choice(lis2)
    cık3 = random.choice(["çıkarma işlemi", "sayıyı bir sayıdan", "sayıyı başka bir sayıdan", "sayıyı bir başka sayıdan"])
    if cık3 == "çıkarma işlemi":
        cık4 = random.choice(lis3)
    else:
        cık4 = random.choice(["çıkarabiliriz!", "çıkarabilirim!"])
    cık5 = random.choice(lis5)
    etiket2.config(text=f"{cık} {cık2} bir {cık3} {cık4} Lütfen sayıları {cık5}")
    etiket3 = Label(pencere2, text="Eksilen:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    etiket4 = Label(pencere2, text="Çıkan:")
    etiket4.pack()
    entry2 = ttk.Entry(pencere2)
    entry2.pack()
    def gönder():
        try:
            if not entry.get() or not entry2.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
                    entry2.delete(0, END)
            else:
                a = float(entry.get())
                b = float(entry2.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                if isinstance(b, float):
                    if b.is_integer():
                        b = int(b)
                    else:
                        entry.delete(0, END)
                        entry2.delete(0, END)
                son = a - b
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"{a} - {b} = {son}")
                etiket5.config(text="\n".join(işlemler))
                cık6 = random.choice(["çıkarırsak", "çıkaracak olursak"])
                cık7 = random.choice(lis7)
                if cık7 == "sonucunu":
                    cık8 = random.choice(lis8)
                else:
                    cık8 = random.choice(lis9)
                mb.showinfo("Bilgi", f"{a} sayısından {b} sayısını {cık6} {son} {cık7} {cık8}")
                etiket2.config(text=f"{a} sayısından {b} sayısını {cık6} {son} {cık7} {cık8}")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
                entry2.delete(0, END)
    def temizle1():
        entry.delete(0, END)
        entry2.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def çarpma():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 155
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Çarpma")
    car = random.choice(lis)
    car2 = random.choice(lis2)
    car3 = random.choice(["bir çarpma işlemi", "iki sayıyı", "bir sayı ile bir sayıyı", "bir sayı ile başka bir sayıyı", "bir sayı ile bir başka sayıyı", "bir sayıyla başka bir sayıyı", "bir sayıyla bir başka sayıyı"])
    if car3 == "bir çarpma işlemi":
        car4 = random.choice(lis3)
    else:
        car4 = random.choice(["çarpabiliriz!", "çarpabilirim!"])
    car5 = random.choice(lis5)
    etiket2.config(text=f"{car} {car2} {car3} {car4} Lütfen sayıları {car5}")
    etiket3 = Label(pencere2, text="Birinci çarpan:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    etiket4 = Label(pencere2, text="İkinci çarpan:")
    etiket4.pack()
    entry2 = ttk.Entry(pencere2)
    entry2.pack()
    def gönder():
        try:
            if not entry.get() or not entry2.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
                    entry2.delete(0, END)
            else:
                a = float(entry.get())
                b = float(entry2.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                if isinstance(b, float):
                    if b.is_integer():
                        b = int(b)
                son = a * b
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"{a} x {b} = {son}")
                etiket5.config(text="\n".join(işlemler))
                car6 = random.choice(["sayısı ile", "sayısıyla"])
                car7 = random.choice(["sayısını", "sayısının"])
                if car7 == "sayısını":
                    car8 = random.choice(["çarparsak", "çarpacak olursak"])
                else:
                    car9 = "çarpımını"
                    car8 = random.choice([f"{car9} hesaplarsak", f"{car9} hesaplayacak olursak", f"{car9} bulursak", f"{car9} bulacak olursak"])
                car10 = random.choice(lis7)
                if car10 == "sonucunu":
                    car11 = random.choice(lis8)
                else:
                    car11 = random.choice(lis9)
                mb.showinfo("Bilgi", f"{a} {car6} {b} {car7} {car8} {son} {car10} {car11}")
                etiket2.config(text=f"{a} {car6} {b} {car7} {car8} {son} {car10} {car11}")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
                entry2.delete(0, END)
    def temizle1():
        entry.delete(0, END)
        entry2.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def bölme():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 155
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Bölme")
    bol = random.choice(lis)
    bol2 = random.choice(lis2)
    bol3 = random.choice(["bölme işlemi", "sayıyı bir sayıya", "sayıyı başka bir sayıya", "sayıyı bir başka sayıya"])
    if bol3 == "bölme işlemi":
        bol4 = random.choice(lis3)
    else:
        bol4 = random.choice(["bölebiliriz!", "bölebilirim!"])
    bol5 = random.choice(lis5)
    etiket2.config(text=f"{bol} {bol2} bir {bol3} {bol4} Lütfen sayıları {bol5}")
    etiket3 = Label(pencere2, text="Bölünen:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    etiket4 = Label(pencere2, text="Bölen:")
    etiket4.pack()
    entry2 = ttk.Entry(pencere2)
    entry2.pack()
    def gönder():
        try:
            if not entry.get() or not entry2.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
                    entry2.delete(0, END)
            else:
                a = float(entry.get())
                b = float(entry2.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                if isinstance(b, float):
                    if b.is_integer():
                        b = int(b)
                son = a / b
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"{a} ÷ {b} = {son}")
                etiket5.config(text="\n".join(işlemler))
                bol6 = random.choice(["sayısını", "sayısının"])
                if bol6 == "sayısını":
                    bol7 = random.choice(["bölersek", "bölecek olursak"])
                else:
                    bol7 = random.choice(["bölümünü bulursak", "bölümünü bulacak olursak"])
                bol8 = random.choice(lis7)
                if bol8 == "sonucunu":
                    bol9 = random.choice(lis8)
                else:
                    bol9 = random.choice(lis9)
                mb.showinfo("Bilgi", f"{a} {bol6} {b} sayısına {bol7} {son} {bol8} {bol9}")
                etiket2.config(text=f"{a} {bol6} {b} sayısına {bol7} {son} {bol8} {bol9}")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
                entry2.delete(0, END)
    def temizle1():
        entry.delete(0, END)
        entry2.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def kare():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 115
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Kare")
    kar = random.choice(lis)
    kar2 = random.choice(lis2)
    kar3 = random.choice(["kare hesaplama işlemi", "kare hesaplaması", "sayının karesini"])
    if kar3 == "sayının karesini":
        kar4 = random.choice(lis4)
    else:
        kar4 = random.choice(lis3)
    kar5 = random.choice(lis5)
    etiket2.config(text=f"{kar} {kar2} bir {kar3} {kar4} Lütfen sayıyı {kar5}")
    etiket3 = Label(pencere2, text="Sayı:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    def gönder():
        try:
            if not entry.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
            else:
                a = float(entry.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                son = a ** 2
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"{a}² = {son}")
                etiket5.config(text="\n".join(işlemler))
                kar6 = random.choice(lis6)
                kar7 = random.choice(lis7)
                if kar7 == "sonucunu":
                    kar8 = random.choice(lis8)
                else:
                    kar8 = random.choice(lis9)
                mb.showinfo("Bilgi", f"{a} sayısının karesini {kar6} {son} {kar7} {kar8}")
                etiket2.config(text=f"{a} sayısının karesini {kar6} {son} {kar7} {kar8}")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
    def temizle1():
        entry.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def küp():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 115
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Küp")
    küp1 = random.choice(lis)
    küp2 = random.choice(lis2)
    küp3 = random.choice(["küp hesaplama işlemi", "küp hesaplaması", "sayının küpünü"])
    if küp3 == "sayının küpünü":
        küp4 = random.choice(lis4)
    else:
        küp4 = random.choice(lis3)
    küp5 = random.choice(lis5)
    etiket2.config(text=f"{küp1} {küp2} bir {küp3} {küp4} Lütfen sayıyı {küp5}")
    etiket3 = Label(pencere2, text="Sayı:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    def gönder():
        try:
            if not entry.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
            else:
                a = float(entry.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                son = a ** 3
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"{a}³ = {son}")
                etiket5.config(text="\n".join(işlemler))
                küp6 = random.choice(lis6)
                küp7 = random.choice(lis7)
                if küp7 == "sonucunu":
                    küp8 = random.choice(lis8)
                else:
                    küp8 = random.choice(lis9)
                mb.showinfo("Bilgi", f"{a} sayısının küpünü {küp6} {son} {küp7} {küp8}")
                etiket2.config(text=f"{a} sayısının küpünü {küp6} {son} {küp7} {küp8}")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
    def temizle1():
        entry.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def üslü():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 155
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Üslü İfadeler")
    üsl = random.choice(lis)
    üsl2 = random.choice(lis2)
    üsl3 = random.choice(["üslü ifade hesaplama işlemi", "üslü ifade hesaplaması", "sayının bir üsünü"])
    if üsl3 == "sayının bir üsünü":
        üsl4 = random.choice(lis4)
    else:
        üsl4 = random.choice(lis3)
    üsl5 = random.choice(lis5)
    etiket2.config(text=f"{üsl} {üsl2} bir {üsl3} {üsl4} Lütfen sayıları {üsl5}")
    etiket3 = Label(pencere2, text="Taban:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    etiket4 = Label(pencere2, text="Üs(kuvvet):")
    etiket4.pack()
    entry2 = ttk.Entry(pencere2)
    entry2.pack()
    def gönder():
        try:
            if not entry.get() or not entry2.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
                    entry2.delete(0, END)
            else:
                a = float(entry.get())
                b = float(entry2.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                if isinstance(b, float):
                    if b.is_integer():
                        b = int(b)
                son = a ** b
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"{a}^{b} = {son}")
                etiket5.config(text="\n".join(işlemler))
                üsl6 = random.choice(lis6)
                üsl7 = random.choice(lis7)
                if üsl7 == "sonucunu":
                    üsl8 = random.choice(lis8)
                else:
                    üsl8 = random.choice(lis9)
                mb.showinfo("Bilgi", f"{a} sayısının {b}. kuvvetini {üsl6} {son} {üsl7} {üsl8}")
                etiket2.config(text=f"{a} sayısının {b}. kuvvetini {üsl6} {son} {üsl7} {üsl8}")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
                entry2.delete(0, END)
    def temizle1():
        entry.delete(0, END)
        entry2.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def karekök():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 115
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Karekök")
    kark = random.choice(lis)
    kark2 = random.choice(lis2)
    kark3 = random.choice(["karekök hesaplama işlemi", "karekök hesaplaması", "sayının karekökünü"])
    if kark3 == "sayının karekökünü":
        kark4 = random.choice(lis4)
    else:
        kark4 = random.choice(lis3)
    kark5 = random.choice(lis5)
    etiket2.config(text=f"{kark} {kark2} bir {kark3} {kark4} Lütfen sayıyı {kark5}")
    etiket3 = Label(pencere2, text="Sayı:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    def gönder():
        try:
            if not entry.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
            else:
                a = float(entry.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                son = math.sqrt(a)
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"√{a} = {son}")
                etiket5.config(text="\n".join(işlemler))
                kark6 = random.choice(lis6)
                kark7 = random.choice(lis7)
                if kark7 == "sonucunu":
                    kark8 = random.choice(lis8)
                else:
                    kark8 = random.choice(lis9)
                mb.showinfo("Bilgi", f"{a} sayısının karekökünü {kark6} {son} {kark7} {kark8}")
                etiket2.config(text=f"{a} sayısının karekökünü {kark6} {son} {kark7} {kark8}")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
    def temizle1():
        entry.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def pi_x():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 115
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Pi ile Çarpma")
    pi = random.choice(lis)
    pi2 = random.choice(lis2)
    pi3 = random.choice(["pi ile çarpma işlemi", "sayıyı pi sayısı ile", "sayıyı pi sayısıyla", "sayıyı pi ile"])
    if pi3 == "pi ile çarpma işlemi":
        pi4 = random.choice(lis3)
    else:
        pi4 = random.choice(["çarpabiliriz!", "çarpabilirim!"])
    pi5 = random.choice(lis5)
    etiket2.config(text=f"{pi} {pi2} bir {pi3} {pi4} Lütfen sayıyı {pi5}")
    etiket3 = Label(pencere2, text="Sayı:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    def gönder():
        try:
            if not entry.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
            else:
                a = float(entry.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                if not entry.get():
                    cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                    etiket2.config(text="Hata! Lütfen bir sayı girin.")
                    if cevap == "cancel":
                        pencere2.destroy()
                    else:
                        entry.delete(0, END)
                son = math.pi * a
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"π({math.pi}) x {a} = {son}")
                etiket5.config(text="\n".join(işlemler))
                pi6 = random.choice(["sayısı ile", "sayısıyla", "sayısı ile çarpımını", "sayısıyla çarpımını", "ile çarpımını"])
                if pi6 == "sayısı ile" or pi6 == "sayısıyla":
                    pi7 = random.choice(["çarparsak", "çarpacak olursak"])
                else:
                    pi7 = random.choice(lis6)
                pi8 = random.choice(lis7)
                if pi8 == "sonucunu":
                    pi9 = random.choice(lis8)
                else:
                    pi9 = random.choice(lis9)
                mb.showinfo("Bilgi", f"{a} sayısını pi({math.pi}) {pi6} {pi7} {son} {pi8} {pi9}")
                etiket2.config(text=f"{a} sayısını pi({math.pi}) {pi6} {pi7} {son} {pi8} {pi9}")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
    def temizle1():
        entry.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def euler_x():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 115
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Euler ile Çarpma")
    eul = random.choice(lis)
    eul2 = random.choice(lis2)
    eul3 = random.choice(["euler ile çarpma işlemi", "sayıyı euler sayısı ile", "sayıyı euler sayısıyla", "sayıyı euler ile"])
    if eul3 == "euler ile çarpma işlemi":
        eul4 = random.choice(lis3)
    else:
        eul4 = random.choice(["çarpabiliriz!", "çarpabilirim!"])
    eul5 = random.choice(lis5)
    etiket2.config(text=f"{eul} {eul2} bir {eul3} {eul4} Lütfen sayıyı {eul5}")
    etiket3 = Label(pencere2, text="Sayı:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    def gönder():
        try:
            if not entry.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
            else:
                a = float(entry.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                son = math.e * a
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"e({math.e}) x {a} = {son}")
                etiket5.config(text="\n".join(işlemler))
                eul6 = random.choice(["sabiti ile", "sabitiyle", "sabitiyle çarpımını", "ile çarpımını"])
                if eul6 == "sabiti ile" or eul6 == "sabitiyle":
                    eul7 = random.choice(["çarparsak", "çarpacak olursak"])
                else:
                    eul7 = random.choice(lis6)
                eul8 = random.choice(lis7)
                if eul8 == "sonucunu":
                    eul9 = random.choice(lis8)
                else:
                    eul9 = random.choice(lis9)
                mb.showinfo("Bilgi", f"{a} sayısını euler({math.e}) {eul6} {eul7} {son} {eul8} {eul9}")
                etiket2.config(text=f"{a} sayısını euler({math.e}) {eul6} {eul7} {son} {eul8} {eul9}")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
    def temizle1():
        entry.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def logaritma():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 155
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Logaritma")
    log = random.choice(lis)
    log2 = random.choice(lis2)
    log3 = random.choice(["logaritma hesaplama işlemi", "logaritma hesaplaması", "sayının bir tabana göre logaritmasını"])
    if log3 == "sayının bir tabana göre logaritmasını":
        log4 = random.choice(lis4)
    else:
        log4 = random.choice(lis3)
    log5 = random.choice(lis5)
    etiket2.config(text=f"{log} {log2} bir {log3} {log4} Lütfen sayıyı {log5}")
    etiket3 = Label(pencere2, text="Sayı:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    etiket4 = Label(pencere2, text="Taban:")
    etiket4.pack()
    entry2 = ttk.Entry(pencere2)
    entry2.pack()
    def gönder():
        try:
            if not entry.get() or not entry2.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
                    entry2.delete(0, END)
            else:
                a = float(entry.get())
                b = float(entry2.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                if isinstance(b, float):
                    if b.is_integer():
                        b = int(b)
                son = math.log(a, b)
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"log {a}({b} tabanına göre) = {son}")
                etiket5.config(text="\n".join(işlemler))
                log6 = random.choice(["sayısına", "tabanına"])
                log7 = random.choice(lis6)
                log8 = random.choice(lis7)
                if log8 == "sonucunu":
                    log9 = random.choice(lis8)
                else:
                    log9 = random.choice(lis9)
                mb.showinfo("Bilgi", f"{a} sayısının {b} {log6} göre logaritmasını {log7} {son} {log8} {log9}")
                etiket2.config(text=f"{a} sayısının {b} {log6} göre logaritmasını {log7} {son} {log8} {log9}")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
                entry2.delete(0, END)
    def temizle1():
        entry.delete(0, END)
        entry2.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def kosinüs():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 115
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Kosinüs")
    cos = random.choice(lis)
    cos2 = random.choice(lis2)
    cos3 = random.choice(["kosinüs hesaplama işlemi", "bir kosinüs hesaplaması", "sayının kosinüsünü"])
    if cos3 == "sayının kosinüsünü":
        cos4 = random.choice(lis4)
    else:
        cos4 = random.choice(lis3)
    cos5 = random.choice(lis5)
    etiket2.config(text=f"{cos} {cos2} bir {cos3} {cos4} Lütfen sayıyı {cos5}")
    etiket3 = Label(pencere2, text="Sayı:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    def gönder():
        try:
            if not entry.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
            else:
                a = float(entry.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                son = math.cos(math.radians(a))
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"cos {a} = {son}")
                etiket5.config(text="\n".join(işlemler))
                cos6 = random.choice(lis6)
                cos7 = random.choice(lis7)
                if cos7 == "sonucunu":
                    cos8 = random.choice(lis8)
                else:
                    cos8 = random.choice(lis9)
                mb.showinfo("Bilgi", f"{a} sayısının kosinüsünü {cos6} {son} {cos7} {cos8}")
                etiket2.config(text=f"{a} sayısının kosinüsünü {cos6} {son} {cos7} {cos8}")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
    def temizle1():
        entry.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def sinüs():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 115
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Sinüs")
    sin = random.choice(lis)
    sin2 = random.choice(lis2)
    sin3 = random.choice(["sinüs hesaplama işlemi", "sinüs hesaplaması", "sayının sinüsünü"])
    if sin3 == "sayının sinüsünü":
        sin4 = random.choice(lis4)
    else:
        sin4 = random.choice(lis3)
    sin5 = random.choice(lis5)
    etiket2.config(text=f"{sin} {sin2} bir {sin3} {sin4} Lütfen sayıyı {lis5}")
    etiket3 = Label(pencere2, text="Sayı:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    def gönder():
        try:
            if not entry.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
            else:
                a = float(entry.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                son = math.sin(math.radians(a))
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"sin {a} = {son}")
                etiket5.config(text="\n".join(işlemler))
                sin6 = random.choice(lis6)
                sin7 = random.choice(lis7)
                if sin7 == "sonucunu":
                    sin8 = random.choice(lis8)
                else:
                    sin8 = random.choice(lis9)
                mb.showinfo("Bilgi", f"{a} sayısının sinüsünü {sin6} {son} {sin7} {sin8}")
                etiket2.config(text=f"{a} sayısının sinüsünü {sin6} {son} {sin7} {sin8}")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
    def temizle1():
        entry.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def tanjant():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 115
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Tanjant")
    tan = random.choice(lis)
    tan2 = random.choice(lis2)
    tan3 = random.choice(["tanjant hesaplama işlemi", "tanjant hesaplaması", "sayının tanjantını"])
    if tan3 == "sayının tanjantını":
        tan4 = random.choice(lis4)
    else:
        tan4 = random.choice(lis3)
    tan5 = random.choice(lis5)
    etiket2.config(text=f"{tan} {tan2} bir {tan3} {tan4} Lütfen sayıyı {tan5}")
    etiket3 = Label(pencere2, text="Sayı:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    def gönder():
        try:
            if not entry.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
            else:
                a = float(entry.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                son = math.tan(math.radians(a))
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"tan {a} = {son}")
                etiket5.config(text="\n".join(işlemler))
                tan6 = random.choice(lis6)
                tan7 = random.choice(lis7)
                if tan7 == "sonucunu":
                    tan8 = random.choice(lis8)
                else:
                    tan8 = random.choice(lis9)
                mb.showinfo("Bilgi", f"{a} sayısının tanjantını {tan6} {son} {tan7} {tan8}")
                etiket2.config(text=f"{a} sayısının tanjantını {tan6} {son} {tan7} {tan8}")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
    def temizle1():
        entry.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def radyan():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 115
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Radyan")
    rad = random.choice(lis)
    rad2 = random.choice(lis2)
    rad3 = random.choice(["radyan hesaplama işlemi", "radyan hesaplaması", "sayının radyanını"])
    if rad3 == "sayının radyanını":
        rad4 = random.choice(lis4)
    else:
        rad4 = random.choice(lis3)
    rad5 = random.choice(lis5)
    etiket2.config(text=f"{rad} {rad2} bir {rad3} {rad4} Lütfen sayıyı {rad5}")
    etiket3 = Label(pencere2, text="Sayı:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    def gönder():
        try:
            if not entry.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
            else:
                a = float(entry.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                son = math.radians(a)
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"rad {a} = {son}")
                etiket5.config(text="\n".join(işlemler))
                rad6 = random.choice(lis6)
                rad7 = random.choice(lis7)
                if rad7 == "sonucunu":
                    rad8 = random.choice(lis8)
                else:
                    rad8 = random.choice(lis9)
                mb.showinfo("Bilgi", f"{a} sayısının radyanını {rad6} {son} {rad7} {rad8}")
                etiket2.config(text=f"{a} sayısının radyanını {rad6} {son} {rad7} {rad8}")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
    def temizle1():
        entry.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def ar_top():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 155
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Ardışık Toplama")
    ard = random.choice(lis)
    ard2 = random.choice(lis2)
    ard3 = random.choice(["bir ardışık toplama işlemi", "ardışık sayıları toplama işlemi", "ardışık sayıları"])
    if ard3 == "ardışık sayıları":
        ard4 = random.choice(["toplayabiliriz!", "toplayabilirim!"])
    else:
        ard4 = random.choice(lis3)
    ard5 = random.choice(lis5)
    etiket2.config(text=f"{ard} {ard2} {ard3} {ard4} Lütfen sayıları {ard5}")
    etiket3 = Label(pencere2, text="Küçük sayı:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    etiket4 = Label(pencere2, text="Büyük sayı:")
    etiket4.pack()
    entry2 = ttk.Entry(pencere2)
    entry2.pack()
    def gönder():
        try:
            if not entry.get() or not entry2.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
                    entry2.delete(0, END)
            else:
                a = float(entry.get())
                b = float(entry2.get())
                if a > b:
                    cevap3 = mb.showerror("Hata!", "İlk sayı ikinci sayıdan küçük olmalı!", type=mb.RETRYCANCEL, parent=pencere2)
                    if cevap3 == "cancel":
                        pencere2.destroy()
                    else:
                        entry.delete(0, END)
                        entry2.delete(0, END)
                if a == b:
                    cevap4 = mb.showerror("Hata!", "Sayılar eşit olamaz!", type=mb.RETRYCANCEL, parent=pencere2)
                    if cevap4 == "cancel":
                        pencere2.destroy()
                    else:
                        entry.delete(0, END)
                        entry2.delete(0, END)
                else:
                    if isinstance(a, float):
                        if a.is_integer():
                            a = int(a)
                    if isinstance(b, float):
                        if b.is_integer():
                            b = int(b)
                    son = sum(range(a, b))
                    if isinstance(son, float):
                        if son.is_integer():
                            son = int(son)
                    işlemler.append(f"{a} ile {b} arası toplamı({a} dahil {b} hariç) = {son}")
                    etiket5.config(text="\n".join(işlemler))
                    ard6 = random.choice(["sayısı ile", "sayısıyla"])
                    ard7 = random.choice(["arasındaki", "aralarındaki"])
                    ard8 = random.choice(["sayıları", "sayıların"])
                    if ard8 == "sayıları":
                        ard9 = random.choice(["toplarsak", "toplayacak olursak", "toplamını bulursak", "toplamını bulursak olursak"])
                    else:
                        ard10 = "toplamını"
                        ard9 = random.choice([f"{ard10} hesaplarsak", f"{ard10} bulursak", f"{ard10} hesaplayacak olursak", f"{ard10} bulacak olursak"])
                    ard11 = random.choice(lis7)
                    if ard11 == "sonucunu":
                        ard12 = random.choice(lis8)
                    else:
                        ard12 = random.choice(lis9)
                    mb.showinfo("Bilgi", f"{a} {ard6} {b} sayısının {ard7} {ard8} {ard9}({a} dahil {b} hariç) {son} {ard11} {ard12}")
                    etiket2.config(text=f"{a} {ard6} {b} sayısının {ard7} {ard8} {ard9}({a} dahil {b} hariç) {son} {ard11} {ard12}")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
                entry2.delete(0, END)
    def temizle1():
        entry.delete(0, END)
        entry2.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def p_teoremi():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 80
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Pisagor Teoremi")
    pis = random.choice(lis)
    pis2 = random.choice(lis2)
    pis3 = random.choice(["Pisagor teoremi hesaplama işlemi", "Pisagor teoremi hesaplaması", "Pisagor teoremini"])
    if pis3 == "Pisagor teoremini":
        pis4 = random.choice(lis4)
    else:
        pis4 = random.choice(lis3)
    pis5 = random.choice(["seç.", "seçin.", "seçiniz.", "seçebilir misin?", "seçebilir misiniz?"])
    etiket2.config(text=f"{pis} {pis2} bir {pis3} {pis4} Lütfen bulunacak değeri {pis5}")
    def hipotenüs(): 
        pencere3 = Toplevel()
        pencereler.append(pencere3)
        pgen3 = 150
        pyuks3 = 155
        ekrangen3 = pencere3.winfo_screenwidth()
        ekranyuks3 = pencere3.winfo_screenheight()
        x3 = (ekrangen3 - pgen3) // 2
        y3 = (ekranyuks3 - pyuks3) // 2
        pencere3.geometry(f"{pgen3}x{pyuks3}+{x3}+{y3}")
        pencere3.title("Hipotenüs Bulma")
        hip = random.choice(lis)
        hip2 = random.choice(lis2)
        hip3 = random.choice(["bir hipotenüs bulma işlemi", "bir hipotenüs değeri bulma işlemi", "hipotenüsü bulmak için işlem", "hipotenüs değerini bulmak için işlem"])
        hip4 = random.choice(lis3)
        hip5 = random.choice(lis5)
        etiket2.config(text=f"{hip} {hip2} {hip3} {hip4} Lütfen sayıları {hip5}")
        etiket3 = Label(pencere3, text="Birinci dik kenar:")
        etiket3.pack()
        entry = ttk.Entry(pencere3)
        entry.pack()
        etiket4 = Label(pencere3, text="İkinci dik kenar:")
        etiket4.pack()
        entry2 = ttk.Entry(pencere3)
        entry2.pack()
        def gönder():
            try:
                if not entry.get() or not entry2.get():
                    cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                    etiket2.config(text="Hata! Lütfen bir sayı girin.")
                    if cevap == "cancel":
                        pencere3.destroy()
                    else:
                        entry.delete(0, END)
                        entry2.delete(0, END)
                else:
                    a = float(entry.get())
                    b = float(entry2.get())
                    if isinstance(a, float):
                        if a.is_integer():
                            a = int(a)
                    if isinstance(b, float):
                        if b.is_integer():
                            b = int(b)
                    son = math.sqrt(a ** 2 + b ** 2)
                    if isinstance(son, float):
                        if son.is_integer():
                            son = int(son)
                    işlemler.append(f"1. Dik kenar = {a}, 2. Dik kenar = {b}, Hipotenüs = {son}")
                    etiket5.config(text="\n".join(işlemler))
                    hip6 = random.choice(lis6)
                    hip7 = random.choice(lis7)
                    if hip7 == "sonucunu":
                        hip8 = random.choice(lis8)
                    else:
                        hip8 = random.choice(lis9)
                    mb.showinfo("Bilgi", f"Birinci dik kenarı {a}, ikinci dik kenarı {b} olan bir dik üçgende hipotenüsü {hip6} {son} {hip7} {hip8}")
                    etiket2.config(text=f"Birinci dik kenarı {a}, ikinci dik kenarı {b} olan bir dik üçgende hipotenüsü {hip6} {son} {hip7} {hip8}")
            except ValueError:
                cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere3)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap2 == "cancel":
                    pencere3.destroy()
                else:
                    entry.delete(0, END)
                    entry2.delete(0, END)
        def temizle1():
            entry.delete(0, END)
            entry2.delete(0, END)
        dgm20 = ttk.Button(pencere3, text="Temizle", command=temizle1)
        dgm20.pack(pady=5)
        dgm21 = ttk.Button(pencere3, text="Gönder", command=gönder)
        dgm21.pack()
    def dik_kenar():
        pencere3 = Toplevel()
        pencereler.append(pencere3)
        pgen3 = 150
        pyuks3 = 155
        ekrangen3 = pencere3.winfo_screenwidth()
        ekranyuks3 = pencere3.winfo_screenheight()
        x3 = (ekrangen3 - pgen3) // 2
        y3 = (ekranyuks3 - pyuks3) // 2
        pencere3.geometry(f"{pgen3}x{pyuks3}+{x3}+{y3}")
        pencere3.title("Dik Kenar Bulma")
        dik = random.choice(lis)
        dik2 = random.choice(lis2)
        dik3 = random.choice(["bir dik kenar bulma işlemi", "bir dik kenar değeri bulma işlemi", "dik kenarı bulmak için işlem", "dik kenar değerini bulmak için işlem"])
        dik4 = random.choice(lis3)
        dik5 = random.choice(lis5)
        etiket2.config(text=f"{dik} {dik2} {dik3} {dik4} Lütfen sayıları {dik5}")
        etiket3 = Label(pencere3, text="Dik kenar:")
        etiket3.pack()
        entry = ttk.Entry(pencere3)
        entry.pack()
        etiket4 = Label(pencere3, text="Hipotenüs:")
        etiket4.pack()
        entry2 = ttk.Entry(pencere3)
        entry2.pack()
        def gönder():
            try:
                if not entry.get() or not entry2.get():
                    cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                    etiket2.config(text="Hata! Lütfen bir sayı girin.")
                    if cevap == "cancel":
                        pencere3.destroy()
                    else:
                        entry.delete(0, END)
                        entry2.delete(0, END)
                else:
                    a = float(entry.get())
                    b = float(entry2.get())
                    if isinstance(a, float):
                        if a.is_integer():
                            a = int(a)
                    if isinstance(b, float):
                        if b.is_integer():
                            b = int(b)
                    son = math.sqrt(b ** 2 - a ** 2)
                    if isinstance(son, float):
                        if son.is_integer():
                            son = int(son)
                    işlemler.append(f"1. dik kenar = {a}, Hipotenüs = {b}, 2. dik kenar = {son}")
                    etiket5.config(text="\n".join(işlemler))
                    dik6 = random.choice(lis6)
                    dik7 = random.choice(lis7)
                    if dik7 == "sonucunu":
                        dik8 = random.choice(lis8)
                    else:
                        dik8 = random.randint(lis9)
                    mb.showinfo("Bilgi", f"Birinci dik kenarı {a}, hipotenüsü {b} olan bir dik üçgende ikinci dik kenarı {dik6} {son} {dik7} {dik8}")
                    etiket2.config(text=f"Birinci dik kenarı {a}, hipotenüsü {b} olan bir dik üçgende ikinci dik kenarı {dik6} {son} {dik7} {dik8}")
            except ValueError:
                cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere3)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap2 == "cancel":
                    pencere3.destroy()
                else:
                    entry.delete(0, END)
                    entry2.delete(0, END)
        def temizle1():
            entry.delete(0, END)
            entry2.delete(0, END)
        dgm20 = ttk.Button(pencere3, text="Temizle", command=temizle1)
        dgm20.pack(pady=5)
        dgm21 = ttk.Button(pencere3, text="Gönder", command=gönder)
        dgm21.pack()
    etiket3 = Label(pencere2, text="Bulunacak değer:")
    etiket3.pack()
    dgm26 = ttk.Button(pencere2, text="Dik kenar", command=dik_kenar)
    dgm26.pack()
    dgm27 = ttk.Button(pencere2, text="Hipotenüs", command=hipotenüs)
    dgm27.pack()
def ç_çevresi():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 115
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Çemberin Çevresi")
    cev = random.choice(lis)
    cev2 = random.choice(lis2)
    cev3 = random.choice(["çemberin çevresini", "çemberde çevre hesaplaması"])
    if cev3 == "çemberin çevresini":
        cev4 = random.choice(lis4)
    else:
        cev4 = random.choice(lis3)
    cev5 = random.choice(lis5)
    etiket2.config(text=f"{cev} {cev2} bir {cev3} {cev4} Lütfen sayıyı {cev5}")
    etiket3 = Label(pencere2, text="Yarıçap:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    def gönder():
        try:
            if not entry.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
            else:
                a = float(entry.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                son = 2 * math.pi * a
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"Yarıçap = {a}, Çevre = {son}")
                etiket5.config(text="\n".join(işlemler))
                cev6 = random.choice(["çemberin çevresini", "çemberde çevre hesaplaması"])
                if cev6 == "çemberin çevresini":
                    cev7 = random.choice(lis6)
                else:
                    cev7 = random.choice(["yaparsak", "yapacak olursak"])
                cev8 = random.choice(lis7)
                if cev8 == "sonucunu":
                    cev9 = random.choice(lis8)
                else:
                    cev9 = random.choice(lis9)
                mb.showinfo("Bilgi", f"Yarıçapı {a} olan bir {cev6} {cev7} {son} {cev8} {cev9}")
                etiket2.config(text=f"Yarıçapı {a} olan bir {cev6} {cev7} {son} {cev8} {cev9}")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
    def temizle1():
        entry.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def ç_alanı():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 115
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Çemberin Alanı")
    ala = random.choice(lis)
    ala2 = random.choice(lis2)
    ala3 = random.choice(["çemberin alanını", "çemberde alan hesaplaması"])
    if ala3 == "çemberin alanını":
        ala4 = random.choice(lis4)
    else:
        ala4 = random.choice(lis3)
    ala5 = random.choice(lis5)
    etiket2.config(text=f"{ala} {ala2} bir {ala3} {ala4} Lütfen sayıyı {ala5}")
    etiket3 = Label(pencere2, text="Yarıçap:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    def gönder():
        try:
            if not entry.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
            else:
                a = float(entry.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                son = math.pi * a ** 2
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"Yarıçap = {a}, Alan = {son}")
                etiket5.config(text="\n".join(işlemler))
                ala6 = random.choice(["çemberin alanını", "çemberde alan hesaplaması"])
                if ala6 == "çemberin çevresini":
                    ala7 = random.choice(lis6)
                else:
                    ala7 = random.choice(["yaparsak", "yapacak olursak"])
                ala8 = random.choice(lis7)
                if ala8 == "sonucunu":
                    ala9 = random.choice(lis8)
                else:
                    ala9 = random.choice(lis9)
                mb.showinfo("Bilgi", f"Yarıçapı {a} olan bir {ala6} {ala7} {son} {ala8} {ala9}")
                etiket2.config(text=f"Yarıçapı {a} olan bir {ala6} {ala7} {son} {ala8} {ala9}")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
    def temizle1():
        entry.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def faktöriyel():
    for pencere in pencereler:
        if pencere.winfo_exists():
            pencere.destroy()
    pencereler.clear()
    pencere2 = Toplevel()
    pencereler.append(pencere2)
    pgen2 = 150
    pyuks2 = 115
    ekrangen2 = pencere2.winfo_screenwidth()
    ekranyuks2 = pencere2.winfo_screenheight()
    x2 = (ekrangen2 - pgen2) // 2
    y2 = (ekranyuks2 - pyuks2) // 2
    pencere2.geometry(f"{pgen2}x{pyuks2}+{x2}+{y2}")
    pencere2.title("Faktöriyel")
    fak = random.choice(lis)
    fak2 = random.choice(lis2)
    fak3 = random.choice(["faktöriyel hesaplama işlemi", "faktöriyel hesaplaması", "sayının faktöriyelini"])
    if fak3 == "sayının faktöriyelini":
        fak4 = random.choice(lis4)
    else:
        fak4 = random.choice(lis3)
    fak5 = random.choice(lis5)
    etiket2.config(text=f"{fak} {fak2} bir {fak3} {fak4} Lütfen sayıyı {fak5}")
    etiket3 = Label(pencere2, text="Sayı:")
    etiket3.pack()
    entry = ttk.Entry(pencere2)
    entry.pack()
    def gönder():
        try:
            if not entry.get():
                cevap = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
                etiket2.config(text="Hata! Lütfen bir sayı girin.")
                if cevap == "cancel":
                    pencere2.destroy()
                else:
                    entry.delete(0, END)
            else:
                a = float(entry.get())
                if isinstance(a, float):
                    if a.is_integer():
                        a = int(a)
                son = math.factorial(a)
                if isinstance(son, float):
                    if son.is_integer():
                        son = int(son)
                işlemler.append(f"{a}! = {son}")
                etiket5.config(text="\n".join(işlemler))
                fak6 = random.choice(lis6)
                fak7 = random.choice(lis7)
                if fak7 == "sonucunu":
                    fak8 = random.choice(lis8)
                else:
                    fak8 = random.choice(lis9)
                mb.showinfo("Bilgi", f"{a} sayısının faktöriyelini {fak6} {son} {fak7} {fak8}")
                etiket2.config(text=f"{a} sayısının faktöriyelini {fak6} {son} {fak7} {fak8}")
        except ValueError:
            cevap2 = mb.showerror("Hata!", "Lütfen bir sayı girin!", type=mb.RETRYCANCEL, parent=pencere2)
            etiket2.config(text="Hata! Lütfen bir sayı girin.")
            if cevap2 == "cancel":
                pencere2.destroy()
            else:
                entry.delete(0, END)
    def temizle1():
        entry.delete(0, END)
    dgm20 = ttk.Button(pencere2, text="Temizle", command=temizle1)
    dgm20.pack(pady=5)
    dgm21 = ttk.Button(pencere2, text="Gönder", command=gönder)
    dgm21.pack()
def basit():
    dgm.config(text="Bilimsel", command=bilimsel)
    dgm6.place_forget()
    dgm7.place_forget()
    dgm8.place_forget()
    dgm9.place_forget()
    dgm10.place_forget()
    dgm11.place_forget()
    dgm12.place_forget()
    dgm13.place_forget()
    dgm14.place_forget()
    dgm15.place_forget()
    dgm16.place_forget()
    dgm17.place_forget()
    dgm22.place_forget()
    dgm23.place_forget()
    dgm24.place_forget()
    dgm25.place_forget()
def bilimsel():
    dgm.config(text="Basit", command=basit)
    dgm6.place(relx=0.797, rely=0.097)
    dgm7.place(relx=0.846, rely=0.097)
    dgm8.place(relx=0.895, rely=0.097)
    dgm9.place(relx=0.944, rely=0.097)
    dgm10.place(relx=0.797, rely=0.129)
    dgm11.place(relx=0.846, rely=0.129)
    dgm12.place(relx=0.895, rely=0.129)
    dgm13.place(relx=0.944, rely=0.129)
    dgm14.place(relx=0.797, rely=0.161)
    dgm15.place(relx=0.846, rely=0.161)
    dgm16.place(relx=0.895, rely=0.161)
    dgm17.place(relx=0.944, rely=0.161)
    dgm22.place(relx=0.797, rely=0.193)
    dgm23.place(relx=0.846, rely=0.193)
    dgm24.place(relx=0.895, rely=0.193)
    dgm25.place(relx=0.944, rely=0.193)
def göster():
    dgm18.config(text="Geçmişi gizle", command=gizle)
    etiket5.place(relx=0.026, rely=0.1)
    dgm19.place(relx=0.078, rely=0.0652)
def gizle():
    dgm18.config(text="Geçmişi göster", command=göster)
    etiket5.place_forget()
    dgm19.place_forget()
def temizle():
    global işlemler
    if not işlemler:
        mb.showerror("Hata!", "İşlem geçmişi zaten boş!")
    else:
        cevap = mb.askquestion("Soru", "İşlem geçmişini temizlemek istediğinize emin misiniz?")
        if cevap == "yes":
            işlemler.clear()
            etiket5.config(text="\n".join(işlemler))
def çıkış():
    cevap = mb.askquestion("Soru", "Programdan çıkmak istediğinze emin misiniz?")
    if cevap == "yes":
        pencere.destroy()
etiket5 = Label(text="\n".join(işlemler))
menü = Menu(pencere)
pencere.config(menu=menü)
menü1 = Menu(menü, tearoff=0)
menü.add_cascade(label="Çıkış", menu=menü1)
menü1.add_command(label="Çıkış", command=çıkış)
dgm = ttk.Button(text="Bilimsel", command=bilimsel)
dgm.place(relx=0.871, rely=0.032)
dgm2 = ttk.Button(text="Toplama", command=toplama)
dgm2.place(relx=0.797, rely=0.065)
dgm3 = ttk.Button(text="Çıkarma", command=çıkarma)
dgm3.place(relx=0.846, rely=0.065)
dgm4 = ttk.Button(text="Çarpma", command=çarpma)
dgm4.place(relx=0.895, rely=0.065)
dgm5 = ttk.Button(text="Bölme", command=bölme)
dgm5.place(relx=0.944, rely=0.065)
dgm6 = ttk.Button(text="Kare", command=kare)
dgm7 = ttk.Button(text="Küp", command=küp)
dgm8 = ttk.Button(text="Üslü", command=üslü)
dgm9 = ttk.Button(text="Karekök", command=karekök)
dgm10 = ttk.Button(text="Pi x", command=pi_x)
dgm11 = ttk.Button(text="Euler x", command=euler_x)
dgm12 = ttk.Button(text="log", command=logaritma)
dgm13 = ttk.Button(text="cos", command=kosinüs)
dgm14 = ttk.Button(text="sin", command=sinüs)
dgm15 = ttk.Button(text="tan", command=tanjant)
dgm16 = ttk.Button(text="rad", command=radyan)
dgm17 = ttk.Button(text="Ar. Top", command=ar_top)
dgm22 = ttk.Button(text="Ç. Çevresi", command=ç_çevresi)
dgm23 = ttk.Button(text="Ç. Alanı", command=ç_alanı)
dgm24 = ttk.Button(text="P. Teoremi", command=p_teoremi)
dgm25 = ttk.Button(text="Faktöriyel", command=faktöriyel)
dgm18 = ttk.Button(text="Geçmişi göster", command=göster)
dgm18.place(relx=0.026, rely=0.0652)
dgm19 = ttk.Button(text="Geçmişi temizle", command=temizle)
pencere.mainloop()