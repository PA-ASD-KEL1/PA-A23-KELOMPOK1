import sys
import subprocess
import importlib
import os
import time
from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)

# Daftar library yang diperlukan
required_libraries = ['colorama', 'pwinput', 'tabulate', 'mysql.connector']

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Periksa dan instal library yang belum terpasang
print("Checking libraries...")
for lib in required_libraries:
    try:
        importlib.import_module(lib)
        print(f"{Fore.GREEN}Library {lib} sudah terinstal.{Style.RESET_ALL}")
    except ImportError:
        print(f"{Fore.YELLOW}Library {lib} belum terinstal. Menginstal...{Style.RESET_ALL}")
        try:
            install_package(lib)
            print(f"{Fore.GREEN}Library {lib} telah diinstal.{Style.RESET_ALL}")
        except subprocess.CalledProcessError:
            print(f"{Fore.RED}Gagal menginstal {lib}. Mohon instal secara manual.{Style.RESET_ALL}")

# Periksa jalur pencarian modul untuk memastikan bahwa modul yang diinstal dapat ditemukan
installed_module_paths = set(sys.path)
print("\nInstalled module paths:")
for path in installed_module_paths:
    print(path)

# Animasi
animation = [
    f"[{Fore.LIGHTBLUE_EX}■{Style.RESET_ALL}□□□□□□□□□]",
    f"[{Fore.LIGHTBLUE_EX}■■{Style.RESET_ALL}□□□□□□□□]",
    f"[{Fore.LIGHTBLUE_EX}■■■{Style.RESET_ALL}□□□□□□□]",
    f"[{Fore.LIGHTBLUE_EX}■■■■{Style.RESET_ALL}□□□□□□]",
    f"[{Fore.LIGHTBLUE_EX}■■■■■{Style.RESET_ALL}□□□□□]",
    f"[{Fore.LIGHTBLUE_EX}■■■■■■{Style.RESET_ALL}□□□□]",
    f"[{Fore.LIGHTBLUE_EX}■■■■■■■{Style.RESET_ALL}□□□]",
    f"[{Fore.LIGHTBLUE_EX}■■■■■■■■{Style.RESET_ALL}□□]",
    f"[{Fore.LIGHTBLUE_EX}■■■■■■■■■{Style.RESET_ALL}□]",
    f"[{Fore.LIGHTBLUE_EX}■■■■■■■■■■{Style.RESET_ALL}]\n",
]

print("\nChecking module installation...")
for i in range(len(animation)):
    time.sleep(0.3)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

# Kode untuk impor aplikasi
try:
    from views.Login_views import App
    print(f"\n{Fore.GREEN}Module berhasil diimpor.{Style.RESET_ALL}")
except ImportError as e:
    print(f"\n{Fore.RED}Error saat mengimpor module: {e}{Style.RESET_ALL}")
    sys.exit(1)

# Kode utama
if __name__ == "__main__":
    while True:
        try:
            App().main_menu()
        except Exception as e:
            print(f"{Fore.RED}Ups! Terjadi kesalahan: {e}{Style.RESET_ALL}")
        except KeyboardInterrupt:
            os.system("cls" if os.name == "nt" else "clear")
            print("\nKeyboard Interrupt")
            for i in range(3, 0, -1):
                time.sleep(1)
                print("Auto Logout In", i)
            continue
