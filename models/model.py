from models.database import MySQLConnectionManager
from mysql.connector import Error
from tabulate import tabulate
# Kelas abstract model
class AbstractModel:
    def __init__(self):
        self.connection_manager = MySQLConnectionManager()

    def read_records(self, table):
        raise NotImplementedError("Subclasses must implement read_records method.")

    def create_record(self, table, data):
        raise NotImplementedError("Subclasses must implement create_record method.")

    def update_record(self, table, record_id, data):
        raise NotImplementedError("Subclasses must implement update_record method.")

    def delete_record(self, table, record_id):
        raise NotImplementedError("Subclasses must implement delete_record method.")

class RecordModel(AbstractModel):
    def __init__(self):
        super().__init__()
        self.records = LinkedList()

    def get_primary_key(self, table):
        try:
            connection = self.connection_manager.get_connection()
            cursor = connection.cursor()
            query = f"DESCRIBE {table}"
            cursor.execute(query)
            columns = cursor.fetchall()
            for column in columns:
                if "PRI" in column:
                    return column[0]  # Return the name of the primary key column
        except Exception as e:
            raise RuntimeError(f"An error occurred while getting primary key: {e}")

    def get_columns(self, table):
        try:
            connection = self.connection_manager.get_connection()
            cursor = connection.cursor()
            query = f"DESC {table}"
            cursor.execute(query)
            columns = [column[0] for column in cursor.fetchall()]
            return columns
        except Exception as e:
            raise RuntimeError(f"An error occurred while getting columns: {e}")

    def read_records(self, table):
        try:
            self.records.clear()  # Reset linked list sebelum membaca record baru
            connection = self.connection_manager.get_connection()
            cursor = connection.cursor(dictionary=True)
            query = f"SELECT * FROM {table}"
            cursor.execute(query)
            records = cursor.fetchall()

            for record in records:
                self.records.append(record)

            rows = [list(record.values()) for record in self.records]
            headers = self.records.head.data.keys() if self.records.head else []
            print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

            return self.records
        except Error as e:
            raise RuntimeError("Error while reading records:", e)

    def create_record(self, table, data, id_column='ID'):
        try:
            connection = self.connection_manager.get_connection()
            cursor = connection.cursor()
            columns = ', '.join(data.keys())
            placeholders = ', '.join(['%s'] * len(data))
            query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            cursor.execute(query, tuple(data.values()))
            connection.commit()
            new_record_id = cursor.lastrowid
            data[id_column] = new_record_id
            self.records.append(data)
            print("Record inserted successfully")
            return data  # mengembalikan nilai record data yang baru
        except Error as e:
            raise RuntimeError("Error while inserting record:", e)

    def update_record(self, table, record_id, data):
        try:
            primary_key = self.get_primary_key(table)  # Dapatkan primary key dari tabel
            connection = self.connection_manager.get_connection()
            cursor = connection.cursor()
            columns = ', '.join([f"{key} = %s" for key in data.keys()])
            query = f"UPDATE {table} SET {columns} WHERE {primary_key} = %s"
            cursor.execute(query, (*data.values(), record_id))
            connection.commit()
            print("Record updated successfully")

            # Perbarui record dalam linked list jika ada
            for record in self.records:
                if record[primary_key] == record_id:
                    record.update(data)
                    break
        except Error as e:
            raise RuntimeError("Error while updating record:", e)

    def delete_record(self, table, record_id):
        try:
            primary_key = self.get_primary_key(table)  # Dapatkan primary key dari tabel
            connection = self.connection_manager.get_connection()
            cursor = connection.cursor()
            query = f"DELETE FROM {table} WHERE {primary_key} = %s"
            cursor.execute(query, (record_id,))
            connection.commit()
            print("Record deleted successfully")

            # Hapus record dari linked list jika ada
            current = self.records.head
            prev = None
            while current:
                if current.data[primary_key] == record_id:
                    if prev:
                        prev.next = current.next
                    else:
                        self.records.head = current.next
                    break
                prev = current
                current = current.next
        except Error as e:
            raise RuntimeError("Error while deleting record:", e)


class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = self.Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = self.Node(data)

    def clear(self):
        self.head = None  # Menghapus semua node dengan mengatur head menjadi None

    def remove(self, value):
        current = self.head
        prev = None
        while current:
            if current.data == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next


class ProjectModel(AbstractModel):
    def read_records(self, table):
        try:
            connection = self.connection_manager.get_connection()
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM project"
            cursor.execute(query)
            projects = cursor.fetchall()
            return projects
        except Error as e:
            print("Error while reading projects:", e)
            return []
    
    def search_by_salary(self, min_salary, max_salary):
        try:
            connection = self.connection_manager.get_connection()
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM project WHERE Gaji BETWEEN %s AND %s"
            cursor.execute(query, (min_salary, max_salary))
            projects = cursor.fetchall()
            return projects
        except Error as e:
            print("Error while searching projects by salary:", e)
            return []
    
    def search_by_time_range(self, time_range):
        try:
            connection = self.connection_manager.get_connection()
            cursor = connection.cursor(dictionary=True)
            # Assuming the project table has a 'duration' field representing time range
            query = "SELECT * FROM project WHERE rentang_waktu = %s"
            cursor.execute(query, (time_range,))
            projects = cursor.fetchall()
            return projects
        except Error as e:
            print("Error while searching projects by time range:", e)
            return []