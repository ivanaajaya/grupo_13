CREATE DATABASE proyecto_db;
USE proyecto_db; 

CREATE TABLE roles (
    id_rol INT AUTO_INCREMENT PRIMARY KEY,
    nombre_rol VARCHAR(50) NOT NULL UNIQUE,
    permisos VARCHAR(200)
);

CREATE TABLE Usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    alias VARCHAR(50) NOT NULL UNIQUE,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(20) NOT NULL,
    fecha_nacimiento DATE,
    password VARCHAR(200) NOT NULL ,
    correo_electronico VARCHAR(50) NOT NULL UNIQUE,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado_activo boolean,
    imagen VARCHAR(255),
    id_rol INT,
    CONSTRAINT fk_usuario_rol_id FOREIGN KEY (id_rol) REFERENCES roles(id_rol)
);

CREATE TABLE servidores (
    id_servidor INT NOT NULL AUTO_INCREMENT,
    nombre_servidor VARCHAR(200) NOT NULL,
    fecha_creacion DATE,
    descripcion VARCHAR(50),
    id_usuario INT,
    PRIMARY KEY (id_servidor),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

CREATE TABLE canales (
    id_canal INT NOT NULL AUTO_INCREMENT,
    nombre_canal VARCHAR(200) NOT NULL,
    id_rol INT,
    id_servidor INT,
    PRIMARY KEY (id_canal),
    FOREIGN KEY (id_rol) REFERENCES roles(id_rol),
    FOREIGN KEY (id_servidor) REFERENCES servidores(id_servidor)
);

CREATE TABLE mensajes (
    id_mensaje INT NOT NULL AUTO_INCREMENT,
    contenido VARCHAR(170),
    hora_mensaje TIME,
    fecha_mensaje DATE,
    id_usuario INT,
    id_canal INT,
    PRIMARY KEY (id_mensaje),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
    FOREIGN KEY (id_canal) REFERENCES canales(id_canal)
);







