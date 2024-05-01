# Platfrom Pekerjaan Fleksibel untuk Pertumbuhan Ekonomi (EcoFusion)
--------------------------------------------------------------------------------------------
## Deskripsi Program
> Ecofusion adalah platfrom freelance yang menghubungkan para freelance dengan 
project-project yang relevan dengan keahlian mereka. Freelance akan memilih project 
dan berkesempatan untuk direktur oleh mitra dari proyek tersebut. Dengan ini dapat membantu 
pertumbuhan ekonomi berkelanjutan. Program ini membantu admin project untuk mengelola pendaftaran project dan memudahkan freelancer untuk memilih project, melakukan project, serta membantu melakukan monitoring terhadap freelancer untuk mendapatkan kontrak dari para recruiter. Memudahkan para freelancer untuk mendapatkan gaji sebagai freelancer dan mendapatkan pekerjaan disebuah perusahaan jika project yang mereka kerjakan diminati oleh perusahaan terkait. Dengan begitu, program ini diharapkan dapat mengurangi para pengangguran yang ada agar mendapatkan pekerjaan yang lebih layak dan membantu perekonomian di zaman sekarang.

> Program ini dibuat dengan menggunakan bahasa pemrograman Python dan mengimplementasikan struktur data Linked List, menggunakan CRUD, dan melakukan sorting serta searching dari data yang ada. Platform Pekerjaan Fleksibel ini hanya menggunakan sebuah database, yaitu database mysql  yang digunakan untuk menyimpan data dari admin projeect, project, perusahaan, freelancer, recruiter, dan kontrak.
-----------------------------------------------------------------------------------------------

## Struktur Project
### Flowchart
- Login dan registrasi
  ![fc ecofusion-Page-1 drawio (2)](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/37772191-f06c-4fe2-b755-65caa7073e89)

- Menu admin
  ![fc ecofusion-Page-4 drawio (1)](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/7767a163-037f-4ee7-8c0a-c658f3c7ca27)
  
  ![fc ecofusion-Page-5 drawio](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/d7c35be3-a90a-427c-a01e-1e4e5570d962)

- Menu User
  ![fc ecofusion-Halaman-2 drawio (2)](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/ef097f63-e0a9-4e36-9e3b-e3b5409ad8e6)

- Menu Recruiter
  ![fc ecofusion-Page-3 drawio](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/5f5dca77-4ae5-4b3b-9ceb-0efd3dcc51a0)

### MVC
> 1. Folder Controller, berisi file-file controller yang akan mengatur alur program serta mengambil data dari model dan menampilkan ke view.                           
> - File Controller Account, sebagai file controller yang berisi logika untuk manajemen akun admin, user (freelancer), dan recruiter untuk mengatur registrasi, login, dan menampilkan profil.
> - File Controller Linked List, sebagai file controller yang berisi logika untuk manajemen data ruang kelas dalam bentuk linked list, dimana data dalam linked list diambil dari database.
> - File Controller User, sebagai file controller yang berisi logika untuk manajemen data user (freelancer) mulai dari menampilkan data profil user (freelancer), menampilkan project, melakukan sorting project, dan searching project.

> 2. Folder Model, berisi file-file model yang berisi fungsi-fungsi untuk mengakses database dan memproses data.
> - File Database, sebagai file yang berisi class untuk menghubungkan python dan database.
> - File model, sebagai file yang berisi definisi class abstractmodel yang digunakan untuk merepresentasikan sebuah node pada struktur data Linked List dan melakukan CRUD.

> 3. Folder View, berisi file-file view yang berisi tampilan antarmuka aplikasi yang akan dilihat oleh pengguna.
> - File admin, sebagai halaman untuk menampilkan informasi, melakukan pemdaftaran dari setiap entitas yang ada, dan melakukan CRUD dari setiap entitas yang bisa diatur oleh admin
> - File login, sebagai halaman untuk menampilkan informasi dan melakukan login untuk pengguna, admin, dan recruiter.
> - File Recruiter, sebagai halaman untuk menampilkan informasi dan melakukan CRUD untuk entitas kontrak yang hanya dapat diatur oleh recruiter.
> - File User, sebagai halaman untuk menampilkan informasi profil user(freelancer), lihat project, dan melakukan pendaftaran project.

