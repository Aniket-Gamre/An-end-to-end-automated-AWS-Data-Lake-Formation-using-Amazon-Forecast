## Set up the Lake Formation data catalog for data lake
1.  On the Lake Formation console, under Data Catalog, choose **Databases** > **Create database**.
2.  For name, enter: **bookingsdata-landing-db**
3.  Location, click Browse and select the path for the landing S3 bucket.
4.  Description is optional
5.  Choose **Create database**
6.  Repeat the steps for the other two buckets, naming the databases appropriately.
7.  On the Databases page, select the database **bookingsdata-landing-db**
8.  From the Actions drop-down menu, choose **Grant**
9.  Choose the IAM users and roles
10. Database permission, select **Create table**
11. Choose **Grant**

*So far, the data lake has been setup with Lake Formation.*
