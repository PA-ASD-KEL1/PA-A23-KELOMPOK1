from colorama import Fore, Style
import sys, os, random
import time
from models import Model
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
#Admin menu
def admin_menu():
    model_i = Model()
    while True:
        print("\n\033[1;36m╭───────────────────────╮\033[0m")
        print("\033[1;36m│\033[0;94m       Menu Admin      \033[1;36m│\033[0m")
        print("\033[1;36m├───────────────────────┤\033[0m")
        print("\033[92m│ 1. Daftar Perusahaan  │\033[0m")
        print("\033[92m│ 2. Daftar Kontrak     │\033[0m")
        print("\033[92m│ 3. Daftar Project     │\033[0m")
        print("\033[92m│ 4. Daftar Freelancer  │\033[0m")
        print("\033[92m│ 5. Daftar Admin       │\033[0m")
        print("\033[92m│ 6. Daftar Leader Pro  │\033[0m")
        print("\033[92m│ 7. Daftar Recruiter   │\033[0m")
        print("\033[92m│ 8. Exit               │\033[0m")
        print("\033[1;36m╰───────────────────────╯\033[0m")

        choice = input("\033[3;32mEnter your choice: \033[0m")


        if choice == "1":
            print("Loading...")
            loading_animation()
            sub_menu(model_i, "perusahaan")
        elif choice == "2":
            print("Loading...")
            loading_animation()
            sub_menu(model_i, "kontrak")
        elif choice == "3":
            print("Loading...")
            loading_animation()
            sub_menu(model_i, "project")
        elif choice == "4":
            print("Loading...")
            loading_animation()
            sub_menu(model_i, "freelancer")
        elif choice == "5":
            print("Loading...")
            loading_animation()
            sub_menu(model_i, "admin_project")
        elif choice == "6":
            print("Loading...")
            loading_animation()
            sub_menu(model_i, "leader_project")
        elif choice == "7":
            print("Loading...")
            sub_menu(model_i, "recruiter")
        elif choice == "8":
            loading_animation()
            print("Logging out...")
            break
        else:
            print(Fore.RED + "Invalid choice. Please enter a valid option.")

#sub menu admin
def sub_menu(model, table):
    while True:
        try:
            print("\n\033[1;36m╭───────────────────────╮\033[0m")
            print("\033[1;36m│\033[0;94m       Sub Menu        \033[1;36m│\033[0m")
            print("\033[1;36m├───────────────────────┤\033[0m")
            print("\033[92m│ 1. Create Record      │\033[0m")
            print("\033[92m│ 2. Read Records       │\033[0m")
            print("\033[92m│ 3. Update Record      │\033[0m")
            print("\033[92m│ 4. Delete Record      │\033[0m")
            print("\033[92m│ 5. Return Admin Menu  │\033[0m")
            print("\033[92m│ 6. Exit app           │\033[0m")
            print("\033[1;36m╰───────────────────────╯\033[0m")

            choice = input("\033[3;32mEnter your choice: \033[0m")

            if choice == "1":
                data = {}  # Inisialisasi dictionary untuk menyimpan data
                # Ambil input dari pengguna untuk setiap kolom
                for column in model.get_columns(table):
                    value = input(f"Enter {column}: ")
                    data[column] = value
                model.create_record(table, data)
            elif choice == "2":
                model.read_records(table)
            elif choice == "3":
                record_id = input("Enter record ID to update: ")
                data = {}  # Inisialisasi dictionary untuk menyimpan data yang akan diupdate
                # Ambil input dari pengguna untuk setiap kolom yang akan diupdate
                for column in model.get_columns(table):
                    value = input(f"Enter new value for {column}: ")
                    data[column] = value
                model.update_record(table, record_id, data)
            elif choice == "4":
                record_id = input("Enter record ID to delete: ")
                model.delete_record(table, record_id)
            elif choice == "5":
                print("Loading...")
                loading_animation()
                return
            elif choice == "6":
                loading_animation()
                print(f"{random.choice(colors)}")
                print(f"{random.choice(colors)} Thank you for using our app! {random.choice(goodbyes)}")
                print(Style.RESET_ALL)
                raise SystemExit
            else:
                print(Fore.RED + "Invalid choice. Please enter a valid option.")
        except ValueError as ve:
            print(Fore.RED + f"Invalid input: {ve}")
        except KeyError as ke:
            print(Fore.RED + f"Invalid column name: {ke}")
        except Exception as e:
            print(Fore.RED + f"An error occurred: {e}")