> 4. File main, sebagai file utama yang berfungsi untuk menjalankan program.
---------------------------------------------------------------------------------

## Fitur
Pada program ini terdapat library yang digunakan, diantaranya adalah PrettyTable, Datetime, time, PyMongo, os dan random. 
>  1. Modul os dapat digunakan untuk berinteraksi dengan sistem operasi dan melakukan operasi pada file dan folder.
>  2. Modul random pada adalah modul yang menyediakan fungsi-fungsi untuk menghasilkan bilangan acak.
>  3. Modul time adalah modul yang menyediakan fungsi-fungsi untuk mengelola waktu dan tanggal.
>  4. Modul sys adalah modul untuk memberi akses ke berbagai variabel dan fungsi yang terkait dengan interpretasi Python itu sendiri.
>  5. Modul colorama adalah modul untuk mempermudah penulisan teks berwarna pada konsol atau terminal Python. Fore digunakan untuk mengubah warna teks, sementara Style digunakan untuk mengatur gaya teks seperti cetak tebal, miring, atau normal.
>  6. Modul mysql.connector adalah modul untuk menyediakan fungsi-fungsi untuk menjalankan kueri SQL, memanipulasi data, dan mengelola koneksi ke server MySQL.
>  7. Modul pwinput adalah modul untuk menerima input password tanpa menampilkan karakter yang dimasukkan ke layar, sehingga meningkatkan keamanan saat memasukkan kata sandi.
 
Beberapa fitur yang terdapat pada program ini, yaitu :
- User (Freelancer)
> 1. Melihat profil : User dapat melihat profil yang berisi data diri seperti ID Freelancer, nama, no hp, jenis kelamin, email, alamt
> 2. Melihat Bidang Project : User dapat melihat bidang project yang sesuai dengan yang diminati oleh para freelancer dan akan ditampilkan project-project yang sesuai dengan bidang tersebut.
> 3. Melakukan searching project : User dapat melakukan pencarian dari project dengan beberapa kata kunci.
> 4. Melakukan sorting project: User dapat melakukan pemilahan dari project berdasarkan bidang
> 5. Pendaftaran project: Setelah user mendapatkan project yang sesuai, use dapat melakukan pendaftaran project dan melakukan project tersebut.

- Admin Project
> 1. Membuat dan mengupdate peminjaman : Staff dapat menambahkan daftar kelas dan mengupdate status kelas yang digunakan.
> 2. Konfirmasi Peminjaman : Staff dapat melakukan konfirmasi peminjaman yang telah dilakukan oleh mahasiswa. 
> 3. Mencetak bukti peminjaman : Setelah Staff menambahkan daftar kelas yang akan digunakan maka dapat mencetak bukti peminjaman sebagai bukti tanda kelas digunakan sudah terkonfirmasi oleh staff.
> 4. Mencari NIM : Staff juga dapat mencari NIM Mahasiswa yang mengkonfirmasi peminjaman ruang kelas.
> 5. Menghapus daftar peminjaman : Staff dapat menghapus daftar peminjaman.
> 6. Melihat profil : Staff dapat  melihat profil yang berisi data diri seperti  NIP, Nama, Jenis Kelamin, dan Jabatan.

- Recruiter
> 1. Create kontrak: Recruiter dapat membuat data kontrak kerja terbaru untuk freelancer.
> 2. Read Kontrak: Recruiter dapaat melihat daftar kontrak yang sudah recruiter buat.
> 3. Update Kontrak: Recruiter dapat memperbarui informasi kontrak yang sudah recruiter buat sebelumnya.
> 4. Delete Kontrak: Recruiter dapat menghapus kontrak yang sudah recruiter buat.
--------------------------------------------------------------------------------------------

