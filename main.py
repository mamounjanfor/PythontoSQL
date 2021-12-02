import mysql.connector as mariadb
import sys
try:
    conn = mariadb.connect(
        user="root",
        password="root",
        host="127.0.0.1",
        port=3306,
        database="classicmodels"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
else:
    print("ok")
# Get Cursor
cur = conn.cursor()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass


