# 0x0D. SQL - Introduction

## Description

This project introduces the fundamentals of SQL (Structured Query Language) and relational databases. Students will learn how to create databases, tables, perform basic queries, and understand the principles of relational database management systems using MySQL.

The project covers essential SQL concepts including database creation, data insertion, querying with SELECT statements, filtering, sorting, and basic database administration tasks.

## Learning Objectives

By the end of this project, you should be able to explain:

- What's a database and a relational database
- What does SQL stand for and what it's used for
- What's MySQL and how to use it
- How to create a database in MySQL
- What does DDL and DML mean
- How to CREATE or ALTER a table
- How to SELECT data from a table
- How to INSERT, UPDATE or DELETE data
- What are subqueries
- How to use MySQL functions

## Technologies Used

- **MySQL 8.0**: Database management system
- **Ubuntu 20.04 LTS**: Operating system
- **SQL**: Query language for database operations

## Project Structure

```
0x0D-SQL_introduction/
├── 0-list_databases.sql
├── 1-create_database_if_missing.sql
├── 2-remove_database.sql
├── 3-list_tables.sql
├── 4-first_table.sql
├── 5-full_table.sql
├── 6-list_values.sql
├── 7-insert_value.sql
├── 8-count_89.sql
├── 9-full_creation.sql
├── 10-top_score.sql
├── 11-best_score.sql
├── 12-no_cheating.sql
├── 13-change_class.sql
├── 14-average.sql
├── 15-groups.sql
├── 16-no_link.sql
└── README.md
```

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All files should end with a new line
- All SQL queries should have a comment just before
- All files should start with a comment describing the task
- All SQL keywords should be in uppercase (`SELECT`, `WHERE`, etc.)

### MySQL Installation
```bash
# Install MySQL 8.0
sudo apt update
sudo apt install mysql-server

# Secure installation
sudo mysql_secure_installation

# Connect to MySQL
sudo mysql
```

## File Descriptions

### Basic Database Operations
- **0-list_databases.sql**: Lists all databases on the MySQL server
- **1-create_database_if_missing.sql**: Creates database `hbtn_0c_0` if it doesn't exist
- **2-remove_database.sql**: Deletes database `hbtn_0c_0` if it exists
- **3-list_tables.sql**: Lists all tables in a specified database

### Table Operations
- **4-first_table.sql**: Creates table `first_table` with `id` and `name` columns
- **5-full_table.sql**: Shows full description of `first_table`
- **6-list_values.sql**: Lists all rows in `first_table`
- **7-insert_value.sql**: Inserts a new row into `first_table`

### Advanced Queries
- **8-count_89.sql**: Counts records with specific criteria
- **9-full_creation.sql**: Creates and populates `second_table` with sample data
- **10-top_score.sql**: Lists records ordered by score (descending)
- **11-best_score.sql**: Lists records with score >= 10, ordered by score
- **12-no_cheating.sql**: Updates score for specific record
- **13-change_class.sql**: Removes records with specific score
- **14-average.sql**: Computes average score of all records
- **15-groups.sql**: Lists score and count, grouped by score
- **16-no_link.sql**: Lists records excluding those without name value

## Getting Started

### Installation and Setup

1. **Install MySQL**:
```bash
sudo apt update
sudo apt install mysql-server
sudo mysql_secure_installation
```

2. **Connect to MySQL**:
```bash
sudo mysql
```

3. **Basic MySQL commands**:
```sql
-- Show available databases
SHOW DATABASES;

-- Use a specific database
USE database_name;

-- Show tables in current database
SHOW TABLES;

-- Exit MySQL
EXIT;
```

### Running SQL Files

Execute SQL files from the command line:
```bash
# Method 1: Using mysql command
mysql -u root -p < 0-list_databases.sql

# Method 2: From MySQL prompt
mysql> source 0-list_databases.sql

# Method 3: Using cat and pipe
cat 0-list_databases.sql | mysql -u root -p
```

## Usage Examples

### Basic Database Operations
```sql
-- Create a database
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;

-- Use the database
USE hbtn_0c_0;

-- Create a table
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);

-- Insert data
INSERT INTO first_table (id, name) VALUES (89, "Best School");

-- Query data
SELECT * FROM first_table;
```

### Advanced Queries
```sql
-- Count records
SELECT COUNT(*) FROM second_table WHERE id = 89;

-- Order results
SELECT score, name FROM second_table ORDER BY score DESC;

-- Group and count
SELECT score, COUNT(*) as number 
FROM second_table 
GROUP BY score 
ORDER BY number DESC;

-- Calculate average
SELECT AVG(score) as average FROM second_table;
```

