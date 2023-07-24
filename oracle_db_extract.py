import oracledb
import pandas
import os

# oracledb.init_oracle_client(lib_dir="/opt/oracle/instantclient_21_10")

def load_configuration():

    username = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    database = os.getenv('DATABASE')

    return username, password, host, port, database

def execute_query(connection, query_file):
    with open(query_file, 'r') as sql_file:
        sql_script = sql_file.read()

    with connection.cursor() as cursor:
        cursor.execute(sql_script)
        results = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        df = pandas.DataFrame(results, columns=columns)
        return df

def export_to_excel(df, file_path):
    try:
        df.to_excel(file_path, index=False)
        # print(f"Results exported to {file_path}")
    except Exception as e:
        # print(f"Error exporting results to {file_path}: {str(e)}")

query_file = "rar_query.sql"
# This is a file name for within the Docker container. The long term file name should be: f"output_{date.today().strftime('%Y-%m-%d')}_{query_file.replace('.sql', '')}.xlsx"
output_file_name = "rar_output.xlsx"
# This is a path within the Docker conatiner. The long term destination should be: //objectstore.nrs.bcgov/datafoundations_prod/rar_query_output
output_file_path = f"/extracts/{output_file_name}"

try:
    username, password, host, port, database = load_configuration()

    #ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    #ssl_context.options |= ssl.OP_SINGLE_DH_USE
    #ssl_context.load_cert_chain(certfile=ssl_certfile)


    dsn = oracledb.makedsn(host=host, port=port, service_name=database)

    with oracledb.connect(user=username, password=password, dsn=dsn) as con:
        print("Connected to the database:", database)
        print("Database version:", con.version)
        print("Thin:", con.thin)

        df = execute_query(con, query_file)
        print("Query executed successfully")

        # export_to_excel(df, output_file_path)
        # print("Excel file exported successfully")

except oracledb.DatabaseError as e:
    print("Database error:", str(e))
except Exception as e:
    print("Other error:", str(e))