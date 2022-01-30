#course tkinter on pythontutorial.net 

#import packages
import tkinter as tk

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


# place a label on the root window
message = tk.Label(root, text="Hello, World!")
message.pack()

# keep the window displaying
root.mainloop()