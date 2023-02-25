import tkinter as tk
from tkinter import filedialog as fd

# build window
window = tk.Tk()
window.title('Image Converter')
window.resizable(False, False)
window.geometry('700x365')

# input label
input_label = tk.Label(window, text='Input', justify='center')
input_label.place(x='20', y='15')

# file browse
def openfile():
    return fd.askopenfilenames()
open_button = tk.Button(window, text='Open', command=openfile)
open_button.place(x='20', y='315')

# output label
output_label = tk.Label(window, text='Output', justify='center')
output_label.place(x='380', y='15')

# options buttons
var = tk.IntVar()
gray_option = tk.Radiobutton(window, text='Grayscale', variable=var, value=1)
gray_option.place(x='380', y='50')
sepia_option = tk.Radiobutton(window, text='Sepia', variable=var, value=2)
sepia_option.place(x='380', y='80')
mirror_option = tk.Radiobutton(window, text='Mirror', variable=var, value=3)
mirror_option.place(x='380', y='110')
reflect_option = tk.Radiobutton(window, text='Reflect', variable=var, value=4)
reflect_option.place(x='380', y='140')
scale_option = tk.Radiobutton(window, text='Scale', variable=var, value=5)
scale_option.place(x='380', y='170')

# conversion action button
conver_button = tk.Button(text='CONVERT')
conver_button.place(x='440', y='315')

window.mainloop()
