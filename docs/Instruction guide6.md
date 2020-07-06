## Final stage- Setup Athena to query the results and visualize the data using Amazon QuickSight.

1. You can download a copy of Sample dataset from this link
[SampleDataset](https://github.com/Aniket-Gamre/An-end-to-end-automated-AWS-Data-Lake-Formation-using-Amazon-Forecast/blob/master/Sample%20dataset.xlsx)

2. Open S3 console and open the bucket that was created at the start of this tutorial with the name **bookingsdata-published**.

3. Upload the Sample dataset(.xlsx) in this bucket.

3. Open **Glue console** and run the crawler you created earlier on the published bucket **bookingsdata-published**

4. Once the crawler completes, open the **Lake formation** and click on **Tables** from the left hand pane.

5. From the list of tables click on a table named **bookingsdata-published** and verify all the columns have the appropriate data types.



## Setup Athena and query the forecast data using Athena

1. Open **Lake Formation console** and select **Tables**

2. Click on the table named **bookingsdata-published** that belongs to the database **bookingsdata-published-db**

3. From Actions drop down, click **Grant**

4. In the IAM users and roles dropdown, select the appropriate role.

5. Click on the **Select** table permission and click **Grant**

6. From Actions drop down, click **View data**

7. If you are using Amazon Athena for the first time, there will be a pop up just click **Get Started**

8. Click on the blue banner to setup the query result bucket for Athena

9. On the settings dialog boc, copy and paste your S3 bucket name for Athena queries and click **Save**

10. From the left hand pane, under **Tables** click the ellipsis and click **Preview table**

11. This will show you the entire results from your data.


## Building visualization in Amazon QuickSight








