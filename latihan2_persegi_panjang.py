#masukkan panjang dan lebar persegi panjang
panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))

#menghitung luas dan keliling persegi panjang dan menampilkan hasilnya
Luas = panjang * lebar
print(f"Luas persegi panjang adalah: {Luas} m2")

#menghitung keliling persegi panjang dan menampilkan hasilnya
Keliling = 2 * (panjang + lebar)
print(f"Keliling persegi panjang adalah: {Keliling} m")


# TRACE TABLE (TABEL PENELUSURAN)
# Contoh Simulasi Nilai Input: panjang = 5.0, lebar = 3.0

# | Baris | Kode / Instruksi                | panjang | lebar | Luas  | Keliling | Output / Tampilan di Layar        |
# |-------|---------------------------------|---------|-------|-------|----------|-----------------------------------|
# | 1     | panjang = float(input(...))     | 5.0     | -     | -     | -        | Masukkan panjang persegi panjang: |
# | 2     | lebar = float(input(...))       | 5.0     | 3.0   | -     | -        | Masukkan lebar persegi panjang:   |
# | 4     | Luas = panjang * lebar          | 5.0     | 3.0   | 15.0  | -        | -                                 |
# | 5     | print(...) (Luas)               | 5.0     | 3.0   | 15.0  | -        | Luas persegi panjang adalah: 15.0 m2|
# | 7     | Keliling = 2 * (panjang + lebar)| 5.0     | 3.0   | 15.0  | 16.0     | -                                 |
# | 8     | print(...) (Keliling)           | 5.0     | 3.0   | 15.0  | 16.0     | Keliling persegi panjang adalah: 16.0 m|
