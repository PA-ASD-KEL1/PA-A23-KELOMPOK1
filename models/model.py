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

    def get_recruiter_and_company_info(self):
        try:
            connection = self.connection_manager.get_connection()
            cursor = connection.cursor(dictionary=True)
            
            query = """
            SELECT recruiter.ID_Recruiter, recruiter.Nama_recruiter, 
                perusahaan.ID_Perusahaan, perusahaan.Nama_perusahaan
            FROM recruiter
            LEFT OUTER JOIN perusahaan ON recruiter.ID_Recruiter = perusahaan.ID_Perusahaan
            
            UNION
            
            SELECT recruiter.ID_Recruiter, recruiter.Nama_recruiter, 
                perusahaan.ID_Perusahaan, perusahaan.Nama_perusahaan
            FROM recruiter
            RIGHT OUTER JOIN perusahaan ON recruiter.ID_Recruiter = perusahaan.ID_Perusahaan
            """
            cursor.execute(query)
            rows = cursor.fetchall()
            
            results = []
            for row in rows:
                result_row = [row['ID_Recruiter'], row['Nama_recruiter'], row['ID_Perusahaan'], row['Nama_perusahaan']]
                results.append(result_row)
            
            headers = ["ID Recruiter", "Nama Recruiter", "ID Perusahaan", "Nama Perusahaan"]
            print(tabulate(results, headers=headers, tablefmt="grid"))
            
        except Exception as e:
            print("Error occurred:", str(e))
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

    def jump_search(self, value):
        current = self.head
        prev = None
        while current and current.data['Gaji'] < value:
            prev = current
            current = current.next

        if not current:
            return prev

        return prev

    def quick_sort(self):
        self.head = self._quick_sort_recursive(self.head)

    def _quick_sort_recursive(self, node):
        if not node or not node.next:
            return node

        pivot = node
        smaller_head = None
        smaller_tail = None
        equal_head = None
        equal_tail = None
        larger_head = None
        larger_tail = None

        current = node

        while current:
            if current.data['Gaji'] < pivot.data['Gaji']:
                if not smaller_head:
                    smaller_head = current
                    smaller_tail = current
                else:
                    smaller_tail.next = current
                    smaller_tail = current
            elif current.data['Gaji'] == pivot.data['Gaji']:
                if not equal_head:
                    equal_head = current
                    equal_tail = current
                else:
                    equal_tail.next = current
                    equal_tail = current
            else:
                if not larger_head:
                    larger_head = current
                    larger_tail = current
                else:
                    larger_tail.next = current
                    larger_tail = current

            current = current.next

        if smaller_tail:
            smaller_tail.next = None
        if equal_tail:
            equal_tail.next = None
        if larger_tail:
            larger_tail.next = None

        smaller_head = self._quick_sort_recursive(smaller_head)
        larger_head = self._quick_sort_recursive(larger_head)

        if smaller_head:
            pivot_node = smaller_head
            while pivot_node.next:
                pivot_node = pivot_node.next
            pivot_node.next = equal_head
        else:
            smaller_head = equal_head

        if equal_head:
            equal_tail.next = larger_head
        else:
            smaller_tail = larger_head

        return smaller_head

    def JumpSearch_rw(self, rentang_waktu):
        current = self.head
        while current and current.data['rentang_waktu'] < rentang_waktu:
            current = current.next
        if current and current.data['rentang_waktu'] == rentang_waktu:
            return current.data
        return None

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

    def Search_by_salary(self, gaji):
        try:
            connection = self.connection_manager.get_connection()
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM project WHERE Gaji >= %s AND Gaji <= %s"
            cursor.execute(query, (gaji, gaji))
            results = cursor.fetchall()

            if results:
                linked_list = LinkedList()
                for result in results:
                    linked_list.append(result)

                linked_list.quick_sort()
                table = []
                for data in linked_list:
                    table.append([data['Judul'], data['Deskripsi'], data['Bidang'], data['Gaji']])
                print(tabulate(table, headers=["Judul", "Deskripsi", "Bidang", "Gaji"], tablefmt="grid"))
            else:
                print("\033[3;91mTidak ada proyek dengan gaji mendekati atau sama dengan", gaji)
        except Error as e:
            print("Error while searching projects by salary:", e)


    def find_project_by_id(self, project_id):
        try:
            connection = self.connection_manager.get_connection()
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM Project WHERE ID_Project = %s"
            cursor.execute(query, (project_id,))
            project = cursor.fetchone()
            return project
        except Error as e:
            print(f"Error ketika mencari proyek berdasarkan ID: {e}")
            # Mengembalikan None jika terjadi kesalahan


    def search_by_time_range(self, time_range):
        try:
            connection = self.connection_manager.get_connection()
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM project WHERE rentang_waktu = %s"
            cursor.execute(query, (time_range,)) 
            projects = cursor.fetchall()

            if projects:
                ls = LinkedList()
                for project in projects:
                    ls.append(project)
                result = ls.JumpSearch_rw(time_range) 

                if result:
                    table = [[result['ID_Project'], result['Judul'], result['Status'], result['Deskripsi'], 
                            result['Bidang'], result['Gaji'], result['ID_adminproject'], result['rentang_waktu'], 
                            result['nama_freelancer']]]
                    print(tabulate(table, headers=["ID_Project", "Judul", "Status", "Deskripsi", "Bidang", "Gaji", 
                                                "ID_adminproject", "Rentang Waktu", "Nama Freelancer"], tablefmt="grid"))
                else:
                    print("\033[91mData proyek dengan rentang waktu", time_range, "tidak ditemukan.")

        except Error as e:
            print("Error while searching projects by time range:", e)

    def register_for_project(self, project_id, nama_freelancer):
        try:
            connection = self.connection_manager.get_connection()
            cursor = connection.cursor(dictionary=True)
            query = "UPDATE project SET Status = 'Menunggu Persetujuan', nama_freelancer = %s WHERE ID_Project = %s"
            cursor.execute(query, (nama_freelancer, project_id))
            connection.commit()
            print("Pendaftaran untuk proyek berhasil!")
        except Error as e:
            print("Error while registering for project:", e)