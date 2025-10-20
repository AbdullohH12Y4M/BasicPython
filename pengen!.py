print("1. Tipe Data dan Variabel")
int=12
str="23"
float=0.6

print(int,"  ",type(int))
print(str,"  ",type(str))
print(float,"  ",type(float))
print('............................................')
soal1 = [12,"23",0.6]
for i in range(len(soal1)):
    print(soal1[i] ,"  ",type(soal1[i]))
    if i==(len(soal1)-1):
        print("Ini adalah akhir dari perulangan LIST")
        print()
        print()
        break
print("2. List dan Manipulasi")
list= ["Beras","Minyak","Telur"]
list.append("Gula")
list.append("Kopi")
for i in range(len(list)):
    print(list[i])
    if i==(len(list)-1):
        print("Ini adalah akhir dari perulangan LIST")
        print()
        print()
        break
print("3. Dictionary")
mokleter = {
    "nama": "Hisyam",
    "kelas": "RPL 1",
    "expertise": "Fullstack Developer"
}
print(mokleter["nama"])
print(mokleter["kelas"])
print(mokleter["expertise"])
mokleter["umur"]=17
print("setelah ditambahkan umur"+" : ",mokleter["umur"])
del mokleter["kelas"]
print("setelah dihapus kelas : ",mokleter)
for k, v in mokleter.items():
    print(k, ":", v)

print()
print()
print()

print("4. Percabangan")
b = int
p = int
t= int
def volumeBalok(b, p, t):
    return b * p * t

print("Menghitung volume balok")

b = (input("Masukkan lebar balok : "))
p = (input("Masukkan panjang balok : "))
t = (input("Masukkan tinggi balok : "))

v = volumeBalok(b, p, t)
print("Hasilnya adalah :", v)