## Common SQL Commands Reference

### Data Definition Language (DDL)
- `CREATE DATABASE`: Create a new database
- `DROP DATABASE`: Delete a database
- `CREATE TABLE`: Create a new table
- `ALTER TABLE`: Modify table structure
- `DROP TABLE`: Delete a table

### Data Manipulation Language (DML)
- `SELECT`: Query data from tables
- `INSERT`: Add new records
- `UPDATE`: Modify existing records
- `DELETE`: Remove records

### Common Clauses
- `WHERE`: Filter results
- `ORDER BY`: Sort results
- `GROUP BY`: Group results
- `HAVING`: Filter grouped results
- `LIMIT`: Limit number of results

## Debugging and Testing

### Check MySQL Status
```bash
sudo systemctl status mysql
sudo systemctl start mysql    # Start MySQL service
sudo systemctl stop mysql     # Stop MySQL service
sudo systemctl restart mysql  # Restart MySQL service
```

### Common Issues and Solutions

1. **Permission denied**:
   ```bash
   sudo mysql -u root -p
   ```

2. **Database doesn't exist**:
   ```sql
   CREATE DATABASE database_name;
   USE database_name;
   ```

3. **Table doesn't exist**:
   ```sql
   SHOW TABLES;
   DESCRIBE table_name;
   ```

## Style Guidelines

- All SQL keywords must be in UPPERCASE
- Proper indentation for readability
- Comments before each query explaining the purpose
- Consistent naming conventions for databases and tables
- Each file should contain only one SQL statement or related statements

## Testing

Test your SQL files using:
```bash
# Test database creation
mysql -u root -p < 1-create_database_if_missing.sql

# Verify database exists
echo "SHOW DATABASES;" | mysql -u root -p

# Test table operations
mysql -u root -p hbtn_0c_0 < 4-first_table.sql
```

## Resources

### Documentation
- [MySQL 8.0 Reference Manual](https://dev.mysql.com/doc/refman/8.0/en/)
- [SQL Tutorial - W3Schools](https://www.w3schools.com/sql/)
- [MySQL Tutorial](https://www.mysqltutorial.org/)

### Tools
- MySQL Workbench: GUI for MySQL
- phpMyAdmin: Web-based MySQL administration
- DBeaver: Universal database tool

## Common MySQL Functions

- `COUNT()`: Count number of rows
- `AVG()`: Calculate average value
- `SUM()`: Calculate sum of values
- `MAX()`: Find maximum value
- `MIN()`: Find minimum value
- `CONCAT()`: Concatenate strings
- `NOW()`: Current timestamp
- `UPPER()`: Convert to uppercase
- `LOWER()`: Convert to lowercase

## Environment

- **OS**: Ubuntu 20.04 LTS
- **MySQL Version**: 8.0.25
- **Character Set**: utf8mb4
- **Collation**: utf8mb4_0900_ai_ci

## Contributing

1. Fork the repository
2. Create a feature branch
3. Follow SQL coding standards
4. Test your queries thoroughly
5. Submit a pull request

## Troubleshooting

### MySQL Connection Issues
```bash
# Reset MySQL root password
sudo mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your_password';
FLUSH PRIVILEGES;
EXIT;
```

### File Permission Issues
```bash
# Make SQL files executable
chmod +x *.sql
```

## Project Tasks Checklist

- [ ] 0. List databases
- [ ] 1. Create a database
- [ ] 2. Delete a database  
- [ ] 3. List tables
- [ ] 4. First table
- [ ] 5. Full description
- [ ] 6. List all in table
- [ ] 7. First add
- [ ] 8. Count 89
- [ ] 9. Full creation
- [ ] 10. List by best
- [ ] 11. Select the best
- [ ] 12. Cheating is bad
- [ ] 13. Score update
- [ ] 14. Average
- [ ] 15. Number by score
- [ ] 16. Say my name

## License

This project is part of the ALX Software Engineering curriculum.

## Author

**Abd_al-rahman Ajamy**  
📧 Email: abdorahman0283@gmail.com 
---

*Part of ALX Higher Level Programming - SQL Introduction Module*

## Acknowledgments

- **ALX Africa**: For providing the curriculum and learning platform
- **Holberton School**: For the original project design
- **MySQL Community**: For the excellent database system and documentation
