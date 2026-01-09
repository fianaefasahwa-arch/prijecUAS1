from data import Data
from process import Process
from view import View

try:
    nama = input("Masukkan Nama  : ")
    nilai = int(input("Masukkan Nilai : "))

    if nilai < 0 or nilai > 100:
        raise ValueError

    data = Data(nama, nilai)

    proses = Process()
    proses.tentukan_status(data)

    view = View()
    view.tampilkan(data)

except ValueError:
    print("Input salah! Nilai harus 0 - 100")