## Set up data transformation and forecast generation
Ensure you have the raw data ingested into the datalake landing bucket. You can then execute a custom AWS Glue workflow to organise the automation of data transformation, and leverage AWS Forecast to load/train/forecast execution.

**Follow the instructions**
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
Once the workflow is created, you can then add triggers, jobs and a crawler in your workflow.

16. Choose the workflow you created earlier.

17. Select **Add trigger** and click on the tab **Add new**.

18. Enter the name (Example: StartWorkflow)

19. Trigger type, select **On demand** and choose **Add**.

20. Click on **Add node** box next to the Trigger

21. From the **Jobs** tab, choose the **TransformData** job and select **Add**

22. Create a new trigger to watch the end of the transform job and start the data import job.

23. From **Actions** menu within the workflow, choose **Add trigger**

24. Click on **Add New** tab. Name = StartDataImport

25. For Trigger type, select **Event**

26. For Trigger logic, **Start after ANY watched event**.

27. Choose **Add**

28. Choose **Add node** to the left of the trigger and choose the data **TransformData** job

29. Choose **Add node** to the right of the trigger and choose the **ImportDataSet** job

30. You will need to repeat the above steps (from step 22 to step 29) to create the following triggers by replacing job names as below:

Trigger | Glue job to complete | Glue job to start
------------------- | -------------- |------------------
CheckImportTrigger |  ImportDataSet | CheckImportStatus
StartPredictorTrigger | CheckImportStatus | TrainPredictor
CheckPredictorTrigger | TrainPredictor |  CheckPredictorStatus
GenerateForecastTrigger | CheckPredictorStatus | CreateForecast
CheckForecastTrigger | CreateForecast | CheckForecastStatus
ExportForecastTrigger | CheckForecastStatus | ExportForecast
CheckExportTrigger | ExportForecast | CheckExportStatus
StartCrawlerTrigger |CheckExportStatus | Crawler you created to crawl the published S3 bucket

So far, the set-up for the Glue workflow to orchestrate the steps to automate forecasting is complete.

Next, open the **Lake Formation console** and verify that the Blueprint has completed before proceeding further.

31. Go to the Glue console, select **workflows** from the left-hand pane

32. Select your **AmazonForecastBookingsWorkflow** and from the **Actions** drop-down menu, choose **Run**

33. Click on the workflow name again, in the bottom **History** tab, click **View run details**


![End-to-End Process](https://github.com/Aniket-Gamre/An-end-to-end-automated-AWS-Data-Lake-Formation-using-Amazon-Forecast/blob/master/Design-flow%20diagrams/triggers-end-to-end%20forecasting%20process.PNG)
Note: The image above illustrates the end-to-end forecasting process which may take approx. 50 mins to complete.

