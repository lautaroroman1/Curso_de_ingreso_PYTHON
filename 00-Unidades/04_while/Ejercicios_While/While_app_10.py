import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Lautaro
apellido: Román
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón 'Comenzar ingreso', solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_positivos = 0
        suma_negativos = 0
        contador_positivos = 0
        contador_negativos = 0
        contador_ceros = 0


        while True:
            numero = prompt("UTN", "Ingrese un número")

            if numero == None:
                break

            else:
                numero = float(numero)

                if numero > 0:
                    suma_positivos += numero
                    contador_positivos += 1

                elif numero < 0:
                    suma_negativos += numero
                    contador_negativos += 1

                else:
                    contador_ceros += 1

        diferencia_cantidad = abs(contador_positivos - contador_negativos)

        mensaje = f"La cantidad de números positivos es: {contador_positivos}.\n La cantidad de números negativos es: {contador_negativos}.\n La suma de los números positivos es: {suma_positivos}. \n La suma de los números negativos es {suma_negativos}.\n La diferencia entre la cantidad de números positivos y negativos es: {diferencia_cantidad}."

        alert("UTN", mensaje)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
