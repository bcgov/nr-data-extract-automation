import oracledb
import pandas
import os
import boto3
from dotenv import load_dotenv

# oracledb.init_oracle_client(lib_dir="/opt/oracle/instantclient_21_10")
query_file = "rar_query.sql"

def load_configuration():
    load_dotenv()
    username = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    database = os.getenv('DATABASE')
    objid = os.getenv('OBJ_STOR_ID')
    objkey = os.getenv('OBJ_STOR_KEY')

    return username, password, host, port, database, objid, objkey

def execute_query(connection, query_file):
    with open(query_file, 'r') as sql_file:
        sql_script = sql_file.read()

    with connection.cursor() as cursor:
        cursor.execute(sql_script)
        results = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        df = pandas.DataFrame(results, columns=columns)
        return df

def export_to_excel(df, objid, objkey):

    endpoint_url= 'https://nrs.objectstore.gov.bc.ca' 
    
    bucketname = 'bvtnvt'

    s3_client = boto3.client('s3', endpoint_url=endpoint_url, aws_access_key_id=objid, aws_secret_access_key=objkey)

    s3_key = 'rar-query-output/rar_output_from_docker.xlsx'

    excel_file_path = 'extracts/rar_output.xlsx'

    try:
        
        s3_client.upload_file(Filename=df, Bucket=bucketname,Key=excel_file_path) 

    except Exception as e:
        print(f"An error occurred: {e}")

    print(f'Successfully uploaded {excel_file_path} to S3 bucket {bucketname} with key {s3_key}.')
    
    print(f'Here are all the objects currently stored in {bucketname}:')

    session = boto3.Session(aws_access_key_id=objid, aws_secret_access_key=objkey)

    s3_resource = session.resource('s3', endpoint_url=endpoint_url)

    my_bucket = s3_resource.Bucket(bucketname)

    for my_bucket_object in my_bucket.objects.all():
        print(my_bucket_object.key)

try:
    username, password, host, port, database, objid, objkey = load_configuration()

    dsn = oracledb.makedsn(host=host, port=port, service_name=database)

    with oracledb.connect(user=username, password=password, dsn=dsn) as con:
        print("Connected to the database:", database)
        print("Database version:", con.version)
        print("Thin:", con.thin)

        df = execute_query(con, query_file)
        print("Query executed successfully")

        export_to_excel(df, objid, objkey)
        

except oracledb.DatabaseError as e:
    print("Database error:", str(e))
except Exception as e:
    print("Other error:", str(e))