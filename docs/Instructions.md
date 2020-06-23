## Set up the data lake storage

1. bookingsdata-landing
2. bookingsdata-processed
3. bookingsdata-published


## Centralized access control on the data lake using AWS Lake Formation
1. Go to AWS Lake Formation console, for first time users you will need to set a data lake administrator. Hence Click **Add Administrators**.
2. Select the role from the IAM users and roles drop down and click Save.
   For managing the access control from Lake Formation, you need to register the s3 buckets as data lake locations with Lake Formation.
3. Select **Dashboard** from the left hand menu
4. On the lake Formation dashboard, Choose Register Location.
5. The above steps could be repeated for the other two buckets- **processed , published**.


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






 
