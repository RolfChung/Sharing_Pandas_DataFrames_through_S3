# %load S3_helpers_pckg/S3_helpers.py
import boto3
import botocore
import logging
from botocore.exceptions import ClientError
import os
import pathlib

class S3_helpers:
    def __init__(self, name, S3_client):
        self.name = name
        self.S3_client = S3_client
        
    def get_names_buckets(self):
        bucket_list = self.S3_client.list_buckets()
        buckets_in_bucket_list = bucket_list['Buckets']
        n_buckets=len(buckets_in_bucket_list)
        bucket_names_list = []
        for i in range(0,n_buckets):
            name=bucket_list['Buckets'][i]['Name']
            bucket_names_list.append(name)
        return bucket_names_list
    
    def check_bucket_exists(self, bucket_name):
        bucket_names_list = self.get_names_buckets()
        # print(bucket_names_list)
        if bucket_name in bucket_names_list:
            x="Bucket {} exists.".format(bucket_name)
            return x 
        else:
            y="Bucket {} does not exist.".format(bucket_name)
            return y
        
    
    def create_multiple_buckets(self, create_buckets_list):
        for bucket in create_buckets_list:
            self.S3_client.create_bucket(Bucket=bucket)
            
        # print(self.get_names_buckets())
        
        for name in create_buckets_list:
            if name in self.get_names_buckets():
                print("Bucket {} is successfully created. I am happy!".format(name))
            else:
                print("Buckets are not successfully created. I am sad!")
            
    
    def delete_multiple_buckets(self, delete_buckets_list):
        for bucket in delete_buckets_list:
            self.S3_client.delete_bucket(Bucket=bucket)
            
    def delete_bucket_completely(self, bucket_name):

            client = self.S3_client

            response = client.list_objects_v2(
                Bucket=bucket_name,
            )

            while response['KeyCount'] > 0:
                print('Deleting %d objects from bucket %s' % (len(response['Contents']),bucket_name))
                response = client.delete_objects(
                    Bucket=bucket_name,
                    Delete={
                        'Objects':[{'Key':obj['Key']} for obj in response['Contents']]
                    }
                )
                response = client.list_objects_v2(
                    Bucket=bucket_name,
                )

            print('Now deleting bucket %s' % bucket_name)
            response = client.delete_bucket(
                Bucket=bucket_name
            )
            

    def upload_file_with_check(self, file_name, bucket, object_name=None):
            """Upload a file to an S3 bucket

            :param file_name: File to upload
            :param bucket: Bucket to upload to
            :param object_name: S3 object name. If not specified then file_name is used
            :return: True if file was uploaded, else False
            """

            # If S3 object_name was not specified, use file_name
            if object_name is None:
                object_name = os.path.basename(file_name)
                
            s3_client=self.S3_client 

            # Upload the file
            try:
                response = s3_client.upload_file(file_name, bucket, object_name)
            except ClientError as e:
                logging.error(e)
                return False
            return True
        
        
    def upload_multiple_files_with_check(self, file_list, bucket, object_name=None):
            """Upload multiple files to an S3 bucket

            :param file_name: File to upload
            :param bucket: Bucket to upload to
            :param object_name: S3 object name. If not specified then file_name is used
            :return: True if file was uploaded, else False
            """
            
            s3_client=self.S3_client 
            
            
            for file_name in file_list:
                    
                    # If S3 object_name was not specified, use file_name
                    if object_name is None:
                        object_string = os.path.basename(file_name)
                        
                    else:
                        file_name_split= file_name.split("/")[-1]
                        object_string= object_name + "/" + str(file_name_split)
                
                    # Upload the file
                    try:
                        response = s3_client.upload_file(Filename=file_name, Bucket=bucket, Key=object_string)
                    except ClientError as e:
                        logging.error(e)
                        return False
            return True
        
        
        
        
    def list_object_names(self, bucket):
            """Returns the names of the objects in the bucket."""
            s3_client=self.S3_client
            objects_list=s3_client.list_objects(Bucket=bucket)
            len_contents=len(objects_list['Contents'])
      

            objects_dict={}
            objects_names_list=[]

            for e,i in enumerate(range(0, len_contents), start=1):

                value=objects_list['Contents'][i]['Key']
                objects_dict[e] = value
                objects_names_list.append(value)

            return objects_dict, objects_names_list
    
    def getting_metadata(self, bucket, file_list=[]):
            """Returns the names of the objects in the bucket."""
            s3_client=self.S3_client
            
            if len(file_list) == 0:
                file_list_obj=self.list_object_names(bucket)
                file_list=file_list_obj[1]

            header_dict={}
            # header_list=[]
            
            for e, k in enumerate(file_list):
                header=s3_client.head_object(Bucket=bucket, Key=k)
                header_dict[e]=header
                
            return header_dict
        
    def download_with_error_check(self, file_name, bucket_name, key_name):
    
            s33 = s3_client=self.S3_client

            try:
                # The Bucket method is only given in the resource, but not in the client func
                s33.download_file(Filename=file_name, Bucket=bucket_name, Key=key_name)
                print('The object exists and is downloaded.')
                
            except botocore.exceptions.ClientError as e:
                if e.response['Error']['Code'] == "404":
                    print("The object does not exist.")
                else:
                    raise
                    
            