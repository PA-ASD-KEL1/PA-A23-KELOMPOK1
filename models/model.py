from .database import MySQLDatabase, Error
from tabulate import tabulate
class Model:
    def __init__(self):
        self.db = MySQLDatabase(host="127.0.0.1", user="root", password="", database="ecofusion")

    def create_record(self, table, data):
        try:
            cursor = self.db.connection.cursor()
            columns = ', '.join(data.keys())
            placeholders = ', '.join(['%s'] * len(data))
            query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            cursor.execute(query, tuple(data.values()))
            self.db.connection.commit()
            print("Record inserted successfully")
        except Error as e:
            print("Error while inserting record:", e)
    
    def read_records(self, table):
        try:
            cursor = self.db.connection.cursor(dictionary=True)
            query = f"SELECT * FROM {table}"
            cursor.execute(query)
            records = cursor.fetchall()
            headers = records[0].keys() if records else []  # Ambil nama kolom dari keys dictionary pertama jika ada
            rows = [list(record.values()) for record in records]  # Ambil nilai dari setiap record
            if rows:
                print(tabulate(rows, headers=headers, tablefmt="pretty"))  # Tampilkan data dalam bentuk tabel
            else:
                print("No records found.")
            return records
        except Error as e:
            print("Error while reading records:", e)

    def update_record(self, table, record_id, data):
        try:
            cursor = self.db.connection.cursor()
            columns = ', '.join([f"{key} = %s" for key in data.keys()])
            query = f"UPDATE {table} SET {columns} WHERE id = %s"
            cursor.execute(query, (*data.values(), record_id))
            self.db.connection.commit()
            print("Record updated successfully")
        except Error as e:
            print("Error while updating record:", e)

    def delete_record(self, table, record_id):
        try:
            cursor = self.db.connection.cursor()
            query = f"DELETE FROM {table} WHERE id = %s"
            cursor.execute(query, (record_id,))
            self.db.connection.commit()
            print("Record deleted successfully")
        except Error as e:
            print("Error while deleting record:", e)
