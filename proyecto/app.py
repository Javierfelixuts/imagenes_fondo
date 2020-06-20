from tkinter import *
from tkinter import ttk


class PantallaInicial():
	def __init__(self, window):
		self.window = window
		self.miFrame=Frame(self.window)
		self.miFrame.pack()

	def armarpantalla(self):
		self.botonCobertura=Button(self.miFrame, text="Buscar", width=8, height=0, command=lambda:cobertura().pantalla())
		self.botonCobertura.grid(row=0, column=0,  sticky="w", padx=10)


class cobertura():
	def __init__(self):
		self.rootcob_inicial=Toplevel()
		self.miFramecob=Frame(self.rootcob_inicial)
		self.miFramecob.grid(row=0,column=0)
		self.cuadro_cobertura=StringVar()

	def pantalla(self):
		self.EntradaDES=Entry(self.miFramecob,  width=30, textvariable=self.cuadro_cobertura)
		self.EntradaDES.grid(row=2, column=1, padx=10, pady=10)

		self.botonImprimir=Button(self.miFramecob, text="Imprimir", command=self.imprimir)
		self.botonImprimir.grid(row=3, column=2,  sticky="e", padx=10, pady=10)

		self.rootcob_inicial.mainloop()

	def imprimir(self):
		print(self.cuadro_cobertura.get())
		print("hola")


window=Tk()
prueba=PantallaInicial(window)
prueba.armarpantalla()

window.mainloop()