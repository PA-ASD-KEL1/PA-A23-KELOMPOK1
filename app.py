import subprocess, importlib, os, time, sys
from colorama import Fore, Style
from colorama import init, Fore, Back, Style
init(autoreset=True)
# Daftar library yang diperlukan
required_libraries = ['colorama', 'pwinput', 'tabulate']

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

# Periksa dan instal library yang belum terpasang
print("Checking library")
for i in range(len(animation)):
    time.sleep(0.3)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

for lib in required_libraries:
    try:
        importlib.import_module(lib)
        print(f"Library {lib} sudah terinstal.")
    except ImportError:
        print(f"Library {lib} belum terinstal. Menginstal...")
        subprocess.check_call(["pip", "install", lib])
        for i in range(3, 0, -1):
            time.sleep(1)
            print("Installing Library")
        print(f"Library {lib} telah diinstal.")

if __name__ == "__main__":
    from views.Login_views import App
    # while True:
    try:
        App().main_menu()
    except Exception as e:
        print("Ups Error!!: \nError Message: ", e)
    except KeyboardInterrupt:
        os.system("cls")
        print("\nKeyboard Interrupt")
        for i in range(3, 0, -1):
            time.sleep(1)
            print("Auto Logout In", i)
            # continue

