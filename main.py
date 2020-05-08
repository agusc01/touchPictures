from tkinter import *
from tkinter import filedialog
from PIL import Image


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
	# print(path)

	# ===========================================
	# ======== ACA OBTENGO EL NOMBRE DEL ARCHIVO
	# auxPath tiene el string del path invertido
	"""
	auxPath=path[::-1]
	nameFile=""
	for c in auxPath:
		if c == '/' or c =='\\':
			break
		nameFile+=c

	nameFile=nameFile[::-1]
	# Aca nameFile tiene el nombre del archivo
	print(nameFile)
	"""
	# ===========================================

	# ===========================================
	# ======== CREO UN STRING CON .webp
	fileNewExtend=""
	for c in path:
		if c == '.':
			break
		fileNewExtend+=c
	fileNewExtend+=".webp"
	print(fileNewExtend) 
	# ===========================================

	imagen = Image.open(path)
	imagen.save(fileNewExtend)

	print("Done!")

root=Tk()
root.title("Touch Pictures !")
root.geometry('350x70')
btn=Button(root,text="Add image",command=openFile).pack()
root.mainloop()