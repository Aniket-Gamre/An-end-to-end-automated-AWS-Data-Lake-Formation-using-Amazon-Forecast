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
