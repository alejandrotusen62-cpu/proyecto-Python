# type:ignore
import tkinter as tk
import os

from dotenv import load_dotenv
load_dotenv()

APP_USER = os.getenv("APP_USER")
APP_PASSWORD = os.getenv("APP_PASSWORD")


def validar_credenciales(usuario, password):
    if usuario == APP_USER and password == APP_PASSWORD:
        label_mensaje.config(text="Acceso correcto", fg="green")
    else:
        label_mensaje.config(text="Usuario o contraseña incorrectos", fg="red")


def capturar_valor():

    valor_usuario = campo_entrada_usuario.get()
    valor_password = campo_entrada_password.get()

    print(f"El valor ingresado es: {valor_usuario}")
    print(f"La contraseña ingresada es: {valor_password}")

    validar_credenciales(valor_usuario, valor_password)


ventana = tk.Tk()
ventana.title("mi primera app en Tkinter")
ventana.geometry("500x500")


# Label usuario
label_usuario = tk.Label(ventana, text="Usuario", font=("Arial",16), fg="red")
label_usuario.pack()

campo_entrada_usuario = tk.Entry(ventana)
campo_entrada_usuario.pack()


# Label password
label_password = tk.Label(ventana, text="Password", font=("Arial",16), fg="blue")
label_password.pack()

campo_entrada_password = tk.Entry(ventana, show="*")
campo_entrada_password.pack()


# Botón
boton = tk.Button(ventana, text="Capturar", command=capturar_valor)
boton.pack()

# Label mensaje
label_mensaje = tk.Label(ventana, text="", font=("Arial", 14))
label_mensaje.pack()

# Bucle principal
ventana.mainloop()