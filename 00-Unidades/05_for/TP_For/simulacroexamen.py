import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

"""
Un famoso casino de mar del plata,  requiere una app para controlar el egreso de dinero durante una jornada. Para ello se ingresa por cada ganador:

    -Nombre
    -Importe ganado (mayor o igual $1000)
    -Género (“Femenino”, “Masculino”, “Otro”)
    -Juego (Ruleta, Poker, Tragamonedas)

Necesitamos saber:

    1) Nombre y género de la persona que más ganó.
    2) Promedio de dinero ganado en Ruleta.
    3) Porcentaje de personas que jugaron en el Tragamonedas.
    4) Cuál es el juego menos elegido por los ganadores.
    5) Promedio de importe ganado de las personas que NO jugaron Poker, siempre y cuando el importe supere los $15000
    6) Porcentaje de dinero en función de cada juego.
"""

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):

        seguir_ingresando = True

        maximo_ganador = 0
        bandera_maximo = False

        acumulador_ruleta = 0
        contador_ruleta = 0

        contador_tragamonedas = 0
        contador_personas = 0

        contador_poker = 0

        contador_NO_poker = 0
        acumulador_NO_poker = 0

        acumulador_poker = 0
        acumulador_tragamonedas = 0

        while seguir_ingresando:

            contador_personas += 1

            nombre = prompt("Datos", "Ingrese su nombre: ")
            
            importe = prompt("Datos", "Importe ganado: ")
            importe = float(importe)

            while importe < 1000:
                importe = prompt("Datos", "Reingrese el importe ganado (no menor a 1000): ")
                importe = float(importe)

            genero = prompt("Datos", "Ingrese su género")

            while genero != "Femenino" and genero != "Masculino" and genero != "Otro":
                genero = prompt("Datos", "Reingrese su género")

            tipo_juego = prompt("Datos", "Tipo de juego (Ruleta, Poker, Tragamonedas): ")

            while tipo_juego != "Ruleta" and tipo_juego != "Poker" and tipo_juego != "Tragamonedas":
                tipo_juego = prompt("Datos", "Reingrese el tipo de juego (Ruleta, Poker, Tragamonedas): ")

            if importe > maximo_ganador or bandera_maximo == False:
                maximo_ganador = importe
                nombre_maximo = nombre
                genero_maximo = genero
                bandera_maximo = True

            match tipo_juego:
                case "Ruleta":
                    contador_ruleta += 1
                    acumulador_ruleta += importe

                case "Poker":
                    contador_poker += 1
                    acumulador_poker += importe

                case "Tragamonedas":
                    contador_tragamonedas += 1
                    acumulador_tragamonedas += importe

            seguir_ingresando = question("Continuar", "¿Desea seguir ingresando datos?")

        if contador_ruleta < contador_poker and contador_ruleta < contador_tragamonedas:
            menos_elegido = "Ruleta"

        elif contador_poker < contador_tragamonedas:
            menos_elegido = "Poker"

        else:
            menos_elegido = "Tragamonedas"

        if importe > 15000 and tipo_juego != "Poker":
            contador_NO_poker += 1
            acumulador_NO_poker += importe


        importe_total = (acumulador_poker + acumulador_ruleta + acumulador_tragamonedas)

        porcentaje_dinero_ruleta = acumulador_ruleta * 100 / importe_total
        porcentaje_dinero_poker = acumulador_poker * 100 / importe_total
        porcentaje_dinero_tragamonedas = acumulador_tragamonedas * 100 / importe_total

        if contador_ruleta > 1:
            promedio_ruleta = acumulador_ruleta / contador_ruleta

        else:
            promedio_ruleta = "No se ingresó Ruleta"

        porcentaje_tragamonedas = contador_tragamonedas * 100 / contador_personas

        if contador_NO_poker > 1:
            promedio_NO_poker = acumulador_NO_poker / contador_NO_poker
        
        else:
            promedio_NO_poker = "Sólo se jugó Poker o no se superaron los 15000"

        mensaje = f"1)Nombre y género de la persona que mas ganó: {nombre_maximo}, {genero_maximo} \n 2) Promedio de dinero ganado en ruleta: {promedio_ruleta} \n 3) Porcentaje de personas que jugaron en el Tragamonedas: {porcentaje_tragamonedas}% \n 4) Cuál es el juego menos elegido por los ganadores: {menos_elegido} \n 5) Promedio de importe ganado de las personas que NO jugaron Poker, siempre y cuando el importe supere los $15000: {promedio_NO_poker} \n 6) Porcentaje de dinero en función de cada juego: \n Ruleta: {porcentaje_dinero_ruleta}%, Poker: {porcentaje_dinero_poker}%, Tragamonedas: {porcentaje_dinero_tragamonedas}%"

        alert("Resultados", mensaje)




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
