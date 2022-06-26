buah = [["Apel",  30000], ["Jeruk", 10000], ["Mangga", 20000],["Anggur", 25000], ["Jambu", 5000]]

def daftar_buah() :
  print("No| Nama Buah | Harga ")
  i = 1
  for item in buah:
    print(str(i)+ " |" + item[0] + "     |" +str(item[1]))
    i += 1
  return
daftar_buah()

jawaban = " "
catetan_pilihan = [ ]

while jawaban != "selesai":
  jawaban = input("Ketik pilihan anda (tulis selesai jika sudah) : ")
  if jawaban != "selesai":
    catetan_pilihan.append(int(jawaban)-1)

no = 1
print("Pesanan Anda : ")
print("No| Nama Buah | Harga ")
i = 1
for item in buah:
    print(str(i)+ " |" + item[0] + "     |" +str(item[1]))
    i += 1
total = 0

for pilihan in catetan_pilihan:
  print(buah[pilihan][0] + "Harga " +str(buah[pilihan][1]))
  no += 1
  total = total + buah[pilihan][1]
print("Total pesanan buah : " +str(total))
