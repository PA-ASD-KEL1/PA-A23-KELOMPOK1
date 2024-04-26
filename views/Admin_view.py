from colorama import Fore, Style
import sys
import os
import random
import time
from models import model

# Estetika
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

class Menu:
    def loading_animation(self):
        animation = [
            f"[{Fore.LIGHTBLUE_EX}■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□□□□□□□□□]",
            f"[{Fore.LIGHTBLUE_EX}■■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□□□□□□□□]",
            f"[{Fore.LIGHTBLUE_EX}■■■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□□□□□□□]",
            f"[{Fore.LIGHTBLUE_EX}■■■■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□□□□□□]",
            f"[{Fore.LIGHTBLUE_EX}■■■■■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□□□□□]",
            f"[{Fore.LIGHTBLUE_EX}■■■■■■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□□□]",
            f"[{Fore.LIGHTBLUE_EX}■■■■■■■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□□]",
            f"[{Fore.LIGHTBLUE_EX}■■■■■■■■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□]",
            f"[{Fore.LIGHTBLUE_EX}■■■■■■■■■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}□]",
            f"[{Fore.LIGHTBLUE_EX}■■■■■■■■■■{Style.RESET_ALL}{Fore.BLACK}□{Style.RESET_ALL}]",
            f"[{Fore.LIGHTBLUE_EX}■■■■■■■■■■{Style.RESET_ALL}{Fore.BLACK}■{Style.RESET_ALL}]",
        ]
        for frame in animation:
            sys.stdout.write("\r" + frame)
            sys.stdout.flush()
            time.sleep(0.2)

class Administrator(Menu):
    def __init__(self):
        self.model_i = model.RecordModel()

    # Admin menu
    def admin_menu(self):
        while True:
            try:
                print("\n\033[1;36m╭───────────────────────╮\033[0m")
                print("\033[1;36m│\033[0;94m       Menu Admin      \033[1;36m│\033[0m")
                print("\033[1;36m├───────────────────────┤\033[0m")
                print("\033[92m│ 1. Daftar Perusahaan  │\033[0m")
                print("\033[92m│ 2. Daftar Project     │\033[0m")
                print("\033[92m│ 3. Daftar Freelancer  │\033[0m")
                print("\033[92m│ 4. Daftar Admin       │\033[0m")
                print("\033[92m│ 5. Daftar Leader Pro  │\033[0m")
                print("\033[92m│ 6. Daftar Recruiter   │\033[0m")
                print("\033[92m│ 7. Exit               │\033[0m")
                print("\033[1;36m╰───────────────────────╯\033[0m")

                choice = input("\033[3;32mEnter your choice: \033[0m")

                if choice == "1":
                    print("Loading...")
                    self.loading_animation()
                    self.sub_menu("perusahaan")
                elif choice == "2":
                    print("Loading...")
                    self.loading_animation()
                    self.sub_menu("project")
                elif choice == "3":
                    print("Loading...")
                    self.loading_animation()
                    self.sub_menu("freelancer")
                elif choice == "4":
                    print("Loading...")
                    self.loading_animation()
                    self.sub_menu("admin_project")
                elif choice == "5":
                    print("Loading...")
                    self.loading_animation()
                    self.sub_menu("leader_project")
                elif choice == "6":
                    print("Loading...")
                    self.sub_menu("recruiter")
                elif choice == "7":
                    self.loading_animation()
                    print("Logging out...")
                    break
                else:
                    print(Fore.RED + "Invalid choice. Please enter a valid option.")
            except ValueError as ve:
                print(Fore.RED + f"Invalid input: {ve}")
            except KeyError as ke:
                print(Fore.RED + f"Invalid column name: {ke}")
            except Exception as e:
                print(Fore.RED + f"An error occurred: {e}")

    # Sub menu admin
    def sub_menu(self, table):
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
                    data = {}
                    for column in self.model_i.get_columns(table):
                        value = input(f"Enter value for {column}: ")
                        data[column] = value
                    self.model_i.create_record(table, data)
                elif choice == "2":
                    self.model_i.read_records(table)
                elif choice == "3":
                    record_id = input("Enter record ID to update: ")
                    data = {}
                    for column in self.model_i.get_columns(table):
                        value = input(f"Enter new value for {column}: ")
                        data[column] = value
                    self.model_i.update_record(table, record_id, data)
                elif choice == "4":
                    record_id = input("Enter record ID to delete: ")
                    self.model_i.delete_record(table, record_id)
                elif choice == "5":
                    print("Loading...")
                    self.loading_animation()
                    return
                elif choice == "6":
                    self.loading_animation()
                    print(f"{random.choice(colors)}")
                    print(
                        f"{random.choice(colors)} Thank you for using our app! {random.choice(goodbyes)}"
                    )
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
