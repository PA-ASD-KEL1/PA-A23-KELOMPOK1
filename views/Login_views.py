from colorama import Fore, Style
import sys
import random
import time
from controllers.auth_controller import LoginAdmin, LoginPengguna, LoginRecruiter


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

colors = [
    Fore.RED, Fore.GREEN, Fore.YELLOW,
    Fore.BLUE, Fore.MAGENTA, Fore.CYAN
]


class App:
    def __init__(self):
        self.login_admin = LoginAdmin()
        self.login_pengguna = LoginPengguna()
        self.login_recruiter = LoginRecruiter()


    def loading_animation(self):
        animation = [
            f"[{Fore.LIGHTBLUE_EX}■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□□□□□□□□□]",
            f"[{Fore.LIGHTBLUE_EX}■■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□□□□□□□□]",
            f"[{Fore.LIGHTBLUE_EX}■■■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□□□□□□□]",
            f"[{Fore.LIGHTBLUE_EX}■■■■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□□□□□□]",
            f"[{Fore.LIGHTBLUE_EX}■■■■■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□□□□□]",
            f"[{Fore.LIGHTBLUE_EX}■■■■■■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□□□]",
            f"[{Fore.LIGHTBLUE_EX}■■■■■■■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□□□]",
            f"[{Fore.LIGHTBLUE_EX}■■■■■■■■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□□]",
            f"[{Fore.LIGHTBLUE_EX}■■■■■■■■■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□]",
            f"[{Fore.LIGHTBLUE_EX}■■■■■■■■■■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□]",
            f"[{Fore.LIGHTBLUE_EX}■■■■■■■■■■{Style.RESET_ALL}{Fore.BLACK}■{Style.RESET_ALL}]",
        ]
        for frame in animation:
            sys.stdout.write("\r" + frame)
            sys.stdout.flush()
            time.sleep(0.2)

    def main_menu(self):
        while True:
            print("╔════════════════════════════════════════════╗")
            print("║           \033[0;34mSelamat Datang di Aplikasi\033[0m       ║")
            print("║               \033[3;34m      Ecofusion      \033[0m        ║")
            print("╠════════════════════════════════════════════╣")
            print("║               \033[0;36m 1. Login Admin\033[0m              ║")
            print("║               \033[0;36m 2. Login Pengguna\033[0m           ║")
            print("║               \033[0;36m 3. Login Recruiter\033[0m          ║")
            print("║               \033[0;36m 4. Registrasi Akun\033[0m          ║")
            print("║               \033[0;36m 5. Keluar\033[0m                   ║")
            print("╚════════════════════════════════════════════╝")
            pilihan = input("\033[0;37mMasukkan pilihan Anda:\033[0m ").strip()
            if pilihan == "1":
                print("Anda memilih untuk login sebagai Admin")
                print("Loading...")
                self.loading_animation()
                self.login_admin.login()
            elif pilihan == "2":
                print("Anda memilih untuk login sebagai Pengguna")
                print("Loading...")
                self.loading_animation()
                self.login_pengguna.login()
            elif pilihan == "3":
                print("Anda memilih untuk login sebagai Recruiter")
                print("Loading...")
                self.loading_animation()
                self.login_recruiter.login()
            elif pilihan == "4":
                print("Anda memilih untuk registrasi akun")
                print("Loading...")
                self.loading_animation()
                self.login_pengguna.register_pengguna()
            elif pilihan == "5":
                self.loading_animation()
                print(f"{random.choice(colors)}")
                print(f"{random.choice(colors)} Thank you for using our app! {random.choice(goodbyes)}")
                print(Style.RESET_ALL)
                raise SystemExit
            else:
                print("Pilihan tidak valid. Silakan pilih opsi yang benar.")
