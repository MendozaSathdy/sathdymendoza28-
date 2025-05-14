import tkinter as tk
import math

def operacion():
    radio = float(entrada.get())
    area = 3.1416 * (radio ** 2)
    perimetro = 2 * 3.1416 * radio
    etiqueta_resultado.config(text=f"El área es: {area:.2f} y el perímetro es: {perimetro:.2f}")
    if area > 100:
        etiqueta_comparacion.config(text=f"El área es grande")
        etiqueta_comparacion2.config(text="")
    else:
        etiqueta_comparacion2.config(text=f"El área es pequeña")
        etiqueta_comparacion.config(text="")

def limpiar():
    entrada.delete(0, tk.END)
    etiqueta_resultado.config(text="")
    etiqueta_comparacion.config(text="")
    etiqueta_comparacion2.config(text="")

ventana = tk.Tk()
ventana.title("Área y perímetro del círculo :)")
ventana.geometry("400x350")
ventana.configure(bg="green")

etiqueta = tk.Label(ventana, text="Dame el radio del círculo: ", bg="green")
etiqueta.pack()
entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Calcula", command=operacion)
boton.pack()

boton_limpiar = tk.Button(ventana, text="Limpiar y repetir", command=limpiar)
boton_limpiar.pack()

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

etiqueta_comparacion = tk.Label(ventana, text="")
etiqueta_comparacion.pack()

etiqueta_comparacion2 = tk.Label(ventana, text="")
etiqueta_comparacion2.pack()

ventana.mainloop()