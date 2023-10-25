data = ["3 minggu 3 hari 7 jam 21 menit", "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]

# Fungsi untuk mengambil hanya nilai integer dari setiap elemen data
def get_integers(text):
    return list(filter(str.isdigit, text.split()))

# Menggunakan fungsi filter untuk mengambil hanya nilai integer
filtered_data = list(map(get_integers, data))

# Mencetak hasil
for item in filtered_data:
    print(item)
