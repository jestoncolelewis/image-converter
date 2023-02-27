import os
import cv2 as cv
from image_functions import *
import tkinter as tk
from tkinter import filedialog as fd

# build window
window = tk.Tk()
window.title('Image Converter')
window.resizable(False, False)
window.geometry('700x365')

file_scroll = tk.Scrollbar(window)
file_box = tk.Listbox(window, yscrollcommand= file_scroll.set, height=15, width=30)
file_box.place(x='20', y='50')
file_scroll.config(command=file_box.yview)

# input label
input_label = tk.Label(window, text='Input', anchor='center')
input_label.place(x='20', y='15')

# file browse and open and save
def openfile():
    global images, path
    images = fd.askopenfilenames()
    for name in images:
        img_name = name[:]
        name_l = name.rfind('/')
        img_name = name[name_l+1:]
        file_box.insert('end', img_name)
images = ()
open_button = tk.Button(window, text='Open', command=openfile)
open_button.place(x='20', y='315')

# output label
output_label = tk.Label(window, text='Output', anchor='center')
output_label.place(x='380', y='15')

# options buttons
var = tk.StringVar()
gray_option = tk.Radiobutton(window, text='Grayscale', variable=var, value='grayscale')
gray_option.place(x='380', y='50')
sepia_option = tk.Radiobutton(window, text='Sepia', variable=var, value='sepia')
sepia_option.place(x='380', y='80')
mirror_option = tk.Radiobutton(window, text='Mirror', variable=var, value='mirror')
mirror_option.place(x='380', y='110')
reflect_option = tk.Radiobutton(window, text='Reflect', variable=var, value='reflect')
reflect_option.place(x='380', y='140')
scale_option = tk.Radiobutton(window, text='Scale', variable=var, value='scale')
scale_option.place(x='380', y='170')

s = tk.IntVar()
half_option = tk.Radiobutton(window, text='.5x', variable=s, value=1)
half_option.place(x='400',y='200')
double_option = tk.Radiobutton(window, text='2x', variable=s, value=2)
double_option.place(x='400',y='230')

def new_factor():
    if s.get() == 1:
        factor = 2.0
    if s.get() == 2:
        factor = 0.5
    return factor

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

# conversion action button
process_button = tk.Button(text='PROCESS', command=process)
process_button.place(x='440', y='315')

window.mainloop()