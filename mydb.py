import sys
sys.path.append('C:\\dcrm\\virt\\Lib\\site-packages\\mysql_connector_python-8.2.0.dist-info')

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
)

cursorObject =dataBase.cursor()

cursorObject.execute("CREATE DATABASE humberco")

print("All done")
