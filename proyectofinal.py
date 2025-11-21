import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# -------------------------
# FUNCIONES (NO SE TOCAN)
# -------------------------
def abrir_registro_productos():
    reg = tk.Toplevel()
    reg.title("Registro de Productos")
    reg.geometry("400x400")
    reg.resizable(False, False)
    
       # --- Etiquetas y Campos de Texto ---
    lbl_id = tk.Label(reg, text="ID del Producto:", font=("Arial", 12))
    lbl_id.pack(pady=5)
    txt_id = tk.Entry(reg, font=("Arial", 12))
    txt_id.pack(pady=5)
    lbl_desc = tk.Label(reg, text="Descripción:", font=("Arial", 12))
    lbl_desc.pack(pady=5)
    txt_desc = tk.Entry(reg, font=("Arial", 12))
    txt_desc.pack(pady=5)
    lbl_precio = tk.Label(reg, text="Precio:", font=("Arial", 12))
    lbl_precio.pack(pady=5)
    txt_precio = tk.Entry(reg, font=("Arial", 12))
    txt_precio.pack(pady=5)
    lbl_categoria = tk.Label(reg, text="Categoría:", font=("Arial", 12))
    lbl_categoria.pack(pady=5)
    txt_categoria = tk.Entry(reg, font=("Arial", 12))
    txt_categoria.pack(pady=5)

   # --- Función para guardar ---
    def guardar_producto():
      id_prod = txt_id.get().strip()
      descripcion = txt_desc.get().strip()
      precio = txt_precio.get().strip()
      categoria = txt_categoria.get().strip()
      # Validaciones
      if id_prod == "" or descripcion == "" or precio == "" or categoria == "":
         messagebox.showwarning("Campos Vacíos", "Por favor complete todos los campos.")
         return
      # Validar precio como número
      try:
         float(precio)
      except:
         messagebox.showerror("Error", "El precio debe ser un número.")
         return

      # Guardar en archivo de texto
      BASE_DIR = os.path.dirname(os.path.abspath(__file__))
      archivo = os.path.join(BASE_DIR,"productos.txt")
      with open(archivo, "a", encoding="utf-8") as archivo:
         archivo.write(f"{id_prod}|{descripcion}|{precio}|{categoria}\n")
         messagebox.showinfo("Guardado", "Producto registrado correctamente.")
         # Limpiar campos
         txt_id.delete(0, tk.END)
         txt_desc.delete(0, tk.END)
         txt_precio.delete(0, tk.END)
         txt_categoria.delete(0, tk.END)
   # --- Botón Guardar ---
    btn_guardar = tk.Button(reg, text="Guardar Producto", command=guardar_producto)
    btn_guardar.pack(pady=20)

def abrir_reportes():
    messagebox.showinfo("Reportes", "Aquí irá el módulo de reportes.")

def abrir_registro_ventas():
    messagebox.showinfo("Registro de Ventas", "Aquí irá el módulo de registro de ventas.")

def abrir_acerca_de():
    messagebox.showinfo("Acerca de", "Punto de Venta de Ropa\nProyecto Escolar\nVersión 1.0")


# -------------------------
# VENTANA PRINCIPAL
# -------------------------
ventana = tk.Tk()
ventana.title("Punto de Venta - Ropa")
ventana.geometry("500x600")
ventana.resizable(False, False)

# Fondo verde menta claro
ventana.configure(bg="#D8F3DC")


# -------------------------
# LOGO
# -------------------------
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    imagen = Image.open(os.path.join(BASE_DIR, "ventas2025.png"))
    imagen = imagen.resize((250, 250))
    img_logo = ImageTk.PhotoImage(imagen)

    lbl_logo = tk.Label(ventana, image=img_logo, bg="#D8F3DC")
    lbl_logo.pack(pady=20)
except:
    lbl_sin_logo = tk.Label(
        ventana, 
        text="(Aquí va el logo del sistema)", 
        font=("Arial", 14), 
        bg="#D8F3DC"
    )
    lbl_sin_logo.pack(pady=40)


# -------------------------
# ESTILO DE BOTONES REDONDOS (más pequeños)
# -------------------------
estilo = ttk.Style()
estilo.theme_use("clam")

BOTON_COLOR = "#FFFFFF"
BOTON_HOVER = "#70D6FF"

estilo.configure(
    "Rounded.TButton",
    font=("Arial", 12),
    padding=5,                     # 🔽 Padding más pequeño
    background=BOTON_COLOR,
    foreground="black",
    borderwidth=0,
    relief="flat"
)

estilo.map(
    "Rounded.TButton",
    background=[("active", BOTON_HOVER)],
    foreground=[("active", "black")]
)


# -------------------------
# FUNCIÓN PARA CREAR BOTÓN REDONDO
# -------------------------
def crear_boton_redondo(texto, comando):
    btn = ttk.Button(
        ventana, 
        text=texto, 
        command=comando, 
        style="Rounded.TButton"
    )

    # Botón más pequeño aquí:
    btn.pack(pady=8, ipadx=25, ipady=6)   # 🔽 Más pequeño

    btn.configure(cursor="hand2")

    return btn


# -------------------------
# BOTONES (MISMA LÓGICA)
# -------------------------
crear_boton_redondo("Registro de Productos", abrir_registro_productos)
crear_boton_redondo("Reportes", abrir_reportes)
crear_boton_redondo("Registro de Ventas", abrir_registro_ventas)
crear_boton_redondo("Acerca de", abrir_acerca_de)


# -------------------------
# INICIO DE LA APP
# -------------------------
ventana.mainloop()