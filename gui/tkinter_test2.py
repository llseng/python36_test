# -*- coding: utf-8 -*-
# @Descripttion: 
# @version: 
# @Author: llseng
# @Date: 2021-01-21 12:16:10
# @LastEditors: llseng
# @LastEditTime: 2021-01-21 12:16:11
#

import tkinter as tk, tkinter.messagebox as tk_msgbox

def main():
    
    flag = True

    top = tk.Tk()
    frame = tk.Frame( top, bg='grey' )
    label = tk.Label( frame, text='提示信息' )
    btn_l = tk.Button( frame, text='修改' )
    btn_r = tk.Button( frame, text='关闭' )

    def update_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello World!') if flag else ('green', 'Goodbye World!')
        label.config( fg=color, text=msg )
    
    def close_window():
        if tk_msgbox.askokcancel( "提示框",  "确定要关闭窗口吗?" ):
            top.quit()

    label.pack( side=tk.TOP )

    btn_l.config( command=update_label_text )
    btn_l.pack( side=tk.LEFT )
    btn_r.config( command=close_window )
    btn_r.pack( side=tk.RIGHT )

    frame.config( width=600, height=600 )
    frame.pack( side=tk.BOTTOM )

    top.geometry( '600x600' )
    top.title( '模拟提示框' )

    top.mainloop()

if __name__ == "__main__":
    main()