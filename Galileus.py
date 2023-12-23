#Galileus.py è in Beta 1.0.0
#Galileus.py è un programma che permette di riprodurre dei suoni tramite la pressione di un tasto
#Galileus.py è stato creato da Emanuele Moro
#Galileus.py è stato concepito il 20/12/2023
#Diritti riservati ad Emanuele Moro
#Galileus.py è open source
#Galileus.py è gratuito
#Galileus.py è NON può essere venduto

import tkinter as tk
import pygame
from tkinter import Tk
from tkinter.filedialog import askopenfilename

#dir con dentro 20 'void'
dir = ['void']*20
pygame.mixer.init()

def selectAudio(id):
    global dir

    Tk().withdraw()
    dir[id] = askopenfilename()
    updateLabel(id)
    updateGalimem()

def goodName(dir):
    tmp = dir.split('/')[-1]
    tmp = tmp.split('.')[0]
    if len(tmp) > 15:
        tmp = tmp[:15] + '...'
    return tmp

def updateLabel(id):
    global dir
    if dir[id] != '':
        lblArray[id].config(text=goodName(dir[id]))
    else:
        dir[id] = 'void'
        lblArray[id].config(text='Void')

def play_sound(event):
    key = event.char

    global dir

    if key == '1':
        pygame.mixer.music.load(dir[1])
        pygame.mixer.music.play()
    elif key == '2':
        pygame.mixer.music.load(dir[2])
        pygame.mixer.music.play()
    elif key == '3':
        pygame.mixer.music.load(dir[3])
        pygame.mixer.music.play()
    elif key == '4':
        pygame.mixer.music.load(dir[4])
        pygame.mixer.music.play()
    elif key == '5':
        pygame.mixer.music.load(dir[5])
        pygame.mixer.music.play()
    elif key == '6':
        pygame.mixer.music.load(dir[6])
        pygame.mixer.music.play()
    elif key == '7':
        pygame.mixer.music.load(dir[7])
        pygame.mixer.music.play()
    elif key == '8':
        pygame.mixer.music.load(dir[8])
        pygame.mixer.music.play()
    elif key == '9':
        pygame.mixer.music.load(dir[9])
        pygame.mixer.music.play()
    elif key == '0':
        pygame.mixer.music.load(dir[0])
        pygame.mixer.music.play()
    elif key == 'q':
        pygame.mixer.music.load(dir[10])
        pygame.mixer.music.play()
    elif key == 'w':
        pygame.mixer.music.load(dir[11])
        pygame.mixer.music.play()
    elif key == 'e':
        pygame.mixer.music.load(dir[12])
        pygame.mixer.music.play()
    elif key == 'r':
        pygame.mixer.music.load(dir[13])
        pygame.mixer.music.play()
    elif key == 't':
        pygame.mixer.music.load(dir[14])
        pygame.mixer.music.play()
    elif key == 'y':
        pygame.mixer.music.load(dir[15])
        pygame.mixer.music.play()
    elif key == 'u':
        pygame.mixer.music.load(dir[16])
        pygame.mixer.music.play()
    elif key == 'i':
        pygame.mixer.music.load(dir[17])
        pygame.mixer.music.play()
    elif key == 'o':
        pygame.mixer.music.load(dir[18])
        pygame.mixer.music.play()
    elif key == 'p':
        pygame.mixer.music.load(dir[19])
        pygame.mixer.music.play()

def stop_sound(event):
    key = event.keysym
    if key == 'Escape':
        pygame.mixer.music.stop()

def updateGalimem():
    global dir
    f = open('galimem.gmf', 'w')
    for i in range(20):
        f.write(dir[i] + '\n')
    f.close()

root = tk.Tk()

root.title('Galileus Beta 1.0.0')

Beta = tk.Label(root, text='                                                                                      Beta', font=('Avenir Next', 10, 'italic')).grid(row=1, column=2, columnspan=12)
Galileus = tk.Label(root, text='~Galileus', font=('Avenir Next', 50, 'bold')).grid(row=1, column=1, columnspan=12)

#Dissolvi
disArray = []

