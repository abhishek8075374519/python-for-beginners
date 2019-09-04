import os
from tkinter import *


fileExplorer = Tk()
fileExplorer.geometry('500x500')

#search the file on click
def searchBtn():
    nFile = searchField.get() + '.txt'
    try:
        if nFile!="":
            txtFld.delete('1.0', END)
            nFile = searchField.get()+'.txt'
            fo = open(nFile, 'r')
            fContent = fo.read()
            print(fContent)
            txtFld.insert('1.0', fContent)
            fo.close()
    except:
        lbl3 = Label(fileExplorer, text='File cannot be created..Please enter a file name!', fg='red')
        lbl3.grid(row=2, column=0)

#save the file on click
def saveCnt():
    try:
        nText = txtFld.get('1.0', END)
        nnFile = searchField.get() + '.txt'
        fo = open(nnFile, 'w')
        fo.write(nText)
        fo.close()
    except:
        pass

#search bar

lbl1 = Label(fileExplorer, text='Search your file here:')
lbl1.grid(row=0, column=0)
searchField = Entry(fileExplorer, width='50')
searchField.grid(row=1, column=0)
srchBtn = Button(fileExplorer, text='Go', command=searchBtn)
srchBtn.grid(row=1, column=1)

#file editor/view

lbl2 = Label(fileExplorer, text='View or edit your file here:')
lbl2.grid(row=3, column=0)
txtFld = Text(fileExplorer, width='50')
txtFld.grid(row=4, column=0)
sutBtn = Button(fileExplorer, text='Save File', command= saveCnt)
sutBtn.grid(row=4, column=1)


#create directory

try:
    os.mkdir('New Folder')
except:
    pass
os.chdir('New Folder')

fileExplorer.mainloop()
