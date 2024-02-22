import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:  
apellido: 
---
Ejercicio: while_10
---
Enunciado:
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
que promete revolucionar el mercado. 
Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT) o 
# Procesamiento de lenguaje natural (NLP).

Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT)   

En esta opción, se ingresaran empleados hasta que el usuario lo desee.

Una vez finalizado el ingreso, mostrar:

    #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #!X 2) - Tecnología que mas se votó.
    #!X 3) - Porcentaje de empleados por cada genero
    #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")

    def btn_comenzar_ingreso_on_click(self):
        seguir_ingresando = True

        contador_masculino_IA_IOT = 0
        contador_IOT_edad = 0

        contador_IA = 0
        contador_IOT = 0
        contador_RV_RA = 0

        contador_masculino = 0
        contador_femenino = 0
        contador_otro = 0

        contador_femenino_IA = 0
        acumulador_edad_femenino = 0

        bandera_minimo = False
        minimo_RV_RA = 0


        while seguir_ingresando:
            nombre = input("Ingrese su nombre: ")

            edad = input("Ingrese su edad: ")
            edad = int(edad)

            while edad < 18:
                edad = input("Reingrese su edad: ")
                edad = int(edad)

            genero = input("Ingrese su género: Masculino, Femenino u Otro ")

            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = input("Reingrese su género: Masculino, Femenino u Otro ")

            tecnologia = input("Ingrese tecnología: IA, RV/RA, IOT")
            
            while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
                tecnologia = input("Reingrese tecnología: IA, RV/RA, IOT ")

            match tecnologia:
                case "IA":
                    contador_IA += 1

                case "IOT":
                    contador_IOT += 1

                    if (edad > 18 and edad < 25) or edad > 33 and edad < 42:
                        contador_IOT_edad += 1

                case "RV/RA":
                    contador_RV_RA += 1

                    if edad < minimo_RV_RA or bandera_minimo == False:
                        minimo_RV_RA = edad
                        bandera_minimo = True

                        nombre_minimo = nombre
                        genero_minimo = genero

            match genero:
                case "Masculino":
                    contador_masculino += 1
                    
                    if (tecnologia == "IOT" or tecnologia == "IA") and edad >= 25 and edad <= 50:
                        contador_masculino_IA_IOT += 1
                
                case "Femenino":
                    contador_femenino += 1

                    if tecnologia == "IA":
                        contador_femenino_IA += 1
                        acumulador_edad_femenino += edad

                case "Otro":
                    contador_otro += 1

            seguir_ingresando = question("Continuar", "¿Desea seguir ingresando datos?: ")

        if contador_IA > contador_IOT and contador_IA > contador_RV_RA:
            print("2. Se voto más IA")

        elif contador_IOT > contador_RV_RA:
            print("2. Se voto más IOT")

        else:
            print("2. Se voto más RV/RA")

        total_empleados = contador_masculino + contador_femenino + contador_otro

        porcentaje_masculino = (contador_masculino * 100) / total_empleados
        porcentaje_femenino = (contador_femenino * 100) / total_empleados
        porcentaje_otro = 100 - (porcentaje_masculino + porcentaje_femenino)

        porcentaje_IOT_edad =  (contador_IOT_edad * 100) / contador_IOT

        if contador_femenino_IA > 0:
            promedio_femenino_ia = acumulador_edad_femenino / contador_femenino_IA

        else:
            promedio_femenino_ia = 0
        
        print(f"1. Cantidad de empleados de género masculino que votaron por IA/IOT entre 25 y 50 años: {contador_masculino_IA_IOT}")
        print(f"3. Porcentajes de género: \n Masculino: {porcentaje_masculino}% \n Femenino: {porcentaje_femenino}% \n Otro: {porcentaje_otro}%")
        print(f"4. Pocentaje de empleados que votaron por IOT entre 18 y 25 o 33 y 42 años (en base a los empleados que votaron por IOT): {porcentaje_IOT_edad}%")
        print(f"5. Promedio de empleadas femeninas que votaron por IA: {promedio_femenino_ia}")
        print(f"6. Nombre y género del empleado más joven que votó por RV/RA: {nombre_minimo}, {genero_minimo}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()