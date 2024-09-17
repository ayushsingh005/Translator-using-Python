from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES


def change(text="type",src="English",dest="Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text
def data():
    s = comb_su.get()
    d = comb_dest.get()
    mes = Su_txt.get(1.0,END)
    text_get = change(text= mes,src = s,dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,text_get)









root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='Red')

lb_txt = Label(root,text="Translator",font=("Time New Roman",40,"bold"))
lb_txt.place(x=100,y=40,height=50,width=300)

frame = Frame(root).pack(side=BOTTOM)

lb_txt = Label(root,text="Source Text",font=("Time New Roman",20,"bold"),fg="Black",bg="Red")
lb_txt.place(x=100,y=100,height=20,width=300)

Su_txt = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
Su_txt.place(x=10,y=130,height=150,width=480)

li_txt = list(LANGUAGES.values())

comb_su = ttk.Combobox(frame,value=li_txt)
comb_su.place(x=10,y=300,height=40,width=150)
comb_su.set("english")

bt_change = Button(frame,text="Translate",relief=RAISED,command=data)
bt_change.place(x=170,y=300,height=40,width=150)

comb_dest = ttk.Combobox(frame,value=li_txt)
comb_dest.place(x=330,y=300,height=40,width=150)
comb_dest.set("english")

lb_txt = Label(root,text="Destination Text",font=("Time New Roman",20,"bold"),fg="Black",bg="Red")
lb_txt.place(x=100,y=360,height=20,width=300)

dest_txt = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)







root.mainloop()
