# Library import
from tkinter import *

#Initailizing GUI window and variables
window = Tk()
ptoc= StringVar()
ctop= StringVar()

#Main code logic of Atbash Ciper - PA0

def plaintocipher():
    t2.delete(0,'end')
    c=ptoc.get()
    cipher_text=""
    for a in range(len(c)):
        char = c[a]
        if(char.isupper()):
            cipher_text += chr(90-(ord(char)-65)%26)
        elif(char ==" ") :
            cipher_text +=" "
        elif(char.islower()):
            cipher_text += chr(122-(ord(char)-97)%26)
        else:
            cipher_text +=char
    t2.insert(0,cipher_text)

def ciphertoplain():
    t1.delete(0,'end')
    c=ctop.get()
    cipher_text=""
    for a in range(len(c)):
        char = c[a]
        if(char.isupper()):
            cipher_text += chr(90-(ord(char)-65)%26)
        elif(char ==" ") :
            cipher_text +=" "
        elif(char.islower()):
            cipher_text += chr(122-(ord(char)-97)%26)
        else:
            cipher_text +=char
    t1.insert(0,cipher_text)


#GUI creation and working

window.geometry("600x300")
window.resizable(False,False)
window.title("Atbash cipher - PA0")
window.config(bg="#2e7175")

l1=Label(window,text="Plain text", bg="white",padx=10,pady=10,width=25).place(x=10,y=10)
l2=Label(window,text="Cipher text", bg="white",padx=10,pady=10,width=25).place(x=350,y=10)

t1=Entry(window,bg="white",textvariable=ptoc)
t1.place(x=10,y=50,width=270,height=100)
t1.insert(0,"hello")
t2=Entry(window,bg="white" ,textvariable=ctop)
t2.place(x=350,y=50,width=270,height=100)
t2.insert(0,"svool")

b1=Button(window,text="Click me to Encrypt Plain Text",command=plaintocipher).place(x=10,y=160)
b2=Button(window,text="Click me to Decrypt Cipher Text",command=ciphertoplain).place(x=350,y=160)

window.mainloop()