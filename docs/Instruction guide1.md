## Set up the data lake storage
You will need three S3 buckets for the purpose of this tutorial.

1. bookingsdata-landing (Storing the raw data)
2. bookingsdata-processed (Transformed data)
3. bookingsdata-published (Data stored for the consumers)


## Allow centralized access control on the data lake using AWS Lake Formation
1. Go to AWS Lake Formation console, for first time users you will need to set a data lake administrator. Hence Click **Add Administrators**.

2. Select the role from the IAM users and roles drop down and click Save.
   For managing the access control from Lake Formation, you need to register the three s3 buckets created, as data lake locations with Lake Formation.
   
3. Select **Dashboard** from the left hand menu

4. On the lake Formation dashboard, Choose **Register Location**.

<img src = "Register Location.png">

5. The above steps could be repeated for the other two buckets- **processed , published**.
