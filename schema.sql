CREATE TABLE users(
id integer PRIMARY KEY AUTOINCREMENT,
name text NOT NULL,
password text NOT NULL,
expert boolean NOT NULL,
admin boolean NOT NULL
);