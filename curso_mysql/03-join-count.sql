-- ahora vamos a crear otra tabla para cruza con la tabla user
create table products (
id int not null auto_increment,
name varchar(50) not null,
created_by int not null,
marca varchar(50) not null,
primary key(id),
foreign key(created_by) references user(id));

-- ahora veamos como renombrar una tabla
rename table products to product;

-- ahora veamos como insertar datos con un solo insert
insert into product (name, created_by, marca)
values
	('ipad', 1, 'apple'),
    ('iphone', 1, 'apple'),
    ('watch', 2, 'apple'),
    ('macbook', 1, 'apple'),
    ('imac', 3, 'apple'),
    ('ipad mini', 2, 'apple');
select * from product;

-- la tabla de user se le denomina con lef join, porque a partir
-- de ella vamos a hacer varias consultas
select u.id, u.email, p.name from user u left join product p on u.id = p.created_by;
-- la u es un alias que le estamos dando a la tabla de user
-- p a product y tenemos que especificar con un . las columnas
-- que vamos a unir en la nueva consulta
-- on se utiliza para enlazazar las columnas que le decimos
-- osea que va a asignar un usuario al numero de created_by
-- al final solo trae los resultados de la tabla produc enlazada 
-- a usuarios de la tabla user, por eso nos muestra usuarios que no han creado productos

-- ahora veamos un rigth join, que es lo mismo pero tomando como principal la talba de product
select u.id, u.email, p.name from user u right join product p on u.id = p.created_by;
-- de esta manera no nos muestra a chanchito ya que no esta enlazado a ningun producto de la tabla principal

-- ahora veamos lo que hace el inner join que es una interseccion
-- nos va a arrojar tantos datos enlazados como sea posible
select u.id, u.email, p.name from user u inner join product p on u.id = p.created_by;

-- ahora veamos el cross join que nos va a entregar el producto cartesiano entre 2 tablas
select u.id, u.name, p.id, p.name from user u cross join product p;
-- aqui no se especifican las tablas de donde vamos a obtener los registros
-- por lo que debemos tener mucho cuidado, ya que nos puede
-- arrojar una cantidad enorme de informacion ya que va a 
-- cruzar todos los registros de una tabla con la otra

-- ahora veamos group by, es cual va a agrupar registros dentro de una categoria
select count(id), marca from product group by marca; -- da 6 apple de count(id), marca

-- ahora convinemos las consultas con un left join en products
select count(p.id), u.name from product p left join user u on u.id = p.created_by group by p.created_by;
-- esta ultima consulta nos dice cuantos productos ha creado cada usuario
-- pero ahora vamos a filtrar los resultados que nos interesen
-- por ejemplo aquellos usuarios que solo hayan creado mas de 2 productos
select count(p.id), u.name from product p left join user u 
on u.id = p.created_by group by p.created_by
having count(p.id) >= 2;

-- para eliminar una tabla usamos el metodo drop
drop table product; -- pero no lo ejecutaréalter


    