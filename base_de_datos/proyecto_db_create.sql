
CREATE DATABASE PROYECTO;
USE PROYECTO; 

CREATE TABLE estado_usuario (
    id_estado INT AUTO_INCREMENT PRIMARY KEY,
    nombre_estado VARCHAR(50) NOT NULL
);

CREATE TABLE Usuarios (
    id_usuario INT NOT NULL AUTO_INCREMENT,
    alias VARCHAR(50) NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(20) NOT NULL,
    fecha_nacimiento DATE,
    password VARCHAR(200) NOT NULL,
    correo_electronico VARCHAR(50) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_estado INT,
    PRIMARY KEY (id_usuario),
    CONSTRAINT fk_usuario_estado_id FOREIGN KEY (id_estado) REFERENCES estado_usuario(id_estado)
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

CREATE TABLE roles (
    id_rol INT NOT NULL AUTO_INCREMENT,
    nombre_rol VARCHAR(50) NOT NULL,
    permisos VARCHAR(200),
    id_usuario INT,
    PRIMARY KEY (id_rol),
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







