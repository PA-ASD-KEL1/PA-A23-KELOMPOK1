# Platfrom Pekerjaan Fleksibel untuk Pertumbuhan Ekonomi (EcoFusion)
--------------------------------------------------------------------------------------------
### Deskripsi Program
> Ecofusion adalah platfrom freelance yang menghubungkan para freelance dengan 
project-project yang relevan dengan keahlian mereka. Freelance akan memilih project 
dan berkesempatan untuk direktur oleh mitra dari proyek tersebut. Dengan ini dapat membantu 
pertumbuhan ekonomi berkelanjutan. Program ini membantu admin project untuk mengelola pendaftaran project dan memudahkan freelancer untuk memilih project, melakukan project, serta membantu melakukan monitoring terhadap freelancer untuk mendapatkan kontrak dari para recruiter. Memudahkan para freelancer untuk mendapatkan gaji sebagai freelancer dan mendapatkan pekerjaan disebuah perusahaan jika project yang mereka kerjakan diminati oleh perusahaan terkait. Dengan begitu, program ini diharapkan dapat mengurangi para pengangguran yang ada agar mendapatkan pekerjaan yang lebih layak dan membantu perekonomian di zaman sekarang.

> Program ini dibuat dengan menggunakan bahasa pemrograman Python dan mengimplementasikan struktur data Linked List, menggunakan CRUD, dan melakukan sorting serta searching dari data yang ada. Platform Pekerjaan Fleksibel ini hanya menggunakan sebuah database, yaitu database mysql  yang digunakan untuk menyimpan data dari admin projeect, project, perusahaan, freelancer, recruiter, dan kontrak.
-----------------------------------------------------------------------------------------------

### Struktur Project

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

### Fitur
Pada program ini terdapat library yang digunakan, diantaranya adalah PrettyTable, Datetime, time, PyMongo, os dan random.
>  1. PrettyTable merupakan library atau pustaka dalam python yang digunakan untuk membuat / mengeluarkan data dalam bentuk tabel.
>  2. Datetime adalah sebuah library atau modul yang dipanggil jika anda membutuhkan segala operasi yang berhubungan dengan waktu.
>  3. Modul time adalah modul yang menyediakan fungsi-fungsi untuk mengelola waktu dan tanggal. 
>  4. PyMongo berisi alat untuk bekerja dengan MongoDB, dan merupakan cara yang disarankan untuk bekerja dengan MongoDB dari Python.
     Untuk menjalankan PyMongo sendiri, hal yang harus dilakukan adalah mengakses MongoDB ataupun menginstall MongoDB. 
     Selanjutnya user dapat memverifikasi apakah instalasi telah selesai dengan sukses, kita akan terhubung ke server database MongoDB menggunakan alat mongo dan melihat status koneksi melalui MongoDB. 
>  5. Modul os dapat digunakan untuk berinteraksi dengan sistem operasi dan melakukan operasi pada file dan folder.
>  6. Modul random pada adalah modul yang menyediakan fungsi-fungsi untuk menghasilkan bilangan acak. 

Beberapa fitur yang terdapat pada program ini, yaitu :
- User 
> 1. Pemilihan ruangan : User dapat melihat daftar kelas yang dapat dilakukan peminjaman.
> 2. Membuat peminjaman : User dapat membuat peminjaman kelas yang akan digunakan.
> 3. Mencari ruangan : User dapat mencari kelas untuk mengecek apakah kelas tersebut digunakan atau tidak, apabila digunakan maka akan memunculkan informasi daftar kelas yang digunakan.
> 4. Melihat profil : User dapat melihat profil yang berisi data diri seperti NIM, Nama, Program Studi dan Jenis Kelamin.

- Staff
> 1. Membuat dan mengupdate peminjaman : Staff dapat menambahkan daftar kelas dan mengupdate status kelas yang digunakan.
> 2. Konfirmasi Peminjaman : Staff dapat melakukan konfirmasi peminjaman yang telah dilakukan oleh mahasiswa. 
> 3. Mencetak bukti peminjaman : Setelah Staff menambahkan daftar kelas yang akan digunakan maka dapat mencetak bukti peminjaman sebagai bukti tanda kelas digunakan sudah terkonfirmasi oleh staff.
> 4. Mencari NIM : Staff juga dapat mencari NIM Mahasiswa yang mengkonfirmasi peminjaman ruang kelas.
> 5. Menghapus daftar peminjaman : Staff dapat menghapus daftar peminjaman.
> 6. Melihat profil : Staff dapat  melihat profil yang berisi data diri seperti  NIP, Nama, Jenis Kelamin, dan Jabatan.
--------------------------------------


