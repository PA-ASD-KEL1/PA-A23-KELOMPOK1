from tabulate import tabulate
from models.model import ProfileModel, ProjectModel
import math

class AbstractController:
    def __init__(self):
        self.model = None

    def display_data(self):
        raise NotImplementedError("Subclasses must implement display_data method.")

    def search_data(self):
        raise NotImplementedError("Subclasses must implement search_data method.")

    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quick_sort(left) + middle + self.quick_sort(right)

class ProfileController(AbstractController):
    def __init__(self):
        super().__init__()
        self.model = ProfileModel()

    def display_data(self):
        profiles = self.model.read_records('freelancer')  # Menggunakan metode read_records dari ProfileModel
        if profiles:
            headers = ["Nama", "Alamat", "Email", "Jenis Kelamin", "No. HP"]
            print(tabulate(profiles, headers=headers, tablefmt="fancy_grid"))
        else:
            print("Profil tidak Ditemukan.")

class ProjectController(AbstractController):
    def __init__(self):
        super().__init__()
        self.model = ProjectModel()

    def display_data(self):
        fields = ["Desain Grafis", "Event", "Fashion", "Marketing", "Teknologi", "Kesehatan", "Media"]

        print("\n\033[1;36m╭──────────────────────────╮\033[0m")
        print("\033[1;36m│\033[0;94m    Pilih Bidang Project   \033[1;36m│\033[0m")
        print("\033[1;36m├──────────────────────────┤\033[0m")
        for index, field in enumerate(fields, start=1):
            print(f"\033[92m│ {index}. {field:<24} │\033[0m")
        print("\033[1;36m│ 0. Kembali                │\033[0m")
        print("\033[1;36m╰──────────────────────────╯\033[0m")

        choice = input("\033[3;32mPilih bidang (0 untuk kembali): \033[0m")
        try:
            choice = int(choice)
            if choice == 0:
                return
            elif 1 <= choice <= len(fields):
                chosen_field = fields[choice - 1]
                projects = self.model.read_records('project')  # Menggunakan metode read_records dari ProjectModel
                filtered_projects = [proj for proj in projects if proj["Bidang"] == chosen_field]
                if filtered_projects:
                    self.display_projects_table(filtered_projects)
                else:
                    print("Tidak ada project dalam bidang ini.")
            else:
                print("\033[91mPilihan tidak valid!\033[0m")
        except ValueError:
            print("\033[91mMasukkan angka sebagai pilihan!\033[0m")

    def display_projects_table(self, projects):
        headers = ["ID Project", "Judul", "Status", "Deskripsi", "Bidang", "Gaji", "ID Admin", "Rentang Waktu"]
        project_data = [[proj["ID_Project"], proj["Judul"], proj["Status"], proj["Deskripsi"], proj["Bidang"], proj["Gaji"], proj["ID_adminproject"], proj["rentang_waktu"]] for proj in projects]
        print(tabulate(project_data, headers=headers, tablefmt="fancy_grid"))
    
    def search_data(self):
        print("\n\033[1;36m╭──────────────────────────╮\033[0m")
        print("\033[1;36m│\033[0;94m   Pilih Kriteria Pencarian  \033[1;36m│\033[0m")
        print("\033[1;36m├──────────────────────────┤\033[0m")
        print("\033[92m│ 1. Berdasarkan Gaji       │\033[0m")
        print("\033[92m│ 2. Berdasarkan Rentang Waktu │\033[0m")
        print("\033[1;36m│ 0. Kembali                │\033[0m")
        print("\033[1;36m╰──────────────────────────╯\033[0m")

        choice = input("\033[3;32mPilih kriteria (0 untuk kembali): \033[0m")
        try:
            choice = int(choice)
            if choice == 0:
                return
            elif choice == 1:
                min_salary = input("\033[3;32mMasukkan gaji minimum: \033[0m")
                max_salary = input("\033[3;32mMasukkan gaji maksimum: \033[0m")
                projects = self.model.search_by_salary(min_salary, max_salary)  # Menyesuaikan dengan metode yang tersedia di ProjectModel
                if projects:
                    sorted_projects = self.quick_sort(projects)
                    self.display_projects_table(sorted_projects)
                else:
                    print("Tidak ada project dalam rentang gaji ini.")
            elif choice == 2:
                time_range = input("\033[3;32mMasukkan rentang waktu (contoh: '1 minggu', '2 hari'): \033[0m")
                projects = self.model.search_by_time_range(time_range)  # Menyesuaikan dengan metode yang tersedia di ProjectModel
                if projects:
                    sorted_projects = self.quick_sort(projects)
                    self.display_projects_table(sorted_projects)
                else:
                    print("Tidak ada project dalam rentang waktu ini.")
            else:
                print("\033[91mPilihan tidak valid!\033[0m")
        except ValueError:
            print("\033[91mMasukkan angka sebagai pilihan!\033[0m")
