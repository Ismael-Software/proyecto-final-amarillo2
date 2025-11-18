

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from PIL import Image, ImageTk
import requests
from io import BytesIO
import mysql.connector

# ------------------- Configuración de la conexión -------------------
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="refaccionaria"
    )

# ------------------- Funciones de BD (CRUD simples) -------------------
def fetch_all(table):
    try:
        db = conectar()
        cur = db.cursor()
        cur.execute(f"SELECT * FROM {table}")
        rows = cur.fetchall()
        cur.close()
        db.close()
        return rows
    except Exception as e:
        messagebox.showerror("Error BD", f"No se pudo leer {table}: {e}")
        return []

def insert(table, columns, values):
    cols = ", ".join(columns)
    placeholders = ", ".join(["%s"] * len(values))
    sql = f"INSERT INTO {table} ({cols}) VALUES ({placeholders})"
    try:
        db = conectar()
        cur = db.cursor()
        cur.execute(sql, values)
        db.commit()
        cur.close()
        db.close()
        return True, None
    except mysql.connector.IntegrityError as ie:
        return False, str(ie)
    except Exception as e:
        return False, str(e)

# ------------------- Interfaz -------------------
def mostrar_login():
    login = tk.Tk()
    login.title("Inicio de sesión")
    login.geometry("420x340")
    login.configure(bg="#FFF0F6")

    cont = tk.Frame(login, bg="#FFF6FA", bd=0)
    cont.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(cont, text="Bienvenida 💕", bg="#FFF6FA", fg="#6B2B4A", font=("Segoe UI", 16, "bold")).pack(pady=(8,12))
    tk.Label(cont, text="Usuario:", bg="#FFF6FA", fg="#6B2B4A", font=("Segoe UI", 11)).pack(anchor="w", padx=12)
    usuario_entry = tk.Entry(cont, font=("Segoe UI", 11), bg="#FFF0F6")
    usuario_entry.pack(ipady=6, padx=12, pady=(2,8))

    tk.Label(cont, text="Contraseña:", bg="#FFF6FA", fg="#6B2B4A", font=("Segoe UI", 11)).pack(anchor="w", padx=12)
    contrasena_entry = tk.Entry(cont, show="*", font=("Segoe UI", 11), bg="#FFF0F6")
    contrasena_entry.pack(ipady=6, padx=12, pady=(2,12))

    tk.Label(cont, text="Ingresa tus credenciales", bg="#FFF6FA", fg="#9A567F", font=("Segoe UI", 9, "italic")).pack()

    def validar_login():
        if usuario_entry.get() == "admin" and contrasena_entry.get() == "1234":
            login.destroy()
            abrir_sistema()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    btn = tk.Button(cont, text="💖 Iniciar sesión", command=validar_login,
                    bg="#FF9EC4", fg="white", font=("Segoe UI", 11, "bold"), relief="flat")
    btn.pack(pady=8)

    login.bind("<Return>", lambda e: validar_login())
    login.mainloop()

