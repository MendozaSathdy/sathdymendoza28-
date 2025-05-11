import tkinter as tk

def suma():
    valoa = int(entrada_prim.get())
    valorb = int(entrada_seg.get())
    resultado = valoa + valorb
    etiqueta_resultado.config(text=f"resultado de la suma es {resultado}") 

def resta():
    valoa = int(entrada_prim.get())  
    valorb = int(entrada_seg.get())
    resultado = valoa - valorb
    etiqueta_resultado.config(text=f" resultado de la resta es {resultado}")
  
ventana = tk.Tk()
ventana.title("operacion de suma y resta ")
ventana.geometry("400x200")


etiqueta = tk.Label(ventana, text="Ingresa tu primer valor:")
etiqueta.pack()

entrada_prim = tk.Entry(ventana)
entrada_prim.pack()

etiqueta = tk.Label(ventana, text="ingresa tu segundo valor: ")
etiqueta.pack()

entrada_seg = tk.Entry(ventana)
entrada_seg.pack()

boton = tk.Button(ventana, text="suma", command=suma)
boton.pack()

boton = tk.Button(ventana, text="resta", command=resta)
boton.pack()


etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()


ventana.mainloop()