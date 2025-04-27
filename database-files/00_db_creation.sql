DROP SCHEMA IF EXISTS `northwind`;
CREATE SCHEMA IF NOT EXISTS db DEFAULT CHARACTER SET latin1;
USE db;

CREATE TABLE IF NOT EXISTS db.Company (
    companyID INT PRIMARY KEY,
    name VARCHAR(50),
    phoneNumber VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS db.Manager (
    manager_id INT PRIMARY KEY,
    managerLevel VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS db.Store (
    store_id INT PRIMARY KEY,
    name VARCHAR(50),
    isOnline VARCHAR(50),
    location VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS db.Brand (
    brandID INT PRIMARY KEY,
    name VARCHAR(50),
    sustainability_score INT,
    accessibility_rating INT
);

CREATE TABLE IF NOT EXISTS db.Customer (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50),
    age INT,
    address VARCHAR(50),
    middle_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS db.Advertisement (
    adID INT PRIMARY KEY,
    companyID INT,
    managerID INT,
    content VARCHAR(50),
    target_segment VARCHAR(50),
    FOREIGN KEY (companyID) REFERENCES db.Company(companyID),
    FOREIGN KEY (managerID) REFERENCES db.Manager(manager_id)
);

CREATE TABLE IF NOT EXISTS db.AdvertisementViews (
    adID INT,
    customerID INT,
    PRIMARY KEY (adID, customerID),
    FOREIGN KEY (adID) REFERENCES db.Advertisement(adID),
    FOREIGN KEY (customerID) REFERENCES db.Customer(customer_id)
);

CREATE TABLE IF NOT EXISTS db.CustomerPreferences (
    customerID INT,
    preference VARCHAR(50),
    PRIMARY KEY (customerID, preference),
    FOREIGN KEY (customerID) REFERENCES db.Customer(customer_id)
);

CREATE TABLE IF NOT EXISTS db.Employee (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50),
    middle_name VARCHAR(50),
    role VARCHAR(50),
    StoreID INT,
    FOREIGN KEY (StoreID) REFERENCES db.Store(store_id)
);

CREATE TABLE IF NOT EXISTS db.EmployeeInteractions (
    interaction_id INT PRIMARY KEY,
    employee_id INT,
    customer_id INT,
    message VARCHAR(50),
    date DATE,
    FOREIGN KEY (employee_id) REFERENCES db.Employee(employee_id),
    FOREIGN KEY (customer_id) REFERENCES db.Customer(customer_id)
);

CREATE TABLE IF NOT EXISTS db.EventAttendees (
    eventID INT,
    customerID INT,
    PRIMARY KEY (eventID, customerID),
    FOREIGN KEY (eventID) REFERENCES db.VirtualEvent(eventID),
    FOREIGN KEY (customerID) REFERENCES db.Customer(customer_id)
);

CREATE TABLE IF NOT EXISTS db.Inventory (
    storeID INT,
    SKU VARCHAR(50),
    reorder_level INT,
    quantity INT,
    PRIMARY KEY (storeID, SKU),
    FOREIGN KEY (storeID) REFERENCES db.Store(store_id),
    FOREIGN KEY (SKU) REFERENCES db.Product(SKU)
);

CREATE TABLE IF NOT EXISTS db.ManagerInteractions (
    interaction_id INT PRIMARY KEY,
    manager_id INT,
    customer_id INT,
    message VARCHAR(50),
    date DATE,
    FOREIGN KEY (manager_id) REFERENCES db.Manager(manager_id),
    FOREIGN KEY (customer_id) REFERENCES db.Customer(customer_id)
);

CREATE TABLE IF NOT EXISTS db.OrderData (
    orderID INT PRIMARY KEY,
    customerID INT,
    storeID INT,
    total DECIMAL(6,2),
    status VARCHAR(50),
    date DATE,
    FOREIGN KEY (customerID) REFERENCES db.Customer(customer_id),
    FOREIGN KEY (storeID) REFERENCES db.Store(store_id)
);

CREATE TABLE IF NOT EXISTS db.OrderProduct (
    orderID INT,
    SKU VARCHAR(50),
    quantity INT,
    PRIMARY KEY (orderID, SKU),
    FOREIGN KEY (orderID) REFERENCES db.OrderData(orderID),
    FOREIGN KEY (SKU) REFERENCES db.Product(SKU)
);

CREATE TABLE IF NOT EXISTS db.Product (
    SKU VARCHAR(50) PRIMARY KEY,
    brandID INT,
    name VARCHAR(50),
    category VARCHAR(50),
    price VARCHAR(50),
    material VARCHAR(50),
    trendScore INT,
    eco_certification VARCHAR(50),
    FOREIGN KEY (brandID) REFERENCES db.Brand(brandID)
);

CREATE TABLE IF NOT EXISTS db.ProductFeatures (
    SKU VARCHAR(50),
    feature VARCHAR(50),
    PRIMARY KEY (SKU, feature),
    FOREIGN KEY (SKU) REFERENCES db.Product(SKU)
);

CREATE TABLE IF NOT EXISTS db.Review (
    reviewID INT PRIMARY KEY,
    customerID INT,
    SKU VARCHAR(50),
    comment VARCHAR(50),
    rating INT,
    comfort_score INT,
    FOREIGN KEY (customerID) REFERENCES db.Customer(customer_id),
    FOREIGN KEY (SKU) REFERENCES db.Product(SKU)
);

CREATE TABLE IF NOT EXISTS db.VirtualEvent (
    eventID INT PRIMARY KEY,
    managerID INT,
    adID INT,
    name VARCHAR(50),
    FOREIGN KEY (managerID) REFERENCES db.Manager(manager_id),
    FOREIGN KEY (adID) REFERENCES db.Advertisement(adID)
);
