#course tkinter on pythontutorial.net 

#import packages
import tkinter as tk
from tkinter import ttk

#create the root window
root = tk.Tk()

#add title
root.title('Tkinter Window Demo')

#add window dimensions
root.geometry('600x400+50+50')
root.resizable(False, False) #if both width and height can not be resize

# #if window can be resizable
# root.minsize(min_width, min_height)
# root.maxsize(min_height, max_height)

root.iconbitmap('./img/pedras.ico')

#show a Label 
label=ttk.Label(root,text='this is a label')
label.pack(ipadx=10,ipady=10)

#show a Label with text formated
label=ttk.Label(root,text='this is a label in helvetica 14',font=('Helvetica',14))
label.pack(ipadx=10,ipady=10)


#displaying an image as in Label
photo=tk.PhotoImage(file='./img/pitao.png')
image_label=ttk.Label(root, text='Python', image=photo, padding=5, compound='top')
image_label.pack()


# keep the window displaying
root.mainloop()