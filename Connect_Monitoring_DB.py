import pyodbc 
from datetime import datetime
import time
import logging



server = '' 
database = '' 
username = '' 
password = '' 


def get_branch():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()
    cursor.execute('''
          select branch_name FROM [Live_Monitoring_DB].[dbo].[Branch]
    ''')
    data = cursor.fetchall()
    cursor.close()
    return data

def get_network_status(x):
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()
    cursor.execute('''
          select top 1* FROM [Live_Monitoring_DB].[dbo].[Network_Monitoring] where branch = '{0}' order by createdtime desc
    '''.format(str(x)))
    data = cursor.fetchall()
    cursor.close()
    return data

def add_network_status(x):
    ts = time.time()
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Network_Monitoring (branch,network_status,createdtime)
        VALUES ('{0}',1, {1});
    '''.format(str(x),ts))

    try:
        cursor.commit()
    except Exception as ex:
        cursor.rollback()
        #logger.error(str(ex))
    cursor.close()


def get_live_data_status(x):
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()
    cursor.execute('''
              select machine, MAX (created_datetime) FROM [Live_Monitoring_DB].[dbo].[Monitoring_Live_Data] where branch = '{0}' group by machine
    '''.format(str(x)))
    data = cursor.fetchall()
    cursor.close()   
    return data


def get_Ma_Status(x):
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()
    cursor.execute('''
          select Serial_Number, MAX (Created_Datetime) FROM [Live_Monitoring_DB].[dbo].[Ma_Live] where branch = '{0}' group by Serial_Number
    '''.format(str(x)))
    data = cursor.fetchall()
    cursor.close()
    return data

def add_Result_MA_Live(data,name):
    ts = time.time()
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Ma_Live (Serial_Number,Ip_address,Status,Created_Datetime,branch)
        VALUES ('{0}','{1}', 0,{2}, '{3}');
    '''.format(str(data[0]),str(data[1]),ts,str(name)))

    try:
        cursor.commit()
    except Exception as ex:
        cursor.rollback()
        #logger.error(str(ex))
    cursor.close()

def add_live_data_monitoring(data,branch):
    ts = time.time()
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Monitoring_Live_Data (branch,machine,created_datetime,last_receive_time)
        VALUES ('{0}','{1}',{2}, {3});
    '''.format(branch,data[0],ts,data[1]))

    try:
        cursor.commit()
    except Exception as ex:
        cursor.rollback()
        #logger.error(str(ex))
    cursor.close()

def performance_nuc(cpu,memory):
    ts = time.time()
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Performance_Nuc (Branch,CPU,MEMORY,datetime)
        VALUES ('ARA','{0}',{1}, {2});
    '''.format(cpu,memory,ts))

    try:
        cursor.commit()
    except Exception as ex:
        cursor.rollback()
        #logger.error(str(ex))
    cursor.close()

if __name__ == "__main__":

    add_network_status('Ara')