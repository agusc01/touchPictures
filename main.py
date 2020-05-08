from tkinter import *
from tkinter import filedialog

def openFile():
	filesType=(
		("All","*.*")
		,("GIF","*.gif")
		,("TIFF","*.tif;*.tiff")
		,("HEIC","*.heic")
		,("JPEG","*.jpg;*.jpeg;*.jpe;*.jfif")
		,("PNG","*.png")
		,("WEBP","*.webp")
		)
	nameTitle="Open"

	path=filedialog.askopenfilename(title=nameTitle, initialdir=".",filetypes=filesType)
	print(path)

root=Tk()
root.title("Touch Pictures !")
root.geometry('350x350')

Button(root,text="Add image",command=openFile).pack()

root.mainloop()