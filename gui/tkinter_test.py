# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-01-21 10:30:46
# @LastEditors: llseng
# @LastEditTime: 2021-01-21 10:30:46
#

import tkinter, tkinter.messagebox

root = tkinter.Tk()

tk = tkinter.Frame( root )
tk1 = tkinter.Frame( root, width = 600, height=600, bg = 'green' )

list1 = [165,1,3,61,51,61,98,123,61,85,1,61,5,156]
list2 = ['c:','Users','Administrator','.vscode','extensions','ms-python.python-2020.12']

tk_listbox = tkinter.Listbox( tk )
tk_listbox2 = tkinter.Listbox( tk1 )

for x in list1[-1::-1]:
    tk_listbox.insert( 0, x )

for x in list2[-1::-1]:
    tk_listbox2.insert( 0, x )

tk_listbox.pack()
tk_listbox2.pack()

C = tkinter.Canvas( tk, bg = 'white' )
C.create_rectangle(5, 5, 100, 100)
C.pack()

message =  tkinter.Message( tk, text='asdasd' )
message.pack()

def mb():
    tkinter.messagebox.askokcancel( '提示', '这是一个提示框' )

btn = tkinter.Button( tk, command=mb, text='一个提示框' )
btn.pack()

cb1 = tkinter.IntVar()
cb2 = tkinter.IntVar()
def show_cb():
    print( cb1.get(), cb2.get() )

check_b = tkinter.Checkbutton( tk1, text='复选框1', onvalue = 1, variable = cb1, command=show_cb )
check_b.pack()
check_b2 = tkinter.Checkbutton( tk1, text='复选框2', onvalue = 1, offvalue = 0, variable = cb2, command=show_cb )
check_b2.pack()

label = tkinter.Label( tk1, text='输入框' )
label.pack( side='left' )
entry = tkinter.Entry( tk1 )
entry.pack( side="right" )

tk.pack(side='left')
tk1.pack(side='right')
root.mainloop()
