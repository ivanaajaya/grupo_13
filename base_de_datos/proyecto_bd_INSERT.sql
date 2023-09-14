use proyecto;

INSERT INTO estado_usuario (nombre_estado) VALUES ('active');
INSERT INTO estado_usuario (nombre_estado) VALUES ('suspended');
INSERT INTO estado_usuario (nombre_estado) VALUES ('deactivated');

INSERT INTO usuarios (alias, nombre, apellido, fecha_nacimiento, password, correo_electronico, id_estado) 
VALUES ("alias1", "nombre", "apellido", "2000-10-10", "contraseña", "correo_electronico", 1);
INSERT INTO proyecto.usuarios (alias, nombre, apellido, fecha_nacimiento, password, correo_electronico, id_estado) 
VALUES ("alias1", "nombre", "apellido", "2000-10-10", "contraseña", "correo_electronico", 2);
INSERT INTO proyecto.usuarios (alias, nombre, apellido, fecha_nacimiento, password, correo_electronico, id_estado) 
VALUES ("alias1", "nombre", "apellido", "2000-10-10", "contraseña", "correo_electronico", 3);

INSERT INTO roles (nombre_rol, permisos,id_usuario) VALUES ('Anonimo', "Leer mensajes públicos, Registrarse en la plataforma",1);
INSERT INTO roles (nombre_rol, permisos,id_usuario) VALUES ('Registrado', 'Enviar mensajes públicos, Leer mensajes privados',2);
INSERT INTO roles (nombre_rol, permisos,id_usuario) VALUES ('Administrador', 'Todas las capacidades de Moderador, Eliminar o suspender cuentas de usuarios, Administrar roles de usuarios (asignar roles de Moderador o Administrador)',3);


