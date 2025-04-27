# `database-files` Folder

TODO: Put some notes here about how this works. include how to re-bootstrap the db.

00_db_creation.sql creates the database and initializes all the relationships and tables. It also includes some initial
insert statements. Every subsequent file from 01 to 19 inserts the data into a table given by the file's name.