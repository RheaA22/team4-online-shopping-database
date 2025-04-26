USE team4_online_shopping_database;
create table OrderData (
                           orderID INT,
                           customerID INT,
                           storeID INT,
                           total DECIMAL(6,2),
                           status VARCHAR(50),
                           date DATE
);

insert into OrderData (orderID, customerID, storeID, total, status, date) values (2, 2, 1, 320.75, 'completed', '2025-02-24');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (3, 3, 2, 545.60, 'completed', '2025-02-25');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (4, 4, 3, 130.45, 'pending', '2025-02-26');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (5, 5, 4, 215.80, 'completed', '2025-02-27');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (6, 6, 5, 875.90, 'completed', '2025-02-28');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (7, 7, 1, 299.99, 'pending', '2025-03-01');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (8, 8, 2, 630.55, 'completed', '2025-03-02');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (9, 9, 3, 442.40, 'shipped', '2025-03-03');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (10, 10, 4, 100.15, 'completed', '2025-03-04');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (11, 11, 5, 380.65, 'completed', '2025-03-05');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (12, 12, 1, 210.45, 'pending', '2025-03-06');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (13, 13, 2, 660.00, 'completed', '2025-03-07');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (14, 14, 3, 155.20, 'completed', '2025-03-08');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (15, 15, 4, 99.99, 'shipped', '2025-03-09');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (16, 16, 5, 300.10, 'pending', '2025-03-10');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (17, 17, 1, 720.50, 'completed', '2025-03-11');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (18, 18, 2, 150.25, 'completed', '2025-03-12');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (19, 19, 3, 920.60, 'shipped', '2025-03-13');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (20, 20, 4, 125.30, 'completed', '2025-03-14');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (21, 21, 5, 380.40, 'pending', '2025-03-15');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (22, 22, 1, 640.75, 'completed', '2025-03-16');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (23, 23, 2, 110.90, 'shipped', '2025-03-17');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (24, 24, 3, 550.50, 'pending', '2025-03-18');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (25, 25, 4, 410.35, 'completed', '2025-03-19');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (26, 26, 5, 770.60, 'completed', '2025-03-20');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (27, 27, 1, 324.45, 'shipped', '2025-03-21');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (28, 28, 2, 410.85, 'completed', '2025-03-22');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (29, 29, 3, 105.60, 'completed', '2025-03-23');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (30, 30, 4, 525.30, 'pending', '2025-03-24');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (31, 31, 5, 115.75, 'shipped', '2025-03-25');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (32, 32, 1, 402.80, 'completed', '2025-03-26');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (33, 33, 2, 390.20, 'completed', '2025-03-27');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (34, 34, 3, 275.30, 'pending', '2025-03-28');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (35, 35, 4, 550.60, 'completed', '2025-03-29');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (36, 36, 5, 670.80, 'shipped', '2025-03-30');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (37, 37, 1, 380.55, 'completed', '2025-03-31');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (38, 38, 2, 990.90, 'shipped', '2025-04-01');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (39, 39, 3, 215.45, 'pending', '2025-04-02');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (40, 40, 4, 610.75, 'completed', '2025-04-03');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (41, 41, 5, 530.90, 'shipped', '2025-04-04');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (42, 42, 1, 655.30, 'completed', '2025-04-05');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (43, 43, 2, 690.50, 'pending', '2025-04-06');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (44, 44, 3, 405.40, 'completed', '2025-04-07');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (45, 45, 4, 925.20, 'shipped', '2025-04-08');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (46, 46, 5, 385.10, 'pending', '2025-04-09');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (47, 47, 1, 520.60, 'completed', '2025-04-10');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (48, 48, 2, 270.90, 'shipped', '2025-04-11');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (49, 49, 3, 115.60, 'completed', '2025-04-12');
insert into OrderData (orderID, customerID, storeID, total, status, date) values (50, 50, 4, 875.10, 'pending', '2025-04-13');
