#Import libraries
from tkinter import *
from tkinter.messagebox import *
import os
import datetime
import time
from datetime import datetime as dt
#========================================================================================================
#Windows host file path
hostsPath=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
#Add the website you want to block, in this list
websites=[]

#=========================================================================================================
def g():
    try:
        r.destroy()
    except:
        pass
    global counter ,label
    s=Tk()
    s.title("LOGIN.wEb BlOcK__SHUBHASHIS MONDAL")
    s.geometry("6000x6000")
    #____________________________________background pic________________________________________________________________
    global logo,logo_final
    logo = PhotoImage(file="bg.png")
    logo_final= Label(s,image=logo,bg='#FFFFFF',fg = "Blue").place(x=0,y=0)
    Button(s, fg = "black", font = ('arial', 30, 'bold'), width = 10,activebackground="green", text = "GO", bg = 'green', command =lambda:h(s)).place(x=1200,y=300)
    Label(s, text="click here",bg='black', fg="red", font="Verdana 20") .place(x=1250,y=380)
    s.mainloop()


def count():
    global counter 
    display=str(counter)
    label['text']=" "+display+"   "
    # label.after(arg1, arg2) delays by 
    # first argument given in milliseconds 
    # and then calls the function given as second argument. 
    # Generally like here we need to call the 
    # function in which it is present repeatedly. 
    # Delays by 1000ms=1 seconds and call count again. 
    label.after(1000, count)
    t=datetime.datetime.now()
    counter =t.time().isoformat(timespec='seconds')
#=================================================================================================
def h(s):
    try:
        s.destroy()
    except:
        pass
    global counter,label,phot,phtof,r
    r=Tk()
    r.title("MAIN.wEb BlOcK__SHUBHASHIS MONDAL")
    r.geometry('6000x6000')
    phot=PhotoImage(file='321.png')
    photf=Label(r,image=phot).place(x=0,y=0)
    tt=datetime.datetime.now()
    date=tt.date()
    counter=tt.time().isoformat(timespec='seconds')
    label=Label(r, text="",bg='#f8d305', fg="black", font="Verdana 20") 
    label.place(x=1360,y=0)
    label1=Label(r, text="TIME   ",bg='#f8d305', fg="black", font="Verdana 20 bold") 
    label1.place(x=1250,y=0)
    label2 =Label(r, text="DATE : ",bg='#f8d305', fg="black", font="Verdana 20 bold") 
    label2.place(x=1250,y=38)
    label3 =Label(r, text=date,bg='#f8d305', fg="black", font="Verdana 20") 
    label3.place(x=1360,y=38)
    label.after(1000, count)
    Button(r, fg = "black", font = ('arial', 16, 'bold'), width = 10,activebackground="green", text = "<<<BACK", bg = 'red', command =lambda:g()).place(x=0,y=0)
    Label(r, fg = "black", font = ('arial', 40, 'bold'), width = 30,activebackground="white", text = "Enter the website you want to block", bg = 'green', command =None).place(x=300,y=250)
    w1=Entry(r,bd=10,font = ('arial', 20, 'bold'),width=30,bg='#bc946b',insertwidth = 5)
    w1.place(x=450,y=350)
    Button(r, fg = "black", font = ('arial', 20, 'bold'), width = 10,activebackground="green", text = "+Add", bg = 'red', command =lambda:add(w1,r)).place(x=950,y=348)
    Button(r, fg = "black", font = ('arial', 20, 'bold'), width = 10,activebackground="green", text = "BLOCK", bg = 'red', command =lambda:block()).place(x=450,y=410)
    Button(r, fg = "black", font = ('arial', 20, 'bold'), width = 13,activebackground="green", text = "UNBLOCK ALL", bg = 'red', command =lambda:unblock()).place(x=700,y=410)
    
    r.mainloop()
def add(w1,r):
    websites.append(w1.get())
    print(websites)
def block():
    with open(hostsPath,'r+') as file:
        content=file.read()
        for site in websites:
            if site in content:
                pass
            else:
                file.write(redirect+" "+site+"\n")
def unblock():
    with open(hostsPath,'r+') as file:
        content=file.readlines()
        file.seek(0)
        for line in content:
            if not any(site in line for site in websites):
                file.write(line)
        file.truncate()
try:
    g()
except:
    pass

        

