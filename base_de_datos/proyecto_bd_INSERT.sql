USE proyecto_db;

INSERT INTO roles (nombre_rol, permisos) VALUES ('Anonimo', "Leer mensajes públicos, Registrarse en la plataforma");
INSERT INTO roles (nombre_rol, permisos) VALUES ('Registrado', 'Enviar mensajes públicos, Leer mensajes privados');
INSERT INTO roles (nombre_rol, permisos) VALUES ('Administrador', 'Todas las capacidades de Moderador, Eliminar o suspender cuentas de usuarios, Administrar roles de usuarios (asignar roles de Moderador o Administrador)');

INSERT INTO usuarios (alias, nombre, apellido, fecha_nacimiento, password, correo_electronico, estado_activo, imagen, id_rol) 
VALUES ("alias1", "nombre1", "apellido1", "2000-10-10", "contraseña1", "correo_electronico1", True, null, 1);
INSERT INTO usuarios (alias, nombre, apellido, fecha_nacimiento, password, correo_electronico, estado_activo, imagen, id_rol) 
VALUES ("alias2", "nombre2", "apellido2", "2000-10-10", "contraseña2", "correo_electronico2", True, null, 2);
INSERT INTO usuarios (alias, nombre, apellido, fecha_nacimiento, password, correo_electronico, estado_activo, imagen, id_rol) 
VALUES ("alias3", "nombre3", "apellido3", "2000-10-10", "contraseña3", "correo_electronico3", True, null, 3);


-- Inserción de mensajes
INSERT INTO mensajes (contenido, hora_mensaje, fecha_mensaje, id_usuario, id_canal)
VALUES
    ('¡Hola a todos!', '10:15:00', '2023-09-20', 1, 1),
    ('¿Alguien quiere unirse a una partida de ajedrez?', '14:30:45', '2023-09-20', 1, 2),
    ('Hoy tenemos noticias importantes que discutir.', '09:00:00', '2023-09-19', 2, 3);