#index   0(-4)    1(-3)   2(-2)    3(-1)
nama = ["tiara", "amrina", "ratin","noer"]
dosen = ["edy","jarir","iman","fuad","indri"]

# mengambil data dari list
data_pertama = nama [-2]
print(f"data terakhir : {data_pertama}")

# mengambil data terakhir
data_terakhir = nama [-1]
print(f"data terakhir : {data_terakhir}")

# menambahkan data
# nama.insert(posisi,item)
nama.insert(1,"dika")
print(f"data setelah ditambah: {nama}")
 
# menambahkan data paling akhir
# nama.insert(-1,"zulfikar")
nama.insert(1,"dika")
print(f"data setelah ditambah diakhir: {nama}")

# menggabungkan list
nama.extend(dosen)
print(f"data list gabung: {nama}")

# menggabungkan nama dosen ditengah2
nama[2:2]=dosen
print(f"data list gabung dosen ditengah: \n{nama}")

# merubah data
nama[0] = "up to you"
print(f"data setelah diedit: {nama}")

# menghapus data
nama.remove("iman")
print(f"data setelah dihapus: {nama}")

# menghapus data paling akhir
nama.pop()
print(f"data paling akhir dihapus: \n{nama}")

