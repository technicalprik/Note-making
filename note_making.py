import os,tkinter
from tkinter import *
from tkinter.messagebox import *
from PIL import ImageTk, Image

def files():
    ##for getting the names of the files stored
    global f_list
    f_list=[]
    for f in os.listdir('D:/prik/note making/notes'):
        if f.endswith('.txt'):
            f_list+=[f]
    return f_list

def mainscreen():
    ##creating the screen
    global screen
    screen=Tk()
    screen.geometry('900x600')
    screen.title("Note Maker")
    
    ##getting the list of files
    files()

    ##creating frames
    f1 = Frame(screen,height=600,width=300)
    f2 = Frame(screen,height=600,width=600)

    ##making the text box
    global area
    area=Text(f2,font=('calibri',12),bg='#DCF9F7',height=32,wrap='word')
    area.pack()
    
    ##f1 background
    img = ImageTk.PhotoImage(Image.open('note_bg.ppm'))
    panel = tkinter.Label(f1, image = img)
    panel.pack()
    
    ##displaying the files present
    vary()
    for j in range(0,len(f_list)):
        exec(tuple(bu_dic.values())[j])

    ##placing the frames
    f1.pack(side='left')
    f2.pack(side='right')

    ##making the menu bar
    head=Menu(screen)
                #creating file menu
    filemenu=Menu(head,tearoff=0)
    filemenu.add_command(label="New",command=newfile)
    filemenu.add_command(label="Find",command=find)
    filemenu.add_command(label="Save",command=saver)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=screen.destroy)
    head.add_cascade(label='File' ,menu=filemenu)
                #creating edit menu
    editmenu=Menu(head,tearoff=0)
    editmenu.add_command(label="Cut",command=cutter)
    editmenu.add_command(label="Copy",command=copier)
    editmenu.add_command(label="Paste",command=paster)
    head.add_cascade(label='Edit' ,menu=editmenu)
    
    ##finalising the things
    screen.config(menu=head)
    screen.mainloop()

#for creating new files and naming them
def newfile():
    with open("D:/prik/note making/notes/Untitled.txt","w") as newfile :
        pass
    scn()
    os.chdir('D:/prik/note making/notes')
    os.rename('Untitled.txt',(str(gamma1)+'.txt'))
    os.chdir('D:/prik/note making')
    mainscreen()
    
def _f():
    f_dic={}
    for i in range(f_list):
        f_dic[f'f__{i}']=f_list[i]

#to find if a word exists in the opened file
def find():
    global screenf
    screenf=Tk()
    screenf.geometry('280x120')
    Label(screenf,text="What do you want to find?",font=('fenix',18)).pack()
    Label(screenf,text=" ",font=('fenix',6)).pack()
    global delta
    delta=StringVar()
    global epsilon
    epsilon=Entry(screenf,textvariable=delta,font=('fenix',12))
    epsilon.pack()
    Button(screenf,text='Find',command=scn__,fg='white',bg='black').place(x=75,y=80)
    Button(screenf,text='Close',command=screenf.destroy,fg='white',bg='black').place(x=160,y=80)
    screenf.mainloop()

def scn__():
    global epsilon1
    epsilon1=epsilon.get()
    epsilon11=epsilon1+'\n'
    pathp='D:/prik/note making/notes/%s'
    _path=pathp % (yo)
    with open(_path,"r") as f_ile:
        f_ile_=f_ile.readlines()
        epsilon2=None
        for i in range(0,len(f_ile_)):
            if epsilon1 in f_ile_[i]:
                epsilon2=True
                break
            else:
                pass
        if epsilon2==None:
            tkinter.messagebox.showerror("Not Found","%s doesn't exists in the file!"%epsilon1)
        else:
            tkinter.messagebox.showinfo("Found","%s exists in the file!"%epsilon1)

#to save a file
def saver():
    path="D:/prik/note making/notes/%s"
    file = open(path%(yo),"w") 
    file.write(area.get(1.0,END))
    file.close()
    tkinter.messagebox.showinfo('Success!', 'File Saved.')

#to cut
def cutter():
    area.event_generate("<<Cut>>")

#to copy
def copier():
    area.event_generate("<<Copy>>")

#to paste
def paster():
    area.event_generate("<<Paste>>")

#opening a file
def opener(alpha):
    global yo
    yo=f_list[alpha]
    path="D:/prik/note making/notes/%s"
    with open(path%(yo),'r') as b:
        screen.title(yo[0:-4])
        area.delete(1.0,END)
        area.insert(1.0,b.read())

#new note's name screen
def scn():
    global scrn
    scrn=Tk()#oplevel(screen)
    scrn.title("Name")
    scrn.geometry('200x150')
    global gamma
    gamma=StringVar()
    Label(scrn,text='What should be\nthe name\nof your new note?',font=('fenix',18)).pack()
    global name
    name=Entry(scrn,textvariable=gamma,font=('fenix',12))
    name.pack()
    Button(scrn,text='Rename',command=scn_).place(x=75,y=115)
    scrn.mainloop()

#for getting what was written in name box on new note and quitting the screen
def scn_():
    global gamma1
    gamma1=name.get()
    scrn.destroy()
    screen.destroy()

#creating dictionary for buttons
def vary():
    global bu_dic
    bu_dic={}
    for i in range(len(f_list)):
        bu_dic[f"b_{i}"]=f"Button(text=f_list[{i}][:-4],font=('fenix',12),command=lambda:opener({i})).place(x=6,y=(({i}+3)*35))"

#__main__
mainscreen()