## Fungsionalitas
>  1. Registrasi User. Para Freelancer dapat melakukan pendaftaran untuk dapat masuk ke dalam platfrom pekerjaan fleksibel dengan mengisi formulir pendaftaran. User harus memberikan informasi pribadi seperti username, ID Freelancer,email, password, no hp, alamat, jenis kelamin.
>  2. Login dan Logout (Exit). User dapat melakukan login ke dalam sistem dengan menggunakan email dan password mereka. User juga dapat keluar dari program dengan melalui pilihan Exit.
>  3. User dapat melihat profil diri sendiri, melihat project sesuai dengan bidangnya masing-masing (terdapat sorting berdasarkan bidang), melakukan pendaftaran terhadap project yang diminati, mencari project berdasarkan gaji dan rentang waktu.
>  4. CRUD admin. Admin dapat melakukan penambahan data baru, melihat data, menghapus data, dan mengupdate data mulai dari data perusahaan,project,freelancer,adminproject,leader project, dan recruiter. Namun, admin tidak dapat melakukan perubahan pada data recruiter.
>  5. CRUD Recruiter. Recruiter dapat melakukan perubahan data kontrak mulai dari menambah data, menghapus data, melihat data, dan terakhir mengupdate data yang sudah ada sebelumnya. Selain itu recruiter juga dapat melihat project agar dapat memisahkan mana yang dapat pekerjaan diperusahaan terkait dan mana yang hanya mendapatkan gaji sebatas freelancer saja.
-------------------------------------------------------------------------------------------------

## Cara Penggunaan

 - Login dan registrasi freelancer: Freelancer harus melakukan login terlebih dahulu sebelum dapat melakukan pendaftaran project dan mengerjakan project. Jika freelancer belum terdaftar, maka ia dapat melakukan registrasi terlebih dahulu.
> Registrasi User
> ![image](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/93fcc725-1561-4ec2-9caa-1e23e1d66e34)

> Login User
>![image](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/f82eb46e-5e28-4e45-8dec-f452630ce8e2)

 - Login admin project dan recruiter: Recruiter dan admin project harus melakukan login agar dapat melakukan pekerjaannya. Admin project dapat mengatur data mulai dari data perusahaan hingga data recruiter kecuali kontrak. Recruiter dapat mengatur data kontrak untuk seorang freelancer yang diterima kerja di perusahaan terkait.
> ![image](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/1f644a42-e4a5-4f01-8089-fd82cc9caeef)
![image](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/3e39d137-b656-4567-bb10-f22fca9cb758)

### Admin
- CRUD Admin. Admin dapat melakukan operasi Create, Read, Update, dan Delete pada aplikasi ecofusion ini.
> - Menu utama admin. Disini admin dapat memilih data mana yang akan dilakukan perubahan menggunakan operasi CRUD.
![image](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/5c60771d-050b-4e45-b567-1f00c5dc6864)

- CRUD menu sub admin. Setelah admin memilih data mana yang akan dilakukan perubahan data dengan CRUD. Dimenu sub admin inilah admin dapat melakukan perubahan data sesuai dengan yang di pilih di menu utama.
> Saya memilih akan melakukan perubahan pada data project. Saya dapat melakukan penambahan data project, melihat project, mengupdate project, dan menghapus project.
![image](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/045b16b4-8647-46fa-8c98-4ea5d0591d66)

- Menambah data project. Pada menu ini admin dapat menambahkan project apa yang inigin ditambahkan di dalam aplikasi ini. Jadi lebih banyak lagi freelancer yang memiliki kemampuan dengan bidang yang sesuai dengan yang mereka minati.
![image](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/7136aa28-2e97-43c0-a158-10d9f23f4962)

