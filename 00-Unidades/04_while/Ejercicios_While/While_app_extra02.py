import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Se nos ha solicitado desarrollar una aplicación para llevar registro de las entradas vendidas en el Estadio River 
Plate, para el concierto de Taylor Swift. Para ello, se solicitará al usuario la siguiente información al momento de 
comprar cada entrada:

Al presionar el boton se debera pedir la carga de los siguientes datos, hasta que el usuario lo desee:

Los datos que deberas pedir para los ventas son:
    * Nombre del comprador
    * Edad (no menor a 16)
    * Género (Masculino, Femenino, Otro)
    * Tipo de entrada (General, Campo delantero, Platea)
    * Medio de pago (Crédito, Efectivo, Débito) 
    * Precio de la entrada (Se debe calcular)

Para cada venta, se calculará el total a pagar en función del tipo de entrada elegida, 
el medio de pago y su precio correspondiente.

 * Lista de precios: 
        * General: $16000
        * Campo:   $25000
        * Platea:  $30000

Las entradas adquiridas con tarjeta de crédito tendrán un 20% de descuento sobre el 
precio de la entrada, mientras que las adquiridas con tarjeta de débito un 15%. 

Al finalizar la carga, el programa debera mostrar los siguientes informes:

    #! 1) - Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo".
    #! 2) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta 
    #!          de crédito y su edad promedio.
    #! 3) - Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y 
    #!          pagaron con tarjeta de débito  respecto al total de personas en la lista. TODAS
    #! 4) - Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de 
    #!          los aplicados a tarjetas de crédito MONTO TOTAL
    #! 5) - El nombre y la edad de la persona que pagó el precio más alto por una entrada de 
    #!          tipo "General" y pagó con tarjeta de débito (Solo la primera que se encuentre)
    #! 6) - La cantidad de personas que compraron entradas de tipo "Platea" y cuya 
    #!          edad es un número primo.
    #! 7) - Calcula el monto total recaudado por la venta de entradas de tipo "Platea" y 
    #!          pagadas con tarjeta de debito por personas cuyas edades son múltiplos de 6.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        seguir_ingresando = True

        contador_campo_masculino = 0
        contador_campo_femenino = 0
        contador_campo_otro = 0
        mayor_genero_campo = 0

        contador_general_credito = 0
        acumulador_edades_credito = 0

        while seguir_ingresando:
            nombre_comprador = prompt("Datos", "Ingrese su nombre: ")

            edad = prompt("Datos", "Ingrese su edad: ")
            edad = int(edad)

            while edad < 16:
                edad = prompt("Datos", "Ingrese su edad: ")
                edad = int(edad)

            genero = prompt("Datos", "Ingrese su género (Masculino, Femenino, Otro): ")

            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = prompt("Datos", "Ingrese su género (Masculino, Femenino, Otro): ")

            tipo_entrada = prompt("Datos", "Tipo de entrada (General, Campo, Platea): ")

            while tipo_entrada != "General" and tipo_entrada != "Campo" and tipo_entrada != "Platea":
                tipo_entrada = prompt("Datos", "Tipo de entrada (General, Campo, Platea): ")

            medio_de_pago = prompt("Datos", "Ingrese su medio de pago (Credito, Efectivo, Debito): ")
            
            while medio_de_pago != "Credito" and medio_de_pago != "Efectivo" and medio_de_pago != "Debito":
                medio_de_pago = prompt("Datos", "Ingrese su medio de pago (Credito, Efectivo, Debito): ")

            

            match tipo_entrada:
                case "General":
                    valor_entrada = 16000

                    if medio_de_pago == "Credito":
                        contador_general_credito += 1
                        acumulador_edades_credito += edad


                case "Campo":
                    valor_entrada = 25000

                    match genero:
                        case "Masculino":
                            contador_campo_masculino += 1

                        case "Femenino":
                            contador_campo_femenino += 1

                        case "Otro":
                            contador_campo_otro += 1

                case "Platea":
                    valor_entrada = 30000


            if medio_de_pago == "Credito":
                descuento_entrada = 20

            elif medio_de_pago == "Debito":
                descuento_entrada = 15

            else:
                descuento_entrada = 0




            seguir_ingresando = question("Continuar", "¿Desea seguir ingresando datos?")

        if contador_campo_masculino > contador_campo_femenino and contador_campo_masculino > contador_campo_otro:
            mayor_genero_campo = "Masculino"

        elif contador_campo_femenino > contador_campo_otro:
            mayor_genero_campo = "Femenino"

        else:
            mayor_genero_campo = "Otro"

        promedio_edad_credito = acumulador_edades_credito / contador_general_credito


        mensaje = f"1) Género más frecuente que compró entradas de tipo 'Campo': {mayor_genero_campo} \n 2) Cantidad de personas que compraron entradas de tipo 'General' con tarjeta de crédito: {contador_general_credito}, edad promedio de estas personas: {promedio_edad_credito} \n 3)"
        alert("", mensaje)
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()