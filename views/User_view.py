def user_menu(self):
    while True:
        print("\n\033[1;36m╭───────────────────────╮\033[0m")
        print("\033[1;36m│\033[0;94m       Menu User       \033[1;36m│\033[0m")
        print("\033[1;36m├───────────────────────┤\033[0m")
        print("\033[92m│ 1. Profil             │\033[0m")
        print("\033[92m│ 2. Daftar Project     │\033[0m")
        print("\033[92m│ 3. Registrasi Project │\033[0m")
        print("\033[92m│ 4. Keluar             │\033[0m")
        print("\033[1;36m╰───────────────────────╯\033[0m")

        choice = input("\033[3;32mEnter your choice: \033[0m")

        if choice == '1':
            # Tambahkan logika untuk opsi Profil
            print("Anda memilih opsi Profil")
        elif choice == '2':
            # Tambahkan logika untuk opsi Daftar Project
            print("Anda memilih opsi Daftar Project")
        elif choice == '3':
            # Tambahkan logika untuk opsi Registrasi Project
            print("Anda memilih opsi Registrasi Project")
        elif choice == '4':
            # Tambahkan logika untuk opsi Keluar
            print("Anda memilih opsi Keluar")
            break  # Keluar dari loop dan fungsi user_menu
        else:
            print("\033[91mInvalid choice! Please enter a valid option.\033[0m")
