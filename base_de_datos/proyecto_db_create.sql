CREATE DATABASE proyecto_db;
USE proyecto_db; 

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
    imagen VARCHAR(255)
);

CREATE TABLE Servidores (
    id_servidor INT NOT NULL AUTO_INCREMENT,
    nombre_servidor VARCHAR(200) NOT NULL,
    descripcion VARCHAR(50),
    cantUser INT,
    PRIMARY KEY (id_servidor)
);

CREATE TABLE UsuarioServidor (
    id_UsuarioServidor INT AUTO_INCREMENT PRIMARY KEY,
    nombre_rol VARCHAR(50) NOT NULL UNIQUE,
    fecha_unirse TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_usuario INT,
    id_servidor INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
    FOREIGN KEY (id_servidor) REFERENCES Servidores(id_servidor)
);

CREATE TABLE canales (
    id_canal INT NOT NULL AUTO_INCREMENT,
    nombre_canal VARCHAR(200) NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_servidor INT NOT NULL,
    PRIMARY KEY (id_canal),
    FOREIGN KEY (id_servidor) REFERENCES servidores(id_servidor)
);

CREATE TABLE mensajes (
    id_mensaje INT NOT NULL AUTO_INCREMENT,
    contenido VARCHAR(170) NOT NULL,
    hora_mensaje TIME,
    fecha_mensaje DATE,
    id_usuario INT,
    id_canal INT,
    PRIMARY KEY (id_mensaje),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
    FOREIGN KEY (id_canal) REFERENCES canales(id_canal)
);







