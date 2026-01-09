class View:
    def tampilkan(self, data):
        print("\nHASIL DATA")
        print("---------------------------")
        print("Nama\tNilai\tStatus")
        print("---------------------------")
        print(f"{data.nama}\t{data.nilai}\t{data.status}")
        print("---------------------------")