while True:
    input_1 = input("1 (atau ketik 'q' untuk keluar): ")
    if input_1.lower() == 'q':
        print("program selesai. Terima kasih!")
        break

    try:
        angka = int(input_1)
        angka2 = int(input("2: "))
    except ValueError:
        print("masukkan angka yang valid!\n")
        continue

    if angka % 2 == 0:
        print(f"angka {angka} adalah bilangan genap")
    else :
        print(f"angka {angka} adalah bilangan ganjil")
    if angka2 % 2 == 0:
        print(f"angka2 {angka2} adalah bilangan genap")
    else :
        print(f"angka2 {angka2} adalah bilangan ganjil")
print("_" * 30)
