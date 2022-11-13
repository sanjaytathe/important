##  THEORY

1) what is SQl ? (structure query language)
-> sql is the standardised programming language that is used to manage relational database & perform various operation on data

2) what is Mysql ?
-> mysql is relational database management system (RDMS) developed by oracle

3)Database -> A database is collection of structure,information or data

4)Query -> quary is any command used to retrive data from table


5) wgat is sub-language ?
-> 1. DDL( data defination language)
   -> this sub-language deal with objec of database. it provide 5 commands. create, drop, truncate, alter, rename

   2. DML(data manipulate language)
   -> it deal  with data of object. it provide 3 commands. insert, upsate, delete

   3. DQL(data query language)
   -> it is used to retrieve information from data.it has only one command. select,


6) what is advantage of mysql ?
-> 1. manage large amount of data
   2. easy to update
   3. mysql runs all operating sysyem
   4. support for large database
   5. easy to research data
   6. mysql database server is very fast


7) what is difference between sql and mysql ?
-> sql known as structure query language. it used to intract with database like mysql and mysql is database that store various type of data


8) what is difference between database and table ?
-> Tables represent the division of data in database. while,database is collection of table and data.


9) why do we use mysql database server ?
-> 1. mysql database server is very fast
   2. reliable and easy to use
   3. you can easily use and modify the software
   4. msql software can be downloaded free of cost from internet


 
10)  PRIMARY                                        UNIQUE
  1. doesnt allow null value                  allow null value
  2. each table hold just one                 A table can more than one 
      primary key                              unique key
  3. we can not delete or modify              we can delete  or modify
     value in primary key


11) primary key -> primary key is a field in a table that uniquely indentifies each row and records in database and table
                -> primary value must contain unique value
                -> it can not be null
                -> there must be a single primar key



12) foreign key -> a foreign is contraint  is a key used to linked two table together
                -> An attribute in one table that refer to the primary in other table


13) super key -> A super key is all possible attribute that can uniquely indentifies each row and records in database and table
              -> A table can have more super key

14) composite key ->  composite key is a combination of two or more than two column in a table that can uniquely indentifies each row and records in database and table


15) Candidate key ->  candidate key is key or group of multiple key that can uniquely indentifies each row and records in database and table


16) how can you intract with database ?
-> using command line tool
-> via web interface
-> through programming language



17) what is constraint ?
->sql constraint are used to specify rule for data in table.not null,check,default,primary key,unique key, foreign key


18) Truncate -> trunacte are used to delete all rows or data
    Delete -> delete some or all rows from tabletable based on condition
    Drop -> it is used to remove object from database


19) what is join ?
-> join are used to retrieve data from multiple table
    1. INNER JOIN
       -> inner join basically return records that have matching value in both side

    2. CROSS JOIN
       -> cross join can be defined as product of two table included in join

    3. LEFT JOIN
       -> left join return rows which are common betwenn the tables and all records left hand side tables


20) what is relationship?
-> relationship are the established association between two or more table
oto -> oto relationship occcur when each row in one table has only related row im second table
otm -> in a otm relationship one records in a table can be associate with one or more records in another table
mtm -> mtm occurs mutiple records in a table are associate with mutiple records in another table


21) what is normalization?
-> normalization is the process of eliminate data redundancy & enhance data integrity in the table
-> normalization is the process of organising data in database
-> normalization divides larger tables into smaller tables and link them using relationship
-> there are diff. type of normalization
1. 1NF
   -> A column or attribute of a table cannot hold multiple value
   -> each records needs to be unique

2. 2NF
   -> it should be in 1NF
   -> all non-key attribute /column are fully functional dependent on the primary key

3. 3NF
   -> it is in 2NF
   -> there is no transitive functional dependency
    When an indirect relationship causes functional dependency it is called Transitive Dependency
    The functional dependency is a relationship that exists between two attributes.



########################################################################################################################################################
# DATATYPE

# STRING DATATYPE
1. varchar(size) -> 0 to 65535
2. char(sixe) -> 0 to 255
3. text

# NUMERIC DATATYPE
1. int(size)
2. float
3. double(size,d)
4. dec(size,d)

# DATE
1. date -> yyy-mm-dd
2. datetime -> yyyy-mm-dd hh:mm:ss

# TIME
1. select current_time
2. select curtime

3. select time('2019-6-15 13:15:20') as time -> 13:15:20
4. select hour('2019-6-15 13:15:20') as time -> 13

##########################################################################################################################################################
# cOMMAND

1. OPEN IN COOMAND PROMPT ->c:\program\mysql\server\bin 8.0
                          -> mysql -u root -p
                          -> password -> root

2. TO CHECK CURRENT USER -> select user();
3. CHANGE USER -> system mysql -u sanjay -p;
4. CREATE USER -> create user 'username'@'localhost' identified by 'password';
5. DELETE USER -> drop user 'username'@'localhost';

6. SHOW DATABASES -> show databases;
7. USE DATABASE -> use database_name;
8. CREATE DATABASE -> create database database_name;
9. DELETE DATABSE -> drop database database_name;

10. CREATE TABLE ->  CREATE TABLE users(
                         id INT AUTO_INCREMENT,
                         first_name VARCHAR(100),
                         last_name VARCHAR(100),
                         register_date DATETIME,
                         PRIMARY KEY(id)
                         );
11. DROP TABLE -> drop table tablename;
    TRUNCATE -> truncate table_name;
12. SHOW TABLES -> show tables;
13. INSERT DATA -> insert into table_name values(val1, val2)
                -> insert into table_name(col1, col2) values(val1, val2)
14. SELECT -> select * from table;
              desc table_name;

#ALTER

15. ADD COLUMN -> alter table table_name
                  add column col_name datatype;
                  
