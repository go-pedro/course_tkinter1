#course tkinter on pythontutorial.net 

#import packages
import tkinter as tk

#create the root window
root = tk.Tk()

#add title
root.title('Tkinter Window Demo')


# place a label on the root window
message = tk.Label(root, text="Hello, World!")
message.pack()

# keep the window displaying
root.mainloop()