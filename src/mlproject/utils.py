import os
import sys
import pandas as pd
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
from dotenv import load_dotenv
import pymysql



load_dotenv()

host = os.getenv("host")
user = os.getenv("user")        
password = os.getenv("password")
db = os.getenv("db")


def read_sql_data():
    logging.info("Reading SQL database started")
    try:    
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("connection Established",mydb)

        df = pd.read_sql_query("SELECT * FROM students", mydb)
        print(df.head())

        return df


    except Exception as e:
        raise CustomException(e, sys)

