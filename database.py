import pandas as pd
import oracledb
import os
from sql_p import sql
from dotenv import load_dotenv, dotenv_values


def get_data(sql):
    load_dotenv()
    adress_ip = os.environ.get("adress_ip")
    port = os.environ.get("port")
    service_name = os.environ.get("service_name")
    user = os.environ.get("user")
    password = os.environ.get("password")
    dsn = oracledb.makedsn(adress_ip, port, service_name=service_name)
    connection = None
    try:
        connection = oracledb.connect(user=user, password=password, dsn=dsn)
        df = pd.read_sql(sql, con=connection)
        return df
    except oracledb.Error as e:
        print(f'Error: {e}')
        return pd.DataFrame()
    finally:
        if connection:
            connection.close()