# ------------------- Ventana principal con pestañas y tablas enlazadas -------------------
def abrir_sistema():
    root = tk.Tk()
    root.title("Sistema de Gestión - Refaccionaria Automotriz")
    root.geometry("1000x650")
    root.configure(bg="#FFF8FB")

    style = ttk.Style()
    style.theme_use("default")

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True, padx=8, pady=8)

    main_frame = tk.Frame(notebook, bg="#FFF8FB")
    notebook.add(main_frame, text="Inicio 💕")
    tk.Label(main_frame, text="Bienvenida al Sistema de Gestión de Refacciones", bg="#FFF8FB", fg="#5A1A3C",
             font=("Segoe UI", 16, "bold")).pack(pady=40)

    def cargar_imagen(url, tamaño=(200,200)):
        try:
            r = requests.get(url, timeout=5)
            r.raise_for_status()
            img = Image.open(BytesIO(r.content)).resize(tamaño)
            return ImageTk.PhotoImage(img)
        except Exception:
            return None

    url_pantalla = "https://raw.githubusercontent.com/Ismael-Software/proyecto-final-amarillo2/refs/heads/desarrollo/Img/Pantalla.png"
    url_aceite = "https://raw.githubusercontent.com/Ismael-Software/proyecto-final-amarillo2/refs/heads/desarrollo/Img/Aceite.jpg"
    img_prov = cargar_imagen(url_aceite)
    img_ref = cargar_imagen(url_pantalla)
    img_client = cargar_imagen(url_aceite)
    img_ventas = cargar_imagen(url_pantalla)

    root.image_refs = [img_prov, img_ref, img_client, img_ventas]

    # ---------------- Proveedores ----------------
    frame_prov = ttk.Frame(notebook)
    notebook.add(frame_prov, text="Proveedores 🧾")
    tk.Label(frame_prov, text="Gestión de Proveedores", font=("Segoe UI", 16, "bold"), fg="#5A1A3C", bg="#FFF8FB").pack(pady=10)
    content_prov = tk.Frame(frame_prov, bg="#FFF0F6")
    content_prov.pack(fill="both", expand=True, padx=10, pady=10)

    if img_prov:
        tk.Label(content_prov, image=img_prov, bg="#FFF0F6").grid(row=0,column=0,rowspan=7,padx=20,pady=10)

    form_prov = tk.Frame(content_prov, bg="#FFF0F6")
    form_prov.grid(row=0,column=1,sticky="nw",padx=10,pady=10)

    labels = ["ID:","Nombre:","Teléfono:","Correo:","Dirección:"]
    for i,lbl in enumerate(labels): tk.Label(form_prov,text=lbl,bg="#FFF0F6").grid(row=i,column=0,sticky="w")

    id_prov = tk.Entry(form_prov); nombre_prov = tk.Entry(form_prov)
    telefono_prov = tk.Entry(form_prov); correo_prov = tk.Entry(form_prov); direccion_prov = tk.Entry(form_prov)
    id_prov.grid(row=0,column=1); nombre_prov.grid(row=1,column=1)
    telefono_prov.grid(row=2,column=1); correo_prov.grid(row=3,column=1); direccion_prov.grid(row=4,column=1)

    tabla_prov = ttk.Treeview(frame_prov, columns=("ID","Nombre","Teléfono","Correo","Dirección"), show="headings", height=6)
    for col in tabla_prov["columns"]:
        tabla_prov.heading(col,text=col); tabla_prov.column(col,width=160,anchor="center")
    tabla_prov.pack(fill="x",padx=10,pady=10)

    def cargar_proveedores():
        tabla_prov.delete(*tabla_prov.get_children())
        for row in fetch_all("proveedor"):
            tabla_prov.insert("","end",values=row)

    def guardar_prov():
        try:
            datos = (int(id_prov.get()), nombre_prov.get(), telefono_prov.get(), correo_prov.get(), direccion_prov.get())
        except ValueError:
            messagebox.showerror("Error","Revisa los tipos de datos")
            return
        ok,err = insert("proveedor", ("id","nombre","telefono","correo","direccion"), datos)
        if ok:
            messagebox.showinfo("Éxito","Proveedor guardado en BD")
            cargar_proveedores()
            for e in (id_prov,nombre_prov,telefono_prov,correo_prov,direccion_prov): e.delete(0,tk.END)
        else:
            messagebox.showerror("Error BD", err)

    tk.Button(form_prov,text="💖 Guardar Proveedor", command=guardar_prov, bg="#FF9EC4").grid(row=5,column=0,columnspan=2,pady=8)
    cargar_proveedores()

    # ---------------- Refacciones ----------------
    frame_ref = ttk.Frame(notebook)
    notebook.add(frame_ref, text="Refacciones")
    tk.Label(frame_ref, text="Gestión de Refacciones", font=("Arial", 14, "bold"), bg="#FDE2E4", fg="#4B2E39").pack(pady=10)
    content_ref = tk.Frame(frame_ref, bg="#FDE2E4")
    content_ref.pack(fill="both", expand=True, padx=10, pady=10)

    if img_ref:
        tk.Label(content_ref, image=img_ref, bg="#FDE2E4").grid(row=0,column=0,rowspan=7,padx=20,pady=10)

    form_ref = tk.Frame(content_ref, bg="#FDE2E4")
    form_ref.grid(row=0,column=1,sticky="nw",padx=10,pady=10)

    labels = ["ID:","Nombre:","Categoría:","Precio Unitario:","Stock:"]
    for i,lbl in enumerate(labels): tk.Label(form_ref,text=lbl,bg="#FDE2E4").grid(row=i,column=0,sticky="w")

    id_ref = tk.Entry(form_ref); nombre_ref = tk.Entry(form_ref)
    categoria_ref = tk.Entry(form_ref); precio_ref = tk.Entry(form_ref); stock_ref = tk.Entry(form_ref)
    id_ref.grid(row=0,column=1); nombre_ref.grid(row=1,column=1)
    categoria_ref.grid(row=2,column=1); precio_ref.grid(row=3,column=1); stock_ref.grid(row=4,column=1)

    tabla_ref = ttk.Treeview(frame_ref, columns=("ID","Nombre","Categoría","Precio","Stock"), show="headings", height=6)
    for col in tabla_ref["columns"]:
        tabla_ref.heading(col,text=col); tabla_ref.column(col,width=140,anchor="center")
    tabla_ref.pack(fill="x",padx=10,pady=10)

    def cargar_refacciones():
        tabla_ref.delete(*tabla_ref.get_children())
        for row in fetch_all("refaccion"):
            tabla_ref.insert("","end",values=row)

    def guardar_ref():
        try:
            datos = (int(id_ref.get()), nombre_ref.get(), categoria_ref.get(), float(precio_ref.get()), int(stock_ref.get()))
        except ValueError:
            messagebox.showerror("Error","Revisa los tipos de datos")
            return
        ok,err = insert("refaccion", ("id","nombre","categoria","precio","stock"), datos)
        if ok:
            messagebox.showinfo("Éxito","Refacción guardada en BD")
            cargar_refacciones()
            actualizar_menu_refacciones()
            for e in (id_ref,nombre_ref,categoria_ref,precio_ref,stock_ref): e.delete(0,tk.END)
        else:
            messagebox.showerror("Error BD", err)

    tk.Button(form_ref, text="Guardar Refacción", command=guardar_ref, bg="#F9C6CF").grid(row=5,column=0,columnspan=2,pady=8)
    cargar_refacciones()

    # ---------------- Clientes ----------------
    frame_client = ttk.Frame(notebook)
    notebook.add(frame_client, text="Clientes")
    tk.Label(frame_client, text="Gestión de Clientes", font=("Arial", 14, "bold"), bg="#FDE2E4", fg="#4B2E39").pack(pady=10)
    content_client = tk.Frame(frame_client, bg="#FDE2E4")
    content_client.pack(fill="both", expand=True, padx=10, pady=10)

    if img_client:
        tk.Label(content_client, image=img_client, bg="#FDE2E4").grid(row=0,column=0,rowspan=6,padx=20,pady=10)

    form_client = tk.Frame(content_client, bg="#FDE2E4")
    form_client.grid(row=0,column=1,sticky="nw",padx=10,pady=10)

    labels = ["ID:","Nombre:","Teléfono:","Correo:"]
    for i,lbl in enumerate(labels): tk.Label(form_client,text=lbl,bg="#FDE2E4").grid(row=i,column=0,sticky="w")

    id_client = tk.Entry(form_client); nombre_client = tk.Entry(form_client)
    telefono_client = tk.Entry(form_client); correo_client = tk.Entry(form_client)
    id_client.grid(row=0,column=1); nombre_client.grid(row=1,column=1)
    telefono_client.grid(row=2,column=1); correo_client.grid(row=3,column=1)

    tabla_client = ttk.Treeview(frame_client, columns=("ID","Nombre","Teléfono","Correo"), show="headings", height=6)
    for col in tabla_client["columns"]:
        tabla_client.heading(col,text=col); tabla_client.column(col,width=160,anchor="center")
    tabla_client.pack(fill="x",padx=10,pady=10)

    def cargar_clientes():
        tabla_client.delete(*tabla_client.get_children())
        for row in fetch_all("cliente"):
            tabla_client.insert("","end",values=row)

    def guardar_cliente():
        try:
            datos = (int(id_client.get()), nombre_client.get(), telefono_client.get(), correo_client.get())
        except ValueError:
            messagebox.showerror("Error","Revisa los tipos de datos")
            return
        ok,err = insert("cliente", ("id","nombre","telefono","correo"), datos)
        if ok:
            messagebox.showinfo("Éxito","Cliente guardado en BD")
            cargar_clientes()
            actualizar_menu_clientes()
            for e in (id_client,nombre_client,telefono_client,correo_client): e.delete(0,tk.END)
        else:
            messagebox.showerror("Error BD", err)

    tk.Button(form_client, text="Guardar Cliente", command=guardar_cliente, bg="#F9C6CF").grid(row=4,column=0,columnspan=2,pady=8)
    cargar_clientes()

    # ---------------- Ventas ----------------
    frame_ventas = ttk.Frame(notebook)
    notebook.add(frame_ventas, text="Ventas")
    tk.Label(frame_ventas, text="Registro de Ventas", font=("Arial", 14, "bold"), bg="#FDE2E4", fg="#4B2E39").pack(pady=10)
    content_ventas = tk.Frame(frame_ventas, bg="#FDE2E4")
    content_ventas.pack(fill="both", expand=True, padx=10, pady=10)

    if img_ventas:
        tk.Label(content_ventas, image=img_ventas, bg="#FDE2E4").grid(row=0,column=0,rowspan=7,padx=20,pady=10)

    form_venta = tk.Frame(content_ventas, bg="#FDE2E4")
    form_venta.grid(row=0,column=1,sticky="nw",padx=10,pady=10)

    tk.Label(form_venta, text="Folio:", bg="#FDE2E4").grid(row=0,column=0,sticky="w")
    tk.Label(form_venta, text="Cliente:", bg="#FDE2E4").grid(row=1,column=0,sticky="w")
    tk.Label(form_venta, text="Refacción:", bg="#FDE2E4").grid(row=2,column=0,sticky="w")
    tk.Label(form_venta, text="Cantidad:", bg="#FDE2E4").grid(row=3,column=0,sticky="w")

    folio_var = tk.StringVar(value=f"TKT-0001")
    folio = tk.Entry(form_venta, textvariable=folio_var, state="readonly")

    cliente_v = ttk.Combobox(form_venta, values=[])
    refaccion_v = ttk.Combobox(form_venta, values=[])
    cantidad_v = tk.Entry(form_venta)

    folio.grid(row=0,column=1); cliente_v.grid(row=1,column=1); refaccion_v.grid(row=2,column=1); cantidad_v.grid(row=3,column=1)

    tabla_ventas = ttk.Treeview(frame_ventas, columns=("Folio","Cliente","Refacción","Cantidad","Subtotal","Fecha","Total"), show="headings", height=8)
    for col in tabla_ventas["columns"]:
        tabla_ventas.heading(col,text=col); tabla_ventas.column(col,width=120,anchor="center")
    tabla_ventas.pack(fill="x",padx=10,pady=10)

    def actualizar_menu_refacciones():
        refacciones_bd = fetch_all("refaccion")
        refaccion_v["values"] = [r[1] for r in refacciones_bd]

    def actualizar_menu_clientes():
        clientes_bd = fetch_all("cliente")
        cliente_v["values"] = [r[1] for r in clientes_bd]

    def cargar_ventas():
        tabla_ventas.delete(*tabla_ventas.get_children())
        for row in fetch_all("venta"):
            tabla_ventas.insert("","end",values=row)


    def registrar_venta():
        try:
            cantidad = int(cantidad_v.get())
            ref_bd = fetch_all("refaccion")
            precio_unitario = 0.0
            for r in ref_bd:
                if r[1] == refaccion_v.get():
                    precio_unitario = float(r[3])
                    break
            subtotal = precio_unitario * cantidad
            total = subtotal
            fecha = datetime.now().strftime("%Y-%m-%d")
            folio_val = f"TKT-{len(fetch_all('venta'))+1:04d}"
            datos = (folio_val, cliente_v.get(), refaccion_v.get(), cantidad, subtotal, fecha, total)
            ok,err = insert("venta", ("folio","cliente","refaccion","cantidad","subtotal","fecha","total"), datos)
            if ok:
                messagebox.showinfo("Éxito","Venta registrada en BD")
                cargar_ventas()
                folio_var.set(f"TKT-{len(fetch_all('venta'))+1:04d}")
                try:
                    db = conectar(); cur = db.cursor()
                    cur.execute("UPDATE refaccion SET stock = stock - %s WHERE nombre = %s", (cantidad, refaccion_v.get()))
                    db.commit(); cur.close(); db.close()
                except Exception:
                    pass
                actualizar_menu_refacciones(); actualizar_menu_clientes()
                for e in (cliente_v, refaccion_v, cantidad_v):
                    try: e.set("")
                    except: e.delete(0,tk.END)
            else:
                messagebox.showerror("Error BD", err)
        except ValueError:
            messagebox.showerror("Error","Ingresa valores válidos")

    tk.Button(form_venta, text="Registrar Venta", command=registrar_venta, bg="#F9C6CF").grid(row=4,column=0,columnspan=2,pady=8)

    cargar_proveedores(); cargar_refacciones(); cargar_clientes(); cargar_ventas()
    actualizar_menu_refacciones(); actualizar_menu_clientes()

    root.mainloop()

if __name__ == "__main__":
    mostrar_login()
