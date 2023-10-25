# Data list dari Kegiatan 1
data = ["3 minggu 3 hari 7 jam 21 menit", "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]

# Filter untuk memisahkan nilai float, int, dan string
filtered_data = [
    [val for val in item.split() if val.isdigit()] for item in data
]

# Map untuk memetakan nilai int menjadi satuan, puluhan, dan ratusan
mapped_data = [
    {
        'ratusan': int(val[0][0]),
        'puluhan': int(val[1][0]),
        'satuan': int(val[2]),
    }
    for val in filtered_data
]

# Menampilkan hasil
for item in mapped_data:
    if all(isinstance(value, int) for value in item.values()):
        print("Data Int:")
        print(item)
    elif all(isinstance(value, float) for value in item.values()):
        print("Data Float", item)
    elif all(isinstance(value, str) for value in item.values()):
        print("Data String", [val for val in item.values()])