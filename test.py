from PIL import Image, ImageTk, ImageFilter

import tkinter as tk
from tkinter import filedialog as fd

im = None
tk_img = None
deg = 0
is_blur = False


def open():
    global im, tk_img
    fname = fd.askopenfilename()
    im = Image.open(fname)
    tk_img = ImageTk.PhotoImage(im)
    canvas.create_image(250, 250, image=tk_img)
    window.update()

def quit():
    window.quit()
    
def image_rotate():
    global im, tk_img, deg
    if deg == -360:
        deg = 0
        
    deg -= 45    
        
    if is_blur == True:
        out = im.rotate(deg)
        out = im.filter(ImageFilter.BLUR).rotate(deg)
        tk_img = ImageTk.PhotoImage(out)
    else:
        out = im.rotate(deg)
        tk_img = ImageTk.PhotoImage(out)
    
    canvas.create_image(250, 250, image=tk_img)
    window.update()
    
def image_blur():
    global im,tk_img, deg, is_blur
    if is_blur == False:
        is_blur = True
    else:
        is_blur = False
        out = im.rotate(deg)
        tk_img = ImageTk.PhotoImage(out)
        canvas.create_image(250, 250, image=tk_img)
        window.update()
        
    if is_blur == True:
        out = im.filter(ImageFilter.BLUR).rotate(deg)
        tk_img = ImageTk.PhotoImage(out)
        canvas.create_image(250, 250, image=tk_img)
        window.update()
    
window = tk.Tk()
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
ipmenu = tk.Menu(menubar)

filemenu.add_command(label="열기", command=open)
filemenu.add_command(label="종료", command=quit)
ipmenu.add_command(label="영상회전", command=image_rotate)
ipmenu.add_command(label="영상흐리게", command=image_blur)
menubar.add_cascade(label="파일", menu=filemenu)
menubar.add_cascade(label="영상처리", menu=ipmenu)

window.config(menu=menubar)
window.mainloop()