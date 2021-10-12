import tkinter as tk
from tkinter import filedialog
from  tkinter import messagebox
from PIL import Image
import os
import shutil
from PIL import Image
import sys

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 250, bg = 'azure3', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Sıkıştırma Uygulaması', bg = 'azure3')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

def getPNG ():
    src = filedialog.askdirectory(mustexist=True)
    if not messagebox.askokcancel(title=None, message="Klasörü doğru seçtiğinden emin misin?"):
        sys.exit()
    yeni_klasor = "pressed"
    os.mkdir(yeni_klasor)
    dizin = os.getcwd()
    dest = os.getcwd()+os.sep+yeni_klasor+os.sep+src.split("/")[-1]
    shutil.copytree(src, dest)
    klasorler_hepsi = [k for k in os.walk(yeni_klasor)]
    for klasorler in klasorler_hepsi:
        os.chdir(dizin+os.sep+klasorler[0]) 
        if len(klasorler[2])==0:
            continue   
        for i in klasorler[2]:
            if i.endswith(".jpg"):
                img = Image.open(i)
                img.save(i,
                optimize=True,
                quality=80)

    sys.exit()


    
    
browseButton_PNG = tk.Button(text=" CMS'ten indirilen dosyayı seç ", command=getPNG, bg='royalblue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_PNG)

root.mainloop()
