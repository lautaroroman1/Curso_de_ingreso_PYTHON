import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Lautaro
apellido: Román
---
TP: While_validaciones_rising_btl
---
Enunciado:
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.txt_tipo = customtkinter.CTkEntry(master=self)
        self.txt_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        apellido = prompt("UTN", "Ingrese su apellido")

        edad = prompt("UTN", "Ingrese su edad")
        edad = int(edad)
        
        while edad < 18 or edad > 91:
            edad = prompt("UTN", "Reingrese su edad")
            edad = int(edad)

        estado_civil = prompt("UTN", "Ingrese su estado civil")

        while estado_civil != "Casado" and estado_civil != "Soltero" and estado_civil != "Viudo" and estado_civil != "Divorciado":
            estado_civil = prompt("UTN", "Reingrese su estado civil")

        numero_legajo = prompt("UTN", "Ingrese su número de legajo")
        numero_legajo = int(numero_legajo)
                
        while numero_legajo < 1000 or numero_legajo > 9999:
            numero_legajo = prompt("UTN", "Reingrese su número de legajo: ")
            numero_legajo = int(numero_legajo)

        self.txt_apellido.delete(0, "end")
        self.txt_edad.delete(0, "end")
        self.txt_tipo.delete(0, "end")
        self.txt_legajo.delete(0, "end")
        
        self.txt_apellido.insert(0, apellido)
        self.txt_edad.insert(0, edad)
        self.txt_tipo.insert(0, estado_civil)
        self.txt_legajo.insert(0, numero_legajo)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
