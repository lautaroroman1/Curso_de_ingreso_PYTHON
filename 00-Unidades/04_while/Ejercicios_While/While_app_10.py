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
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). #

Luego calcular:
    A. La suma acumulada de los negativos

    B. La suma acumulada de los positivos

    C. Cantidad de números positivos ingresados

    D. Cantidad de números negativos ingresados
    
    E. Cantidad de ceros

    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

    G. El maximo. Solo uno

    H. El minimo valor (incluyendo en que iteracion se encontro, solo la primera)

    Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
    
        numeros_negativos = 0
        cantidad_negativa = 0

        numero_postiva = 0
        cantidad_positiva = 0

        contador_cero = 0

        numero_maximo = 0
        numero_minimo = 0

        bandera_primer_ingreso = True

        contador_primer_minimo = 0
        iteracion_primer_minimo = 0


        while True:
            contador_primer_minimo += 1

            numero = prompt("UTN", "Ingrese un numero")
            
            if numero == None:
                break

            numero = float(numero)

            if numero < 0:
                numeros_negativos += numero   
                cantidad_negativa += 1

            elif numero > 0:
                numero_postiva += numero
                cantidad_positiva += 1 

            else:
                contador_cero += 1

            if numero > numero_maximo or bandera_primer_ingreso == True:
                numero_maximo = numero
                
            if numero < numero_minimo or bandera_primer_ingreso == True:
                numero_minimo = numero
                bandera_primer_ingreso = False
                
                iteracion_primer_minimo = contador_primer_minimo
                

        diferencia = abs(cantidad_negativa - cantidad_positiva)
        
        mensaje = f"La suma de números de numeros negativos es: {numeros_negativos} \n La cantidad de numeros negativos es: {cantidad_negativa} \n La suma de números positivos es: {numero_postiva} \n La cantidad de números positivos es: {cantidad_positiva} \n Hay {contador_cero} ceros. \n La diferencia entre la cantidad de numeros positivos y negativos es: {diferencia}. \n El numero mayor es: {numero_maximo}. El número menor es {numero_minimo}. \n El número menor se encontró en la {iteracion_primer_minimo} iteración"
        alert("UTN", mensaje)


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

