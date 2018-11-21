d = {
    "NIM" : "L200180157",
    "Nama" : "Nanang dwi prasetyo",
    "Alamat" : "sragen",
    "Kode Pos" : "57778",
    "No HP" : "085338505261",
    "Jurusan" : "Informatika",
    "Kelas Praktikum" : "Kelas c",
    }

def data1():
    print "NIM: " + d["NIM"]
    return;
def data2():
    print "Nama: " + d["Nama"]
    return;
def data3():
    print "Alamat: " + d["Alamat"]
    return;
def data4():
    print "Kode Pos: " + d["Kode Pos"]
    return;
def data5():
    print "No HP: " + d["No HP"]
    return;
def data6():
    print "Jurusan: " + d["Jurusan"]
    return;
def data7():
    print "Kelas Praktikum: " + d["Kelas Praktikum"]
    return;

print ("""Pilihan yang tersedia:
               b menampilkan bantuan ini
               a menampilkan NIM
               c menampilkan Nama
               d menampilkan Alamat
               e menampilkan Kode Pos
               f menampilkan No HP
               g menampilkan Jurusan
               h meanmpilkan Kelas Praktikum""")
x = "s"
while x != "k":
    x = str(raw_input("Masukan Pilihan: "))
    if x == "b":
        print ("""Pilihan yang tersedia:
               b menampilkan bantuan ini
               a menampilkan NIM
               c menampilkan Nama
               d menampilkan Alamat
               e menampilkan Kode Pos
               f menampilkan No HP
               g menampilkan Jurusan
               h meanmpilkan Kelas Praktikum""")
    elif x == "a":
        print("Pilihan saudara: a")
        data1()
    elif x == "c":
        print("Pilihan saudara: c")
        data2()
    elif x == "d":
        print("Pilihan saudara: d")
        data3()
    elif x == "e":
        print("Pilihan saudara: e")
        data4()
    elif x == "f":
        print("Pilihan saudara: f")
        data5()
    elif x == "g":
        print("Pilihan saudara: g")
        data6()
    elif x == "h":
        print("Pilihan saudara: h")
        data7()
    elif x == "k":
        print("Keluar")
    else:
        print("Pilihan tidak dikenali")
