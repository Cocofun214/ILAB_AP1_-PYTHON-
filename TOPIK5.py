------ Prelab 5.1 -------

== 1 ==

# Program ini menuliskan teks "Bandung", "Jakarta", "Depok" masing-masing dalam satu baris ke file kota.txt
def main():
    dim = open('kota.txt', 'w')
    dim.write('Bandung\n')
    dim.write('Jakarta\n')
    dim.write('Depok')
    dim.close()
    
main()

== 2 ==

# Program ini membaca keseluruhan isi file kota.txt
def main():
    dim = open('kota.txt', 'r')
    isi_dim = dim.read()
    dim.close()
    print(isi_dim)
main()


== 3 ==

'Depok\nBekasi\nJakarta\n'

== 4 ==

# Program ini menambahkan teks 'Surabaya' dan 'Medan'
# masing-masing dalam satu baris ke file kota.txt
def main():
    dim = open('kota.txt', 'a')
    dim.write('Surabaya\n')
    dim.write('Medan')
    dim.close()
main()


== 5 ==

Program membuat file kota.txt


== 6 ==

# Program ini meminta pengguna memasukkan sebuah nama kota
# dan menambahkan nama kota yang dimasukkan tersebut ke file kota.txt
def main():
    dim = input('Masukkan nama kota: ')
    dima = open('kota.txt', 'a')
    dima.write(dim + '\n')
    dima.close()
    print('Data telah ditambahkan ke file kota.txt.')
main()


== 7 ==

# Program ini membaca file menggunakan statement with
def main():
    with open('kota.txt', 'r') as input_dim:
        d1 = input_dim.readline()
        d2 = input_dim.readline()
        d3 = input_dim.readline()
        d4 = input_dim.readline()
    d = d1.rstrip(\n)
    i = d2.rstrip(\n)
    m = d3.rstrip(\n)
    a = d4.rstrip(\n)
    print(d)
    print(i)
    print(m)
    print(a)
main()



== 8 ==

# Program ini membaca file kota.txt dan menampilkan isi file
# dengan format: Baris <n>: <isi_file_baris_ke_n>
def main():
    with open('kota.txt', 'r') as dima:
        d1 = dima.readline()
        d2 = dima.readline()
        d3 = dima.readline()
    dim1 = d1.rstrip('\n')
    dim2 = d2.rstrip('\n')
    dim3 = d3.rstrip('\n')
    print('Baris {}: {}'.format(1,dim1))
    print('Baris {}: {}'.format(2,dim2))
    print('Baris {}: {}'.format(3,dim3))
main()

 
 
 --- Prelab 5.2 ----
 

== 1 ==

# Program ini meminta pengguna memasukkan tiga buah angka float
# dan menuliskan keduanya, masing-masing dalam satu baris, 
# ke file angka.txt
def main():
    j = float(input('Masukkan sebuah angka desimal: '))
    o = float(input('Masukkan sebuah angka desimal lainnya: '))
    n = float(input('Masukkan sebuah angka desimal lainnya: '))
    k = open('angka.txt', 'w')
    k.write(str(j)+'\n')
    k.write(str(o)+'\n')
    k.write(str(n)+'\n')
    k.close()
    print('Data telah berhasil disimpan dalam file angka.txt.')
main()



== 2==

# Program ini membaca isi file angka_float.txt
# dan mengalikan angka yang terdapat dalam file tersebut
def main():
    j = open('angka_float.txt', 'r')
    o = float(j.readline())
    n = float(j.readline())
    j.close()
    
    t = o*n
    print(f'Baris 1 file angka_float.txt berisi: {o}')
    print(f'Baris 2 file angka_float.txt berisi: {n}')
    print(f'Hasil kali baris 1 dan baris 2 = {t:.2f}')
main()



----- Prelab 5.3 ------


== 1 ==

import random
def main():
    x = open('daftar_angka.txt', 'w')
    for i in range(1, 101):
        x.write(str(i) + '\n')
    x.close()
            
main()


== 2 ==

def main():
    a = 0.0
    b = 0.0
    x = open('sales.txt', 'r')
    baris = x.readline()
    while baris != '':
        a = a + float(baris)
        b = b + 1
        baris = x.readline()
        avg = a / b
    print(f'Rata-rata penjualan: {avg:,.2f}')
# Panggil fungsi main
main()


== 3 ==

def main():
    a = 0.0
    b = 0
    x = open('sales.txt', 'r')
    for baris in x:
        a = a + float(baris)
        b = b + 1
        avg = a / b
    print(f'Rata-rata penjualan: {avg:,.2f}')
main()




------------- Prelab 5.4 ------------------


== 1 == 

BandungJakartaMedanSurabaya

== 2 ==

Program menghasilkan error


== 3 ==

def main():
    angka = [234, 694, 123, 789, 923, 674, 534]
    with open('list_angka.txt', 'w') as x:
        for a in angka:
            x.write(str(a) + '\n')
main()


