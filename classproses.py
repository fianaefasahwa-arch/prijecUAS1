class Process:
    def tentukan_status(self, data):
        if data.nilai >= 75:
            data.status = "LULUS"
        else:
            data.status = "TIDAK LULUS"