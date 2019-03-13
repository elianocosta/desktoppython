from tkinter import *
import time,datetime,pygame,sys,random
import serial

pygame.init()
janela=Tk()
ser = serial.Serial('COM8',baudrate=9600, timeout=5,bytesize=serial.EIGHTBITS,parity=serial.PARITY_NONE)

def bt_click():
    print(ser.name)

janela.title("Terminal Digital")
#janela.geometry('1082x750+0+0')
janela.resizable(False,False)

janela["bg"]="black"
FrameABC = Frame(janela,bg="blue",bd=20,relief = RIDGE)
FrameABC.grid()

FrameABC1 = Frame(FrameABC,bg="blue",bd=10,relief = RIDGE)
FrameABC1.grid(row=0,column=0,columnspan=4,sticky=W)


FrameABC2 = Frame(FrameABC,bg="white",bd=10,relief = RIDGE)
FrameABC2.grid(row=1,column=0,sticky=W)

FrameABC3 = Frame(FrameABC,bg="blue",bd=10,relief = RIDGE)
FrameABC3.grid(row=1,column=1,sticky=W)

FrameABC4 = Frame(FrameABC,bg="blue",bd=10,relief = RIDGE)
FrameABC4.grid(row=1,column=2,sticky=W)

FrameABC5 = Frame(FrameABC4,bg="blue",bd=10,relief = RIDGE)
FrameABC5.grid(row=0,column=0,sticky=W)

FrameABC6 = Frame(FrameABC4,bg="blue",bd=10,relief = RIDGE)
FrameABC6.grid(row=1,column=0,columnspan=4,sticky=W)
#==========Label horas ==================
Date1 = StringVar()
Time1 = StringVar()
Date1.set(time.strftime("%d/%m/%Y"))
Time1.set(time.strftime("%H:%M:%S"))
lblDate = Label(FrameABC1,textvariable=Date1,font=('arial',30,'bold'),padx=9,pady=9,bd=14,bg="Cadet Blue",fg="Cornsilk",justify=CENTER).grid(row=0,column=0)

lblTitle = Label(FrameABC1,text="\tSistema Digital \t",font=('arial',30,'bold'),padx=9,pady=9,bd=14,bg="Cadet Blue",fg="Cornsilk",justify=CENTER).grid(row=0,column=1)

lblHora = Label(FrameABC1,textvariable=Time1,font=('arial',30,'bold'),padx=9,pady=9,bd=14,bg="Cadet Blue",fg="Cornsilk",justify=CENTER).grid(row=0,column=2)
#=====================Variavel ====================
lblsendsequences = Label(FrameABC2,text="send sequences",font=('arial',20,'bold'),padx=8,bd=1,bg="yellow",fg="black",width="25",justify=CENTER).grid(row=0,column=0,columnspan=4)
#btclaro = Button(FrameABC2,width=10, text="Claro", command=bt_click).grid(row=0,column=0)

lblsend = Label(FrameABC2,text="send",font=('arial',20,'bold'),padx=8,bd=7,bg="white",fg="black",justify=CENTER).grid(row=1,column=0)
lblname = Label(FrameABC2,text="name",font=('arial',20,'bold'),padx=8,bd=7,bg="white",fg="black",justify=CENTER).grid(row=1,column=1)
lblsequence = Label(FrameABC2,text="sequence",font=('arial',20,'bold'),padx=8,bd=7,bg="white",fg="black",justify=CENTER).grid(row=1,column=2)
btsenhaclaro = Button(FrameABC2,width=10, text="----->", command=bt_click).grid(row=2,column=0)
lblsenhaclaro = Label(FrameABC2,text="Senha claro",font=('arial',8),padx=8,bd=7,bg="blue",fg="black",justify=CENTER).grid(row=2,column=1)
lblsequenceclaro = Label(FrameABC2,text="41 54 24 41 50 50 20 50 41 52 41 4D 20 32 33 31 35 2C 30 2C 63 6C 61 72 6F 0D 0A",font=('arial',8),padx=8,bd=7,bg="white",fg="black",justify=CENTER).grid(row=2,column=2)


btiprc = Button(FrameABC2,width=10, text="----->", command=bt_click).grid(row=3,column=0)
lbliprc = Label(FrameABC2,text="IP-RC",font=('arial',8),padx=8,bd=7,bg="white",fg="black",justify=CENTER).grid(row=3,column=1)
lblsequenceclaro = Label(FrameABC2,text="41 54 24 41 50 50 20 50 41 52 41 4D 20 32 33 31 39 2C 30 2C 6E 61 74 2E 74 72 69 78 6C 6F 67 2E 63 6F 6D 0D 0A",font=('arial',8),padx=8,bd=7,bg="white",fg="black",justify=CENTER).grid(row=3,column=2)

btportarc = Button(FrameABC2,width=10, text="----->", command=bt_click).grid(row=4,column=0)
lblportarc = Label(FrameABC2,text="Senha claro",font=('arial',8),padx=8,bd=7,bg="white",fg="black",justify=CENTER).grid(row=2,column=1)
btiprc = Button(FrameABC2,width=10, text="----->", command=bt_click).grid(row=3,column=0)

#lblvivo = Label(FrameABC2,text="vivo",font=('arial',20,'bold'),padx=8,bd=7,bg="blue",fg="black",justify=CENTER).grid(row=3,column=0,columnspan=4)


#lblsend1 = Label(FrameABC2,text="send1",font=('arial',20,'bold'),padx=8,bd=7,bg="blue",fg="black",justify=CENTER).grid(row=4,column=0,columnspan=4)

#lblsend2 = Label(FrameABC2,text="send2",font=('arial',20,'bold'),padx=8,bd=7,bg="blue",fg="black",justify=CENTER).grid(row=5,column=0,columnspan=4)

lblreceivedsequences = Label(FrameABC2,text="received sequences",font=('arial',20,'bold'),padx=8,bd=1,bg="yellow",fg="black",width="25",justify=CENTER).grid(row=6,column=0,columnspan=4)
janela.mainloop()