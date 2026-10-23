#memasukkan suhu dalam Celsius
Celsius = float(input("Masukkan suhu dalam Celsius: "))

#menghitung konversi suhu ke Fahrenheit dan Kelvin
Fahrenheit = (Celsius * 9/5) + 32
print(f"Suhu dalam Fahrenheit adalah: {Fahrenheit} °F")

#menghitung konversi suhu ke Kelvin
Kelvin = Celsius + 273.15

#menampilkan hasil konversi suhu ke Kelvin
print(f"Suhu dalam Kelvin adalah: {Kelvin} K")