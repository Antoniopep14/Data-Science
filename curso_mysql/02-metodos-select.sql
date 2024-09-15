create table user (
id int not null auto_increment,
name varchar(50) not null,
edad int not null,
email varchar (100) not null,
primary key (id));

insert into  user (name, edad, email) values ('Oscar', 25, 'oscar@gmail.com');
insert into  user (name, edad, email) values ('Layla', 15, 'layla@gmail.com');
insert into  user (name, edad, email) values ('Nicolas', 36, 'nicolas@gmail.com');
insert into  user (name, edad, email) values ('Chanchito', 7, 'chanchito@gmail.com');

-- ahora veamos varias combinaciones de select
select * from user;
select * from user limit 1; 
-- esto va a limitar a enseñarnos el no de registros que le indiquemos
select * from user where edad > 15;
select * from user where edad >= 15;
-- cuando usas and y or primero evalua lo de la izq
select * from user where edad > 20 and email = 'nicolas@gmail.com';
select * from user where edad > 20 or email = 'layla@gmail.com';
select * from user where email != 'layla@gmail.com';
select * from user where edad between 15 and 30;
-- cuando usamos between tenemos que darle 2 parametros
-- el sig se usa cuando un usuario quiere buscar algo
select * from user where email like '%gmail%';
-- esto nos daria todo lo que tenga gmail con lo que sea antes o despues
-- para que nos de todo lo que termine con gmail.com, seria:
select * from user where email like '%gmail.com';
-- si solo sabemos el inicio o fraccion del inicio del correo podriamos usar
select * from user where email like 'layl%';
-- ahora vamos a ordenar nuestro resultados
select * from user order by edad asc;
-- asc = ascendente, desc = descendente
-- ahora veamos el registro de mayor y menor edad
select max(edad) as mayor from user; -- nos da 36
select min(edad) as menor from user; -- nos da 7
-- mayor y menor despues de as son los nombres que le asignamos a las nuevas columnas

-- para hacer un select dif a *, es decir de una columna:
select id, name from user;
-- ahora cambiemos el alias de una columna
select id, name as chanchito from user;



