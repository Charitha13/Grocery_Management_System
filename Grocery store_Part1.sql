-- create database

create database if not exists grocerystore;

-- use database to start performing any operations on the database

use grocerystore;

-- Creating tables Location, designation, employees

create table location( Location_Id varchar(10) not null, Zipcode int not null, City varchar(20) not null, 
Street varchar(30) not null, primary key (Location_Id));

insert into location values("JTP01", 413245, "New York", "Jericho"), ("NHP02", 413287, "New York", "Hyde Park"),
("WGP03", 417654, "Pennsylvania", "Willow Grove");
 

create table designation(Dsgn_Id varchar(20) not null, Designation varchar(20) not null,
 Salary int, primary key(Dsgn_Id));

insert into designation values("AM01", "Asst.Manager", 80000), ("LVL1", "Level 1", 70000), ("M01", "Manager", 100000); 

create table employees(Location_Id varchar(20) not null, 
Email varchar(40) not null, Mobile varchar(15) not null,
First_Name varchar(40) not null, Last_Name varchar(30) not null,E_Id int not null,
Dsgn_Id varchar(20) not null, primary key(E_Id), foreign key(Location_Id) references location(Location_Id),
foreign key(Dsgn_Id) references designation(Dsgn_Id) );

-- Inserting values into the tables location, employees, designation
insert into employees values ("JTP01", "katjohn@gmail.com", "9875678987", "Katherine", "Johnson", 313100, "M01"),
  ("NHP02", "Marjason@gmail.com", "9865467435", "Mark", "Jason", 315178, "M01"),
  ("WGP03", "Rickstark@gmail.com", "9456789876", "Rick", "Stark", 314768, "M01");
  

insert into location values("MCA04", 414876, "New York", "Marcus Avenue"),
("HPG05", 415665, "New York", "Hauppage"),
("STF06", 416876, "New York", "Statford"),
("GCP07", 416766, "New York", "Garden City Park"),
("MRA08", 416321, "New York", "Merillon Avenue"),
("ATA09", 418765, "New York", "Atlantic Avenue"),
("MNL10", 415397, "New York", "Mineola"),
("WLP11", 418657, "New York", "Williston Park"),
("RDS12", 537878, "New Haven", "Rodney Street"),
("STA13", 538766, "New Haven", "Stevens Avenue"),
("LSS14", 527687, "New Haven", "Lester Street"),
("RCP15", 526856, "New Haven", "Richards PI"),
("MLR16", 546765, "New Haven", "Meloy Rd"),
("HRS17", 613245, "Pennsylvania", "Horsham"),
("HTB18", 614387, "Pennsylvania", "Hatboro"),
("JRT19", 616655, "Pennsylvania", "Jarrettown"),
("STN20", 618984, "Pennsylvania", "Stenton");

insert into designation values("SM01", "Senior Manager", 140000),
("CSH01", "cashier", 50000),
("AST01", "Aisle Staff", 50000),
("LVL2", "Level 2", 70000),
("LVL3", "Level 3", 70000),
("LVL4", "Level 4", 70000),
("LVL5", "Level 5", 70000),
("DPM1", "Deputy Manager", 80000),
("STF1", "Staff", 50000),
("RPN1", "Receptionist", 50000),
("DTR1", "Director", 200000),
("LVL6", "Level 6", 70000),
("LVL7", "Level 7", 70000),
("LVL8", "Level 8", 70000),
("LVL9", "Level 9", 70000),
("STF2", "Staff 2", 50000),
("STF3", "Staff 3", 50000);

insert into employees values("ATA09", "raczeen@gail.com", "9432187654", "Rachel", "Zeen", 316532, "M01"),
("GCP07", "mikgur@gmail.com","9422177654", "Mike", "Gurrero", 312432, "M01"),
("HPG05", "harspec@gmail.com","9413217698", "Harvey", "Spectar",307654, "M01"),
("HRS17", "lukross@gmail.com","9433127498",  "Luke", "Ross",310765, "M01"),
("HTB18", "jesann@gmail.com", "9453217654", "Jessica", "Aniston",305654, "M01"),
("JRT19", "mongrec@gmail.com","9428769932",  "Monica", "Grecher",343234, "M01"),
("MLR16", "jencox@gmail.com", "9446579127", "Jennifer", "Cox",324876, "M01"),
("LSS14", "matkudr@gmail.com", "9446623438", "Matt", "Kudrow",365432, "M01"),
("MCA04", "jamtyl@gmail.com", "9454537657", "James", "Tyler",329873, "M01"),
("MNL10", "bruwil@gmail.com", "9658794309", "Bruce", "Wills",319808, "M01"),
("MRA08", "liswhel@gmail.com", "6543287623", "Lisa", "Wheller",312435, "M01"),
("RCP15", "tomsib@gmail.com", "6754391239", "Tom", "Sibbett",376543, "M01"),
("RDS12", "jacgel@gmail.com","8439796397", "Jack", "Geller", 376541, "M01"),
("STA13", "jontay@gmail.com","8712309784", "Jon", "Taylor", 412345, "M01"),
("STF06", "eddcah@gmail.com","7650982115", "Eddie", "Cahill", 333421, "M01"),
("STN20", "ellhec@gmail.com", "5198760954","Elle", "Hecht", 327654, "M01"),
("WLP11", "katpage@gmail.com","5981297287", "Kathy", "Paget", 374867, "M01");

