import os
import io
import requests
import boto3
import pandas
import sys

objurl= os.environ['=objurl']
objbucket = os.environ['objbucket']
objid = os.environ['objid']
objkey =  os.environ['objkey'] 
s3key = os.environ['s3key']

apiurl = 'http://nr-oracle-service'
apikey =  os.environ['apikey']
apiheaders = {
    'X-API-Key': apikey,
    'Content-Type': 'application/json'
}
apiquery = os.environ['apiquery']

def perform_api_request(apiurl, apiheaders, apiquery):
    try:
        response = requests.post(apiurl, headers=apiheaders, json=apiquery)
        jsondata = response.json()
        return jsondata
    except Exception as e:
        raise Exception(f"API Request Error: {str(e)}")

def create_excel_dataframe(jsondata):
    df = pandas.DataFrame(jsondata)
    with io.BytesIO() as output:
        with pandas.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer)
        exceldata = output.getvalue()
    return exceldata

def upload_to_s3(objbucket, objid, objkey, s3key, exceldata):
    try:
        session = boto3.Session(aws_access_key_id=objid, aws_secret_access_key=objkey)
        s3_client = boto3.client('s3',endpoint_url=objurl, aws_access_key_id=objid, aws_secret_access_key=objkey)
        s3_resource = session.resource('s3', endpoint_url=objurl)
        s3_client.delete_object(Bucket=objbucket,Key=s3key)    
        bucket = s3_resource.Bucket(objbucket)  
        bucket.put_object(Key=s3key, Body=exceldata)
        print(f'Here are all the objects currently stored in {objbucket}:')
        for my_bucket_object in bucket.objects.all():
            print(my_bucket_object.key)
    except Exception as e:
        raise Exception(f"S3 Error: {str(e)}")

try:
    jsondata = perform_api_request(apiurl, apiheaders, apiquery)
    exceldata = create_excel_dataframe(jsondata)
    upload_to_s3(objbucket, objid, objkey, s3key, exceldata)
    print(f'Successfully uploaded to S3 bucket {objbucket} with key {s3key}.')
    sys.exit(0)

except Exception as e:
    print(f"Error: {str(e)}")
    sys.exit(1)








