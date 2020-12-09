#!/usr/bin/python3 
import boto3 
import pandas as pd 
import io 
import argparse 
import tempfile 
import time 
import os 
import sys 
 
 
#Config 
TABLE_NAME              = "hotels" 
AWS_OUTPUT_BUCKET       = "subsidiary-apac-datasource" 
AWS_OUTPUT_KEY          = "parquet/{}/".format(TABLE_NAME) 
AWS_OUTPUT_FILE_LATEST  = "parquet_latest/{0}/{0}.parquet".format(TABLE_NAME) 
 
def main(): 
    output_file = "{}.parquet".format(os.path.basename(args.key)) 
    tmp_file = "{}/{}".format(tempfile.gettempdir(), output_file) 
 
    #Connect to S3 and get object 
    s3 = boto3.client('s3') 
    obj = s3.get_object(Bucket=args.bucket, Key=args.key) 
 
    #Read file and create dataframe 
    df = pd.read_csv(io.BytesIO(obj['Body'].read()),na_values=["\\N"]) 
 
    #Cleaning data
    df['HotelId'] = df['HotelId'].astype('int32') 
    df['PropertyName'] = df['PropertyName'].astype('int32')
    df['Hotel Rating'] = df['Hotel Rating'].astype('int32') 


    #Convert to parquet 
    df.to_parquet(tmp_file) 
    if args.verbose: 
        print(df.dtypes) 
 
    #Upload to S3 (parquet) 
    s3.upload_file(tmp_file, AWS_OUTPUT_BUCKET, "{}{}".format(AWS_OUTPUT_KEY, output_file)) 
 
    #Read the current latest file 
    obj = s3.get_object(Bucket=AWS_OUTPUT_BUCKET, Key=AWS_OUTPUT_FILE_LATEST) 
    df_latest = pd.read_parquet(io.BytesIO(obj['Body'].read()), engine='pyarrow') 

    df['HotelId'] = df['HotelId'].astype('int32') 
    df['PropertyName'] = df['PropertyName'].astype('int32')
    df['Hotel Rating'] = df['Hotel Rating'].astype('int32') 
   
 
    #Merge the current latest file with the updates 
    df_new_latest = pd.concat([df, df_latest], sort=False) 
 
    #Sort by Last Update Descending and keep the first row when is duplicated 
    df_new_latest.sort_values(by=['LatestAmendment'], ascending=False) 
    df_new_latest.drop_duplicates(subset=['BookingId'], keep='first', inplace=True) 
 
    #Convert to parquet 
    df_new_latest.to_parquet(tmp_file) 
 
    #Copy to (parquet_latest) 
    s3.upload_file(tmp_file, AWS_OUTPUT_BUCKET, AWS_OUTPUT_FILE_LATEST) 
 
    #Delete temporary file 
    os.remove(tmp_file) 
 
 
if __name__ == '__main__': 
    parser = argparse.ArgumentParser() 
    parser.add_argument( '-b', '--subsidiary-apac-datasource', help="AWS Bucket",   type=str, required=True) 
    parser.add_argument( '-k', '--hotels',    help="AWS key",      type=str, required=True) 
    parser.add_argument( '-v', '--verbose', help="Vervose mode",action='store_true'    ) 
    args = parser.parse_args() 
 
    main() 
