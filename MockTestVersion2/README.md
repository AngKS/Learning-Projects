# Food Menu Database (BED Mock Test 02)
This repository contains the scripts, sql file and package.json file for the Express Server to properly run in your localhost.

# Usage
After cloning/downloading the files, do run `npm install` to install all the dependencies before running the scripts.
Also enter your `user` and `password` values in the `databaseConfig.js` file.



# Guide

## Server.js
The `server.js` file is responsible for providing the port number and initializing the application.




## MYSQL Scripts

- GET Method -- `SELECT * FROM {DATABASE}`
- POST Method -- `INSERT INTO {DATABASE} (table_headers) VALUES (?)`
- PUT Method -- `UPDATE {DATABASE} SET (table_headers) = (?)`
- DELETE Method -- `DELETE FROM {DATABASE} WHERE id = (?)`

# Dependencies
- [Express.js](https://expressjs.com/)
- [mysql.js](https://www.npmjs.com/package/mysql)
- [body-parser.js](https://www.npmjs.com/package/body-parser)

&copy; 2020 angkahshin