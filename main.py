import time
import sys
def kalimat_berjalan(teks, kecepatan=0.1):
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(kecepatan)

angka = 0

while angka < 100:
    print("I LOVE YOU", angka, "%")
    angka += 1
    time.sleep(0.5)

kalimat = "I LOVE YOU SOO much"
kalimat_berjalan(kalimat, kecepatan=0.1)
