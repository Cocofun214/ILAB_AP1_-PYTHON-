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