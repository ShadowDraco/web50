# MySQL


## DATA TYPES
TEXT
NUMERIC (boolean, date, not really a number but can be represented as one)
INTEGER
REAL (for decimals)
BLOB (Binary Large OBject) for images, audio, video and other large data

CHAR(size) for storing specific length of characters
VARCHAR (size) store characters up to (size)
-- uses different amount of bytes of memory to store
SMALLINT 
INT
BIGINT
--
FLOAT - for floating point values
DOUBLE - for floating point values with extra precision

## Contraints

CHECK - obeys certain condition
DEFAULT - make this value default to *x*
NOT NULL - value cannot be NULL
PRIMARY KEY
AUTO INCREMENT

# SQLite

### CREATE TABLE: 
    CREATE TABLE flights (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        origin TEXT NOT NULL,
        destination TEXT NOT NULL,
        duration INTEGER NOT NULL
    );

### INSERT DATA:
    INSERT INTO flights
    (origin, destination, duration)
    VALUES ('New York', 'London', 415);

GET DATA:
    SELECT * FROM flights;
    SELECT origin, destination FROM flights;
    SELECT * FROM flights WHERE id = 3;
    SELECT * FROM flights WHERE origin = "New York";

sqlite3 flights -> use sqlite tool to interact with database 
.tables -> List tables
.mode columns -> Display text as columns
.headers yes -> display table headers

### Real test data

INSERT INTO flights (origin, destination, duration) VALUES ('Shanghai', 'Paris', 760);
INSERT INTO flights (origin, destination, duration) VALUES ('Istanbul', 'Tokyo', 700);
INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'Paris', 435);
INSERT INTO flights (origin, destination, duration) VALUES ('Moscow', 'Paris', 245);
INSERT INTO flights (origin, destination, duration) VALUES ('Lima', 'New York', 455);

SELECT * FROM flights WHERE origin LIKE '%a%';
SELECT * FROM flights WHERE origin IN ('New York', 'Lima');

### Built in functions
AVERAGE
COUNT
MAX
MIN
SUM
...


### UPDATE:
    UPDATE flights
        SET duration = 430
        WHERE origin = 'New York'
        AND destination = 'London'


### DELETE:
    DELETE FROM flights WHERE destination = 'London'

### OTHERE CLAUSES
LIMIT        SELECT * FROM flights LIMIT 5
ORDER BY     SELECT * FROM flights ORDER BY duration
GROUP BY     SELECT * FROM flights GROUP BY origin
HAVING


## NEW DATABASE STRUCTURE

flights:
    id, passenger_id (foreign key)

passenger:
    id, first, last (name (text))

airport:
    id, code (char(3))

INDEX:
    CREATE INDEX:
    CREATE INDEX name_index ON passengers (last); -> create an index on the table so that last names can easily be located

    SELECT * FROM name_index

### JOINING TABLES

SELECT first, origin, destination 
    FROM flight JOIN passengers
ON passenges.flight_id = flights.id

## Risks in SQL

    SQL Injection: (inject harmful data)
        SELECT * FROM users
        WHERE username = 'Harry' AND password = '12345'; <-- okay

        SELECT * FROM users 
        WHERE username = 'hacker'--' and password = ''; <-- Bad syntax skips password check

    Race Conditions: (How does the database handle multiple actions at once)
        