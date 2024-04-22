from colorama import Fore, Style
import sys,os, random
import time
#Estetika
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

colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

def loading_animation():
    animation = [
        f"[{Fore.LIGHTBLUE_EX}■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□□□□□□□□□]",
        f"[{Fore.LIGHTBLUE_EX}■■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□□□□□□□□]",
        f"[{Fore.LIGHTBLUE_EX}■■■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□□□□□□□]",
        f"[{Fore.LIGHTBLUE_EX}■■■■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□□□□□□]",
        f"[{Fore.LIGHTBLUE_EX}■■■■■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□□□□□]",
        f"[{Fore.LIGHTBLUE_EX}■■■■■■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□□□□]",
        f"[{Fore.LIGHTBLUE_EX}■■■■■■■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□□□]",
        f"[{Fore.LIGHTBLUE_EX}■■■■■■■■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□□]",
        f"[{Fore.LIGHTBLUE_EX}■■■■■■■■■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□]",
        f"[{Fore.LIGHTBLUE_EX}■■■■■■■■■■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}]",
        f"[{Fore.LIGHTBLUE_EX}■■■■■■■■■■{Style.RESET_ALL}{Fore.BLACK}■{Style.RESET_ALL}]",
    ]
    for frame in animation:
        sys.stdout.write("\r" + frame)
        sys.stdout.flush()
        time.sleep(0.2)

def main():
    while True:
        print("╔════════════════════════════════════════════╗")
        print("║           \033[0;34mSelamat Datang di Aplikasi\033[0m       ║")
        print("║               \033[3;34m      Ecofusion      \033[0m        ║")
        print("╠════════════════════════════════════════════╣")
        print("║               \033[0;36m 1. Login Admin\033[0m              ║")
        print("║               \033[0;36m 2. Login Pengguna\033[0m           ║")
        print("║               \033[0;36m 3. Login Recruiter\033[0m          ║")
        print("║               \033[0;36m 4. Keluar\033[0m                   ║")
        print("╚════════════════════════════════════════════╝")
        
        pilihan = input("\033[0;37mMasukkan pilihan Anda:\033[0m ").strip()

        if pilihan == "1":
            # Login Admin
            print("Loading...")
            loading_animation()
            print("Anda memilih untuk login sebagai Admin")
            from views import Admin_view
            Admin_view.admin_menu()
        elif pilihan == "2":
            # Login Pengguna
            print("Loading...")
            loading_animation()
            print("Anda memilih untuk login sebagai Pengguna")
            from views import user_menu
        elif pilihan == "3":
            # Login Recruiter
            print("Loading...")
            loading_animation()
            print("Anda memilih untuk login sebagai Recruiter")
            # Tambahkan logika login recruiter di sini
        elif pilihan == "4":
            # Keluar
            loading_animation()
            print(f"{random.choice(colors)}")
            print(f"{random.choice(colors)} Thank you for using our app! {random.choice(goodbyes)}")
            print(Style.RESET_ALL)
            raise SystemExit
        else:
            print("Pilihan tidak valid. Silakan pilih opsi yang benar.")
