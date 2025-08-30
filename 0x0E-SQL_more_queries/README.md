# 0x0E. SQL - More queries

## Description

This project builds upon the fundamentals of SQL, diving deeper into advanced querying techniques, user management, privileges, constraints, and joins. Students will learn to work with multiple tables, manage database users, implement data integrity constraints, and perform complex queries using subqueries and joins.

The project emphasizes practical database administration skills and advanced SQL operations essential for real-world database management and application development.

## Learning Objectives

By the end of this project, you should be able to explain:

- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What's a PRIMARY KEY and FOREIGN KEY
- How to use NOT NULL and UNIQUE constraints
- How to retrieve data from multiple tables in one request
- What are subqueries and how to use them
- What are JOIN and UNION operations
- How to use GROUP BY and aggregate functions
- How to create and use indexes for performance

## Technologies Used

- **MySQL 8.0**: Database management system
- **Ubuntu 20.04 LTS**: Operating system
- **SQL**: Query language for advanced database operations

## Project Structure

```
0x0E-SQL_more_queries/
├── 0-privileges.sql
├── 1-create_user.sql
├── 2-create_read_user.sql
├── 3-force_name.sql
├── 4-never_empty.sql
├── 5-unique_id.sql
├── 6-states.sql
├── 7-cities.sql
├── 8-cities_of_california_subquery.sql
├── 9-cities_by_state_join.sql
├── 10-genre_id_by_show.sql
├── 11-genre_id_all_shows.sql
├── 12-no_genre.sql
├── 13-count_shows_by_genre.sql
├── 14-my_genres.sql
├── 15-comedy_only.sql
├── 16-shows_by_genre.sql
├── 100-not_my_genres.sql
├── 101-not_a_comedy.sql
├── 102-rating_shows.sql
├── 103-rating_genres.sql
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
- A `README.md` file at the root of the project folder is mandatory

### MySQL Setup
```bash
# Install MySQL 8.0 if not already installed
sudo apt update
sudo apt install mysql-server

# Connect to MySQL as root
sudo mysql

