import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Lautaro
apellido: Román
---
Ejercicio: for_08
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Mostrar cada número primo entre 1 y el número ingresado, e informar la cantidad de números primos encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):

        #Resuelto con bandera
        limite = prompt("UTN", "Ingrese un número: ")
        limite = int(limite)

        contador_primos = 0

        for i in range(2, limite+1):

            bandera_divisores = False

            for j in range(2, i):
                if i % j == 0:
                    bandera_divisores = True
                    break
        
            if bandera_divisores == False:
                print(f"Primo: {i}")
                contador_primos += 1

        alert("UTN", f"Cantidad: {contador_primos}")

        """
        #Resuelto con contador
        limite = prompt("UTN", "Ingrese un número: ")
        limite = int(limite)

        contador_primos = 0

        for i in range(2, limite+1):

            contador_divisores = 0

            for j in range(1, i+1):
                if i % j == 0:
                    contador_divisores += 1
        
            if contador_divisores == 2:
                print(f"Primo: {i}")
                contador_primos += 1

        alert("UTN", f"Cantidad: {contador_primos}")

        """

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()