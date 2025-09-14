# 0x0F. Python - Object-relational mapping

## Description
This project introduces Object-Relational Mapping (ORM) in Python, specifically using SQLAlchemy. You'll learn how to connect Python scripts to MySQL databases and perform database operations using both raw SQL queries and ORM techniques. The project covers the transition from writing SQL queries directly to using Python objects to interact with databases.

## Learning Objectives
At the end of this project, you should be able to explain:

- Why Python programming is awesome
- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table
- How to create a Python Virtual Environment

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Your files will be executed with MySQLdb version 2.0.x
- Your files will be executed with SQLAlchemy version 1.4.x
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class or method (the length of it will be verified)
- You are not allowed to use `execute` with sqlalchemy

### More Info

#### Install MySQL 8.0 on Ubuntu 20.04 LTS
```bash
$ sudo apt update
$ sudo apt install mysql-server
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
```

#### Install MySQLdb module version 2.0.x
```bash
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
```

#### Install SQLAlchemy module version 1.4.x
```bash
$ sudo pip3 install SQLAlchemy
```

## Project Structure

### Tasks Overview

| Task | File | Description |
|------|------|-------------|
| 0 | `0-select_states.py` | Get all states |
| 1 | `1-filter_states.py` | Filter states |
| 2 | `2-my_filter_states.py` | Filter states by user input |
| 3 | `3-my_safe_filter_states.py` | SQL Injection... |
| 4 | `4-cities_by_state.py` | Cities by states |
| 5 | `5-filter_cities.py` | All cities by state |
| 6 | `6-model_state.py` | First state model |
| 7 | `7-model_state_fetch_all.py` | All states via SQLAlchemy |
| 8 | `8-model_state_fetch_first.py` | First state |
| 9 | `9-model_state_filter_a.py` | Contains `a` |
| 10 | `10-model_state_my_get.py` | Get a state |
| 11 | `11-model_state_insert.py` | Add a new state |
| 12 | `12-model_state_update_id_2.py` | Update a state |
| 13 | `13-model_state_delete_a.py` | Delete states |
| 14 | `14-model_city_fetch_by_state.py` | Cities in state |
| 15 | `relationship_city.py`, `relationship_state.py`, `100-relationship_states_cities.py` | Relationship |

## Database Setup

For testing, you'll need to set up a MySQL database. Here's an example setup:

```sql
-- Create database and tables for testing
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;

CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);

INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");
```

## Usage Examples

### Raw SQL with MySQLdb
```python
#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
```

### Using SQLAlchemy ORM
```python
#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    
    session.close()
```

## Key Concepts

### MySQLdb (Raw SQL)
- Direct SQL query execution
- Manual connection management
- Vulnerable to SQL injection if not handled properly
- Lower level database interaction

### SQLAlchemy ORM
- Object-oriented database interaction
- Automatic SQL generation
- Built-in protection against SQL injection
- Higher level abstraction
- Relationship management between tables

## Testing

Run your scripts with the following format:
```bash
$ ./script_name.py <mysql_username> <mysql_password> <database_name>
```

Example:
```bash
$ ./0-select_states.py root root hbtn_0e_0_usa
```

## Author
This project is part of the ALX Software Engineering Program.

## Resources
- [Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)
- [mysqlclient/MySQLdb documentation](https://mysqlclient.readthedocs.io/)
- [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
- [Introduction to SQLAlchemy](https://www.youtube.com/watch?v=woKYyhLCcnU)
- [Flask SQLAlchemy](https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW)
- [10 common stumbling blocks for SQLAlchemy newbies](http://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html)

## License
This project is licensed under the terms of the ALX Software Engineering Program.
