import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from PIL import Image, ImageTk
import requests
from io import BytesIO

# ========================== LOGIN ==========================
def mostrar_login():
    login = tk.Tk()
    login.title("Inicio de sesión")
    login.geometry("400x300")
    login.configure(bg="#F2F2F2")

    tk.Label(login, text="Usuario:", bg="#F2F2F2", font=("Segoe UI", 12)).pack(pady=10)
    usuario_entry = tk.Entry(login, font=("Segoe UI", 12))
    usuario_entry.pack()

    tk.Label(login, text="Contraseña:", bg="#F2F2F2", font=("Segoe UI", 12)).pack(pady=10)
    contrasena_entry = tk.Entry(login, show="*", font=("Segoe UI", 12))
    contrasena_entry.pack()

    def validar_login():
        usuario = usuario_entry.get()
        contrasena = contrasena_entry.get()
        if usuario == "admin" and contrasena == "1234":
            login.destroy()
            abrir_sistema()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    tk.Button(login, text="Iniciar sesión", command=validar_login,
              bg="#0078D7", fg="white", font=("Segoe UI", 11),
              activebackground="#005A9E", cursor="hand2").pack(pady=20)

    login.mainloop()

# ========================== Crear ventana ==========================
def abrir_sistema():
    root = tk.Tk()
    root.title("Sistema de Gestión - Refaccionaria Automotriz")
    root.geometry("1000x650")
    root.configure(bg="white")



    # comntario de Victor


    # ========================== Crear pestañas ==========================
    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)


    # ========================== Cargar Imgs desde Git ==========================
    def cargar_imagen(url, tamaño=(200, 200)):
        try:
            respuesta = requests.get(url)
            respuesta.raise_for_status()
            img = Image.open(BytesIO(respuesta.content)).resize(tamaño)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Error al cargar imagen desde {url}: {e}")
            return None


    url_pantalla = "https://raw.githubusercontent.com/Ismael-Software/proyecto-final-amarillo2/refs/heads/desarrollo/Img/Pantalla.png"
    url_aceite = "https://raw.githubusercontent.com/Ismael-Software/proyecto-final-amarillo2/refs/heads/desarrollo/Img/Aceite.jpg"

    img_admin = cargar_imagen(url_pantalla)
    img_prov = cargar_imagen(url_aceite)
    img_ref = cargar_imagen(url_pantalla)
    img_client = cargar_imagen(url_aceite)
    img_ventas = cargar_imagen(url_pantalla)

    root.image_refs = [img_admin, img_prov, img_ref, img_client, img_ventas]

    root.image_refs = [img_admin, img_prov, img_ref, img_client, img_ventas]

    # ========================== ADMINISTRADOR ==========================
    frame_admin = ttk.Frame(notebook)
    notebook.add(frame_admin, text="Administrador")

    tk.Label(frame_admin, text="Gestión del Administrador", font=("Arial", 14, "bold")).pack(pady=10)

    content_admin = tk.Frame(frame_admin, bg="white")
    content_admin.pack(pady=10)

    tk.Label(content_admin, image=img_admin, bg="white").grid(row=0, column=0, rowspan=6, padx=20, pady=10)

    form_admin = ttk.Frame(content_admin)
    form_admin.grid(row=0, column=1, sticky="nw")

    tk.Label(form_admin, text="ID:").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(form_admin, text="Nombre:").grid(row=1, column=0, padx=5, pady=5)
    tk.Label(form_admin, text="Usuario:").grid(row=2, column=0, padx=5, pady=5)
    tk.Label(form_admin, text="Contraseña:").grid(row=3, column=0, padx=5, pady=5)

    id_admin = tk.Entry(form_admin)
    nombre_admin = tk.Entry(form_admin)
    usuario_admin = tk.Entry(form_admin)
    contrasena_admin = tk.Entry(form_admin, show="*")

    id_admin.grid(row=0, column=1)
    nombre_admin.grid(row=1, column=1)
    usuario_admin.grid(row=2, column=1)
    contrasena_admin.grid(row=3, column=1)

    admins = []


    def registrar_admin():
        datos = (id_admin.get(), nombre_admin.get(), usuario_admin.get(), contrasena_admin.get())
        if not all(datos):
            messagebox.showerror("Error", "Completa todos los campos.")
            return
        admins.append(datos)
        tabla_admin.insert("", "end", values=datos)
        messagebox.showinfo("Éxito", "Administrador registrado.")
        for e in (id_admin, nombre_admin, usuario_admin, contrasena_admin):
            e.delete(0, tk.END)


    tk.Button(form_admin, text="Registrar Administrador", command=registrar_admin).grid(row=4, column=0, columnspan=2,
                                                                                        pady=10)

    tabla_admin = ttk.Treeview(frame_admin, columns=("ID", "Nombre", "Usuario", "Contraseña"), show="headings")
    for col in tabla_admin["columns"]:
        tabla_admin.heading(col, text=col)
    tabla_admin.pack(fill="x", padx=10, pady=10)

    # ========================== PROVEEDORES ==========================
    frame_prov = ttk.Frame(notebook)
    notebook.add(frame_prov, text="Proveedores")

    tk.Label(frame_prov, text="Gestión de Proveedores", font=("Arial", 14, "bold")).pack(pady=10)

    content_prov = tk.Frame(frame_prov, bg="white")
    content_prov.pack(pady=10)

    tk.Label(content_prov, image=img_prov, bg="white").grid(row=0, column=0, rowspan=7, padx=20, pady=10)

    form_prov = ttk.Frame(content_prov)
    form_prov.grid(row=0, column=1, sticky="nw")

    tk.Label(form_prov, text="ID:").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(form_prov, text="Nombre:").grid(row=1, column=0, padx=5, pady=5)
    tk.Label(form_prov, text="Teléfono:").grid(row=2, column=0, padx=5, pady=5)
    tk.Label(form_prov, text="Correo:").grid(row=3, column=0, padx=5, pady=5)
    tk.Label(form_prov, text="Dirección:").grid(row=4, column=0, padx=5, pady=5)

    id_prov = tk.Entry(form_prov)
    nombre_prov = tk.Entry(form_prov)
    telefono_prov = tk.Entry(form_prov)
    correo_prov = tk.Entry(form_prov)
    direccion_prov = tk.Entry(form_prov)

    id_prov.grid(row=0, column=1)
    nombre_prov.grid(row=1, column=1)
    telefono_prov.grid(row=2, column=1)
    correo_prov.grid(row=3, column=1)
    direccion_prov.grid(row=4, column=1)

    proveedores = []


    def guardar_prov():
        datos = (id_prov.get(), nombre_prov.get(), telefono_prov.get(), correo_prov.get(), direccion_prov.get())
        if not all(datos):
            messagebox.showerror("Error", "Completa todos los campos.")
            return
        proveedores.append(datos)
        tabla_prov.insert("", "end", values=datos)
        messagebox.showinfo("Éxito", "Proveedor registrado correctamente")
        for e in (id_prov, nombre_prov, telefono_prov, correo_prov, direccion_prov):
            e.delete(0, tk.END)


    tk.Button(form_prov, text="Guardar Proveedor", command=guardar_prov).grid(row=5, column=0, columnspan=2, pady=10)

    tabla_prov = ttk.Treeview(frame_prov, columns=("ID", "Nombre", "Teléfono", "Correo", "Dirección"), show="headings")
    for col in tabla_prov["columns"]:
        tabla_prov.heading(col, text=col)
    tabla_prov.pack(fill="x", padx=10, pady=10)

    # ========================== REACCIONES ===========================
    frame_ref = ttk.Frame(notebook)
    notebook.add(frame_ref, text="Refacciones")

    tk.Label(frame_ref, text="Gestión de Refacciones", font=("Arial", 14, "bold")).pack(pady=10)

    content_ref = tk.Frame(frame_ref, bg="white")
    content_ref.pack(pady=10)

    tk.Label(content_ref, image=img_ref, bg="white").grid(row=0, column=0, rowspan=7, padx=20, pady=10)

    form_ref = ttk.Frame(content_ref)
    form_ref.grid(row=0, column=1, sticky="nw")

    tk.Label(form_ref, text="ID:").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(form_ref, text="Nombre:").grid(row=1, column=0, padx=5, pady=5)
    tk.Label(form_ref, text="Categoría:").grid(row=2, column=0, padx=5, pady=5)
    tk.Label(form_ref, text="Precio Unitario:").grid(row=3, column=0, padx=5, pady=5)
    tk.Label(form_ref, text="Stock:").grid(row=4, column=0, padx=5, pady=5)

    id_ref = tk.Entry(form_ref)
    nombre_ref = tk.Entry(form_ref)
    categoria_ref = tk.Entry(form_ref)
    precio_ref = tk.Entry(form_ref)
    stock_ref = tk.Entry(form_ref)

    id_ref.grid(row=0, column=1)
    nombre_ref.grid(row=1, column=1)
    categoria_ref.grid(row=2, column=1)
    precio_ref.grid(row=3, column=1)
    stock_ref.grid(row=4, column=1)

    refacciones = []


    def guardar_ref():
        datos = (id_ref.get(), nombre_ref.get(), categoria_ref.get(), precio_ref.get(), stock_ref.get())
        if not all(datos):
            messagebox.showerror("Error", "Completa todos los campos.")
            return
        refacciones.append(datos)
        tabla_ref.insert("", "end", values=datos)
        messagebox.showinfo("Éxito", "Refacción registrada correctamente")
        for e in (id_ref, nombre_ref, categoria_ref, precio_ref, stock_ref):
            e.delete(0, tk.END)

        actualizar_menu_refacciones()


    tk.Button(form_ref, text="Guardar Refacción", command=guardar_ref).grid(row=5, column=0, columnspan=2, pady=10)

    tabla_ref = ttk.Treeview(frame_ref, columns=("ID", "Nombre", "Categoría", "Precio", "Stock"), show="headings")
    for col in tabla_ref["columns"]:
        tabla_ref.heading(col, text=col)
    tabla_ref.pack(fill="x", padx=10, pady=10)

    # ========================== CLIENTES ==========================
    frame_client = ttk.Frame(notebook)
    notebook.add(frame_client, text="Clientes")

    tk.Label(frame_client, text="Gestión de Clientes", font=("Arial", 14, "bold")).pack(pady=10)

    content_client = tk.Frame(frame_client, bg="white")
    content_client.pack(pady=10)

    tk.Label(content_client, image=img_client, bg="white").grid(row=0, column=0, rowspan=6, padx=20, pady=10)

    form_client = ttk.Frame(content_client)
    form_client.grid(row=0, column=1, sticky="nw")

    tk.Label(form_client, text="ID:").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(form_client, text="Nombre:").grid(row=1, column=0, padx=5, pady=5)
    tk.Label(form_client, text="Teléfono:").grid(row=2, column=0, padx=5, pady=5)
    tk.Label(form_client, text="Correo:").grid(row=3, column=0, padx=5, pady=5)

    id_client = tk.Entry(form_client)
    nombre_client = tk.Entry(form_client)
    telefono_client = tk.Entry(form_client)
    correo_client = tk.Entry(form_client)

    id_client.grid(row=0, column=1)
    nombre_client.grid(row=1, column=1)
    telefono_client.grid(row=2, column=1)
    correo_client.grid(row=3, column=1)

    clientes = []


    def guardar_cliente():
        datos = (id_client.get(), nombre_client.get(), telefono_client.get(), correo_client.get())
        if not all(datos):
            messagebox.showerror("Error", "Completa todos los campos.")
            return
        clientes.append(datos)
        tabla_client.insert("", "end", values=datos)
        messagebox.showinfo("Éxito", "Cliente registrado correctamente")
        for e in (id_client, nombre_client, telefono_client, correo_client):
            e.delete(0, tk.END)


    tk.Button(form_client, text="Guardar Cliente", command=guardar_cliente).grid(row=4, column=0, columnspan=2, pady=10)

    tabla_client = ttk.Treeview(frame_client, columns=("ID", "Nombre", "Teléfono", "Correo"), show="headings")
    for col in tabla_client["columns"]:
        tabla_client.heading(col, text=col)
    tabla_client.pack(fill="x", padx=10, pady=10)

    # ========================== VENTAS ==========================
    frame_ventas = ttk.Frame(notebook)
    notebook.add(frame_ventas, text="Ventas")

    tk.Label(frame_ventas, text="Registro de Ventas", font=("Arial", 14, "bold")).pack(pady=10)

    content_ventas = tk.Frame(frame_ventas, bg="white")
    content_ventas.pack(pady=10)

    tk.Label(content_ventas, image=img_ventas, bg="white").grid(row=0, column=0, rowspan=7, padx=20, pady=10)

    form_venta = ttk.Frame(content_ventas)
    form_venta.grid(row=0, column=1, sticky="nw")

    ventas = []

    tk.Label(form_venta, text="Folio:").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(form_venta, text="Cliente:").grid(row=1, column=0, padx=5, pady=5)
    tk.Label(form_venta, text="Refacción:").grid(row=2, column=0, padx=5, pady=5)
    tk.Label(form_venta, text="Cantidad:").grid(row=3, column=0, padx=5, pady=5)

    folio_var = tk.StringVar(value=f"TKT-{len(ventas) + 1:04d}")
    folio = tk.Entry(form_venta, textvariable=folio_var, state="readonly")
    cliente_v = tk.Entry(form_venta)
    refaccion_v = ttk.Combobox(form_venta, values=[r[1] for r in refacciones])
    cantidad_v = tk.Entry(form_venta)

    folio.grid(row=0, column=1)
    cliente_v.grid(row=1, column=1)
    refaccion_v.grid(row=2, column=1)
    cantidad_v.grid(row=3, column=1)


    def actualizar_menu_refacciones():
        refaccion_v["values"] = [r[1] for r in refacciones]


    def registrar_venta():
        try:
            cantidad = int(cantidad_v.get())
            precio_unitario = float(next((r[3] for r in refacciones if r[1] == refaccion_v.get()), 0))
            subtotal = precio_unitario * cantidad
            total = subtotal
            fecha = datetime.now().strftime("%Y-%m-%d")
            datos = (folio.get(), cliente_v.get(), refaccion_v.get(), cantidad, subtotal, fecha, total)
            ventas.append(datos)
            tabla_ventas.insert("", "end", values=datos)
            messagebox.showinfo("Éxito", "Venta registrada correctamente")
            folio_var.set(f"TKT-{len(ventas) + 1:04d}")
            for e in (folio, cliente_v, refaccion_v, cantidad_v):
                e.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Ingresa valores válidos.")


    tk.Button(form_venta, text="Registrar Venta", command=registrar_venta).grid(row=4, column=0, columnspan=2, pady=10)

    tabla_ventas = ttk.Treeview(
        frame_ventas,
        columns=("Folio", "Cliente", "Refacción", "Cantidad", "Subtotal", "Fecha", "Total"),
        show="headings"
    )
    for col in tabla_ventas["columns"]:
        tabla_ventas.heading(col, text=col)
    tabla_ventas.pack(fill="x", padx=10, pady=10)

    # ========================== ESTILO ==========================
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TFrame", background="#F2F2F2")
    style.configure("TLabel", background="#F2F2F2", foreground="#000000", font=("Segoe UI", 10))
    style.configure("TButton", background="#0078D7", foreground="white", font=("Segoe UI", 9, "bold"))
    style.map("TButton", background=[("active", "#005A9E")])

    root.mainloop()

if __name__ == "__main__":
    mostrar_login()
