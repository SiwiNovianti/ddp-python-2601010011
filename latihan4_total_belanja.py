#pengguna memasukkan nama barang, harga satuan, dan jumlah barang
nama_barang, harga_satuan, jumlah_barang = input("Masukkan nama barang, harga satuan, dan jumlah barang (pisahkan dengan koma): ").split(",")

#mengubah tipe data input menjadi string dan integer
nama_barang = str(nama_barang)
harga_satuan = int(harga_satuan)
jumlah_barang = int(jumlah_barang)

#menghitung subtotal, PPN, dan total bayar
Subtotal = harga_satuan * jumlah_barang
PPN = 0.11 * Subtotal
Total_bayar = Subtotal + PPN

print(f"Subtotal belanja {nama_barang} adalah: Rp {Subtotal}, PPN yang dikenakan adalah: Rp {PPN}, Total bayar yang harus dibayarkan adalah: Rp {Total_bayar}")

