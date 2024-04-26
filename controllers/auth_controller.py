import mysql.connector
import pwinput
from views.Admin_view import Administrator
from views.User_view import User
from views.Recruiter_view import RecruiterMenu
from models.database import MySQLConnectionManager

MAX_ATTEMPTS = 3

class AbstractLogin:
    def __init__(self):
        self.connection_manager = MySQLConnectionManager()

    def login(self):
        raise NotImplementedError("Subclasses must implement login method.")

    def register_pengguna(self):
        raise NotImplementedError("Subclasses must implement register_pengguna method.")

class LoginAdmin(AbstractLogin):
    def login(self):
        connection = self.connection_manager.get_connection()

        attempts = 0

        while attempts < MAX_ATTEMPTS:
            email = input("Masukkan email admin: ").strip()
            password = input("Masukkan password admin: ").strip()

            try:
                cursor = connection.cursor(dictionary=True)

                query = "SELECT * FROM admin_project WHERE email = %s"
                cursor.execute(query, (email,))
                admin = cursor.fetchone()

                if admin:
                    if admin["password"] == password:
                        print("Login berhasil sebagai admin.")
                        # Creating an instance of Administrator and calling its admin_menu method
                        admin_view = Administrator()
                        admin_view.admin_menu()
                        break
                    else:
                        print("Password salah. Silakan coba lagi.")
                else:
                    print("Email salah atau tidak terdaftar sebagai admin.")

                cursor.close()

            except mysql.connector.Error as error:
                print("Error:", error)

            finally:
                attempts += 1

        if attempts >= MAX_ATTEMPTS:
            raise SystemExit("Batas percobaan login tercapai. Keluar dari program.")

class LoginPengguna(AbstractLogin):
    def login(self):
        connection = self.connection_manager.get_connection()

        attempts = 0

        while attempts < MAX_ATTEMPTS:
            email = input("Masukkan email pengguna: ").strip()
            password = pwinput.pwinput(prompt="Masukkan password pengguna: ").strip()

            try:
                cursor = connection.cursor(dictionary=True)

                query = "SELECT * FROM freelancer WHERE email = %s"
                cursor.execute(query, (email,))
                user = cursor.fetchone()

                if user:
                    if user["password"] == password:
                        print("Login berhasil sebagai pengguna.")
                        user_view = User()
                        user_view.user_menu()  # atau metode lain yang diperlukan
                        break
                    else:
                        print("Password salah. Silakan coba lagi.")
                else:
                    print("Email salah atau tidak terdaftar sebagai pengguna.")

            except mysql.connector.Error as error:
                print("Error:", error)

            finally:
                attempts += 1

        if attempts >= MAX_ATTEMPTS:
            raise SystemExit("Batas percobaan login tercapai. Keluar dari program.")

    def register_pengguna(self):
        connection = self.connection_manager.get_connection()

        nama = input("Masukkan username pengguna: ").strip()
        email = input("Masukkan email pengguna: ").strip()
        password = pwinput.pwinput(prompt="Masukkan password pengguna: ").strip()

        try:
            cursor = connection.cursor()

            query = "SELECT * FROM freelancer WHERE email = %s"
            cursor.execute(query, (email,))
            if cursor.fetchone():
                print("Email sudah terdaftar. Silakan gunakan email lain.")
                return

            query = "INSERT INTO freelancer (nama, email, password) VALUES (%s, %s, %s)"
            cursor.execute(query, (nama, email, password))
            connection.commit()
            print("Registrasi berhasil.")

        except mysql.connector.Error as error:
            print("Error:", error)

class LoginRecruiter(AbstractLogin):
    def login(self):
        connection = self.connection_manager.get_connection()

        attempts = 0

        while attempts < MAX_ATTEMPTS:
            nama = input("Masukkan nama recruiter: ").strip()
            password = input("Masukkan password recruiter: ").strip()

            try:
                cursor = connection.cursor(dictionary=True)

                query = "SELECT * FROM recruiter WHERE Nama_recruiter = %s"
                cursor.execute(query, (nama,))
                recruiter = cursor.fetchone()

                if recruiter:
                    if recruiter["password"] == password:
                        print("Login berhasil sebagai recruiter.")
                        recruiter_view = RecruiterMenu()
                        recruiter_view.display_menu()
                        break
                    else:
                        print("Password salah. Silakan coba lagi.")
                else:
                    print("Nama salah atau tidak terdaftar sebagai recruiter.")

            except mysql.connector.Error as error:
                print("Error:", error)

            finally:
                attempts += 1

        if attempts >= MAX_ATTEMPTS:
            raise SystemExit("Batas percobaan login tercapai. Keluar dari program.")
