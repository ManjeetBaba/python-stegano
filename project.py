from tkinter import *
from tkinter.filedialog import *
from PIL import ImageTk,Image
from stegano import exifHeader as stg
from tkinter import messagebox


def encode():
    main.destroy()
    enc=Tk()
    enc.title("encode")
    enc.geometry("500x400+300+150")


    label1=Label(text="Secrate message")
    label1.place(relx=.1,rely=.1,height=20,width=100)

    entry=Entry()
    entry.place(relx=.4,rely=.1)


    label2=Label(text="File Name")
    label2.place(relx=.1,rely=.2,height=20,width=100)

    entrysave=Entry()
    entrysave.place(relx=0.4,rely=0.2)

    def openfile():
        global fileopen
        fileopen=StringVar()
        fileopen=askopenfilename(initialdir="/Desktop",title="select file",filetypes=((".jpeg files","*jpg"),("all files","*.*")))

        label3=Label(text=fileopen)
        label3.place(relx=.3,rely=.3)

    buttonselect=Button(text="selectfile", command=openfile)
    buttonselect.place(relx=.1,rely=.3)

    def encodee ():
        response=messagebox.askyesno("pop up","do you want to encode")
    
        if response == 1:   
            stg.hide (fileopen,entrysave.get()+ '.jpg',entry.get())
            messagebox.showinfo("pop up","successfully encode")

        else:
            messagebox.showwarning("pop up","unsuccessfull")

    buttoncode=Button(text="Encode", command=encodee)
    buttoncode.place(relx=.4,rely=.5)


def decode():
    main.destroy()
    dnc=Tk()
    dnc.title("decode")
    dnc.geometry("500x400+300+150")

    def openfile():
        global fileopen
        fileopen=StringVar()
        fileopen=askopenfilename(initialdir="/Desktop",title="select file",filetypes=((".jpeg files","*jpg"),("all files","*.*")))


    def deodee ():
        message=stg.reveal(fileopen)

        label4=Label(text=message)
        label4.place(relx=.3,rely=.3)

    
    buttoncode=Button(text="Decode", command=deodee)
    buttoncode.place(relx=.4,rely=.5)

    buttonselect=Button(text="select file",command=openfile)
    buttonselect.place(relx=.1,rely=.3)

main=Tk()
main.title("img stegano")
main.geometry("500x400+300+150")

encodeb=Button(text="Encode",command= encode)
encodeb.place(relx=0.3,rely=.3,height=40,width=80)

decodeb=Button(text="Decode",command= decode)
decodeb.place(relx=0.5,rely=.3,height=40,width=80)

main.mainloop()