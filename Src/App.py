import pandas as pd
import  DBConnection
import DBOperations

orders_schema = ['order_id','order_date','order_customer_id','order_status']

#print(help(pd.read_json))
orders = pd.read_json('D:\\DE\Material\\data-engineering-spark-main\\data-engineering-spark-main\\data\\retail_db_json\\orders\\part-r-00000-990f5773-9005-49ba-b670-631286032674', lines=True)

conn = DBConnection.ConnectDB(5432,'localhost','itversity_retail_user','itversity','itversity_retail_db')
folder = 'D:\\DE\Material\\data-engineering-spark-main\\data-engineering-spark-main\\data\\retail_db_json\\orders'

DBO = DBOperations.DBOperations()
files = DBO.get_files(folder)
file = folder+'\\'+files

print(conn.get_connection())
print(files)

ordersDF = DBO.get_data(file)
print(ordersDF['order_status'][:5])

DBO.load_data(ordersDF,conn.get_connection())