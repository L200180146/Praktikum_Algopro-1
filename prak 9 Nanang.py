##Kegiatan 1
berkas = open("L200180157","w")
berkas.write("L200180157 \n")
berkas.write("25-07-2000 \n")
berkas.write("Nanang Dwi Prasetyo \n")
berkas.close()

##Kegiatan 2
berkas = open("L200180157","w")
berkas.write("L200180157 \n")
berkas.write("Nanang Dwi Prasetyo \n")
berkas.write("Sragen\n")
berkas.write("25-07-2000 \n")
berkas.close()

import shelve
f = open("L200180157","r")
Nim = f.readline()
Nama = f.readline()
Asal = f.readline()
Tl = f.readline()
f.close()

f = shelve.open("Nanang")
f['b'] = [Nama, Asal, Tl, Nim]
f.close()

f = shelve.open("Nanang")

print f['b'][0]
print f['b'][1]
print f['b'][2]
print f['b'][3]

##Kegiatan 3
import shelve
f = open("L200180157","r")
Nim = f.readline()
Nama = f.readline()
Asal = f.readline()
Tl = f.readline()
f.close()


f = shelve.open("Nanang")
f['b'] = [Nama, Asal, Tl, Nim]
f.close()

##Kegiatan 4
import shelve
f = shelve.open("Nanang")
print 'Nama :' , f['b'][0]
print 'Asal :' , f['b'][1]
print 'Tl   :' , f['b'][2]
print 'Nim  :' , f['b'][3]


