import Sybase
import sys

db_host = '192.168.1.18'
db_name = 'ZB00_JXC'
db_user = 'JL_USER'
db_password = '610422'

connection_string = 'Driver={SQL Server};Server=' + db_host + ';Database=' + db_name + ';UID=' + db_user + ';PWD=' + db_password + ';'
db = pyodbc.connect(connection_string)

SQL = "SELECT top 10 SPCODE,TAX_RATE,BARCODE,NAME,SPGG,SB,SPFL,FBID,UNIT,SPCD,ZLDJ,HWMZ FROM SPXX \
WHERE REGIST_DATE>='2017-8-31' AND TTBJ!=1 AND SPCODE <'500000'"

db.execute(SQL)
