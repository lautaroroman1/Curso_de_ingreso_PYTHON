import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar en la bolsa de 
valores:

Para ello deberás programar el botón  para poder cargar 10 operaciones de compra con los siguientes datos:
    * Nombre
    * Monto en pesos de la operación (no menor a $10000)
    * Tipo de instrumento(CEDEAR, BONOS, MEP) 
    * Cantidad de instrumentos  (no menos de cero) 
    
Realizar los siguientes informes:

    #! 1) - Tipo de instrumento que menos se operó en total. --
    #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP --
    #! 3) - Cantidad de usuarios que no compraron CEDEAR --
    #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR --
    #! 5) - Nombre y posicion del usuario que invirtio menos dinero --
    #! 6) - Promedio de dinero en CEDEAR  ingresado en total. --
    #! 7) - Promedio de cantidad de instrumentos  MEP vendidos en total

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        contador_datos = 1

        contador_CEDEAR = 0
        contador_BONOS = 0
        contador_MEP = 0

        contador_usuarios_MEP = 0

        contador_NO_CEDEAR = 0

        bandera_primer_BONOS_CEDEAR = False
        cantidad_BONOS_CEDEAR = 0

        bandera_minimo = False
        minimo_dinero = 0
        posicion_minimo_dinero = 0

        acumulador_CEDEAR = 0

        acumulador_MEP = 0

        while contador_datos <= 10:

            nombre = input("Ingrese su nombre: ")

            monto = input("Monto en pesos de la operación: ")
            monto = float(monto)

            while monto < 10000:
                monto = input("Reingrese el monto en pesos de la operación: ")
                monto = float(monto)
    
            tipo_instrumento = input("Ingrese el tipo de instrumento (CEDEAR, BONOS, MEP): ")

            while tipo_instrumento != "CEDEAR" and tipo_instrumento != "BONOS" and tipo_instrumento != "MEP":
                tipo_instrumento = input("Reingrese el tipo de instrumento (CEDEAR, BONOS, MEP): ")

            cantidad_instrumentos = input("Ingrese la cantidad de instrumentos: ")
            cantidad_instrumentos = int(cantidad_instrumentos)

            while cantidad_instrumentos < 0:
                cantidad_instrumentos = input("Ingrese la cantidad de instrumentos: ")
                cantidad_instrumentos = int(cantidad_instrumentos)

            match tipo_instrumento:
                case "CEDEAR":
                    contador_CEDEAR += 1
                    acumulador_CEDEAR += monto

                    if bandera_primer_BONOS_CEDEAR == False:
                        nombre_BONOS_CEDEAR = nombre
                        cantidad_BONOS_CEDEAR = cantidad_instrumentos
                        bandera_primer_BONOS_CEDEAR == True

                case "BONOS":
                    contador_BONOS += 1
                    contador_NO_CEDEAR += 1

                    if cantidad_instrumentos > 50 and cantidad_instrumentos < 200:
                        contador_usuarios_MEP += 1

                    if bandera_primer_BONOS_CEDEAR == False:
                        nombre_BONOS_CEDEAR = nombre
                        cantidad_BONOS_CEDEAR = cantidad_instrumentos
                        bandera_primer_BONOS_CEDEAR == True

                case "MEP":
                    contador_MEP += 1
                    contador_NO_CEDEAR += 1

                    acumulador_MEP += monto

            if monto < minimo_dinero or bandera_minimo == False:
                minimo_dinero = monto
                bandera_minimo == True
                nombre_minimo = nombre
                posicion_minimo_dinero = contador_datos

            contador_datos += 1

        

        if contador_BONOS < contador_CEDEAR and contador_BONOS < contador_MEP:
            minimo_instrumento = "BONOS"

        elif contador_CEDEAR < contador_MEP:
            minimo_instrumento = "CEDEAR"

        else:
            minimo_instrumento = "MEP"

        promedio_CEDEAR = acumulador_CEDEAR / contador_CEDEAR

        promedio_MEP = acumulador_MEP / contador_MEP

        


        mensaje = f"1) Tipo de instrumento que menos se operó: {minimo_instrumento} \n 2) Cantidad de usuarios que compraron entre 50 y 200 MEP: {contador_usuarios_MEP} \n 3) Cantidad de usuarios que no compraron CEDEAR: {contador_NO_CEDEAR} \n 4) Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR: {nombre_BONOS_CEDEAR}, {cantidad_BONOS_CEDEAR} \n 5) Nombre y posicion del usuario que invirtio menos dinero: {nombre_minimo}, {posicion_minimo_dinero}° \n 6) Promedio de dinero en CEDEAR  ingresado en total: {promedio_CEDEAR} \n 7) Promedio de cantidad de instrumentos MEP vendidos en total: {promedio_MEP}"

        alert("UTN", mensaje)


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()