## Ingest Data and setup a Glue connection to the source database:
For ingesting data, you can use a MYSQL table called **bookings**, containing all the historical bookings data.
The schema for the table is as follows:

Column Name | Column Type
------------ | --------------
booking_id	| int
booking_date|	varchar(50)
destination_country	| varchar(100)
transactions| int
sales | int
sales_avg |	int

Also, you need to have an RDS instance running.
Open the RDS console and verify that there is an RDS MYSQL instance present.


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
                 
![Image of Yaktocat](https://github.com/Aniket-Gamre/An-end-to-end-automated-AWS-Data-Lake-Formation-using-Amazon-Forecast/blob/master/Design-flow%20diagrams/Connection%20properties.png)

![Image of Yaktocat](https://github.com/Aniket-Gamre/An-end-to-end-automated-AWS-Data-Lake-Formation-using-Amazon-Forecast/blob/master/Design-flow%20diagrams/Connection%20access.png)
                  
3. On the connections page, test the Glue connection by selecting it and clicking Test connection
4. Select the appropriate workflow role from IAM role drop down and click Test connection

Once this connection is successful, you can now proceed to the next steps.
