use proyecto_db;
-- Insertar datos en la tabla Usuarios
INSERT INTO Usuarios (alias, nombre, apellido, fecha_nacimiento, password, correo_electronico, estado_activo, imagen) VALUES
    ('usuario1', 'Juan', 'Pérez', '1990-05-15', 'contrasena1', 'juan@example.com', true, 'imagen1.jpg'),
    ('usuario2', 'María', 'López', '1985-08-20', 'contrasena2', 'maria@example.com', true, 'imagen2.jpg'),
    ('usuario3', 'Pedro', 'Gómez', '1995-03-10', 'contrasena3', 'pedro@example.com', false, 'imagen3.jpg');

-- Insertar datos en la tabla Servidores
INSERT INTO Servidores (nombre_servidor, descripcion, cantUser) VALUES
    ('Servidor1', 'Descripción del servidor 1', 10),
    ('Servidor2', 'Descripción del servidor 2', 20),
    ('Servidor3', 'Descripción del servidor 3', 15);

-- Insertar datos en la tabla UsuarioServidor
INSERT INTO UsuarioServidor (nombre_rol, id_usuario, id_servidor) VALUES
    ('Rol1', 1, 1),
    ('Rol2', 2, 1),
    ('Rol3', 1, 2),
    ('Rol4', 3, 2);

-- Insertar datos en la tabla canales
INSERT INTO canales (nombre_canal, id_servidor) VALUES
    ('Canal1', 1),
    ('Canal2', 1),
    ('Canal3', 2),
    ('Canal4', 2);

-- Insertar datos en la tabla mensajes
INSERT INTO mensajes (contenido, hora_mensaje, fecha_mensaje, id_usuario, id_canal) VALUES
    ('Mensaje 1', '14:30:00', '2023-09-27', 1, 1),
    ('Mensaje 2', '15:45:00', '2023-09-27', 2, 1),
    ('Mensaje 3', '10:15:00', '2023-09-27', 1, 2),
    ('Mensaje 4', '09:00:00', '2023-09-27', 3, 2);
