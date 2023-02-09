from tkinter import *
from PIL import Image, ImageTk
from googletrans import Translator, LANGUAGES
from tkinter import ttk



w=Tk()
w.title('LANGUAGE TRANSLATOR')
w.geometry('1080x400')
w.resizable(0, 0)
w.config(bg='ghost white')
name1 = Label(w, text='TRANSLATOR', font=('Times New Roman', 30, 'bold'), fg='red', bg='yellow', bd=0).pack(side=TOP, fill=X)
name2 = Label(w, text='Phong Dang Thanh', font=('Times New Roman', 20, 'bold'), bg='green', width=20).pack(side=BOTTOM, fill=X)
name3 = Label(w, text='Text - Input', font=('Times New Roman', 13, 'bold'), bg='white smoke').place(x=200, y=60)
name4 = Label(w, text='Text - Output', font=('Times New Roman', 13, 'bold'), bg='white smoke').place(x=780, y=60)

Text_Input = Text(w, font=('Times New Roman',10), height=11, width=60, wrap=WORD, padx=5, pady=5).place(x=30, y=100)
Text_Output = Text(w, font=('Times New Roman',10), height=11, width=60, wrap=WORD, padx=5, pady=5).place(x=600, y=100)

language = list(LANGUAGES.values())

src_lang = ttk.Combobox(w, values = language, width=22)
src_lang.place(x=20, y=60)
src_lang.set('Chọn ngôn ngữ đầu vào')


dest_lang = ttk.Combobox(w, values=language, width=22)
dest_lang.place(x=890, y=60)
dest_lang.set('Chọn ngôn ngữ đầu ra')

def Translate() :
    translator = Translator()
    translated = translator.translate(text=Text_Input.get(1.0, END), src =src_lang.get(), dest =dest_lang.get())
    Text_Output.delete(1.0, END)
    Text_Output.insert(END, translated.text)

trans_btn = Button(w, text='Dịch', font=('Times New Roman', 16, 'bold'), bg='royal blue1', activebackground='sky blue', pady=5, command=Translate)
trans_btn.place(x=475, y=180)









w.mainloop()