#Saya Ellsya Nabella Nur'allifa 2009037 mengerjakan Latihan 4 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk 
#keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin

#untuk kelas human
class Human:
    def __init__(self, NIK, nama, jenis_kelamin): #deklarasi atribut
        self.NIK = NIK
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin

#untuk kelas sivitas akademik
class SivitasAkademik(Human):
    def __init__(self, asal_universitas, email_edu): #deklarasi atribut
        self.asal_universitas = asal_universitas
        self.email_edu = email_edu

#untuk kelas dosen extend dari kelas human dan sivitas akademik
class Dosen(Human):
    def __init__(self, NIP, nama, jenis_kelamin, fakultas, prodi, pend_terakhir, keahlian, asal_universitas, email_edu): #deklarasi atribut
        super().__init__(NIP, nama, jenis_kelamin)
        SivitasAkademik.__init__(self, asal_universitas, email_edu)
        self.NIP = NIP
        self.fakultas = fakultas
        self.prodi = prodi
        self.pend_terakhir = pend_terakhir
        self.keahlian = keahlian
        self.matakuliah = []

    def tambah_matakuliah(self, matakuliah): #deklarasi atribut baru untuk menambah mata kuliah
        self.matakuliah.append(matakuliah)

    def tampilkan_matakuliah(self): #deklarasi atribut untuk tampilkan mata kuliah
        print("Mata kuliah yang diampu:")
        for matakuliah in self.matakuliah:
            print("- " + matakuliah)

#untuk kelas mahasiswa extend dari kelas human
class Mahasiswa(Human):
    def __init__(self, NIM, nama, jenis_kelamin, fakultas, prodi): #deklarasi atribut
        super().__init__(NIM, nama, jenis_kelamin)
        self.NIM = NIM
        self.fakultas = fakultas
        self.prodi = prodi
        self.krs = []

    def tambah_krs(self, krs): #deklarasi atribut baru
        self.krs.append(krs)

    def tampilkan_krs(self): #deklarasi atribut baru
        print("KRS Mahasiswa:")
        for krs in self.krs:
            print("- " + krs)

#untuk kelas course
class Course:
    def __init__(self, nama_matakuliah): #deklarsi atribut
        self.nama_matakuliah = nama_matakuliah

#untuk kelas program studi
class ProgramStudi:
    def __init__(self, nama_prodi, kode): #deklarasi atribut
        self.nama_prodi = nama_prodi
        self.kode = kode
        self.course = []

    def tambah_course(self, course): #deklarasi atribut baru
        self.course.append(course)

    def tampilkan_course(self): #deklarasi atribut baru
        print("Course yang tersedia:")
        for course in self.course:
            print("- " + course.nama_matakuliah)
