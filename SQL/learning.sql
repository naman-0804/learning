use startersql;
-- select * from customers;-- create database startersql;
-- CREATE TABLE users (
-- 		id INT AUTO_INCREMENT PRIMARY KEY,
-- 		name VARCHAR(100) NOT NULL,
-- 		email VARCHAR(100) UNIQUE NOT NULL,
-- 		gender ENUM('Male', 'Female', 'Other'),
-- 		date_of_birth DATE,
-- 		created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- 	);

-- rename table users to customers;
-- alter table customers add column is_active boolean default true;
-- alter table customers drop column is_active;
-- alter table customers modify column email VARCHAR(150);
-- alter table customers modify column email VARCHAR(150) first; 

-- SHOW COLUMNS FROM users;
-- insert into users values
--     (6,'Alce','afdie@gmail.com','Male','1990-01-01','2023-10-01 10:00:00',9000),
--     (8,'Bb','ob@gmdsfail','Female','1992-02-02','2023-10-01 11:00:00',8790);

-- select* from users where id>2;
-- select * from users where gender='Female' order by date_of_birth asc ; 
-- select * from users where gender='Female' order by date_of_birth asc limit 1; 
-- alter table users add column salary varchar(100);

-- update users set salary =7020, email='ok@fg.hgj' where id='3';
-- update users set salary=50000 where salary <5000;

-- delete from users where salary=50000;
-- delete from users where salary is Null;

-- alter table users add constraint unique_name unique(name);
-- alter table users modify column name varchar (100) NULL;
-- insert into users values
-- (9,NULL,'afdie@gmdcl.com','Male','1990-01-01','2023-10-01 10:00:00',9000);
-- alter table users add constraint chk_sl check(salary>300);
-- alter table users alter column name set default "enter";

-- SHOW COLUMNS FROM users;
-- select * from users;

-- select count(*) from users where gender='Male';
-- select min(salary) from users where gender ='Male';
-- select sum(salary) as total from users /or avg;
-- select gender,avg(salary) as avg_sal from users group by gender;

-- select name,length(name) from users group by name;
-- select name,concat(name,"7731") as username,length(name) as name_len from users group by name;
-- select name,concat(name,"7731") as username,length(name) as name_len ,now() as time from users group by name;
-- select round(salary) as rounded from users;
-- select id,mod(id,2) as remainder from users;
-- select name,gender,if(gender='Female','YEs','NO') as is_female from users;

-- Foreign keys 

-- CREATE TABLE addresses (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     user_id INT,
--     street VARCHAR(255),
--     city VARCHAR(100),
--     state VARCHAR(100),
--     pincode VARCHAR(10),
--     FOREIGN KEY (user_id) REFERENCES users(id)
-- );
-- INSERT INTO addresses (user_id, street, city, state, pincode) VALUES
-- (2, '123 MG Road', 'Bengaluru', 'Karnataka', '560001'),
-- (3, '45 Park Street', 'Kolkata', 'West Bengal', '700016'),
-- (6, '78 Nehru Nagar', 'Mumbai', 'Maharashtra', '400001'),
-- (8, '12 Anna Salai', 'Chennai', 'Tamil Nadu', '600002'),
-- (9, '56 Civil Lines', 'Delhi', 'Delhi', '110054');

-- Joins (we have users and addresses with user_id referencing to id)

-- select * from users,addresses where addresses.user_id=users.id;
-- select users.name ,addresses.city from users inner join addresses on users.id=addresses.user_id;
--  select name,gender from users union select city,state from addresses;

-- alter table users add column reffered_by_id INT;
-- UPDATE users SET reffered_by_id = 1 WHERE id IN (2, 3); -- User 1 referred Users 2 and 3
-- UPDATE users SET reffered_by_id = 2 WHERE id = 6;       -- User 2 referred User 4

-- select * from users;
-- select a.id , a.name as username , b.name as referal from users a inner join users b on a.reffered_by_id=b.id; 

-- create view high_salary as select id , name , salary from users where salary>7000;
-- select * from high_salary;

-- show indexes from users ;
 
-- select salary from users where salary>(select avg(salary)from users);
-- select gender , avg(salary) from users group by gender;
-- select gender ,avg(salary) , count(*) from users group by gender having avg(salary)>2000;