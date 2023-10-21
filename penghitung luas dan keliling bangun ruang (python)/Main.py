# nama = input("Nama :")
# alamat = input("Alamat :")
# kelas = input("Kelas :")

# print("<===Biodataku===>")
# print("Nama = "+ nama)
# print("Alamat = "+ alamat)
# print("Kelas = "+ kelas)

while True:

    print("Selamat datang di program sederhana saya")
    print("Pilih program yang ingin di jalankan:")
    print("0. Keluar dari program")
    print("1. Akar kuadrat")
    print("2. Luas dan keliling lingkaran")
    print("3. Luas belah ketupat")
    print("4. Keliling belah ketupat")
    print("5. Volume Kubus")
    print("6. Volume Prisma segi Empat")
    pilihan = str(input("pilih program yang ingin dijalankan (masukkan no program): "))

    if pilihan == "0":
        print("keluar dari program")
        break

    elif pilihan == "1":
        import math
        angka = float(input("Masukkan sebuah angka: "))
        akar_kuadrat = math.sqrt(angka)
        print(f"Akar kuadrat dari {angka} adalah {akar_kuadrat}")

    elif pilihan == "2":
        jari_jari = float(input("Masukkan panjang jari-jari lingkaran: "))
        luas = round(math.pi * (jari_jari ** 2))
        keliling = round(2 * math.pi * (jari_jari))
        print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas}")
        print(f"Keliling lingkaran dengan jari-jari {jari_jari} adalah {keliling}")

    elif pilihan == "3":
        d1 = float(input("Masukkan panjang diagonal (d1): "))
        d2 = float(input("Masukkan panjang diagonal (d2): "))
        # Hitung Luas dan Keliling Belah Ketupat
        Luas = round( 1/2 * d1 * d2)
        print(f"Luas belah ketupat dengan panjang diagonal 1 (d1) {d1} dan diagonal 2 (d2) {d2} adalah {Luas}")

    elif pilihan == "4":
        sisi = float(input("Masukkan panjang sisi: "))
        keliling = round( 4 * sisi)
        print(f"Keliling belah ketupat dengan panjang {sisi} adalah {keliling}")

    elif pilihan == "5":
        sisi = (float(input("Masukkan panjang sisi: ")))
        volume = round(sisi ** 3)
        print(f"Volume kubus dengan panjang sisi {sisi} adalah {volume}")
        
    elif pilihan == "6":
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        tinggi = float(input("Masukkan tinggi: "))
        volume = round((panjang * lebar) * tinggi)
        print(f"Volume kubus dengan panjang panjang {panjang}, lebar {lebar}, tinggi {tinggi} adalah {volume}")
    
    else :
        print("Masukkan input, sesuai dengan no program yang ada")
    print("<=================================>")