16. DELETE CLOUMN -> alter table table_name
                     drop column col_name;
                     
17.. ADD COLUMN MORE THAN 1 -> alter table table_name
                               add column col_name_1 datatype;
                               add column col_name_2 datatype;
                               
18. ADD COLUMN BY POSITION -> alter table table_name
                              add column col_name datatype first;

19. ADD COLUMN BY POSITION -> alter table table_name
                              add column col_name datatype after col_name;
20. ADD COLUMN CONSTRAINT -> alter table table_name
                              add column col_name not null auto_increment first;
                              add primary key(col_name)

21. IF YOU WANT TO SHIFT COLUMN -> alter table table_name
                                   modify email varchar(50) after name;
                                   
22. CHANGE COLUMN NAME -> alter table table_name
                          change column old_col new_col datatype;
 
23. MODIFY COLUMN OR CHANGE CONSTRAINT -> alter table table_name
                                          modify column col_name datatype; # you can change constraint

24. #RENAME
    RENAME TABLE_NAME -> alter table table_name
                         rename new_table_name

25. #DISTICT
           -> select distinct col_name from table;

26. #CONCAT
           -> select concat(first_name, ' ', last_name) as Name from table;

27. # UPDATE
           -> upadte table_name set fees=3000 where id=2;

28. DELETE ROW -> delete from table_name where id=2;

29. # ASCENDING AND DESCENDING
           ->  select * from table_name order by col_name ASC OR DESC;

30. # LIKE
          -> select * from table_name where col_name like '%a';

          '%a' - start with a
          'a%' - ends with a
          '%a%' - a in ant position
          'a%o' - start with a and ends with o

31. # LIMT AND OFFSET
            -> select * from table_name where id limi 2;
            -> select * from table_name where id limi 2,3;

32. # NULL
        -> insert into table_name values(val1,null, val3)
     
33. # AND, OR, NOT, IN,BETWEEN
        -> select * from table_name where fees>=1000 and fees<=1500;
        -> select * from table_name where fees>=1000 or fees<=1500;
        -> select * from table_name where fees>=1000 not fees<=1500;
        -> select * from table_name where fees in (1000,15000,2000);
        -> select * from table_name where fees between 1500 and 2000;

34. # AUTO_INCREMENT
        -> alter table table_name
           auto_increment=10;

35. # ARIHMATIC OPERATION
        -> select fees+id as 'total' from table_name;

36. # AGGREGATE FUNCTION
     1. count()
     2. sum()
     3. avg()
     4. min(),max()
     -> select count(id) from table_name;

37. # FIND SECOND HIGHEST SALARY

    -> select max(salary) from table_name where salary < (select max(salary) from table_name);
    -> select max(salary) from table_name where salary not in (select max(salary) from table_name);
    -> select max(salary) from table_name order by salary desc limit N-1,1:

38. # SYSTEM CLEAR
       -> system cls

39. # GROUP BY
       -> select age, count(age) from table_name where age > 20 group by age;
        
   
40. # HAVING
       -> select age, count(age) from table_name  group by age having age>20;


41. # REPLACE
       -> update table_name set address=replace(address,'p','m') where id=2;

42. # IF CLAUSE
       -> select *,if(mark>35,'pass','fail') as result from table1;

43. # WHEN CLAUSE
       -> select *,
          case
          when mark>=80 and mark<=100 then 'merit',
          when mark>=60 and mark<=80 then '2nd merit',
          end as grade
          from student;

44. # UNION/UNION ALL
         UNION -> remove duplicate records
         UNION ALL -> add all records

         select * from table1
         union/union all
         select * from table2

45. # TIME
    1. select current_time;
    2. select curtime();
    3. select localtime();

46. # CREATE TABLE WITH FREIGN KEY
     create table table1
     (
         id int not null auto_increment,
         VID int,
         constraint fk_table_name('VID table name') foreign key(VID) references vender(VID));

47.# JOIN
   1) INNER JOIN
   -> select * from table2 inner join table1 on table2.cities=table1.id
   -> select p.cid, p.name, q.city from table2 as p inner join table1 as q on p.cities=q.id

   2) CROSS JOIN
   -> select * from table2 cross join table1;

   3) LEFT AND RIGHT JOIN
   -> select * from table2 left join table1 on table2.cities=table1.id

   4) MULTIPLE JOIN
   -> select * from table2 inner join table1 on table2.cities=table1.id
      inner join table3
      on table3.id=table2.cities

#-----------------------------------------------------
 # SQL QUESTION

1. TO PRINT FIRST THREE CHARACTER -> select substring(first_name,1,3) from worker;

2. TO PRINT FIRST_NAME AFTER REMOVING RIGHT  SIDE SPACE -> select RTRIM(first_name) from worker;

3. select replace(fiest_name,'a','A') from worker;

4. select * from worker where first_name like '____h_

5. WHO JOINED IN FEB 2022 -> select * from worker year(joining_date)=2014 and month(joining_date)=2;

6. DROP PRIMARY KEY -> alter table table_name drop primanry key;

7.WHO ALSO HOLD MANAGER -> select * from employee where employee_id in (select manager_id from employee)
                        -> select w.first_name,t.worker_title from worker w inner join title t on w.worker_id=t.worker_ref_id and t.worker_title in('manager')

8. select * from table1
   intersect/minus
   select * from table2

10. FETCH EVEN AND ODD RECORDS
    -> select * from employee where id%2=0;
    -> select * from employee where id%2=1;

11. TO FIND 1ST AND LAST RECORDS
    -> select * from employee limit 1;
    -> select * from employee order by id desc limit 1;

12. FIND LAST RECORDS -> select * from employee where id > (select max(id)-5 from employee;

                        






















          
















    



   





   

   
   





















































     