# Import sample databases (if provided)
mysql> source database_dump.sql
```

## File Descriptions

### User Management and Privileges
- **0-privileges.sql**: Lists all privileges of MySQL users `user_0d_1` and `user_0d_2`
- **1-create_user.sql**: Creates MySQL server user `user_0d_1` with all privileges
- **2-create_read_user.sql**: Creates database `hbtn_0d_2` and user `user_0d_2` with SELECT privilege

### Table Constraints and Structure
- **3-force_name.sql**: Creates table `force_name` with NOT NULL constraint on name
- **4-never_empty.sql**: Creates table `never_empty` with default value for id column
- **5-unique_id.sql**: Creates table `unique_id` with UNIQUE constraint on id
- **6-states.sql**: Creates database and states table with PRIMARY KEY
- **7-cities.sql**: Creates cities table with FOREIGN KEY reference to states

### Basic Joins and Subqueries
- **8-cities_of_california_subquery.sql**: Lists cities of California using subquery
- **9-cities_by_state_join.sql**: Lists cities with state names using JOIN

### Advanced Queries with TV Shows Database
- **10-genre_id_by_show.sql**: Lists shows with at least one genre linked
- **11-genre_id_all_shows.sql**: Lists all shows with their genre IDs (including NULL)
- **12-no_genre.sql**: Lists shows without any genre linked
- **13-count_shows_by_genre.sql**: Lists genres and count of shows per genre
- **14-my_genres.sql**: Lists all genres of the show "Dexter"
- **15-comedy_only.sql**: Lists all Comedy shows
- **16-shows_by_genre.sql**: Lists all shows and their genres

### Advanced Tasks
- **100-not_my_genres.sql**: Lists genres not linked to "Dexter"
- **101-not_a_comedy.sql**: Lists shows that are not Comedy
- **102-rating_shows.sql**: Lists shows by their rating
- **103-rating_genres.sql**: Lists genres by their rating

## Database Schema

### Sample Tables Structure

#### States Table
```sql
CREATE TABLE states (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
```

#### Cities Table
```sql
CREATE TABLE cities (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
```

#### TV Shows Schema
```sql
-- Shows table
CREATE TABLE tv_shows (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(256) NOT NULL
);

-- Genres table
CREATE TABLE tv_genres (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- Junction table for many-to-many relationship
CREATE TABLE tv_show_genres (
    show_id INT NOT NULL,
    genre_id INT NOT NULL,
    FOREIGN KEY (show_id) REFERENCES tv_shows(id),
    FOREIGN KEY (genre_id) REFERENCES tv_genres(id),
    PRIMARY KEY (show_id, genre_id)
);
```

## Key Concepts and Examples

### User Management

#### Creating Users
```sql
-- Create user with password
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';

-- Grant privileges
GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost';
GRANT SELECT ON database_name.* TO 'username'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;
```

#### Viewing Privileges
```sql
-- Show grants for current user
SHOW GRANTS;

-- Show grants for specific user
SHOW GRANTS FOR 'username'@'localhost';
```

### Constraints

#### Primary Key
```sql
CREATE TABLE example (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
```

#### Foreign Key
```sql
CREATE TABLE child_table (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    parent_id INT NOT NULL,
    FOREIGN KEY (parent_id) REFERENCES parent_table(id)
);
```

#### Unique Constraint
```sql
CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE
);
```

### Joins

#### INNER JOIN
```sql
SELECT c.name, s.name 
FROM cities c
INNER JOIN states s ON c.state_id = s.id;
```

#### LEFT JOIN
```sql
SELECT s.title, g.name 
FROM tv_shows s
LEFT JOIN tv_show_genres sg ON s.id = sg.show_id
LEFT JOIN tv_genres g ON sg.genre_id = g.id;
```

#### Subqueries
```sql
-- Using subquery
SELECT * FROM cities 
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
);
```

### Aggregate Functions and Grouping

```sql
-- Count shows by genre
SELECT g.name, COUNT(sg.show_id) as nb_shows
FROM tv_genres g
LEFT JOIN tv_show_genres sg ON g.id = sg.genre_id
GROUP BY g.name
ORDER BY nb_shows DESC;
```

## Getting Started

### Prerequisites
- MySQL 8.0 installed and configured
- Basic understanding of SQL fundamentals
- Access to MySQL root account

### Setup Instructions

1. **Connect to MySQL**:
```bash
sudo mysql
```

2. **Import sample data** (if dump files provided):
```sql
source hbtn_0d_tvshows.sql;
```

3. **Run SQL files**:
```bash
cat 0-privileges.sql | mysql -u root -p
```

## Usage Examples

### User and Privilege Management
```bash
# Create user and grant privileges
mysql -u root -p < 1-create_user.sql

# Create database and limited user
mysql -u root -p < 2-create_read_user.sql

# Check user privileges
mysql -u root -p < 0-privileges.sql
```

### Working with Constraints
```bash
# Create tables with constraints
mysql -u root -p < 6-states.sql
mysql -u root -p < 7-cities.sql

# Test constraint behavior
mysql -u root -p hbtn_0d_usa < insert_test_data.sql
```

### Complex Queries
```bash
# Run join queries
mysql -u root -p hbtn_0d_tvshows < 10-genre_id_by_show.sql

# Execute aggregation queries  
mysql -u root -p hbtn_0d_tvshows < 13-count_shows_by_genre.sql
```

## Common SQL Patterns

### Many-to-Many Relationships
```sql
-- Query shows with their genres
SELECT s.title, g.name as genre
FROM tv_shows s
JOIN tv_show_genres sg ON s.id = sg.show_id  
JOIN tv_genres g ON sg.genre_id = g.id
ORDER BY s.title, g.name;
```

### Conditional Joins
```sql
-- Shows with specific genre
SELECT s.title 
FROM tv_shows s
JOIN tv_show_genres sg ON s.id = sg.show_id
JOIN tv_genres g ON sg.genre_id = g.id
WHERE g.name = 'Comedy';
```

### Exclusion Queries
```sql
-- Shows NOT in a category
SELECT s.title
FROM tv_shows s
WHERE s.id NOT IN (
    SELECT DISTINCT sg.show_id
    FROM tv_show_genres sg
    JOIN tv_genres g ON sg.genre_id = g.id
    WHERE g.name = 'Comedy'
);
```

## Performance Considerations

### Indexing
```sql
-- Create index on foreign key
CREATE INDEX idx_state_id ON cities(state_id);

-- Create composite index
CREATE INDEX idx_show_genre ON tv_show_genres(show_id, genre_id);
```

### Query Optimization
- Use EXPLAIN to analyze query execution plans
- Prefer JOINs over subqueries when possible
- Use appropriate WHERE clauses to filter early
- Consider index usage for frequently queried columns

## Debugging and Testing

### Common Issues

1. **Foreign Key Constraints**:
```sql
-- Check foreign key constraints
SHOW CREATE TABLE cities;

-- Disable foreign key checks temporarily
SET FOREIGN_KEY_CHECKS = 0;
-- ... perform operations
SET FOREIGN_KEY_CHECKS = 1;
```

2. **User Permission Issues**:
```sql
-- Check current user
SELECT USER();

-- Verify privileges
SHOW GRANTS FOR CURRENT_USER();
```

3. **Join Issues**:
```sql
-- Debug joins with table aliases
SELECT s.id, s.title, g.id, g.name
FROM tv_shows s
LEFT JOIN tv_show_genres sg ON s.id = sg.show_id
LEFT JOIN tv_genres g ON sg.genre_id = g.id
WHERE s.title = 'Specific Show';
```

## Advanced Topics

### Views
```sql
-- Create a view for commonly used joins
CREATE VIEW show_genres AS
SELECT s.title, g.name as genre
FROM tv_shows s
JOIN tv_show_genres sg ON s.id = sg.show_id
JOIN tv_genres g ON sg.genre_id = g.id;
```

### Stored Procedures
```sql
-- Example stored procedure
DELIMITER //
CREATE PROCEDURE GetShowsByGenre(IN genre_name VARCHAR(256))
BEGIN
    SELECT s.title
    FROM tv_shows s
    JOIN tv_show_genres sg ON s.id = sg.show_id
    JOIN tv_genres g ON sg.genre_id = g.id
    WHERE g.name = genre_name;
END//
DELIMITER ;
```

## Style Guidelines

### SQL Coding Standards
- Use UPPERCASE for SQL keywords
- Use meaningful table aliases (not just single letters)
- Indent JOIN clauses for readability
- Comment complex queries
- Use consistent naming conventions

### Example of Good Style
```sql
-- List all shows with their genres, ordered by show title
SELECT 
    shows.title AS show_title,
    genres.name AS genre_name
FROM tv_shows shows
INNER JOIN tv_show_genres show_genres 
    ON shows.id = show_genres.show_id
INNER JOIN tv_genres genres 
    ON show_genres.genre_id = genres.id
ORDER BY shows.title, genres.name;
```

## Testing Framework

### Test Your Queries
```bash
#!/bin/bash
# Test script for SQL files

for file in *.sql; do
    echo "Testing $file..."
    mysql -u root -p hbtn_0d_tvshows < "$file"
    if [ $? -eq 0 ]; then
        echo "✅ $file - SUCCESS"
    else
        echo "❌ $file - FAILED"
    fi
done
```

## Resources

### Documentation
- [MySQL 8.0 Reference Manual](https://dev.mysql.com/doc/refman/8.0/en/)
- [MySQL Joins Tutorial](https://www.mysqltutorial.org/mysql-join/)
- [SQL Constraint Types](https://www.w3schools.com/sql/sql_constraints.asp)

### Tools
- MySQL Workbench: Visual database design
- phpMyAdmin: Web-based administration
- Adminer: Lightweight database management

### Learning Resources
- [SQLBolt Interactive Tutorial](https://sqlbolt.com/)
- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)
- [MySQL Tutorial](https://www.mysqltutorial.org/)

## Environment Setup

```bash
# MySQL version check
mysql --version

# Service status
sudo systemctl status mysql

# Configuration file location
/etc/mysql/mysql.conf.d/mysqld.cnf
```

## Project Tasks Checklist

### Basic Tasks
- [ ] 0. My privileges!
- [ ] 1. Root user  
- [ ] 2. Read user
- [ ] 3. Always a name
- [ ] 4. ID can't be null
- [ ] 5. Unique ID
- [ ] 6. States table
- [ ] 7. Cities table
- [ ] 8. Cities of California  
- [ ] 9. Cities by states
- [ ] 10. Genre ID by show
- [ ] 11. Genre ID for all shows
- [ ] 12. No genre
- [ ] 13. Number of shows by genre
- [ ] 14. My genres
- [ ] 15. Only Comedy
- [ ] 16. List shows and genres

### Advanced Tasks  
- [ ] 17. Not my genre
- [ ] 18. No Comedy tonight!
- [ ] 19. Rotten tomatoes
- [ ] 20. Best genre

## Contributing

When contributing to this project:

1. Follow the established SQL coding standards
2. Test all queries thoroughly
3. Include appropriate comments
4. Ensure backwards compatibility
5. Document any new patterns or techniques

## Troubleshooting

### Common MySQL Errors

**Error 1045**: Access denied
```bash
sudo mysql -u root -p
# or
sudo mysql --defaults-file=/etc/mysql/debian.cnf
```

**Error 1146**: Table doesn't exist
```sql
SHOW DATABASES;
USE correct_database;
SHOW TABLES;
```

**Error 1452**: Foreign key constraint fails
```sql
-- Check referenced table exists and has data
SELECT * FROM parent_table WHERE id = referenced_id;
```

## License

This project is part of the ALX Software Engineering curriculum.

## Author

**Abd_al-rahman Ajamy**  
📧 Email: abdorahman0283@gmail.com 
---

*Part of ALX Higher Level Programming - Advanced SQL Queries Module*

## Acknowledgments

- **ALX Africa**: For the comprehensive curriculum
- **Holberton School**: For the original project framework  
- **MySQL Community**: For excellent documentation and tools
- **The SQL community**: For sharing best practices and solutions
