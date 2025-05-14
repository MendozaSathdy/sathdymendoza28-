import tkinter as tk
import math

ventana = tk.Tk()
ventana.title("Área y perímetro del círculo ")
ventana.geometry("400x350")
ventana.configure(bg="blue")

etiqueta = tk.Label(ventana, text="Dame el radio del círculo: ", bg="blue")
etiqueta.pack()
entrada = tk.Entry(ventana)
entrada.pack()

etiqueta_resultado = tk.Label(ventana, text="", bg="blue")
etiqueta_resultado.pack()
etiqueta_comparacion = tk.Label(ventana, text="", bg="blue")
etiqueta_comparacion.pack()
etiqueta_comparacion2 = tk.Label(ventana, text="", bg="blue")
etiqueta_comparacion2.pack()

boton = tk.Button(ventana, text="Calcular", command=lambda: [
    etiqueta_resultado.config(text=f"El área es: {3.1416 * (float(entrada.get()) ** 2):.2f} y el perímetro es: {(2 * 3.1416 * float(entrada.get())):.2f}") if entrada.get().replace('.', '', 1).isdigit() else etiqueta_resultado.config(text="Ingresa un valor"),
    etiqueta_comparacion.config(text="Esta área es grande") if entrada.get().replace('.', '', 1).isdigit() and 3.1416 * (float(entrada.get()) ** 2) > 100 else etiqueta_comparacion.config(text=""),
    etiqueta_comparacion2.config(text="Esta área es pequeña") if entrada.get().replace('.', '', 1).isdigit() and 3.1416 * (float(entrada.get()) ** 2) <= 100 else etiqueta_comparacion2.config(text="")
])
boton.pack()

boton_limpiar = tk.Button(ventana, text="Limpiar y repetir", command=lambda: [
    entrada.delete(0, tk.END),
    etiqueta_resultado.config(text=""),
    etiqueta_comparacion.config(text=""),
    etiqueta_comparacion2.config(text="")
])
boton_limpiar.pack()

ventana.mainloop()