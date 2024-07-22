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

CREATE TABLE: 
    CREATE TABLE flights (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        origin TEXT NOT NULL,
        destination TEXT NOT NULL,
        duration INTEGER NOT NULL
    );

INSERT DATA:
    INSERT INTO flights
    (origin, destination, duration)
    VALUES ("New York", "London", 415);

GET DATA:
    SELECT * FROM flights;
    SELECT origin, destination FROM flights;
    SELECT * FROM flights WHERE id = 3;
    SELECT * FROM flights WHERE origin = "New York";

# Postgres


