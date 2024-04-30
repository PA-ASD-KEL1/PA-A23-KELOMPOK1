from flask import session
import mysql.connector
import pwinput, re
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
            password = pwinput.pwinput(prompt="Masukkan password admin: ").strip()

            try:
                cursor = connection.cursor(dictionary=True)

                query = "SELECT * FROM admin_project WHERE email = %s"
                cursor.execute(query, (email,))
                admin = cursor.fetchone()

                if admin:
                    if admin["password"] == password:
                        print("Login berhasil sebagai admin.")
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
    user_session = {}

    def __init__(self):
        super().__init__()
        self.log = ""

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
                        self.user_session["email"] = user["email"]  # Simpan informasi pengguna ke dalam user_session
                        uv = User()
                        uv.user_menu()
                        return
                    else:
                        print("Password salah. Silakan coba lagi.")
                else:
                    print("Email salah atau tidak terdaftar sebagai pengguna.")

            except mysql.connector.Error as error:
                print("Error:", error)

            finally:
                attempts += 1

        if attempts >= MAX_ATTEMPTS:
            print("Batas percobaan login tercapai. Silakan coba lagi nanti.")

    def register_pengguna(self):
        connection = self.connection_manager.get_connection()

        # Input Nama dan pastikan kapitalisasi huruf
        nama = input("Masukkan username pengguna: ").strip().title()

        # Input ID Freelancer
        while True:
            id_freelancer = input("Masukkan ID Freelancer: ").strip()
            # Periksa apakah ID Freelancer sudah ada di database
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM freelancer WHERE ID_Freelancer = %s", (id_freelancer,))
            if cursor.fetchone():
                print("ID Freelancer sudah terdaftar. Silakan gunakan ID lain.")
            else:
                break

        # Input Email dengan validasi menggunakan regular expression
        while True:
            email = input("Masukkan email pengguna: ").strip()
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                print("Format email tidak valid. Email harus memiliki format yang valid, contoh: example@gmail.com")
            else:
                break

        # Input Password dengan validasi panjang
        while True:
            password = input("Masukkan password pengguna (harus 4 digit): ").strip()
            if len(password) != 4 or not password.isdigit():
                print("Password harus terdiri dari 4 digit angka.")
            else:
                break

        # Input Nomor HP dengan validasi panjang
        while True:
            no_hp = input("Masukkan Nomor HP pengguna (harus 12 digit): ").strip()
            if len(no_hp) != 12 or not no_hp.isdigit():
                print("Nomor HP harus terdiri dari 12 digit angka.")
            else:
                break

        # Input Alamat dengan validasi harus mengandung JL.
        while True:
            alamat = input("Masukkan alamat pengguna (harus mengandung 'JL.'): ").strip()
            if 'JL.' not in alamat:
                print("Alamat harus mengandung 'JL.'. Silakan masukkan alamat yang sesuai.")
            else:
                break

        # Input Jenis Kelamin dengan validasi
        while True:
            jenis_kelamin = input("Masukkan jenis kelamin (laki-laki/perempuan): ").strip().lower()
            if jenis_kelamin not in ['laki-laki', 'perempuan']:
                print("Jenis kelamin hanya bisa diisi dengan 'laki-laki' atau 'perempuan'.")
            else:
                break

        try:
            cursor = connection.cursor()

            # Insert data pengguna ke database
            query = "INSERT INTO freelancer (ID_Freelancer, Nama, email, password, No_hp, Alamat, jenis_kelamin) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (id_freelancer, nama, email, password, no_hp, alamat, jenis_kelamin))
            connection.commit()
            print("Registrasi berhasil.")

        except mysql.connector.Error as error:
            print("Error:", error)

    def profil(self):
        if "email" in LoginPengguna.user_session:
            email = LoginPengguna.user_session["email"]
            connection = self.connection_manager.get_connection()
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM freelancer WHERE email = %s"
                cursor.execute(query, (email,))
                user = cursor.fetchone()
                if user:
                    print("Profil Pengguna:")
                    print(f"\033[96mNama: {user['Nama']}\033[0m")
                    print(f"\033[96mAlamat: {user['Alamat']}\033[0m")
                    print(f"\033[96mEmail: {user['email']}\033[0m")
                    print(f"\033[96mJenis Kelamin: {user['jenis_kelamin']}\033[0m")
                    print(f"\033[96mNo. HP: {user['No_hp']}\033[0m")
                else:
                    print("Pengguna tidak ditemukan.")
            except mysql.connector.Error as error:
                print("Error:", error)
        else:
            print("Anda belum login. Silakan login terlebih dahulu.")

class LoginRecruiter(AbstractLogin):
    def login(self):
        connection = self.connection_manager.get_connection()

        attempts = 0

        while attempts < MAX_ATTEMPTS:
            nama = input("Masukkan nama recruiter: ").strip()
            password = pwinput.pwinput(prompt="Masukkan password recruiter: ").strip()

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