dis12 = tk.Button(root, text='Dissolvi', command=lambda: selectAudio(''), height=2, width=15).grid(row=4, column=2, columnspan=2)
disArray.append(dis12)
dis34 = tk.Button(root, text='Dissolvi', command=lambda: selectAudio(''), height=2, width=15).grid(row=4, column=4, columnspan=2)
disArray.append(dis34)
dis56 = tk.Button(root, text='Dissolvi', command=lambda: selectAudio(''), height=2, width=15).grid(row=4, column=6, columnspan=2) 
disArray.append(dis56)
dis78 = tk.Button(root, text='Dissolvi', command=lambda: selectAudio(''), height=2, width=15).grid(row=4, column=8, columnspan=2)
disArray.append(dis78)
dis90 = tk.Button(root, text='Dissolvi', command=lambda: selectAudio(''), height=2, width=15).grid(row=4, column=10, columnspan=2)
disArray.append(dis90)

#Pulsanti 1-9
btnArray = []
btn0 = tk.Button(root, text='0', command=lambda: selectAudio(0), height=4, width=5, bd=5).grid(row=5, column=11)
btnArray.append(btn0)
btn1 = tk.Button(root, text='1', command=lambda: selectAudio(1), height=4, width=5, bd=5).grid(row=5, column=2)
btnArray.append(btn1)
btn2 = tk.Button(root, text='2', command=lambda: selectAudio(2), height=4, width=5, bd=5).grid(row=5, column=3)
btnArray.append(btn2)
btn3 = tk.Button(root, text='3', command=lambda: selectAudio(3), height=4, width=5, bd=5).grid(row=5, column=4)
btnArray.append(btn3)
btn4 = tk.Button(root, text='4', command=lambda: selectAudio(4), height=4, width=5, bd=5).grid(row=5, column=5)
btnArray.append(btn4)
btn5 = tk.Button(root, text='5', command=lambda: selectAudio(5), height=4, width=5, bd=5).grid(row=5, column=6)
btnArray.append(btn5)
btn6 = tk.Button(root, text='6', command=lambda: selectAudio(6), height=4, width=5, bd=5).grid(row=5, column=7)
btnArray.append(btn6)
btn7 = tk.Button(root, text='7', command=lambda: selectAudio(7), height=4, width=5, bd=5).grid(row=5, column=8)
btnArray.append(btn7)
btn8 = tk.Button(root, text='8', command=lambda: selectAudio(8), height=4, width=5, bd=5).grid(row=5, column=9)
btnArray.append(btn8)
btn9 = tk.Button(root, text='9', command=lambda: selectAudio(9), height=4, width=5, bd=5).grid(row=5, column=10)
btnArray.append(btn9)

#etichette
lblArray = []

lbl0 = tk.label = tk.Label(root, text='Void')
lbl0.grid(row=6, column=11)
lblArray.append(lbl0)

lbl1 = tk.label = tk.Label(root, text='Void')
lbl1.grid(row=6, column=2)
lblArray.append(lbl1)

lbl2 =tk.label = tk.Label(root, text='Void')
lbl2.grid(row=6, column=3)
lblArray.append(lbl2)

lbl3 = tk.label = tk.Label(root, text='Void')
lbl3.grid(row=6, column=4)
lblArray.append(lbl3)

lbl4 = tk.label = tk.Label(root, text='Void')
lbl4.grid(row=6, column=5)
lblArray.append(lbl4)

lbl5 = tk.label = tk.Label(root, text='Void')
lbl5.grid(row=6, column=6)
lblArray.append(lbl5)

lbl6 = tk.label = tk.Label(root, text='Void')
lbl6.grid(row=6, column=7)
lblArray.append(lbl6)

lbl7 = tk.label = tk.Label(root, text='Void')
lbl7.grid(row=6, column=8)
lblArray.append(lbl7)

lbl8 = tk.label = tk.Label(root, text='Void')
lbl8.grid(row=6, column=9)
lblArray.append(lbl8)

lbl9 = tk.label = tk.Label(root, text='Void')
lbl9.grid(row=6, column=10)
lblArray.append(lbl9)


#etichette null
tk.label = tk.Label(root, text='').grid(row=7, column=2)
tk.label = tk.Label(root, text='').grid(row=7, column=3)
tk.label = tk.Label(root, text='').grid(row=7, column=4)
tk.label = tk.Label(root, text='').grid(row=7, column=5)
tk.label = tk.Label(root, text='').grid(row=7, column=6)
tk.label = tk.Label(root, text='').grid(row=7, column=7)
tk.label = tk.Label(root, text='').grid(row=7, column=8)
tk.label = tk.Label(root, text='').grid(row=7, column=9)
tk.label = tk.Label(root, text='').grid(row=7, column=10)
tk.label = tk.Label(root, text='').grid(row=7, column=11)

