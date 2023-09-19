USE proyecto_db;

INSERT INTO roles (nombre_rol, permisos) VALUES ('Anonimo', "Leer mensajes públicos, Registrarse en la plataforma");
INSERT INTO roles (nombre_rol, permisos) VALUES ('Registrado', 'Enviar mensajes públicos, Leer mensajes privados');
INSERT INTO roles (nombre_rol, permisos) VALUES ('Administrador', 'Todas las capacidades de Moderador, Eliminar o suspender cuentas de usuarios, Administrar roles de usuarios (asignar roles de Moderador o Administrador)');

INSERT INTO usuarios (alias, nombre, apellido, fecha_nacimiento, password, correo_electronico, estado_activo, id_rol) 
VALUES ("alias1", "nombre", "apellido", "2000-10-10", "contraseña1", "correo_electronico1", 1, 1);
INSERT INTO usuarios (alias, nombre, apellido, fecha_nacimiento, password, correo_electronico, estado_activo, id_rol) 
VALUES ("alias2", "nombre", "apellido", "2000-10-10", "contraseña2", "correo_electronico2", 1, 1);
INSERT INTO usuarios (alias, nombre, apellido, fecha_nacimiento, password, correo_electronico, estado_activo, id_rol) 
VALUES ("alias3", "nombre", "apellido", "2000-10-10", "contraseña3", "correo_electronico3", 1, 1);
