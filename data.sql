CREATE TABLE Employees (
	Empl_ID INT PRIMARY KEY,
    F_Name VARCHAR(20) NOT NULL,
    L_Name VARCHAR(20) NOT NULL,
    Employee_type VARCHAR(20) NOT NULL
);

SELECT * FROM Employees;

INSERT INTO Employees VALUES(1,'Enzo', 'Morelli', 'Manager');
INSERT INTO Employees VALUES(2,'Mario', 'Pacino', 'Delivery');
INSERT INTO Employees VALUES(3,'Luigi', 'Pacino', 'Delivery');
INSERT INTO Employees VALUES(4,'Giovanni', 'Capone', 'Chef');
INSERT INTO Employees VALUES(5,'Giana', 'Ferrari', 'Chef');

CREATE TABLE Manager (
	Empl_ID INT PRIMARY KEY,
    F_Name VARCHAR(20) NOT NULL,
    L_Name VARCHAR(20) NOT NULL,
    Employee_type VARCHAR(20) NOT NULL,
    FOREIGN KEY (Empl_ID) REFERENCES Employees(Empl_ID)
);

INSERT INTO Manager
SELECT * FROM Employees
WHERE Employee_type = 'Manager';

CREATE TABLE Chef (
	Empl_ID INT PRIMARY KEY,
    F_Name VARCHAR(20) NOT NULL,
    L_Name VARCHAR(20) NOT NULL,
    Employee_type VARCHAR(20) NOT NULL,
    FOREIGN KEY (Empl_ID) REFERENCES Employees(Empl_ID)
);

INSERT INTO Chef
SELECT * FROM Employees
WHERE Employee_type = 'Chef';

CREATE TABLE Delivery (
	Empl_ID INT PRIMARY KEY,
    F_Name VARCHAR(20) NOT NULL,
    L_Name VARCHAR(20) NOT NULL,
    Employee_type VARCHAR(20) NOT NULL,
    FOREIGN KEY (Empl_ID) REFERENCES Employees(Empl_ID)
);

INSERT INTO Delivery
SELECT * FROM Employees
WHERE Employee_type = 'Delivery';

CREATE TABLE Customer (
	Cust_ID INT PRIMARY KEY,
	F_Name VARCHAR(20) NOT NULL,
    L_Name VARCHAR(20) NOT NULL,
    street_addrs VARCHAR(20),
    city VARCHAR(20),
    state VARCHAR(20),
    ZIP INT,
    Email VARCHAR(40) NOT NULL,
    Orders INT
);

SELECT * FROM Customer;

INSERT INTO Customer VALUES(1, 'Jimmy', 'Waters', '11-11 45st', 'New York', 'NY', '11101', 'JimmyW@gmail.com', 51);
INSERT INTO Customer VALUES(2, 'Maria', 'Waters', '11-11 45st', 'New York', 'NY', '11101', 'MariaW@gmail.com', 21);
INSERT INTO Customer VALUES(3, 'Walter', 'White', '56-09 11st', 'New York', 'NY', '11445', 'WalterW@gmail.com', 101);
INSERT INTO Customer VALUES(4, 'Santa', 'Claus', '101 St Nicholas Dr', 'North Pole', 'AK', '99705', 'SantaC@christmas.com', 75);
INSERT INTO Customer VALUES(5, 'Amy', 'Queen', '20 W 34th St', 'New York', 'NY', '10001', 'AmyQ@gmail.com', 65);
INSERT INTO Customer VALUES(6, 'Raquel', 'Santos', '65-58 5st', 'New York', 'NY', '14101', 'RaquelS@gmail.com', 15);
INSERT INTO Customer VALUES(7, 'Raquel', 'Santos', '65-58 5st', 'New York', 'NY', '14101', 'RaquelS@gmail.com', 51);


CREATE TABLE VIP (
	Cust_ID INT PRIMARY KEY,
	F_Name VARCHAR(20) NOT NULL,
    L_Name VARCHAR(20) NOT NULL,
    street_addrs VARCHAR(20),
    city VARCHAR(20),
    state VARCHAR(20),
    ZIP INT,
    Email VARCHAR(40) NOT NULL,
    Orders INT,
     FOREIGN KEY (Cust_ID) REFERENCES Customer(Cust_ID)
);

INSERT INTO VIP
SELECT * FROM Customer
WHERE Orders > 50;

SELECT * FROM VIP;

CREATE TABLE Menu (
	food_item INT PRIMARY KEy,
    food_name VARCHAR(30),
    price FLOAT
);

INSERT INTO Menu VALUES(1, 'Chicken Pasta', 15.50);
INSERT INTO Menu VALUES(2, 'Mozerella Sticks', 8.00);
INSERT INTO Menu VALUES(3, 'Steak', 21.50);

CREATE TABLE Orders (
	Order_ID INT PRIMARY KEY,
    Cust_ID INT,
    price FLOAT,
    FOREIGN KEY (Cust_ID) REFERENCES Customer(Cust_ID)
);

CREATE TABLE OrdersItem (
	order_id INT,
    items_id INT,
    FOREIGN KEY (order_id) REFERENCES Orders(Order_ID),
    FOREIGN KEY (items_id) REFERENCES Menu(food_item)
);

CREATE TABLE Customer_Review (
	Review_ID INT PRIMARY KEY,
    rating INT,
    Comm VARCHAR(200),
    Reviewer_ID INT,
    Employee_ID INT,
	FOREIGN KEY (Reviewer_ID) REFERENCES Customer(Cust_ID),
	FOREIGN KEY (Employee_ID) REFERENCES Employees(Empl_ID)
);

CREATE TABLE Employee_Review (
	Review_ID INT PRIMARY KEY,
    rating INT,
    Comm VARCHAR(200),
    Reviewer_ID INT,
    Customer_ID INT,
	FOREIGN KEY (Reviewer_ID) REFERENCES Employees(Empl_ID),
	FOREIGN KEY (Customer_ID) REFERENCES Customer(Cust_ID)
);