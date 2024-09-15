#para comentar lineas podemos usar -- o #
-- para crear una base de datos usamos
create database holamundo;

-- el sig comnado nos muestra todas las bases de datos
show databases;

-- para crear una tabla, primero debemos referenciar la base 
-- de datos, despues ya creamos la tabla que ira dentro de esa bd
use holamundo;
CREATE TABLE animales (
id int,
tipo varchar(255),
estado varchar(255),
PRIMARY KEY (id));

-- para insertar datos en la tabla usamos:
INSERT INTO animales (tipo, estado) VALUES ('chanchito', 'feliz');
INSERT INTO animales (tipo, estado) VALUES ('dragon', 'feliz');
INSERT INTO animales (tipo, estado) VALUES ('felipe', 'triste');

-- al ejecutar el ultimo comando, nos arrojaria error pues falta
-- el id, pero no le dimos la instruccion de crecer +1
-- ahora veremos como modificar una tabla ya existente
-- despues de modificar y ejecutar el id, ya podemos usar el insert
ALTER TABLE animales MODIFY COLUMN id int auto_increment;

-- si queremos ver el comando que se utilizo para crear una tabla
-- podemos usar el sig comando
SHOW CREATE TABLE animales;
-- lo que nos daria... 
CREATE TABLE `animales` (
  `id` int NOT NULL AUTO_INCREMENT,
  -- NOT NULL indica que esta columna no puede estar vacia
  `tipo` varchar(255) DEFAULT NULL,
  -- default null indica que este campo va a estar vacio por defecto
  `estado` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
); -- ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

-- ahora vamos a listar los registros
SELECT * FROM animales; #nos muestra todo de animales
select * from animales where id = 1;
select * from animales where estado = 'feliz' and tipo = 'chanchito';

-- ahora vamos a actulizar los registros
update animales set estado = 'feliz' where id = 4;
-- ahora ya todos tienen feliz

-- ahora vamos a borrar un registro
delete from animales where estado = 'feliz';
-- Error Code: 1175. You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column.  To disable safe mode, toggle the option in Preferences -> SQL Editor and reconnect.
-- como no le pasamos una id, la proteccion de mysql no permitio hacer el delte

delete from animales where id = 2;
-- teniamos 2 chanchito porque la primer linea la ejecute 2 veces, ahora solo tenemos 1

-- vamos a modificar otro estado
update animales set estado = 'triste' where tipo = 'dragon';
-- lo cual manda error de nuevo porque tenemos que meter el id tambien en update
update animales set estado = 'triste' where id = 3;
SELECT * FROM animales; -- para ver la tabla

 

