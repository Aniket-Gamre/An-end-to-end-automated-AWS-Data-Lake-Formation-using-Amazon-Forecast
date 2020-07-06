## Set up data transformation and forecast generation
Once you have the raw data ingested into the datalake landing bucket, you can then execute a custom AWS Glue workflow to organise the automation of data transformation, leverage AWS Forecast load/train/forecast execution.

**Steps to follow**
1. Open the **Glue console** > click on **Crawlers** from the left hand menu > click **Add crawler button**

2. Enter the **published-bucket-crawler** for the crawler name

3. Source type, select **Data stores** and click Next

4. For data store choose **S3**

5. For include path click the folder icon to browse and select the bucket **bookingsdata-published** and click Next

6. On Add another data source, select **No**

7. For IAM Role, **Choose an existing IAM Role**

8. Frequency = **Run on demand**

9. For Databases, select bookings-published-db

10. Click on the **Finish** button and do not run the crawler now.

Note: Before you proceed, you need to create the following ETL jobs in your account. 

* TransformData(Spark)
* ImportDataSet(Python shell: Python 3)
* CheckImportStatus(Python shell: Python 3)
* TrainPredictor(Python shell: Python 3)
* CheckPredictorStatus(Python shell: Python 3)
* CreateForecast(Python shell: Python 3)
* CheckForecastStatus(Python shell: Python 3)
* ExportForecast(Python shell: Python 3)
* CheckExportStatus(Python shell: Python 3)

The next step is to create a new AWS Glue workflow to orchestrate the entire automation. This will help to build and orchestrate a sequence of AWS Glue jobs and crawlers via triggers.

11. From the AWS Glue console, choose **Workflows** > Add **workflow**

![Workflows](https://github.com/Aniket-Gamre/An-end-to-end-automated-AWS-Data-Lake-Formation-using-Amazon-Forecast/blob/master/Design-flow%20diagrams/Workflows.png)


12. For WorkFlow name, enter **AmazonForecastBookingsWorkflow**

13. Add an optional description

14. For Default **run properties**, click **Add property** and enter the keys and values as below.

Key | Value
----- | -----------
landingDB | bookings-landing-db
landingDBTable | bookings_schema_bookings
processedBucket | bookingsdata-processed
publishedBucket | bookingsdata-published


15. Click **Add workflow.**


