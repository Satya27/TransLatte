'''
----------------------------------------------
TransLatte Versi 1.0 | 20/05/2020
instagram @satya.pdf
source : python 3.6
----------------------------------------------
'''


import tkinter as tk
from tkinter.commondialog import Dialog as dl
import keyboard
import pyperclip
from googletrans import Translator
import time
import urllib.request

translator = Translator()
judul = "TransLatte v1 | @satya.pdf"
lng ="id"



class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("315x75")
        #self.iconbitmap('icon.ico')
        self.title(judul)
        self.resizable(0,0)
        self.editor = tk.Text(self)
        self.editor.pack()
        self.lift()
        self.attributes('-topmost',True)
        self.editor.config(font="Courier 12")
        self.editor.focus_set()
        

        # keyboard.add_hotkey('ctrl+c', self.cekinet)
        keyboard.add_hotkey('ctrl+c', self.show)
        keyboard.add_hotkey('ctrl+c', self.paste)
        keyboard.add_hotkey('alt+a', self.hide)
        #------Ubah Terjemahan---------------------------
        keyboard.add_hotkey('alt+1', self.indonesia)
        keyboard.add_hotkey('alt+2', self.english)
        keyboard.add_hotkey('alt+3', self.france)
        # keyboard.add_hotkey('4', self.korean)
        # keyboard.add_hotkey('5', self.japan)
        # keyboard.add_hotkey('6', self.arabian)
        keyboard.add_hotkey('alt+4', self.german)
        keyboard.add_hotkey('alt+5', self.spanish)
        keyboard.add_hotkey('alt+6', self.italian)

        #------------------------------------------------
    

    def indonesia(self):
        self.editor.delete("1.0", "end")
        global lng
        lng="id"
        self.editor.insert(tk.END,"Ubah terjemahan ke Indonesia")
        self.update()
        self.deiconify()
    
    def english(self):
        self.editor.delete("1.0", "end")
        global lng
        lng="en"
        self.editor.insert(tk.END,"Ubah terjemahan ke English")
        self.update()
        self.deiconify()
    
    def france(self):
        self.editor.delete("1.0", "end")
        global lng
        lng="fr"
        self.editor.insert(tk.END,"Ubah terjemahan ke France")
        self.update()
        self.deiconify()
    
    # def korean(self):
    #     self.editor.delete("1.0", "end")
    #     global lng
    #     lng="ko"
    #     self.editor.insert(tk.END,"Ubah terjemahan ke Korean")
    #     self.update()
    #     self.deiconify()

    # def japan(self):
    #     self.editor.delete("1.0", "end")
    #     global lng
    #     lng="jp"
    #     self.editor.insert(tk.END,"Ubah terjemahan ke Japan")
    #     self.update()
    #     self.deiconify()

    # def arabian(self):
    #     self.editor.delete("1.0", "end")
    #     global lng
    #     lng="ar"
    #     self.editor.insert(tk.END,"Ubah terjemahan ke Arabian")
    #     self.update()
    #     self.deiconify()
    
    def german(self):
        self.editor.delete("1.0", "end")
        global lng
        lng="de"
        self.editor.insert(tk.END,"Ubah terjemahan ke German")
        self.update()
        self.deiconify()

    def spanish(self):
        self.editor.delete("1.0", "end")
        global lng
        lng="es"
        self.editor.insert(tk.END,"Ubah terjemahan ke Spanish")
        self.update()
        self.deiconify()
    
    def italian(self):
        self.editor.delete("1.0", "end")
        global lng
        lng="it"
        self.editor.insert(tk.END,"Ubah terjemahan ke italian")
        self.update()
        self.deiconify()


    def show(self):
        self.update()
        self.deiconify()
        

    def hide(self):
        self.update()
        self.withdraw()

    def paste(self):
        self.editor.delete("1.0", "end")
        time.sleep(0.5)
        x=pyperclip.paste()
        try:
            y=translator.translate(x, dest=lng)
            result=y.text
            self.editor.insert(tk.END,result)
        except:
            self.editor.insert(tk.END,"Tidak ada akses internet")

        

if __name__ == "__main__":
    App().mainloop()