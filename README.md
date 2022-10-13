# Designing a Database From Scratch

## Project Instructions

#### Designing A Database From Scratch

the main purposes of this project are:

To design a database schema on a topic of your choosing.
To implement that schema on your own computer using Postbird.


Part 1 — Research

For this project, you are going to create a database based on a topic of your choosing. To make things even trickier, this project works best when you create a database scheme based on a topic that you don’t already have knowledge about.

Part 2 — Turn Your Diagram Into A Database Schema

Now that you’ve learned about the database that you’ll be creating, it’s time to implement your database in Postgres! We used Postbird to connect to our local PostgreSQL server, but you can use whatever client you are most comfortable with.

Part 3 — Add Data To Your Tables

Now that you’ve created your tables, one of the best ways to verify they’re working as expected is to add some test data. Add enough rows to your tables to test all of the relationships you have created. For example, if you think you have created a one-to-many relationship using foreign keys, make sure that you can actually create multiple rows that all reference a single row from another table.

Part 4 — Edit Your Schema As Necessary

As you entered data into your tables, you might have uncovered some issues that you didn’t anticipate. That’s ok! It’s hard to get a schema perfect on the first try. Maybe a column’s data type needs to be changed. Or maybe you realized that a one-to-many relationship should actually be a many-to-many relationship. Whatever the problem is, this is your opportunity to iterate.

If you’re not familiar with how to edit a table’s structure after it has already been created, you can take a look at the documentation on ALTER TABLE. Specifically, some of the commands that might be useful are ADD COLUMN, DROP COLUMN, SET DATA TYPE, and ADD table_constraint.


## My project

I designed a retail store database using dbdiagram.io which produced an SQL file with tables in SQL script and a diagram of the table database in pdf format. 

CSV files were downloaded and used to insert data into tables. 

When the main.py script is run:

* The tables are empty and data gets inserted by automatically calling populate_tables()
* A list of 20 customer ids, names, and surnames printed 
* User is prompted to enter the customer id to view the sales of a particular customer
* A list of all the historical purchases of customer id is printed
* User is then given an option to select another customer's details or end progress
* program is end with 'Good Bye!!' printed. 

Requirements:

Pandas
Random
sqlite3