== 4 ==
def main():
    rata_rata = 0.0
    nilai_tertinggi = 0.0
    nilai_terendah = 0.0
    number_list = []
    with open('daftar_nilai.txt', 'r') as fp:
        number_list = [float(item) for item in fp.readlines()]
    nilai_terendah = min(number_list)
    nilai_tertinggi = max(number_list)
    rata_rata = sum(number_list) / len(number_list)
    x = "{:.2f}".format(rata_rata)
    print('Rata-rata nilai ujian: ', x)
    print('Nilai ujian tertinggi: ', nilai_tertinggi)
    print('Nilai ujian terendah: ', nilai_terendah)
main()



----------- Prelab 5.5 -------------


== 1 ==


def main():
    x = int(input('Berapa banyak record nilai mahasiswa yang ingin Anda tambahkan? '))
    with open('nilai_mahasiswa.txt', 'a') as nilai:
        for i in range(1, x +1):
            print(f'Masukkan record nilai mahasiswa ke {i}')
            nama = input('Nama: ')
            Nilai = input('Nilai: ')
            nilai.write(nama + '\n')
            nilai.write(Nilai + '\n')
            print()
main()


== 2 ==

def main():
    with open('nilai_mahasiswa.txt', 'r') as d:
        data = d.readline()
        while data !='':
            Nilai = d.readline()
            nama = data.rstrip('\n')
            nilai = Nilai.rstrip('\n')
            print(f'Nama: {nama}')
            print(f'Nilai: {nilai}')
            print()
            data = d.readline()
main()



---------- Prelab 5.6 ---------


== 1 ==

Kode ini menyebabkan ValueError.


== 2 ==

Sebuah error terjadi.


== 3 ==


def main():
    try:
        x = int(input('Masukkan sebuah angka yang akan dibagi: '))
        y = int(input('Masukkan sebuah angka pembagi: '))
        print(f'{x} dibagi dengan {y} sama dengan {x/y}')
    except ValueError:
        print('Nilai yang diinput salah.')
    except ZeroDivisionError:
        print('Tidak dapat membagi dengan nol.')
main()

 
    
== 4 ==


def main():
    data = []
    d = input('Masukkan nama file: ')
    try:
        dim = open(d, 'r')
        for i in dim:
            y = float(i)
            data.append(y)
    except FileNotFoundError:
        print('File tidak ditemukan.')
    except ValueError:
        print('Terdapat data non numerik dalam file.')
    else:
        print('Rata-rata nilai:', round(sum(data) / len(data), 2))
        print('Nilai tertinggi:', max(data))
        print('Nilai terendah:', min(data))
main()



=================== ACT 5 ===================


# Program ini membaca record nilai mahasiswa
# dari file nilai_mahasiswa.txt
def main():

    # Variabel sebagai penanda jika nama mahasiswa yang dicari ditemukan
    found = False
    
    try:
        # [1] Tuliskan statement untuk meminta nama file ke pengguna
        # Gunakan prompt: 'Masukkan nama file: '
        nama_file = input('Masukkan nama file: ')

        # [2] Tuliskan staement untuk membuka file dengan nama file yang diberikan pengguna
        # Anda dapat menggunakan statement with atau 3 langkah menggunakan file: buka, proses, tutup.
        with open(nama_file, 'r') as output_file:
        
            # [3] Tampilkan pesan: "File <nama_file> berhasil dibuka.". Tambahkan baris baru.
            print('File', nama_file, 'berhasil dibuka.\n')
            
            # [4] Tuliskan statement untuk meminta nama mahasiswa yang ingin dicari
            # Gunakan prompt: 'Masukkan nama mahasiswa yang ingin dicari: '
            nama_mahasiswa = input('Masukkan nama mahasiswa yang ingin dicari: ')

            # [5] Tuliskan statement untuk membaca baris pertama dari file (nama mahasiswa).
            output = output_file.readline()
            
            # [6] Tuliskan loop while yang mengiterasi baris-baris file
            while output != '':
            
                # [7] Tuliskan statement untuk membaca nilai mahasiswa
                nilai = output_file.readline()
                
                # [8] Tuliskan statement untuk menghilangkan baris baru pada nama mahasiswa dan nilai mahasiswa
                # Gunakan rstrip.
                output = output.rstrip('\n')
                nilai = nilai.rstrip('\n')
                
                # [9] Tuliskan struktur seleksi yang menentukan apakah nama mahasiswa cocok
                # dengan nama yang ingin dicari
                if nama_mahasiswa == output:
                
                    # [10] Jika nama_mahasiswa sama dengan nama yang ingin dicari
                    # Tampilkan Nama dan Nilai
                    print(f'Nama Mahasiswa: {output}')
                    print(f'Nilai: {nilai}')

                    # [11] Tetapkan nilai variabel penanda found dengan True
                    # Ini karena mahasiswa ditemukan
                    found = True

                # [12] Tuliskan statement membaca baris berikutnya
                output = output_file.readline()

    # [13] Tuliskan klausa except FileNotFoundError
    # Pada body klausa except ini tampilkan: File <nama_file> tidak ditemukan.
    except FileNotFoundError:
        print('File', nama_file, 'tidak ditemukan.')
        
    # [14] Tuliskan klausa else
    # Pada body klausa else tuliskan struktur seleksi jika found tidak sama dengan True
    # tampilkan pesan: "Nama <nama yang dicari> tidak ditemukan."
    except:
        print('Nama', nama_mahasiswa, 'tidak ditemukan.')
                    
# Panggil fungsi main
main()

