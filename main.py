"""
</>
Programmer: Mehroj Majidov
Github: https://github.com/MehrojOfficial
Title: "Password Generator"
</>
"""
from tkinter import *
from mixture import mixture
from PIL import ImageTk, Image
import pyperclip as pc

root = Tk()
root.resizable(0,0)
root.title('Password Generator')
root.configure(bg='#303841')

# Specific Functions

def center_window(w=300, h=300):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

def character_org(length):
    if len(length.get()) != 0:
        if not length.get()[-1].isdigit():
            length.set(length.get()[0:-1])

def character_limit(length):
    if len(length.get()) > 2:
        length.set(length.get()[:2])
        btn_entry.delete(0,99)

def entry_limit(length):
    if len(length.get()) != 0:
        if int(length.get()) > 30:
            btn_entry.delete(0,99)
            btn_entry.insert(0,"Limit is 30 characters")
        else:
            btn_entry.delete(0,99)
def up():
    if int(length.get()) < 30:
        length.set(int(length.get())+1)

def down():
    if int(length.get()) != 0 and int(length.get()) > 8:
        length.set(int(length.get())-1)

def finish():
    global result2
    lent = int(length.get())
    result2 = mixture(r.get(),q.get(),p.get(),e.get(),lent)
    if len(result2) <= 30:
        btn_entry.delete(0,99)
        btn_entry.insert(0,result2)
    else:
        btn_entry.delete(0,99)
        btn_entry.insert(0,"Limit is 30 characters")
    pc.copy(result2)
    result2=''

# Title
pgen = Label(text = "PASSWORD GENERATOR",fg = 'white', bg = '#303841',font=('Arial 13 bold'))
pgen.pack(pady=20)

# Options
r = IntVar()
pnum = Label(text = 'Numbers',fg = 'white', bg = '#303841',font=('Arial 10 bold'))
pnum.place(x=120,y=60)
rbun = Checkbutton(root,borderwidth = 0,text = "", bg = '#303841', variable = r, cursor = 'hand2',foreground='#303841',bd = 0,highlightcolor= "red", activebackground = '#303841', selectcolor = "white")
rbun.place(x=100,y=60)
rbun.select()

q = IntVar()
psym = Label(text = 'Symbols',fg = 'white', bg = '#303841',font=('Arial 10 bold'))
psym.place(x=120,y=80)
rsun = Checkbutton(root,borderwidth = 0,text = "", bg = '#303841', variable = q, cursor = 'hand2',bd = 0,highlightcolor= "red", activebackground = '#303841')
rsun.place(x=100,y=80)
rsun.select()

p = IntVar()
plow = Label(text = 'Lowercase',fg = 'white', bg = '#303841',font=('Arial 10 bold'))
plow.place(x=120,y=100)
rlun = Checkbutton(root,borderwidth = 0,text = "", bg = '#303841', variable = p, cursor = 'hand2',bd = 0,highlightcolor= "red", activebackground = '#303841')
rlun.place(x=100,y=100)
rlun.select()

e = IntVar()
pup = Label(text = 'Uppercase',fg = 'white', bg = '#303841',font=('Arial 10 bold'))
pup.place(x=120,y=120)
rpun = Checkbutton(root,borderwidth = 0,text = "", bg = '#303841', variable = e, cursor = 'hand2',bd = 0,highlightcolor= "red", activebackground = '#303841')
rpun.place(x=100,y=120)
rpun.select()

# Result Entry
btn_entry = Entry(root, fg = '#508DCC',borderwidth = 0, bg = '#17212B',width = 35,justify=CENTER,font=('Arial 10 bold'))
btn_entry.place(x=30, y=200)
result2=''

# Generate Button
click_btn= PhotoImage(file='data/generate-btn.png')
btn_gen = Button(root,image = click_btn, bg = '#303841',bd=0, activebackground='#303841', command=finish)
btn_gen.place(x=100, y=230)

# Password Length
plen = Label(text = 'Pasword Length',fg = 'white', bg = '#303841', font=('Arial 10 bold'))
plen.place(x=75,y=160)

# Length Entry
length = StringVar()
length.set("16")
plenn = Entry(text = length,borderwidth=0, fg = 'white', bg = '#303841',font=('Arial 10 bold'),width=2)
plenn.place(x=190,y=162)

# Control Buttons
cup = Image.open('data/up.png')
cup = cup.resize((10,10), Image.ANTIALIAS)
cup = ImageTk.PhotoImage(cup)

cup_gen = Button(root,image = cup, bg = '#303841',bd=0, activebackground='#303841', command=up, cursor = 'hand2')
cup_gen.place(x=210,y=160)

cdown = Image.open('data/down.png')
cdown = cdown.resize((10,10), Image.ANTIALIAS)
cdown = ImageTk.PhotoImage(cdown)

cdown_gen = Button(root,image = cdown, bg = '#303841',bd=0, activebackground='#303841', command=down, cursor = 'hand2')
cdown_gen.place(x=210,y=170)

# Auto Correctors
length.trace("w", lambda *args: character_limit(length))
length.trace("w", lambda *args: character_org(length))
length.trace("w", lambda *args: entry_limit(length))
center_window()

# Infinite Loop
root.mainloop()