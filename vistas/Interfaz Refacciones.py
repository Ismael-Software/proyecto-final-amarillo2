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
    login.geometry("420x340")
    login.configure(bg="#FFF0F6")  # rosa pastel muy claro

    # Contenedor central para darle padding y borde suave
    cont = tk.Frame(login, bg="#FFF6FA", bd=0, highlightthickness=0)
    cont.place(relx=0.5, rely=0.5, anchor="center")

    # Título
    titulo = tk.Label(cont, text="Bienvenida 💕", bg="#FFF6FA",
                      fg="#6B2B4A", font=("Segoe UI", 16, "bold"))
    titulo.pack(pady=(8, 12))

    # Etiqueta + entrada Usuario
    tk.Label(cont, text="Usuario:", bg="#FFF6FA", fg="#6B2B4A",
             font=("Segoe UI", 11)).pack(anchor="w", padx=12, pady=(6, 0))
    usuario_entry = tk.Entry(cont, font=("Segoe UI", 11), bg="#FFF0F6", relief="flat", bd=1, highlightthickness=1)
    usuario_entry.pack(ipady=6, padx=12, pady=(2, 8))

    # Etiqueta + entrada Contraseña
    tk.Label(cont, text="Contraseña:", bg="#FFF6FA", fg="#6B2B4A",
             font=("Segoe UI", 11)).pack(anchor="w", padx=12, pady=(6, 0))
    contrasena_entry = tk.Entry(cont, show="♥", font=("Segoe UI", 11), bg="#FFF0F6", relief="flat", bd=1, highlightthickness=1)
    contrasena_entry.pack(ipady=6, padx=12, pady=(2, 12))

    # Mensaje de ayuda / ejemplo
    ayuda = tk.Label(cont, text="Ingresa tus credenciales", bg="#FFF6FA", fg="#9A567F", font=("Segoe UI", 9, "italic"))
    ayuda.pack(pady=(0, 8))

    # Función de validación
    def validar_login():
        usuario = usuario_entry.get()
        contrasena = contrasena_entry.get()
        if usuario == "admin" and contrasena == "1234":
            login.destroy()
            abrir_sistema()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    # boton redondeado
    btn_frame = tk.Frame(cont, bg="#FFF6FA")
    btn_frame.pack(pady=(4, 12))
    btn = tk.Button(btn_frame, text="💖 Iniciar sesión", command=validar_login,
                    bg="#FF9EC4", fg="white", font=("Segoe UI", 11, "bold"),
                    activebackground="#FF7CA2", cursor="hand2", relief="flat", bd=0,
                    padx=16, pady=6)
    btn.pack()

    # Hacer que Enter valide también
    login.bind("<Return>", lambda event: validar_login())

    login.mainloop()


