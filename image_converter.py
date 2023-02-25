import glob
import os
import cv2 as cv
from image_functions import *
import tkinter as tk
from tkinter import filedialog as fd

path = os.getcwd()
images = glob.glob("input/*")

# build window
window = tk.Tk()
window.title('Image Converter')
window.resizable(False, False)
window.geometry('700x365')

# input label
input_label = tk.Label(window, text='Input', justify='center')
input_label.place(x='20', y='15')

# file browse
""" def openfile():
    return fd.askopenfile()
open_button = tk.Button(window, text='Open', command=openfile)
open_button.place(x='20', y='315') """

# output label
output_label = tk.Label(window, text='Output', justify='center')
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

factor = 0
def new_factor(factor):
    if s.get() == 1:
        factor = 2.0
    if s.get() == 2:
        factor = 0.5
    return factor

# Create new directory for output
while True:
    if os.path.exists("./output") is True:
        break
    else:
        os.mkdir("./output")

def process():
    for image in images:
        img = cv.imread(image)
        img_name = image[len("input/") :]
        h = img.shape[0]
        w = img.shape[1]

        if var.get() == "grayscale":
            new_name = f"g_{img_name}"
            cv.imwrite(os.path.join(f"{path}/output", new_name), grayscale(img, h, w))
        if var.get() == "sepia":
            new_name = f"s_{img_name}"
            cv.imwrite(os.path.join(f"{path}/output", new_name), sepia(img, h, w))
        if var.get() == "mirror":
            new_name = f"m_{img_name}"
            cv.imwrite(os.path.join(f"{path}/output", new_name), mirror(img, h, w))
        if var.get() == "reflect":
            new_name = f"r_{img_name}"
            flip_img = cv.flip(img, 1)
            cv.imwrite(os.path.join(f"{path}/output", new_name), flip_img)
        if var.get() == "scale":
            new_name = f"sc_{img_name}"
            cv.imwrite(os.path.join(f"{path}/output", new_name), scale(img, h , w, new_factor(factor)))

# conversion action button
conver_button = tk.Button(text='CONVERT', command=process)
conver_button.place(x='440', y='315')

window.mainloop()