import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Lautaro
apellido: Román
---
Ejercicio: for_07
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = prompt("UTN", "Ingrese un número: ")
        numero = int(numero)

        bandera_divisor = False

        for i in range(2, numero):
            if numero % i == 0:
                bandera_divisor = True
                break

        if bandera_divisor == False:
            mensaje = "Es primo"

        else:
            mensaje = "No es primo"

        """"
        for i in range(1, numero+1):
            if numero % i == 0:
                contador += 1
        
        if contador == 2:
            mensaje = "Es primo"

        else:
            mensaje = "No es primo"
        """

        alert("UTN", mensaje)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()