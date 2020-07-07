## Final stage- Setup Athena to query the results and visualize the data using Amazon QuickSight.

1. You can download a copy of Sample dataset from this link
[SampleDataset](https://github.com/Aniket-Gamre/An-end-to-end-automated-AWS-Data-Lake-Formation-using-Amazon-Forecast/blob/master/Sample%20dataset.xlsx)

2. Launch S3 console and open the bucket that was created at the start of this tutorial with the name **bookingsdata-published**.

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

9. On the settings dialog box, copy and paste your S3 bucket name for Athena queries and click **Save**

10. From the left hand pane, under **Tables** click the ellipsis and click **Preview table**

11. This will show you the entire results from your data.


## Building visualization in Amazon QuickSight
1. Open the **Amazon QuickSight** console and sign up for a QuickSight account (In case if you don't have one).

2. Click **Sign up** for QuickSight

3. Choose a **Standard** pricing plan and continue

4. Choose a **QuickSight account name** of your choice

5. Enter your email address in the **Notification email address** and everything else default

6. Click **Finish** and click **Go to Amazon QuickSight**

7. Go back to **Lake Formation** console, locate the table created by the AWS Glue workflow inside your **bookingsdata-published-db** database (This table has the exported forecast data to visualize).

8. Grant **Select** acccess on this table to the Amazon QuickSight service role using the **Grant** action within the LakeFormation.

9. Open **Amazon QuickSight** console.

10. Choose **Manage data** from top right hand corner.

![Amazon QuickSight](https://github.com/Aniket-Gamre/An-end-to-end-automated-AWS-Data-Lake-Formation-using-Amazon-Forecast/blob/master/Design-flow%20diagrams/Amazon%20QuickSight-Console.png)

11. Click on **New data set** to create a data source for **Athena**

12. For Data source name = **bookingsdata-published-db**

13. Choose **Create data source**

![Athena Data source](https://github.com/Aniket-Gamre/An-end-to-end-automated-AWS-Data-Lake-Formation-using-Amazon-Forecast/blob/master/Design-flow%20diagrams/Athena%20data%20source_snapshot.png)

14. For Database, choose **bookingsdata-published-db**

15. Select the table that your crawler created for the forecast **bookingsdata-published**

16. Choose **Select**

17. Select **Direct query your data** and click **Visualize**.

18. Select the columns from the Fields list and a graph from Visual types to generate forecasts at different levels depending upon your use case.


**In conclusion, you have now successfully built an automated end-to-end data lake on AWS using AI through Forecast and Lake Formation**.  









