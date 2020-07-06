## Setup a Lake Formation data ingest job
1. From the Lake Formation console, choose **Blueprints > Use a blueprint**
2. Select the option- incremental database as the blueprint type for the regular ingest of data.
3. Follow the prompts to complete the setup.
4. For Database connection, choose booking-db-conn
5. For source data path, enter bookings_schema/bookings
6. For **incremental data** you can enter the following:

         - Table name: bookings
         
         - Bookmark keys: Date
         
         - Bookmark order: Ascending
         
         - Partitioning schema: This can be left blank
         
         - Target Database: bookingsdata-landing-db
         
         - Data format: Parquet
         
         - Import Frequency: Daily
         
         - Workflow name: bookings-blueprint
         
         - IAM Role: Choose your appropriate role
         
         - Maximum capacity: This can be left blank
         
         - Concurrency blank: This can be left blank
         
         - Click > CREATE

After clicking on Create, it may take a few minutes for the blueprint to create after which you can start the blueprint.
