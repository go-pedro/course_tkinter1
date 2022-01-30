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

#add a funtion trigger by button
def button_clicked():
	print('Button clicked')



# place a label on the root window
message = tk.Label(root, text="Hello, World!")
message.pack()

#label 2 in the root
message_2=ttk.Label(root, text='Themed Label')
message_2.pack()


#button with trigger comand
button=ttk.Button(root,text='Clicked me', command=button_clicked)
button.pack()

# keep the window displaying
root.mainloop()