#btn QWERTYUIOP
btnQ = tk.Button(root, text='Q', command=lambda: selectAudio(10), height=4, width=5, bd=5).grid(row=8, column=2)
btnArray.append(btnQ)
btnW = tk.Button(root, text='W', command=lambda: selectAudio(11), height=4, width=5, bd=5).grid(row=8, column=3)
btnArray.append(btnW)
btnE = tk.Button(root, text='E', command=lambda: selectAudio(12), height=4, width=5, bd=5).grid(row=8, column=4)
btnArray.append(btnE)
btnR = tk.Button(root, text='R', command=lambda: selectAudio(13), height=4, width=5, bd=5).grid(row=8, column=5)
btnArray.append(btnR)
btnT = tk.Button(root, text='T', command=lambda: selectAudio(14), height=4, width=5, bd=5).grid(row=8, column=6)
btnArray.append(btnT)
btnY = tk.Button(root, text='Y', command=lambda: selectAudio(15), height=4, width=5, bd=5).grid(row=8, column=7)
btnArray.append(btnY)
btnU = tk.Button(root, text='U', command=lambda: selectAudio(16), height=4, width=5, bd=5).grid(row=8, column=8)
btnArray.append(btnU)
btnI = tk.Button(root, text='I', command=lambda: selectAudio(17), height=4, width=5, bd=5).grid(row=8, column=9)
btnArray.append(btnI)
btnO = tk.Button(root, text='O', command=lambda: selectAudio(18), height=4, width=5, bd=5).grid(row=8, column=10)
btnArray.append(btnO)
btnP = tk.Button(root, text='P', command=lambda: selectAudio(19), height=4, width=5, bd=5).grid(row=8, column=11)
btnArray.append(btnP)

#etichette
lbl10 = tk.label = tk.Label(root, text='Void')
lbl10.grid(row=9, column=2)
lblArray.append(lbl10)
lbl11 = tk.label = tk.Label(root, text='Void')
lbl11.grid(row=9, column=3)
lblArray.append(lbl11)
lbl12 = tk.label = tk.Label(root, text='Void')
lbl12.grid(row=9, column=4)
lblArray.append(lbl12)
lbl13 = tk.label = tk.Label(root, text='Void')
lbl13.grid(row=9, column=5)
lblArray.append(lbl13)
lbl14 = tk.label = tk.Label(root, text='Void')
lbl14.grid(row=9, column=6)
lblArray.append(lbl14)
lbl15 = tk.label = tk.Label(root, text='Void')
lbl15.grid(row=9, column=7)
lblArray.append(lbl15)
lbl16 = tk.label = tk.Label(root, text='Void')
lbl16.grid(row=9, column=8)
lblArray.append(lbl16)
lbl17 = tk.label = tk.Label(root, text='Void')
lbl17.grid(row=9, column=9)
lblArray.append(lbl17)
lbl18 = tk.label = tk.Label(root, text='Void')
lbl18.grid(row=9, column=10)
lblArray.append(lbl18)
lbl19 = tk.label = tk.Label(root, text='Void')
lbl19.grid(row=9, column=11)
lblArray.append(lbl19)

#grid centrata nella root
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(16, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(12, weight=1)

#slider
bgSound1 = tk.Scale(root, from_=100, to=0, orient=tk.VERTICAL, label='bgSound', length=200)
bgSound1.grid(row=10, column=0, rowspan=4)

bgSound1Var = tk.DoubleVar()

bgSound2 = tk.Scale(root, from_=100, to=0, orient='vertical', label='bgSound', length=200)
bgSound2.grid(row=10, column=12, rowspan=4)

bgSound2Var = tk.DoubleVar()

btnSel1 = tk.Button(root, text='Select', command=lambda: selectAudio(''), height=1, width=8, bd=10).grid(row=15, column=0)
btnSel2 = tk.Button(root, text='Select', command=lambda: selectAudio(''), height=1, width=8, bd=10).grid(row=15, column=12)

#root.attributes('-fullscreen', True)

#apri un file in lettura
try:
    f = open('galimem.gmf', 'r')
    for i in range(20):
        dir[i] = f.readline()
        dir[i] = dir[i].replace('\n', '')
        updateLabel(i)
    f.close()
except:
    #creare file
    f = open('galimem.gmf', 'w')
    for i in range(20):
        f.write('void\n')
    f.close()



root.bind('<KeyPress>', play_sound)
root.bind('<KeyRelease>', stop_sound)
root.mainloop()