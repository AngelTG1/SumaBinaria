import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime

def sumar_binarios():
    # Obtener los valores de las entradas
    binario1 = entry_binario1.get()
    binario2 = entry_binario2.get()
    
    # Validar que las entradas sean binarios válidos
    if not (es_binario(binario1) and es_binario(binario2)):
        messagebox.showerror("Error", "Ingrese números binarios válidos.")
        return

    # Convertir a enteros, sumar y volver a binario
    suma = bin(int(binario1, 2) + int(binario2, 2))[2:]  # Convierte a binario y quita el prefijo '0b'
    messagebox.showinfo("Resultado", f"La suma de {binario1} + {binario2} es: {suma}")

def es_binario(cadena):
    # Validar si una cadena es binaria
    return all(char in '01' for char in cadena)

def guardar_resultado():
    # Guardar el resultado en un archivo de texto
    binario1 = entry_binario1.get()
    binario2 = entry_binario2.get()
    if not (es_binario(binario1) and es_binario(binario2)):
        messagebox.showerror("Error", "Ingrese números binarios válidos antes de guardar.")
        return

    suma = bin(int(binario1, 2) + int(binario2, 2))[2:]
    resultado = f"La suma de {binario1} + {binario2} es: {suma}"
    archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if archivo:
        with open(archivo, "w") as file:
            file.write(resultado)
        messagebox.showinfo("Guardado", "Resultado guardado correctamente.")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Suma de Binarios")
ventana.geometry("300x200")

# Etiquetas y entradas
tk.Label(ventana, text="Primer número binario:").pack(pady=5)
entry_binario1 = tk.Entry(ventana)
entry_binario1.pack()

tk.Label(ventana, text="Segundo número binario:").pack(pady=5)
entry_binario2 = tk.Entry(ventana)
entry_binario2.pack()

# Botones
tk.Button(ventana, text="Sumar", command=sumar_binarios).pack(pady=10)
tk.Button(ventana, text="Guardar Resultado", command=guardar_resultado).pack()

# Ejecutar ventana
ventana.mainloop()
