## What's included: ##

**tournament.sql**
This is a sql file that contains all the tables and 
the relationships between the tables

**tournament.py**
This is a python file that contains the queries to 
extract data from the tables in tournament.sql file

**tournament_test.py**
This is a python file that contains tests to make sure that the database provides accurate results

## How to Run this Program: ##
In order to run this program via vagrant
first bring up the vagrant machine using the command
vagrant up. 

Once the vagrant machine is up, SSH into the vagrant machine and run the PSQL then import the tournament.sql file in the PSQL using the command 
\i tournament.sql, once the tables are in the database go ahead and run the tournament_test.py


