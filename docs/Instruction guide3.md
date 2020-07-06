## Ingest Data and setup a Glue connection to the source database:
For ingesting data, you need to have an RDS instance running.
Example: bookings-db with bookings history already loaded. 

## Setup a Glue Connection to the source database:
1. Open the AWS Glue console, under Data catalog, choose Connections 
2. Choose add connection and choose to enter the following:
               
               - Connection name: bookings-db-conn
               
               - Connection type: Amazon RDS
               
               - Database engine: MYSQL
               
                 Click Next
                 
               - Instance : bookings-db (Note: This has to be the name of your instance that you have created)
               
               - Database name: bookings_schema
               
               - Username: Enter your username
               
               - Password: Enter your password
               
                 Click Next
                  
                 Click Finish
                  
3. On the connections page, test the Glue connection by selecting it and clicking Test connection
4. Select the appropriate workflow role from IAM role drop down and click Test connection

Once this connection is successful, you can now proceed to the next steps.