# ========================== Crear ventana ==========================
def abrir_sistema():
    root = tk.Tk()
    root.title("Sistema de Gestión - Refaccionaria Automotriz")
    root.geometry("1000x650")
    root.configure(bg="#FFF8FB")  # fondo rosa muy claro

    # comentario de Victor

    # ========================== Crear pestañas ==========================
    style = ttk.Style()
    style.theme_use("default")

    # Personalización de las pestañas
    style.configure("TNotebook", background="#FFD8E5", borderwidth=0)
    style.configure("TNotebook.Tab",
                    background="#FFC1DC",
                    foreground="#5A1A3C",
                    font=("Segoe UI", 10, "bold"),
                    padding=(15, 8))
    style.map("TNotebook.Tab",
              background=[("selected", "#FF8AB8")],
              foreground=[("selected", "white")])

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True, padx=8, pady=8)

    # Fondo interno general
    main_frame = tk.Frame(notebook, bg="#FFF8FB")
    notebook.add(main_frame, text="Inicio 💕")

    titulo = tk.Label(main_frame, text="Bienvenida al Sistema de Gestión de Refacciones",
                      bg="#FFF8FB", fg="#5A1A3C", font=("Segoe UI", 16, "bold"))
    titulo.pack(pady=40)

    subtitulo = tk.Label(main_frame, text="Selecciona una pestaña para comenzar",
                         bg="#FFF8FB", fg="#8C4A6E", font=("Segoe UI", 11))
    subtitulo.pack()




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
    notebook.add(frame_admin, text="Administrador 💼")

    # Encabezado bonito
    tk.Label(
        frame_admin,
        text="Gestión del Administrador",
        font=("Segoe UI", 16, "bold"),
        fg="#5A1A3C",
        bg="#FFF8FB"
    ).pack(pady=15)

    # Contenedor principal
    content_admin = tk.Frame(frame_admin, bg="#FFF0F6", bd=2, relief="flat")
    content_admin.pack(pady=10, padx=10, fill="both", expand=True)

    # Imagen decorativa
    tk.Label(content_admin, image=img_admin, bg="#FFF0F6").grid(row=0, column=0, rowspan=6, padx=30, pady=20)

    # Formulario
    form_admin = tk.Frame(content_admin, bg="#FFF0F6")
    form_admin.grid(row=0, column=1, sticky="nw", padx=10, pady=10)

    etiquetas = ["ID:", "Nombre:", "Usuario:", "Contraseña:"]
    for i, texto in enumerate(etiquetas):
        tk.Label(form_admin, text=texto, bg="#FFF0F6", fg="#5A1A3C", font=("Segoe UI", 10, "bold")).grid(row=i,
                                                                                                         column=0,
                                                                                                         padx=5, pady=6,
                                                                                                         sticky="w")

    id_admin = tk.Entry(form_admin, bg="#FFF8FB", font=("Segoe UI", 10), relief="flat")
    nombre_admin = tk.Entry(form_admin, bg="#FFF8FB", font=("Segoe UI", 10), relief="flat")
    usuario_admin = tk.Entry(form_admin, bg="#FFF8FB", font=("Segoe UI", 10), relief="flat")
    contrasena_admin = tk.Entry(form_admin, show="♥", bg="#FFF8FB", font=("Segoe UI", 10), relief="flat")

    id_admin.grid(row=0, column=1, padx=5, pady=6, ipady=3)
    nombre_admin.grid(row=1, column=1, padx=5, pady=6, ipady=3)
    usuario_admin.grid(row=2, column=1, padx=5, pady=6, ipady=3)
    contrasena_admin.grid(row=3, column=1, padx=5, pady=6, ipady=3)

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

    # Botón principal con estilo rosa
    tk.Button(
        form_admin,
        text="💖 Registrar Administrador",
        command=registrar_admin,
        bg="#FF9EC4",
        fg="white",
        font=("Segoe UI", 10, "bold"),
        activebackground="#FF7CA2",
        cursor="hand2",
        relief="flat",
        padx=10,
        pady=5
    ).grid(row=4, column=0, columnspan=2, pady=15)

    # Tabla de administradores
    tabla_admin = ttk.Treeview(frame_admin, columns=("ID", "Nombre", "Usuario", "Contraseña"), show="headings",
                               height=6)
    for col in tabla_admin["columns"]:
        tabla_admin.heading(col, text=col)
        tabla_admin.column(col, anchor="center", width=150)

    # Colores de tabla (pastel)
    style = ttk.Style()
    style.configure("Treeview",
                    background="#FFF8FB",
                    foreground="#4A2E3C",
                    rowheight=25,
                    fieldbackground="#FFF8FB",
                    font=("Segoe UI", 9))
    style.map("Treeview", background=[("selected", "#FFB6CE")])

    tabla_admin.pack(fill="x", padx=10, pady=10)

    # ========================== PROVEEDORES ==========================
    frame_prov = ttk.Frame(notebook)
    notebook.add(frame_prov, text="Proveedores 🧾")

    tk.Label(
        frame_prov,
        text="Gestión de Proveedores",
        font=("Segoe UI", 16, "bold"),
        fg="#5A1A3C",
        bg="#FFF8FB"
    ).pack(pady=15)

    content_prov = tk.Frame(frame_prov, bg="#FFF0F6", bd=2, relief="flat")
    content_prov.pack(pady=10, padx=10, fill="both", expand=True)

    # Imagen decorativa
    tk.Label(content_prov, image=img_prov, bg="#FFF0F6").grid(row=0, column=0, rowspan=7, padx=30, pady=20)

    # Formulario
    form_prov = tk.Frame(content_prov, bg="#FFF0F6")
    form_prov.grid(row=0, column=1, sticky="nw", padx=10, pady=10)

    etiquetas = ["ID:", "Nombre:", "Teléfono:", "Correo:", "Dirección:"]
    for i, texto in enumerate(etiquetas):
        tk.Label(form_prov, text=texto, bg="#FFF0F6", fg="#5A1A3C", font=("Segoe UI", 10, "bold")).grid(row=i, column=0,
                                                                                                        padx=5, pady=6,
                                                                                                        sticky="w")

    id_prov = tk.Entry(form_prov, bg="#FFF8FB", font=("Segoe UI", 10), relief="flat")
    nombre_prov = tk.Entry(form_prov, bg="#FFF8FB", font=("Segoe UI", 10), relief="flat")
    telefono_prov = tk.Entry(form_prov, bg="#FFF8FB", font=("Segoe UI", 10), relief="flat")
    correo_prov = tk.Entry(form_prov, bg="#FFF8FB", font=("Segoe UI", 10), relief="flat")
    direccion_prov = tk.Entry(form_prov, bg="#FFF8FB", font=("Segoe UI", 10), relief="flat")

    id_prov.grid(row=0, column=1, padx=5, pady=6, ipady=3)
    nombre_prov.grid(row=1, column=1, padx=5, pady=6, ipady=3)
    telefono_prov.grid(row=2, column=1, padx=5, pady=6, ipady=3)
    correo_prov.grid(row=3, column=1, padx=5, pady=6, ipady=3)
    direccion_prov.grid(row=4, column=1, padx=5, pady=6, ipady=3)

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

    tk.Button(
        form_prov,
        text="💖 Guardar Proveedor",
        command=guardar_prov,
        bg="#FF9EC4",
        fg="white",
        font=("Segoe UI", 10, "bold"),
        activebackground="#FF7CA2",
        cursor="hand2",
        relief="flat",
        padx=10,
        pady=5
    ).grid(row=5, column=0, columnspan=2, pady=15)

    # Tabla de proveedores
    tabla_prov = ttk.Treeview(frame_prov, columns=("ID", "Nombre", "Teléfono", "Correo", "Dirección"), show="headings",
                              height=6)
    for col in tabla_prov["columns"]:
        tabla_prov.heading(col, text=col)
        tabla_prov.column(col, anchor="center", width=160)

    # Estilo visual de la tabla
    style = ttk.Style()
    style.configure("Treeview",
                    background="#FFF8FB",
                    foreground="#4A2E3C",
                    rowheight=25,
                    fieldbackground="#FFF8FB",
                    font=("Segoe UI", 9))
    style.map("Treeview", background=[("selected", "#FFB6CE")])

    tabla_prov.pack(fill="x", padx=10, pady=10)

    # ========================== REACCIONES ===========================
    frame_ref = ttk.Frame(notebook)
    notebook.add(frame_ref, text="Refacciones")

    tk.Label(frame_ref, text="Gestión de Refacciones", font=("Arial", 14, "bold"), bg="#FDE2E4", fg="#4B2E39").pack(
        pady=10)

    content_ref = tk.Frame(frame_ref, bg="#FDE2E4")  # Fondo rosa pastel
    content_ref.pack(expand=True, fill="both")

    # Centrar el contenido internamente
    content_ref.grid_rowconfigure(0, weight=1)
    content_ref.grid_columnconfigure(0, weight=1)
    content_ref.grid_columnconfigure(1, weight=1)

    tk.Label(content_ref, image=img_ref, bg="#FDE2E4").grid(row=0, column=0, rowspan=7, padx=20, pady=10)

    form_ref = tk.Frame(content_ref, bg="#FDE2E4")
    form_ref.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)


    tk.Label(form_ref, text="ID:", bg="#FDE2E4", fg="#4B2E39").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(form_ref, text="Nombre:", bg="#FDE2E4", fg="#4B2E39").grid(row=1, column=0, padx=5, pady=5)
    tk.Label(form_ref, text="Categoría:", bg="#FDE2E4", fg="#4B2E39").grid(row=2, column=0, padx=5, pady=5)
    tk.Label(form_ref, text="Precio Unitario:", bg="#FDE2E4", fg="#4B2E39").grid(row=3, column=0, padx=5, pady=5)
    tk.Label(form_ref, text="Stock:", bg="#FDE2E4", fg="#4B2E39").grid(row=4, column=0, padx=5, pady=5)

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

    tk.Button(
        form_ref,
        text="Guardar Refacción",
        command=guardar_ref,
        bg="#F9C6CF",
        fg="#4B2E39",
        activebackground="#FADADD"
    ).grid(row=5, column=0, columnspan=2, pady=10)

    tabla_ref = ttk.Treeview(frame_ref, columns=("ID", "Nombre", "Categoría", "Precio", "Stock"), show="headings")
    for col in tabla_ref["columns"]:
        tabla_ref.heading(col, text=col)
    tabla_ref.pack(fill="x", padx=10, pady=10)

    # ========================== CLIENTES ==========================
    frame_client = ttk.Frame(notebook)
    notebook.add(frame_client, text="Clientes")

    tk.Label(
        frame_client,
        text="Gestión de Clientes",
        font=("Arial", 14, "bold"),
        bg="#FDE2E4",  # fondo rosa pastel
        fg="#4B2E39"  # texto marrón suave
    ).pack(pady=10)

    content_client = tk.Frame(frame_client, bg="#FDE2E4")
    content_client.pack(pady=10)

    tk.Label(content_client, image=img_client, bg="#FDE2E4").grid(row=0, column=0, rowspan=6, padx=20, pady=10)

    form_client = tk.Frame(content_client, bg="#FDE2E4")
    form_client.grid(row=0, column=1, sticky="nw")

    tk.Label(form_client, text="ID:", bg="#FDE2E4", fg="#4B2E39").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(form_client, text="Nombre:", bg="#FDE2E4", fg="#4B2E39").grid(row=1, column=0, padx=5, pady=5)
    tk.Label(form_client, text="Teléfono:", bg="#FDE2E4", fg="#4B2E39").grid(row=2, column=0, padx=5, pady=5)
    tk.Label(form_client, text="Correo:", bg="#FDE2E4", fg="#4B2E39").grid(row=3, column=0, padx=5, pady=5)

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

    tk.Button(
        form_client,
        text="Guardar Cliente",
        command=guardar_cliente,
        bg="#F9C6CF",  # rosa más fuerte para resaltar
        fg="#4B2E39",
        activebackground="#FADADD"
    ).grid(row=4, column=0, columnspan=2, pady=10)

    tabla_client = ttk.Treeview(frame_client, columns=("ID", "Nombre", "Teléfono", "Correo"), show="headings")
    for col in tabla_client["columns"]:
        tabla_client.heading(col, text=col)
    tabla_client.pack(fill="x", padx=10, pady=10)

    # ========================== VENTAS ==========================
    frame_ventas = ttk.Frame(notebook)
    notebook.add(frame_ventas, text="Ventas")

    tk.Label(
        frame_ventas,
        text="Registro de Ventas",
        font=("Arial", 14, "bold"),
        bg="#FDE2E4",  # fondo pastel suave
        fg="#4B2E39"  # texto marrón tenue
    ).pack(pady=10)

    content_ventas = tk.Frame(frame_ventas, bg="#FDE2E4")
    content_ventas.pack(pady=10)

    tk.Label(content_ventas, image=img_ventas, bg="#FDE2E4").grid(row=0, column=0, rowspan=7, padx=20, pady=10)

    form_venta = tk.Frame(content_ventas, bg="#FDE2E4")
    form_venta.grid(row=0, column=1, sticky="nw")

    ventas = []

    tk.Label(form_venta, text="Folio:", bg="#FDE2E4", fg="#4B2E39").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(form_venta, text="Cliente:", bg="#FDE2E4", fg="#4B2E39").grid(row=1, column=0, padx=5, pady=5)
    tk.Label(form_venta, text="Refacción:", bg="#FDE2E4", fg="#4B2E39").grid(row=2, column=0, padx=5, pady=5)
    tk.Label(form_venta, text="Cantidad:", bg="#FDE2E4", fg="#4B2E39").grid(row=3, column=0, padx=5, pady=5)

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
            for e in (cliente_v, refaccion_v, cantidad_v):
                e.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Ingresa valores válidos.")

    tk.Button(
        form_venta,
        text="Registrar Venta",
        command=registrar_venta,
        bg="#F9C6CF",  # rosa más fuerte para contraste
        fg="#4B2E39",
        activebackground="#FADADD",
        cursor="hand2"
    ).grid(row=4, column=0, columnspan=2, pady=10)

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

    # Fondo general (frames y etiquetas)
    style.configure("TFrame", background="#FDE2E4")  # Rosa pastel suave
    style.configure("TLabel", background="#FDE2E4", foreground="#4B2E39", font=("Segoe UI", 10))

    # Botones principales
    style.configure(
        "TButton",
        background="#F9C6CF",  # Rosa más fuerte para contraste
        foreground="#4B2E39",
        font=("Segoe UI", 9, "bold"),
        borderwidth=0,
        padding=6
    )
    style.map(
        "TButton",
        background=[("active", "#FADADD")],  # Rosa claro al presionar
        relief=[("pressed", "sunken")]
    )

    # Pestañas del notebook
    style.configure(
        "TNotebook.Tab",
        background="#FDE2E4",
        foreground="#4B2E39",
        font=("Segoe UI", 10, "bold"),
        padding=[10, 5]
    )
    style.map(
        "TNotebook.Tab",
        background=[("selected", "#F9C6CF")],  # Color más fuerte al seleccionar
        foreground=[("selected", "#4B2E39")]
    )

    # Treeview (tablas)
    style.configure(
        "Treeview",
        background="white",
        fieldbackground="white",
        foreground="#4B2E39",
        rowheight=25,
        font=("Segoe UI", 9)
    )
    style.configure(
        "Treeview.Heading",
        background="#F9C6CF",
        foreground="#4B2E39",
        font=("Segoe UI", 9, "bold")
    )
    style.map("Treeview.Heading", background=[("active", "#FADADD")])

    root.mainloop()

if __name__ == "__main__":
    mostrar_login()