-- Creating tables customers, manager, dbusers, commodities, supplier , categories

create table customers(Cust_ID int not null primary key, First_name varchar(20) not null,
Last_name varchar(20) not null, Phone varchar(20) not null, Email varchar(30) not null,
Location_Id varchar(20) not null, foreign key(Location_Id) references location(Location_Id));

insert into customers values(1,'Shane','Lane',5679345679,"shane.l@gmail.com","JTP01"),
(2,'Jack','Jill',9874567845,"Jack.j@gmail.com","JTP01"),
(3,'Liam','Hen',5670983456,"Liam.h@gmail.com","NHP02"),
 (4,'Chris','Morris',5647895876,"Chris.m@gmail.com","NHP02"),
 (5,'Billy','Ben',3459876908,"billy.b@gmail.com","NHP02");

describe customers;


create table Manager(E_Id int not null primary key, 
Mobile varchar(15) not null, Email varchar(30) not null,
foreign key(E_Id) references employees(E_Id));

insert into Manager(E_Id, Mobile, Email) select E_Id, Mobile, Email  from employees where  Dsgn_Id = "M01";

create table DBUsers(E_Id int not null primary key, Username varchar(20),
 Password varchar(50), foreign key(E_Id) references Manager(E_Id)); 
 
-- alter table DBUsers modify Password varchar(50);
 
insert into DBUsers(E_Id, Username, Password) select E_Id, substring(Email, 1, 6), substring(E_Id, 1, 6) from Manager;

create table Commodities( Product_No int not null primary key, 
Product_Name varchar(30) not null, Prod_Quantity int not null, Prod_Price int not null);

create table Suppliers(Supplier_No int NOT NULL Primary Key AUTO_INCREMENT,
 Supplier_Name varchar(20) NOT NULL,
  Mobile varchar(20) NOT NULL,
  Location_Id varchar(20) NOT NULL,
  Email varchar(30) not null,
  Product_No int NOT NULL,  FOREIGN KEY(Product_No) REFERENCES Commodities(Product_No),
  foreign key(Location_Id) references location(Location_Id),
  Prd_Actual_Price decimal(10,2) NOT NULL);

-- To check the structure of the table

describe Commodities;
describe Suppliers;

INSERT INTO Commodities(Product_No,Product_Name,Prod_Quantity,Prod_Price)
VALUES(1,'Noodles',10,12),
(2,'Pasta',16,14),
(3,'Meat',28,10), (4,'Bread',17,2.5),
(5,'Avocado',23,1.2), (6,'Eggs',50, 7);

Insert into Suppliers values(1,'Panera',7654532879,"JTP01","panera@gmail.com",4,2),
(2 ,'Nestle',9599457967,"JTP01" ,"nestle@gmail.com" ,1, 11 ),
(3 ,'Jane Meat Suppliers',2591093897,"NHP02", "janems@gmail.com" ,3 ,9.5),
(4 ,'High Land',3287390523,"JTP01", "high_land@gmail.com" ,6,6 ),
( 5,'Fresh Foods',7689278041 ,"NHP02",  "freshf@gmail.com", 5,0.8 ),
( 6,'Linc',7687454092 ,"JTP01", "linc23@gmail.com" ,2 ,12 );

 
 
 create table Categories(Category_Id varchar(20) not null,
 Category_Name varchar(30), Product_No int not null, foreign key(Product_No) references Commodities(Product_No)); 
 
 -- alter table Categories drop primary key; 
 
 describe Categories;
 
  insert into Categories values("C1", "Pasta and more", 1),
 ("C1", "Pasta and more", 2),
 ("C2", "Meat products", 3),
 ("C3", "Bread", 4),
 ("C4", "Fruits and Salads", 5),
 ("C2", "Meat products", 6);
 
-- Display all data in the tables employees, designation and location and also get the count of the records in each of the tables
select * from employees;
select count(*) from employees;

select * from designation;
select count(*) from designation;

select * from location;
select count(*) from location;

select * from Commodities;
select * from Suppliers;
select * from Categories;
select * from DBUsers;
select * from Manager;
select * from customers;
 
-- Creating a view to display managers and their location
create view Branch_Manager as select ee.First_Name, ee.Last_Name, loc.Street, loc.City, loc.Zipcode from employees
 as ee inner join location as loc on ee.Dsgn_Id = "M01" and ee.Location_ID = loc.Location_Id;
 
 -- Display the view
 select * from Branch_Manager;
