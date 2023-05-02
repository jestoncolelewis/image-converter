import os
import cv2 as cv
from image_functions import *
import tkinter as tk
from tkinter import ttk
from tkinter import * #type: ignore
from tkinter import filedialog as fd

# functions
def openfile():
    global images
    images = fd.askopenfilenames()
    for name in images:
        img_name = name[:]
        name_l = name.rfind('/')
        img_name = name[name_l+1:]
        file_box.insert('end', img_name)

def new_factor():
    if s.get() == 1:
        factor = 2.0
    if s.get() == 2:
        factor = 0.5
    return factor #type: ignore

def process():
    path = fd.askdirectory()
    for image in images:
        img = cv.imread(image)
        img_name = image[:]
        name_l = image.rfind('/')
        img_name = image[name_l+1:]
        h = img.shape[0]
        w = img.shape[1]

        if var.get() == "grayscale":
            new_name = f"g_{img_name}"
            cv.imwrite(os.path.join(f"{path}/", new_name), grayscale(img, h, w))
        if var.get() == "sepia":
            new_name = f"s_{img_name}"
            cv.imwrite(os.path.join(f"{path}/", new_name), sepia(img, h, w))
        if var.get() == "mirror":
            new_name = f"m_{img_name}"
            cv.imwrite(os.path.join(f"{path}/", new_name), mirror(img, h, w))
        if var.get() == "reflect":
            new_name = f"r_{img_name}"
            flip_img = cv.flip(img, 1)
            cv.imwrite(os.path.join(f"{path}/", new_name), flip_img)
        if var.get() == "scale":
            new_name = f"sc_{img_name}"
            cv.imwrite(os.path.join(f"{path}/", new_name), scale(img, h , w, new_factor()))

images = ()

# build window
window = Tk()
window.title('Image Converter')
window.resizable(False, False)
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
frame = ttk.Frame(window, padding='12 12 12 12')
frame.grid(column=0, row=0, sticky=(N, W, E, S)) # type: ignore


# input
input_label = ttk.Label(frame, text='Input')
input_label.grid(column=1, row=1, sticky=W)
file_scroll = ttk.Scrollbar(frame)
file_box = tk.Listbox(frame, yscrollcommand= file_scroll.set)
file_box.grid(column=1, row=2, columnspan=30, rowspan=15, sticky=W)
file_scroll.config(command=file_box.yview)
open_button = ttk.Button(frame, text='Open', command=openfile)
open_button.grid(column=1, row=17, sticky=S)


# output
output_label = ttk.Label(frame, text='Output')
output_label.grid(column=32, row=1, sticky=W)

# options buttons
var = StringVar()
gray_option = ttk.Radiobutton(frame, text='Grayscale', variable=var, value='grayscale')
gray_option.grid(column=32, row=2, sticky=W)
sepia_option = ttk.Radiobutton(frame, text='Sepia', variable=var, value='sepia')
sepia_option.grid(column=32, row=3, sticky=W)
mirror_option = ttk.Radiobutton(frame, text='Mirror', variable=var, value='mirror')
mirror_option.grid(column=32, row=4, sticky=W)
reflect_option = ttk.Radiobutton(frame, text='Reflect', variable=var, value='reflect')
reflect_option.grid(column=32, row=5, sticky=W)
scale_option = ttk.Radiobutton(frame, text='Scale', variable=var, value='scale')
scale_option.grid(column=32, row=6, sticky=W)
s = IntVar()
half_option = ttk.Radiobutton(frame, text='.5x', variable=s, value=1)
half_option.grid(column=32, row=7, sticky=N)
double_option = ttk.Radiobutton(frame, text='2x', variable=s, value=2)
double_option.grid(column=32, row=8, sticky=N)

# conversion action button
process_button = ttk.Button(frame, text='PROCESS', command=process)
process_button.grid(column=32, row=17, sticky=W)

window.mainloop()