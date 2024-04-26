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

    def read_records(self, table):
        try:
            if not self.records.head:  
                connection = self.connection_manager.get_connection()
                cursor = connection.cursor(dictionary=True)
                query = f"SELECT * FROM {table}"
                cursor.execute(query)
                records = cursor.fetchall()
                
                self.records = LinkedList()
                
                for record in records:
                    self.records.append(record)
            
            rows = [list(record.values()) for record in self.records]
            headers = self.records.head.data.keys() if self.records.head else []  
            print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))  

            return self.records
        except Error as e:
            raise Error("Error while reading records:", e)

    def create_record(self, table, data):
        try:
            connection = self.connection_manager.get_connection()
            cursor = connection.cursor()
            columns = ', '.join(data.keys())
            placeholders = ', '.join(['%s'] * len(data))
            query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            cursor.execute(query, tuple(data.values()))
            connection.commit()
            new_record_id = cursor.lastrowid  
            data['id'] = new_record_id  
            self.records.append(data)  
            print("Record inserted successfully")
            return data  # Return the newly created record
        except Error as e:
            print("Error while inserting record:", e)

    def update_record(self, table, record_id, data):
        try:
            connection = self.connection_manager.get_connection()
            cursor = connection.cursor()
            columns = ', '.join([f"{key} = %s" for key in data.keys()])
            query = f"UPDATE {table} SET {columns} WHERE id = %s"
            cursor.execute(query, (*data.values(), record_id))
            connection.commit()
            print("Record updated successfully")
            for record in self.records:
                if record['id'] == record_id:
                    record.update(data)  
                    break
        except Error as e:
            print("Error while updating record:", e)

    def delete_record(self, table, record_id):
        try:
            connection = self.connection_manager.get_connection()
            cursor = connection.cursor()
            query = f"DELETE FROM {table} WHERE id = %s"
            cursor.execute(query, (record_id,))
            connection.commit()
            print("Record deleted successfully")
            current = self.records.head
            prev = None
            while current:
                if current.data['id'] == record_id:
                    if prev:
                        prev.next = current.next
                    else:
                        self.records.head = current.next
                    break
                prev = current
                current = current.next
        except Error as e:
            print("Error while deleting record:", e)

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

class ProfileModel(AbstractModel):
    def read_records(self, table):
        try:
            connection = self.connection_manager.get_connection()
            cursor = connection.cursor(dictionary=True)
            query = "SELECT Nama, Alamat, email, jenis_kelamin, No_hp FROM freelancer"
            cursor.execute(query)
            profiles = cursor.fetchall()
            return profiles
        except Error as e:
            print("Error while reading profiles:", e)
            return []

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
