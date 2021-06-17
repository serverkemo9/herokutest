import mysql.connector
from mysql.connector import Error
import requests;import sys

chat_id = sys.argv[1]
print(chat_id)
connection = mysql.connector.connect(host='localhost',
                                     user='root',
                                     database='users',
                                     password='')
if connection.is_connected():
    db_Info = connection.get_server_info()
    cursor = connection.cursor()
    cursor.execute("SELECT user FROM users;")
    record = cursor.fetchall()
    for i in record:
    	user = i[0]
    	requests.post('https://api.telegram.org/bot1636255183:AAHoclUiLsGhgLu3suU6TFYIN82jRFod19Y/sendMessage', {'chat_id':chat_id, 'text':user})

