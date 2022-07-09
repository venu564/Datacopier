import pandas as pd
import sqlalchemy
import os
class DBOperations:
    path =''

    def get_files(self,path):
        return os.listdir(path)[0]

    def get_data(self,file):
        return pd.read_json(file,lines=True)

    def load_data(self,df,conn):
        df.to_sql('orders',conn,if_exists="append",index=False)