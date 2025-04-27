DROP SCHEMA IF EXISTS `northwind`;
CREATE SCHEMA IF NOT EXISTS online_shop DEFAULT CHARACTER SET latin1;
USE online_shop;

CREATE TABLE IF NOT EXISTS online_shop.Company (
    companyID INT PRIMARY KEY,
    name VARCHAR(50),
    phoneNumber VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS online_shop.Manager (
    manager_id INT PRIMARY KEY,
    managerLevel VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS online_shop.Store (
    store_id INT PRIMARY KEY,
    name VARCHAR(50),
    isOnline VARCHAR(50),
    location VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS online_shop.Brand (
    brandID INT PRIMARY KEY,
    name VARCHAR(50),
    sustainability_score INT,
    accessibility_rating INT
);

CREATE TABLE IF NOT EXISTS online_shop.Customer (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50),
    age INT,
    address VARCHAR(50),
    middle_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS online_shop.Advertisement (
    adID INT PRIMARY KEY,
    companyID INT,
    managerID INT,
    content VARCHAR(50),
    target_segment VARCHAR(50),
    FOREIGN KEY (companyID) REFERENCES online_shop.Company(companyID),
    FOREIGN KEY (managerID) REFERENCES online_shop.Manager(manager_id)
);

CREATE TABLE IF NOT EXISTS online_shop.AdvertisementViews (
    adID INT,
    customerID INT,
    PRIMARY KEY (adID, customerID),
    FOREIGN KEY (adID) REFERENCES online_shop.Advertisement(adID),
    FOREIGN KEY (customerID) REFERENCES online_shop.Customer(customer_id)
);

CREATE TABLE IF NOT EXISTS online_shop.CustomerPreferences (
    customerID INT,
    preference VARCHAR(50),
    PRIMARY KEY (customerID, preference),
    FOREIGN KEY (customerID) REFERENCES online_shop.Customer(customer_id)
);

CREATE TABLE IF NOT EXISTS online_shop.Employee (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50),
    middle_name VARCHAR(50),
    role VARCHAR(50),
    StoreID INT,
    FOREIGN KEY (StoreID) REFERENCES online_shop.Store(store_id)
);

CREATE TABLE IF NOT EXISTS online_shop.EmployeeInteractions (
    interaction_id INT PRIMARY KEY,
    employee_id INT,
    customer_id INT,
    message VARCHAR(50),
    date DATE,
    FOREIGN KEY (employee_id) REFERENCES online_shop.Employee(employee_id),
    FOREIGN KEY (customer_id) REFERENCES online_shop.Customer(customer_id)
);

CREATE TABLE IF NOT EXISTS online_shop.EventAttendees (
    eventID INT,
    customerID INT,
    PRIMARY KEY (eventID, customerID),
    FOREIGN KEY (eventID) REFERENCES online_shop.VirtualEvent(eventID),
    FOREIGN KEY (customerID) REFERENCES online_shop.Customer(customer_id)
);

CREATE TABLE IF NOT EXISTS online_shop.Inventory (
    storeID INT,
    SKU VARCHAR(50),
    reorder_level INT,
    quantity INT,
    PRIMARY KEY (storeID, SKU),
    FOREIGN KEY (storeID) REFERENCES online_shop.Store(store_id),
    FOREIGN KEY (SKU) REFERENCES online_shop.Product(SKU)
);

CREATE TABLE IF NOT EXISTS online_shop.ManagerInteractions (
    interaction_id INT PRIMARY KEY,
    manager_id INT,
    customer_id INT,
    message VARCHAR(50),
    date DATE,
    FOREIGN KEY (manager_id) REFERENCES online_shop.Manager(manager_id),
    FOREIGN KEY (customer_id) REFERENCES online_shop.Customer(customer_id)
);

CREATE TABLE IF NOT EXISTS online_shop.OrderData (
    orderID INT PRIMARY KEY,
    customerID INT,
    storeID INT,
    total DECIMAL(6,2),
    status VARCHAR(50),
    date DATE,
    FOREIGN KEY (customerID) REFERENCES online_shop.Customer(customer_id),
    FOREIGN KEY (storeID) REFERENCES online_shop.Store(store_id)
);

CREATE TABLE IF NOT EXISTS online_shop.OrderProduct (
    orderID INT,
    SKU VARCHAR(50),
    quantity INT,
    PRIMARY KEY (orderID, SKU),
    FOREIGN KEY (orderID) REFERENCES online_shop.OrderData(orderID),
    FOREIGN KEY (SKU) REFERENCES online_shop.Product(SKU)
);

CREATE TABLE IF NOT EXISTS online_shop.Product (
    SKU VARCHAR(50) PRIMARY KEY,
    brandID INT,
    name VARCHAR(50),
    category VARCHAR(50),
    price VARCHAR(50),
    material VARCHAR(50),
    trendScore INT,
    eco_certification VARCHAR(50),
    FOREIGN KEY (brandID) REFERENCES online_shop.Brand(brandID)
);

CREATE TABLE IF NOT EXISTS online_shop.ProductFeatures (
    SKU VARCHAR(50),
    feature VARCHAR(50),
    PRIMARY KEY (SKU, feature),
    FOREIGN KEY (SKU) REFERENCES online_shop.Product(SKU)
);

CREATE TABLE IF NOT EXISTS online_shop.Review (
    reviewID INT PRIMARY KEY,
    customerID INT,
    SKU VARCHAR(50),
    comment VARCHAR(50),
    rating INT,
    comfort_score INT,
    FOREIGN KEY (customerID) REFERENCES online_shop.Customer(customer_id),
    FOREIGN KEY (SKU) REFERENCES online_shop.Product(SKU)
);

CREATE TABLE IF NOT EXISTS online_shop.VirtualEvent (
    eventID INT PRIMARY KEY,
    managerID INT,
    adID INT,
    name VARCHAR(50),
    FOREIGN KEY (managerID) REFERENCES online_shop.Manager(manager_id),
    FOREIGN KEY (adID) REFERENCES online_shop.Advertisement(adID)
);
