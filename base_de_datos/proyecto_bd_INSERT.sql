-- Insertar datos en la tabla Usuarios
INSERT INTO Usuarios (alias, nombre, apellido, fecha_nacimiento, password, correo_electronico, estado_activo, imagen)
VALUES
    ('juanito', 'Juan Pérez', 'Pérez', '1990-05-15', 'contraseña123', 'juan@example.com', 1, 'imagen1.jpg'),
    ('maria22', 'María García', 'García', '1985-08-20', 'clave456', 'maria@example.com', 1, 'imagen2.jpg'),
    ('carlitos', 'Carlos López', 'López', NULL, 'secreto789', 'carlos@example.com', 1, NULL),
    ('anarod', 'Ana Rodríguez', 'Rodríguez', '1992-02-10', 'segura123', 'ana@example.com', 0, 'imagen3.jpg'),
    ('javi78', 'Javier Fernández', 'Fernández', '1988-11-30', 'p4ssw0rd', 'javier@example.com', 1, NULL);

-- Insertar datos en la tabla Servidores
INSERT INTO Servidores (nombre_servidor, descripcion, cantUser)
VALUES
    ('Servidor de Pruebas', 'Servidor de prueba para usuarios nuevos', 0),
    ('Proyecto Web', 'Servidor para desarrolladores web', 0),
    ('Comunidad de Juegos', 'Servidor para amantes de los videojuegos', 0);

-- Insertar datos en la tabla UsuarioServidor
INSERT INTO UsuarioServidor (nombre_rol, id_usuario, id_servidor)
VALUES
    ('Administrador', 1, 1),
    ('Miembro', 2, 1),
    ('Administrador', 3, 2),
    ('Miembro', 4, 2),
    ('Miembro', 5, 3);

-- Insertar datos en la tabla Canales
INSERT INTO Canales (nombre_canal, id_servidor)
VALUES
    ('General', 1),
    ('Desarrollo Web', 1),
    ('Proyectos', 2),
    ('Noticias de Juegos', 3);

-- Insertar datos en la tabla Mensajes
INSERT INTO Mensajes (contenido, id_usuario, id_canal)
VALUES
    ('¡Hola a todos!', 1, 1),
    ('¡Hola, bienvenidos!', 2, 1),
    ('¿En qué proyecto están trabajando?', 3, 3),
    ('Estamos trabajando en un nuevo juego', 4, 3),
    ('¿Alguien quiere unirse a una partida de Fortnite?', 5, 4);
