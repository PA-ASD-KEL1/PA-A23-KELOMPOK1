from colorama import Fore, Style
import random
from models.model import RecordModel
from views import Login_views

class RecruiterMenu:
    def __init__(self):
        self.model = RecordModel()
        self.login_view = Login_views.App()

    def display_menu(self):
        colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
        goodbyes = [
            "See you later, alligator!",
            "Catch you on the flip side!",
            "Adios, amigos!",
            "Until we meet again!",
            "Stay classy!",
            "Farewell, traveler!",
            "Take care, mate!",
            "May the Force be with you!",
            "Auf Wiedersehen!",
            "Arrivederci!",
            "Goodbye, for now!",
            "Keep on coding!",
        ]

        while True:
            table = ("kontrak")
            try:
                print("\n\033[1;36m╭───────────────────────╮\033[0m")
                print("\033[1;36m│\033[0;94m       Recruiter Menu        \033[1;36m│\033[0m")
                print("\033[1;36m├───────────────────────┤\033[0m")
                print("\033[92m│ 1. Tambah Kontrak      │\033[0m")
                print("\033[92m│ 2. Lihat Kontrak       │\033[0m")
                print("\033[92m│ 3. Ubah Kontrak        │\033[0m")
                print("\033[92m│ 4. Hapus Kontrak       │\033[0m")
                print("\033[92m│ 5. Lihat Project       │\033[0m")
                print("\033[92m│ 6. Kembali             │\033[0m")
                print("\033[92m│ 7. Keluar              │\033[0m")
                print("\033[1;36m╰───────────────────────╯\033[0m")

                choice = input("\033[3;32mPilih menu: \033[0m")

                
                if choice == "1":
                    data = {}
                    for column in self.model.get_columns(table):  # Memanggil get_columns() dari objek RecordModel
                        value = input(f"Enter value for {column}: ")
                        data[column] = value
                    self.model.create_record(table, data)

                elif choice == "2":
                    self.model.read_records(table)

                elif choice == "3":
                    record_id = input("Enter record ID to update: ")
                    data = {}
                    for column in self.model.get_columns(table):  
                        value = input(f"Enter new value for {column}: ")
                        data[column] = value
                    self.model.update_record(table, record_id, data)

                elif choice == "4":
                    record_id = input("Enter record ID to delete: ")
                    self.model.delete_record(table, record_id)

                elif choice == "5":
                    self.login_view.loading_animation()
                    self.model.read_records("project")

                elif choice == "6":
                    print("Loading...")
                    self.login_view.loading_animation()
                    return

                elif choice == "7":
                    self.login_view.loading_animation()
                    print(f"{random.choice(colors)}")
                    print(f"{random.choice(colors)} Terima kasih telah menggunakan aplikasi kami! {random.choice(goodbyes)}")
                    print(Style.RESET_ALL)
                    break
                else:
                    print(Fore.RED + "Pilihan tidak valid. Silakan masukkan opsi yang benar.")
            except ValueError as ve:
                print(Fore.RED + f"Input tidak valid: {ve}")
            except KeyError as ke:
                print(Fore.RED + f"Nama kolom tidak valid: {ke}")
            except Exception as e:
                print(Fore.RED + f"Terjadi kesalahan: {e}")
