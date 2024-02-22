import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Lautaro
apellido: Román
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        
        seguir_ingresando = True

        minimo_votado = 0
        maximo_votado = 0
        bandera_candidato = False

        suma_edades = 0
        contador_candidatos = 0

        total_votos = 0

        while seguir_ingresando:
            nombre = prompt("UTN", "Ingrese su nombre: ")

            edad = prompt("UTN", "Ingrese su edad: ")
            edad = int(edad)

            while edad < 25:
                edad = prompt("UTN", "Reingrese su edad: ")
                edad = int(edad)

            cantidad_votos = prompt("UTN", "Ingrese la cantidad de votos: ")
            cantidad_votos = int(cantidad_votos)

            while cantidad_votos < 0:
                cantidad_votos = prompt("UTN", "Reingrese la cantidad de votos (no puede ser menor a 0): ")
                cantidad_votos = int(cantidad_votos)

            if cantidad_votos < minimo_votado or bandera_candidato == False:
                minimo_votado = cantidad_votos
                candidato_menos_votado = nombre
                edad_menos_votado = edad
            
            if cantidad_votos > maximo_votado or bandera_candidato == False:
                maximo_votado = cantidad_votos
                bandera_candidato = True

                candidato_mas_votado = nombre

            suma_edades += edad
            contador_candidatos += 1
            total_votos += cantidad_votos


            seguir_ingresando = question("UTN", "Desea seguir ingresando datos?")

        promedio_edades = suma_edades / contador_candidatos

        mensaje = f"Nombre del candidato con más votos: {candidato_mas_votado} \n Nombre y edad del candidatos menos votado: {candidato_menos_votado}, {edad_menos_votado} \n Promedio de edades de los candidatos: {promedio_edades} \n Total de votos emitidos: {total_votos}"

        alert("UTN", mensaje)
            


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
