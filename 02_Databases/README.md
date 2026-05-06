# Intoduction to Web-App Back-End Development

This is my guide for web-app backend development, based on the [Meta Back-End Developer Professional Certificate](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/professional-certificates/meta-back-end-developer) specialization on Coursera. From that specializatuon, I have selected these topics/courses:

1. [Introduction to Back-End Development](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/learn/introduction-to-back-end-development)
2. [Introduction to Databases for Back-End Development](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/learn/intro-to-databases-back-end-development)
3. [Django Web Framework](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/learn/django-web-framework?authProvider)
4. [APIs](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/learn/apis)
5. [The Full Stack](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/learn/the-full-stack?authProvider=deutschetelekom)
6. [Back-End Developer Capstone Project](https://www.coursera.org/programs/deutsche-telekom-learning-program-ddjuh/learn/back-end-developer-capstone)

This module deals with the second topic/course: **Introduction to Databases for Back-End Development**.

Table of Contents:

- [Intoduction to Web-App Back-End Development](#intoduction-to-web-app-back-end-development)
  - [0. Setup](#0-setup)
  - [1. Introduction to Databases](#1-introduction-to-databases)
    - [Databases and Data](#databases-and-data)
      - [What is a Database?](#what-is-a-database)
      - [How Is Data Related?](#how-is-data-related)
      - [Charts for Relational Data](#charts-for-relational-data)
      - [Other Types of Databases](#other-types-of-databases)
    - [Introduction to SQL](#introduction-to-sql)
      - [SQL Syntax Introduction](#sql-syntax-introduction)
      - [Common SQL (DQL) Commands](#common-sql-dql-commands)
    - [Basic Database Structure](#basic-database-structure)
      - [Tables in Databases](#tables-in-databases)
      - [Database Structure](#database-structure)
      - [Type of Keys in a Database Table](#type-of-keys-in-a-database-table)
  - [2. CRUD Operations: Create, Read, Update, Delete](#2-crud-operations-create-read-update-delete)
    - [MySQL Setup](#mysql-setup)
    - [SQL Data Types](#sql-data-types)
      - [Numeric Data Types](#numeric-data-types)
      - [Exercise: Working with Numbers](#exercise-working-with-numbers)
      - [String Data Types](#string-data-types)
      - [Exercise: Working with Strings](#exercise-working-with-strings)
      - [Default Values](#default-values)
      - [Exercise: Working with Default Values](#exercise-working-with-default-values)
    - [Create and Read](#create-and-read)
    - [Update and Delete](#update-and-delete)
  - [3. SQL Operators and Sorting and Filtering Data](#3-sql-operators-and-sorting-and-filtering-data)
    - [SQL Operators](#sql-operators)
    - [Sorting and Filtering Data](#sorting-and-filtering-data)
  - [4. Database Design](#4-database-design)
    - [Designing Database Schema](#designing-database-schema)
    - [Relational Database Design](#relational-database-design)
    - [Database Normalization](#database-normalization)
  - [5. Assessment](#5-assessment)

## 0. Setup

My guide on SQL: [`mxagar/sql_guide`](https://github.com/mxagar/sql_guide).

The course uses [MySQL](https://www.mysql.com/).

Here's a guide on how to use MySQL with Python on our local machine (installation, connection, and basic operations):

[`mxagar/sql_guide/SQL_Guide.md/MySQL-with-Python`](https://github.com/mxagar/sql_guide/blob/main/SQL_Guide.md#11-mysql-with-python)

## 1. Introduction to Databases

My guide on SQL: [`mxagar/sql_guide`](https://github.com/mxagar/sql_guide).

### Databases and Data

#### What is a Database?

* Data consists of facts and figures about entities, such as personal details or transaction records, and is essential for individuals and organizations.
* A database is an electronic system that stores and organizes data systematically to enable efficient management and retrieval.
* Databases are widely used in real-world applications, such as banking systems and hospital records.
* Data is organized in a structured way, typically in table-like formats with identifiable attributes.
* Data is grouped into entities representing real or conceptual objects (e.g., customer, product, order).
  * In relational databases, entities are tables, attributes are columns, and rows represent instances.
* Relationships between entities allow combining data (e.g., customer + product → order table).
* There are multiple database types: 
  * relational (tables),
  * object-oriented (objects/classes),
  * graph (nodes/edges),
  * document (JSON collections).
* Databases can be hosted on-premises or in the cloud, with cloud solutions being more scalable and cost-effective.

![Object-Oriented Database](./assets/object_oriented_db.png)

![Graph Database](./assets/graph_db.png)

![Document Database](./assets/document_db.png)

#### How Is Data Related?

* Data in a database must be related to other data to produce meaningful information and enable useful queries.
* Relationships are established by linking tables, such as connecting a customer table with an order table using shared identifiers.
* Tables consist of fields (columns) and records (rows), which together represent an entity (e.g., customers or orders).
* Each record must be uniquely identifiable using a **primary key**, which contains unique values (e.g., customer ID).
* To connect tables, a field from one table is reused in another.
  * This field becomes a **foreign key**, linking to the primary key of the original table.
* For example, customer ID is the primary key in the customer table and a foreign key in the order table, enabling retrieval of customer-order relationships.
* These key relationships allow databases to combine and query data across multiple tables effectively.

![Primary and Foreign Key](./assets/primary_foreign_key.png)

#### Charts for Relational Data

![Bar Chart](./assets/bar_chart.png)

![Line Chart](./assets/line_chart.PNG)

![Bubble Chart](./assets/bubble_chart.PNG)

![Pie Chart](./assets/pie_chart.png)

#### Other Types of Databases

* Databases have evolved significantly due to the growth of the internet and the need to handle large volumes of data, especially unstructured data.
* Traditional relational databases are limited because they mainly store structured data, which does not scale well for modern data needs.
* NoSQL databases were introduced to address this limitation by supporting flexible data formats and easier scalability.
  * Common types include document, key-value, and graph databases.
  * They are widely used in social media, IoT, and AI applications that generate large amounts of unstructured data.
* Big data refers to complex datasets that grow rapidly in volume and come from sources like social media, online platforms, and connected devices.
  * It includes structured, semi-structured, and unstructured data.
  * It enables advanced analytics, better decision-making, and solving complex business problems.
* Big data is applied across industries.
  * Manufacturing uses it for predictive maintenance and process optimization.
  * Retail uses it to understand customer behavior and improve pricing.
  * Telecommunications uses it for network planning and customer retention.
* Cloud databases have become popular because they remove the need to manage physical infrastructure and reduce costs.
  * They allow storing and accessing data over the internet (e.g., cloud storage services).
* Business intelligence (BI) represents a shift from just storing data to analyzing it for insights and decision-making.
* Database technologies continue to evolve with trends like NoSQL, big data, cloud computing, and BI shaping modern data systems.

### Introduction to SQL

* To work with data, engineers must interact with databases using **SQL (Structured Query Language)**, the standard language for database operations.
* SQL is used to build and manage databases by performing **CRUD operations**: create, read, update, and delete data.
* SQL is mainly used with **relational databases** such as MySQL, PostgreSQL, Oracle Database, and Microsoft SQL Server.
* SQL instructions are processed through a **Database Management System (DBMS)**.
  * The DBMS translates SQL commands into operations the database can execute.
* SQL is essential for interacting with structured data and is a core skill for data engineers and backend developers.
* SQL is divided into sublanguages based on functionality:
  * **DDL (Data Definition Language)** is used to define and modify database structure.
    * Includes commands like `CREATE`, `ALTER`, and `DROP`.
  * **DML (Data Manipulation Language)** is used to manipulate data within tables.
    * Includes `INSERT`, `UPDATE`, and `DELETE` (core CRUD operations).
  * **DQL (Data Query Language)** is used to retrieve data.
    * Includes the `SELECT` command with filtering and multi-table queries.
  * **DCL (Data Control Language)** is used to manage access and permissions.
    * Includes `GRANT` and `REVOKE`.
* SQL acts as the interface between users and the database, enabling both data management and access control.
* Advantages of SQL:
  * SQL is **simple and user-friendly**, requiring minimal coding since it relies on a small set of keywords for CRUD operations.
  * SQL is **interactive and efficient**, allowing complex queries to be written and executed quickly.
  * SQL is a **standard language** supported across relational databases like MySQL, ensuring broad compatibility and strong community support.
  * SQL is **portable**, meaning the same code can run across different hardware, operating systems, and environments without modification.
  * SQL is **comprehensive**, covering all aspects of database management through sublanguages like DDL, DML, DQL, and DCL.
  * SQL is **efficient at processing large datasets**, enabling fast and scalable data operations.

#### SQL Syntax Introduction

* SQL is the standard language for interacting with relational databases, enabling data access, definition, manipulation, querying, and permission management.
* SQL operations are grouped into five main sublanguages based on functionality:
  * **DDL (Data Definition Language)** defines and modifies database structure (e.g., tables).
  * **DML (Data Manipulation Language)** handles inserting, updating, and deleting data (CRUD).
  * **DQL (Data Query Language)** retrieves data from the database.
  * **DCL (Data Control Language)** manages user permissions and access.
  * **TCL (Transaction Control Language)** manages transactions and ensures data consistency.
* Typical database workflow:
  * Create database and tables (structure).
  * Insert and manage data.
  * Query data for insights.
  * Control access and manage transactions.
* Core concepts and operations include:
  * Creating and modifying tables and schemas.
  * Inserting, updating, deleting, and querying records.
  * Managing permissions (grant/revoke).
  * Handling transactions (commit/rollback).
  * Using comments for documentation.

```sql
-- =====================
-- DDL: Define structure
-- =====================

CREATE DATABASE college;
-- Creates a new database

CREATE TABLE student (id INT, name VARCHAR(100), dob DATE);
-- Creates a table with columns and data types

ALTER TABLE student ADD (email VARCHAR(100));
-- Adds a new column to an existing table

ALTER TABLE student ADD PRIMARY KEY (id);
-- Defines a primary key for unique identification

DROP TABLE student;
-- Deletes the table entirely

TRUNCATE TABLE student;
-- Removes all rows but keeps the table structure

-- Comment example
-- This query retrieves all students
SELECT * FROM student;


-- =====================
-- DML: Manipulate data
-- =====================

INSERT INTO student (id, name, dob)
VALUES (1, 'John Murphy', '2000-01-01');
-- Inserts a new record

UPDATE student
SET dob = '2001-02-02'
WHERE id = 2;
-- Updates specific records based on condition

DELETE FROM student
WHERE id = 3;
-- Deletes specific records


-- =====================
-- DQL: Query data
-- =====================

SELECT * FROM student;
-- Retrieves all data from the table

SELECT name FROM student WHERE id = 1;
-- Retrieves specific data with filtering


-- =====================
-- DCL: Permissions
-- =====================

GRANT SELECT, INSERT ON student TO user1;
-- Gives user permissions

REVOKE INSERT ON student FROM user1;
-- Removes permissions


-- =====================
-- TCL: Transactions
-- =====================

COMMIT;
-- Saves all changes permanently

ROLLBACK;
-- Reverts changes to last committed state
```

#### Common SQL (DQL) Commands

Source: [`mxagar/sql_guide/SQL_Nutshell.md`](https://github.com/mxagar/sql_guide/blob/main/SQL_Nutshell.md).

```sql
-- Get all the contents from the table my_table: we get a table
SELECT * FROM my_table;

-- Get specified columns and compute a new column value: we get a table
SELECT origin, dest, air_time / 60 FROM flights;

-- Filter according to value in column: we get a table
SELECT * FROM students
WHERE grade = 'A';

-- Get the table which contains the destination and tail number of flights that last +10h
SELECT dest, tail_num FROM flights WHERE air_time > 600;

-- Group by: group by category values and apply an aggregation function for each group
-- In this case: number of flights for each unique origin
SELECT COUNT(*) FROM flights
GROUP BY origin;

-- Group by all unique combinations of origin and dest columns
SELECT origin, dest, COUNT(*) FROM flights
GROUP BY origin, dest;

-- Group by unique origin-carrier combinations and for each
-- compute average air time in hrs
SELECT AVG(air_time) / 60 FROM flights
GROUP BY origin, carrier;

-- Flight duration in hrs, new column name
SELECT air_time / 60 AS duration_hrs
FROM flights

-- INNER JOIN: note it is symmetrical, we can interchange TableA and B
SELECT * FROM TableA
INNER JOIN TableB
ON TableA.col_match = TableB.col_match;

-- FULL OUTER JOIN
SELECT * FROM TableA
FULL OUTER JOIN TableB
ON TableA.col_match = Table_B.col_match

-- LEFT OUTER JOIN
-- Left table: TableA; Right table: TableB
SELECT * FROM TableA
LEFT OUTER JOIN TableB
ON TableA.col_match = Table_B.col_match

-- RIGHT OUTER JOIN
-- Left table: TableA; Right table: TableB
SELECT * FROM TableA
RIGHT OUTER JOIN TableB
ON TableA.col_match = Table_B.col_match
```

### Basic Database Structure

#### Tables in Databases

* A **table** is the fundamental structure in a relational database, used to store data in a logical format of rows and columns.
  * Rows (records/tuples) represent individual instances (e.g., one student).
  * Columns (fields/attributes) define the structure and type of data stored (e.g., name, date of birth).
  * A **cell** is the intersection of a row and column, where a single data value is stored.
* Tables are also called **relations**, and each table has a **schema**, which defines its structure (table name, columns, and data types).
  * In real systems, multiple related tables exist (e.g., Student, Teacher, Class, Subject).
* Every column has a **data type**, which defines what values it can store and how SQL handles them.
  * Common types include:
    * Numeric: `INT`, `FLOAT`, `BIGINT`
    * Date/time: `DATE`, `DATETIME`
    * Strings: `CHAR`, `VARCHAR`
    * Binary: `BINARY`, `VARBINARY`
    * Large objects: `CLOB` (text), `BLOB` (binary data like images)
* A **domain** defines the valid set of values for a column, ensuring data consistency (e.g., numeric-only fields, length limits).

![DB Structure: Types](./assets/db_structure_types.png)

* Each table must have a **primary key**, a column (or combination of columns) that uniquely identifies each row.
  * It cannot be NULL and must be unique.
  * It can be **composite** (multiple columns) if one column is not sufficient.
* Tables are connected through **foreign keys**, which reference the primary key of another table.
  * This creates relationships between tables and enables meaningful queries across them.

![DB Structure: Primary Keys](./assets/db_structure_primary_key.png)

![DB Structure: Foreign Keys](./assets/db_structure_foreign_key.png)

* Databases enforce **integrity constraints** to maintain correct and consistent data:
  * **Key constraints**: ensure primary keys are unique and not null.
  * **Domain constraints**: restrict allowed values in columns.
  * **Referential integrity constraints**: ensure foreign key values exist in the referenced table.
* Together, these concepts (tables, schema, data types, keys, relationships, and constraints) define how relational databases structure, link, and validate data.

#### Database Structure

* **Database structure** refers to how data is organized within a database, typically in tables composed of rows (records/tuples) and columns (fields/attributes).
* The main structural components of a database include:
  * **Tables (entities)**: store data about a specific concept.
  * **Attributes/fields (columns)**: describe properties of the entity.
  * **Records (rows)**: represent individual instances of the entity.
  * **Data elements (cell values)**: individual pieces of data in each field.
  * **Primary key**: uniquely identifies each record.
* Each column has a **data type**, which defines the kind of data it can store and how it is processed.
  * Common types include numeric, date/time, string, binary, and large object types (CLOB, BLOB).

![Elements in a Table](./assets/elements_in_table.png)

* The **logical database structure** is represented using an **Entity Relationship Diagram (ERD)**.
  * It visually shows entities, attributes, and relationships.
  * Relationships have **cardinality**: one-to-one, one-to-many, and many-to-many.

![Logical Structure ERD](./assets/logical_structure_erd.png)

* The **physical database structure** implements the logical design using actual tables in a DBMS (e.g., MySQL or Oracle Database).
  * Relationships are created using **foreign keys**, which reference primary keys in other tables.
* Together, tables, fields, records, keys, data types, and relationships define how data is structured, linked, and stored in a relational database.

![Physical Structure](./assets/physical_structure.png)

#### Type of Keys in a Database Table

* The relational database model is based on **entities (tables)** and **relationships** between them, which are established using keys.
* Tables contain attributes (columns), which can be:
  * **Simple attributes** (single value per row).
  * **Multi-valued attributes** (multiple values), which should generally be avoided in relational design.
* A **key attribute** is any column used to uniquely identify a record in a table (e.g., staff ID).
* There are several types of keys in relational databases:
  * **Primary key**: the main unique identifier for each record; cannot be duplicated or null.
  * **Candidate keys**: all columns that could uniquely identify a record.
  * **Alternate (secondary) key**: a candidate key not chosen as the primary key.
  * **Composite key**: a combination of multiple columns used as a unique identifier when a single column is insufficient.
  * **Foreign key**: a column that references the primary key in another table, establishing relationships between tables.
* Non-key attributes are columns that do not uniquely identify records and may contain duplicate values.
* Relationships between tables are built by linking **primary keys** in one table to **foreign keys** in another, enabling structured and connected data across the database.

## 2. CRUD Operations: Create, Read, Update, Delete

### MySQL Setup

This module uses MySQL as the relational database management system (RDBMS) for practicing SQL commands and CRUD operations.

See my note on [MySQL Installation on Windows](https://github.com/mxagar/sql_guide/blob/main/SQL_Guide.md#windows-1).

After that, the exercises can be carried out using MySQL Workbench or the MySQL command line interface.

### SQL Data Types

#### Numeric Data Types

* **Data types** define what kind of values each column in a table can store and how the database interprets them.
* When creating a table, each column must be assigned a data type to ensure data consistency and correct formatting.
* Common data type categories include:
  * Numeric
  * String
  * Date and time
* **Numeric data types** are used to store numbers and include two main types:
  * **Integer**: stores whole numbers (e.g., product quantity).
  * **Decimal**: stores numbers with fractional values (e.g., prices).
* Integer columns automatically round fractional inputs to whole numbers, while decimal columns preserve fractional values.
* Different database systems provide multiple variants of numeric types with different ranges (e.g., `TINYINT`, `INT`).
* Numeric types can typically store both positive and negative values, and some systems allow restricting values to positive only.
* Choosing the correct data type ensures accurate data storage, efficient processing, and proper validation of input values.

#### Exercise: Working with Numbers

See the instructions in [02_Databases/lab/01_numbers/Instructions.md](./lab/01_numbers/Instructions.md).

In the example, the following is done:

- A new database called `cm_devices` is created.
- The `cm_devices` database is selected with `USE`.
- A table called `devices` is created to store mobile device information.
- The table contains:
  * `deviceID`: an integer value for the device identifier.
  * `deviceName`: a string value for the device name.
  * `price`: a decimal value for the device price.
- The created table and its columns are checked with `SHOW TABLES` and `SHOW COLUMNS`.

To carry out the exercise, we need MySQL installed -- check the [MySQL Setup](#mysql-setup) section above. Then, we open the CLI:

```bash
# On local Windows machine (we need root PW)
mysql -u root -p

# ... Or on Coursera VSCode Terminal:
mysql
```

And the SQL commands executed are the following:

```sql
-- Create database
CREATE DATABASE cm_devices;

-- Select database
USE cm_devices;

-- Create table for mobile devices
CREATE TABLE devices (
  deviceID INT,
  deviceName VARCHAR(50),
  price DECIMAL
);

-- Check that the table was created
SHOW TABLES;
--- +----------------------+
--- | Tables_in_cm_devices |
--- +----------------------+
--- | devices              |
--- +----------------------+

-- Check the table structure
SHOW COLUMNS FROM devices;
--- +------------+---------------+------+-----+---------+-------+
--- | Field      | Type          | Null | Key | Default | Extra |
--- +------------+---------------+------+-----+---------+-------+
--- | deviceID   | int           | YES  |     | NULL    |       |
--- | deviceName | varchar(50)   | YES  |     | NULL    |       |
--- | price      | decimal(10,0) | YES  |     | NULL    |       |
--- +------------+---------------+------+-----+---------+-------+
```

The optional additional task asks us to create another table for device stock. The appropriate table name is `stock`, with the following columns:

- `deviceID`: integer device identifier.
- `quantity`: integer number of devices in stock.
- `totalCost`: decimal total cost of that quantity.

The SQL statement is:

```sql
CREATE TABLE stock (
  deviceID INT,
  quantity INT,
  totalCost DECIMAL
);
```

#### String Data Types

* **String data types** are used for columns that store text or mixed character data, including letters, numbers, and special characters.
* Assigning the correct string data type helps maintain **data integrity** by ensuring valid values are stored in each column.
* Common examples of string-based fields include names, usernames, passwords, and email addresses.
* The two most common string data types are:
  * `CHAR`: fixed-length character storage.
  * `VARCHAR`: variable-length character storage.
* `CHAR(n)` reserves exactly `n` characters of storage, regardless of the actual text length.
  * Best used when the size of the stored data is predictable and constant.
* `VARCHAR(n)` stores only the actual number of characters entered, up to a maximum length of `n`.
  * Best used when text lengths vary.
* Additional text data types support larger amounts of text:
  * `TINYTEXT`: short text (<255 characters).
  * `TEXT`: medium-sized text (<65k characters).
  * `MEDIUMTEXT`: very large text (~16.7 million characters).
  * `LONGTEXT`: extremely large text (up to several GB).

```sql
-- Fixed-length string: always reserves 50 characters
username CHAR(50);

-- Variable-length string: stores only used characters, up to 50
student_name VARCHAR(50);

-- Short text content
description TINYTEXT;

-- Article-sized text
article TEXT;

-- Book-sized text
book_content MEDIUMTEXT;

-- Very large text storage
large_document LONGTEXT;
```

#### Exercise: Working with Strings

See the instructions in [02_Databases/lab/02_strings/Instructions.md](./lab/02_strings/Instructions.md) and the tips in [02_Databases/lab/02_strings/README.md](./lab/02_strings/README.md).

In the example, the following is done:

- The existing `cm_devices` database is used. If it does not exist yet, it is created first.
- A table called `customers` is created to store customer information.
- The table contains:
  * `username`: a fixed-length string value for the customer username.
  * `fullName`: a variable-length string value for the customer's full name.
  * `email`: a variable-length string value for the customer's email address.
- `CHAR` is used for values with a fixed length, while `VARCHAR` is used for values whose length can vary.
- The created table and its columns are checked with `SHOW TABLES` and `SHOW COLUMNS`.

To carry out the exercise, we need MySQL installed -- check the [MySQL Setup](#mysql-setup) section above. Then, we open the CLI:

```bash
# On local Windows machine (we need root PW)
mysql -u root -p

# ... Or on Coursera VSCode Terminal:
mysql
```

And the SQL commands executed are the following:

```sql
-- Create database if needed
CREATE DATABASE cm_devices;

-- Select database
USE cm_devices;

-- Create table for customer information
CREATE TABLE customers (
  username CHAR(9),
  fullName VARCHAR(100),
  email VARCHAR(255)
);

-- Check that the table was created
SHOW TABLES;
--- +----------------------+
--- | Tables_in_cm_devices |
--- +----------------------+
--- | customers            |
--- | devices              |
--- | stock                |
--- +----------------------+

-- Check the table structure
SHOW COLUMNS FROM customers;
--- +----------+--------------+------+-----+---------+-------+
--- | Field    | Type         | Null | Key | Default | Extra |
--- +----------+--------------+------+-----+---------+-------+
--- | username | char(9)      | YES  |     | NULL    |       |
--- | fullName | varchar(100) | YES  |     | NULL    |       |
--- | email    | varchar(255) | YES  |     | NULL    |       |
--- +----------+--------------+------+-----+---------+-------+
```

The optional additional task asks us to create another table for customer feedback. The appropriate table name is `feedback`, with the following columns:

- `feedbackID`: fixed-length string value for the feedback identifier.
- `feedbackType`: variable-length string value for the feedback category.
- `comment`: text value for the feedback comment.

The SQL statement is:

```sql
CREATE TABLE feedback (
  feedbackID CHAR(8),
  feedbackType VARCHAR(100),
  comment TEXT(500)
);
```

#### Default Values

* **Database constraints** enforce rules on tables and columns to ensure data accuracy, consistency, and reliability.
* Constraints can operate at:
  * **Column level**: apply rules to a specific column.
  * **Table level**: enforce rules involving multiple columns or relationships between tables.
* If inserted or updated data violates a constraint, the database rejects the operation.
* Two common constraints are:
  * `NOT NULL`: prevents columns from containing empty (`NULL`) values.
  * `DEFAULT`: automatically assigns a predefined value when no value is provided.
* `NOT NULL` is typically used for mandatory fields such as IDs or names, ensuring records are always complete.
* `DEFAULT` is useful when many rows share a common value, reducing repeated manual input.
  * Example: automatically assigning `"Barcelona"` as the default city for players.
* Constraints help maintain data integrity and prevent invalid or incomplete data from entering the database.

```sql
-- Create a table with NOT NULL constraints
CREATE TABLE customer (
    customer_id INT NOT NULL,
    customer_name VARCHAR(100) NOT NULL
);
-- Ensures both columns always contain values

-- Create a table with a DEFAULT constraint
CREATE TABLE player (
    player_name VARCHAR(100) NOT NULL,
    city VARCHAR(100) DEFAULT 'Barcelona'
);
-- Automatically inserts 'Barcelona' if no city is provided
```

#### Exercise: Working with Default Values

See the instructions in [02_Databases/lab/03_default_values/Instructions.md](./lab/03_default_values/Instructions.md) and the tips in [02_Databases/lab/03_default_values/README.md](./lab/03_default_values/README.md).

In the example, the following is done:

- The existing `cm_devices` database is used. If it does not exist yet, it is created first.
- A table called `address` is created to store customer address information.
- The table contains:
  * `id`: an integer value for the customer identifier, which must not be `NULL`.
  * `street`: a variable-length string value for the street address.
  * `postcode`: a variable-length string value for the postcode.
  * `town`: a variable-length string value for the town name.
- The `town` column uses the `DEFAULT` constraint so that `Harrow` is inserted automatically when no town is provided.
- The created table and its columns are checked with `SHOW TABLES` and `SHOW COLUMNS`.

To carry out the exercise, we need MySQL installed -- check the [MySQL Setup](#mysql-setup) section above. Then, we open the CLI:

```bash
# On local Windows machine (we need root PW)
mysql -u root -p

# ... Or on Coursera VSCode Terminal:
mysql
```

And the SQL commands executed are the following:

```sql
-- Create database if needed
CREATE DATABASE cm_devices;

-- Select database
USE cm_devices;

-- Create table for customer addresses
CREATE TABLE address (
  id INT NOT NULL,
  street VARCHAR(255),
  postcode VARCHAR(10),
  town VARCHAR(30) DEFAULT 'Harrow'
);

-- Check that the table was created
SHOW TABLES;
--- +----------------------+
--- | Tables_in_cm_devices |
--- +----------------------+
--- | address              |
--- | customers            |
--- | devices              |
--- | feedback             |
--- | stock                |
--- +----------------------+

-- Check the table structure
SHOW COLUMNS FROM address;
--- +----------+--------------+------+-----+---------+-------+
--- | Field    | Type         | Null | Key | Default | Extra |
--- +----------+--------------+------+-----+---------+-------+
--- | id       | int          | NO   |     | NULL    |       |
--- | street   | varchar(255) | YES  |     | NULL    |       |
--- | postcode | varchar(10)  | YES  |     | NULL    |       |
--- | town     | varchar(30)  | YES  |     | Harrow  |       |
--- +----------+--------------+------+-----+---------+-------+
```

The optional additional task asks us to create the `address` table again, this time with default values for both `postcode` and `town`. Before recreating the table, the existing `address` table must be dropped.

The SQL statements are:

```sql
DROP TABLE address;

CREATE TABLE address (
  id INT NOT NULL,
  street VARCHAR(255),
  postcode VARCHAR(10) DEFAULT 'HA97DE',
  town VARCHAR(30) DEFAULT 'Harrow'
);
```

### Create and Read

### Update and Delete

## 3. SQL Operators and Sorting and Filtering Data

### SQL Operators

### Sorting and Filtering Data

## 4. Database Design

### Designing Database Schema

### Relational Database Design

### Database Normalization

## 5. Assessment
