CREATE DATABASE Refaccionaria;
USE Refaccionaria;

CREATE TABLE Administrador (
    id_admin INT PRIMARY KEY,
    nombre VARCHAR(100),
    usuario VARCHAR(50),
    contrasena VARCHAR(50)
);

CREATE TABLE Proveedor (
    id_proveedor INT PRIMARY KEY,
    nombre VARCHAR(100),
    telefono VARCHAR(20),
    email VARCHAR(100),
    direccion VARCHAR(150)
);

CREATE TABLE Refaccion (
    id_refaccion INT PRIMARY KEY,
    nombre VARCHAR(100),
    categoria VARCHAR(50),
    precio_unitario FLOAT,
    stock INT,
    id_proveedor INT,
    FOREIGN KEY (id_proveedor) REFERENCES Proveedor(id_proveedor)
);

CREATE TABLE Cliente (
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(100),
    telefono VARCHAR(20),
    email VARCHAR(100)
);

CREATE TABLE Venta (
    id_venta INT PRIMARY KEY,
    fecha DATE,
    total FLOAT,
    id_cliente INT,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente)
);

CREATE TABLE DetalleDeVenta (
    id_detalle INT PRIMARY KEY,
    cantidad INT,
    subtotal FLOAT,
    id_venta INT,
    id_refaccion INT,
    FOREIGN KEY (id_venta) REFERENCES Venta(id_venta),
    FOREIGN KEY (id_refaccion) REFERENCES Refaccion(id_refaccion)
)