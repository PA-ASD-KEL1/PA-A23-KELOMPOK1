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
            try:
                print("\n\033[1;36m╭───────────────────────╮\033[0m")
                print("\033[1;36m│\033[0;94m       Recruiter Menu        \033[1;36m│\033[0m")
                print("\033[1;36m├───────────────────────┤\033[0m")
                print("\033[92m│ 1. Tambah Kontrak      │\033[0m")
                print("\033[92m│ 2. Lihat Kontrak       │\033[0m")
                print("\033[92m│ 3. Ubah Kontrak        │\033[0m")
                print("\033[92m│ 4. Hapus Kontrak       │\033[0m")
                print("\033[92m│ 5. Kembali             │\033[0m")
                print("\033[92m│ 6. Keluar              │\033[0m")
                print("\033[1;36m╰───────────────────────╯\033[0m")

                choice = input("\033[3;32mPilih menu: \033[0m")

                if choice == "1":
                    data = {}
                    self.login_view.loading_animation()
                    data["status_kontrak"] = input("Masukkan status kontrak (Aktif/Tidak Aktif): ")
                    data["ID_Recruiter"] = input("Masukkan ID Recruiter: ")
                    data["ID_Perusahaan"] = input("Masukkan ID Perusahaan: ")
                    data["durasi_kontrak"] = input("Masukkan durasi kontrak: ")
                    data["gaji"] = input("Masukkan gaji: ")
                    data["nama_freelancer"] = input("Masukkan nama freelancer: ")
                    self.model.create_record("kontrak", data)
                elif choice == "2":
                    self.login_view.loading_animation()
                    self.model.read_records("kontrak")
                elif choice == "3":
                    self.login_view.loading_animation()
                    record_id = input("Masukkan ID kontrak yang akan diubah: ")
                    data = {}
                    data["status_kontrak"] = input("Masukkan status kontrak baru (Aktif/Tidak Aktif): ")
                    data["ID_Recruiter"] = input("Masukkan ID Recruiter baru: ")
                    data["ID_Perusahaan"] = input("Masukkan ID Perusahaan baru: ")
                    data["durasi_kontrak"] = input("Masukkan durasi kontrak baru: ")
                    data["gaji"] = input("Masukkan gaji baru: ")
                    data["nama_freelancer"] = input("Masukkan nama freelancer baru: ")
                    self.model.update_record("kontrak", record_id, data)
                elif choice == "4":
                    self.login_view.loading_animation()
                    record_id = input("Masukkan ID kontrak yang akan dihapus: ")
                    self.model.delete_record("kontrak", record_id)
                elif choice == "5":
                    print("Loading...")
                    self.login_view.loading_animation()
                    return
                elif choice == "6":
                    self.login_view.loading_animation()
                    print(f"{random.choice(colors)}")
                    print(f"{random.choice(colors)} Terima kasih telah menggunakan aplikasi kami! {random.choice(goodbyes)}")
                    print(Style.RESET_ALL)
                    raise SystemExit
                else:
                    print(Fore.RED + "Pilihan tidak valid. Silakan masukkan opsi yang benar.")
            except ValueError as ve:
                print(Fore.RED + f"Input tidak valid: {ve}")
            except KeyError as ke:
                print(Fore.RED + f"Nama kolom tidak valid: {ke}")
            except Exception as e:
                print(Fore.RED + f"Terjadi kesalahan: {e}")