- Melihat data project. Admin dapat melihat semua daftar project yang telah dilakukan dengan detail ID Project, Judul, Deskripsi, Status, Bidang, Id admin project, rentang waktu, dan nama freelancer. Sedangkan mahasiswa hanya dapat melihat pengajuan project dengan melihat detail yang sama namun hanya dapat melihat perbidang tidak keseluruhan bidang.
> admin project
![image](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/74871f36-5d03-478a-9b1d-b3125fca60b0)
> User atau freelancer
![image](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/212f7468-868b-4f44-975f-d30d54565ea2)

- Mengupdate data project. Admin dapat melakukan update pada pengajuan project yang dilakukan oleh user. Ataupun di data yang telah dibuat oleh admin itu sendiri dan dapat mengganti keseluruhan data.
>Awal data 141 beberapa kolom masi kosong
![image](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/fb7aadaa-9c5a-46f6-a4f8-d149aed9f4cb)
Setelah di update dan data berhasil di update.
![image](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/6d2d1338-5447-480b-a257-23450cc2f2e5)
![image](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/394dbffc-ffd8-43c1-bb9a-a500143a8541)

- Menghapus data project. Admin dapat melakukan penghapusan terhadap data jika data tersebut tidak diperlukan> Penghapusan dilakukan berdaasarkan ID Project dari data tersebut.
>![image](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/8a62cb38-81ef-40f9-bbfc-ced1afac1ca3)

### User/Freelancer
- Profil dari freelancer atau user. User dapat melihat data profilnya. Pada akun user, user dapat melihat nama, alamat, email, jenis kelamin, dan no.hp.
> ![image](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/ea517a10-d188-4d69-9ea9-2cceac12804a)

- Lihat project. Pada fitur inilah dilakukan sorting berdasarkan bidang jadi semua informasi project yang dalam bidang yang sama akan disatukan dan ditampilkan kepada user.
> ![image](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/ce088ed0-eced-4224-9d84-f3b7fa3f47e9)

- Daftar project. Disini freelancer atau user dapat melakukan project berdasarkan kemampuan masing-masing dan dapat memilihnya dengan memasukkan ID Project yang ingin didaftarkan.
> ![image](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/87bcae12-afc3-4457-92ce-57825271cee4)

- Cari project. Fitur searching ada pada menu ini. Menu ini user dapat mencari project dengan memilih dengan mencari berdasarkan gaji atau berdasarkan rentang waktu. dengan kata kunci gaji dan rentang waktu user bisa mencari project yang sesuai dengan kebutuhan.
> ![image](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/24cb0cb1-9587-45c7-8609-fb4117dfa905)

### Recruiter
- Tambah kontrak. Recruiter dapat melakukan penambahan data kontrak dengan memasukkan data mulai dari ID kontrak, status kontrak, ID recruiter,id perusahaan, durasi kontrak, gaji, nama freelancer.
> ![image](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/cb8dcbc3-890d-4138-963e-710272649b59)
> ![image](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/669f5a7c-d41f-4a11-902a-a0cdf52e6712)

- Lihat kontrak. Pada menu ini recruiter dapat melihat seluruh data kontrak yang telah dibuat. Apakah kontrak itu aktif atau tidak aktif juga dapat terlihat oleh recruiter.
> ![image](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/545a574c-732f-49c3-a1bf-04b59699a967)

- Update Kontrak. Recruiter dapat memperbarui data yang sudah ada atau dibuat sebelumnya. Dengan memasukkan id kontrak yang ingin diubah dan memasukkan data seperti saat melakukan tambah kontrak.
> ![image](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/7cd81674-e830-4c4f-9be5-08f3599b7900)
> ![image](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/7f5741bd-435f-4d92-afa0-90eb64df044d)

- Hapus Kontrak. Recruiter dapat menghapus data yang sudah tidak diperlukan lagi. Dengan cara memasukkan ID kontrak.
> ![image](https://github.com/PA-ASD-KEL1/ecofusion/assets/144756486/fd7300d6-8f24-4286-8d8a-80ad02fe0300)




  









--------------------------------------


