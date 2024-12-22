import time
import matplotlib.pyplot as plt
import pandas as pd

# Data dummy: Jumlah siswa di setiap kecamatan Kabupaten Banyumas
data = [
    {"kecamatan": "Ajibarang", "jumlah_siswa": 1200},
    {"kecamatan": "Banyumas", "jumlah_siswa": 1500},
    {"kecamatan": "Cilongok", "jumlah_siswa": 1100},
    {"kecamatan": "Gumelar", "jumlah_siswa": 900},
    {"kecamatan": "Jatilawang", "jumlah_siswa": 1300},
    {"kecamatan": "Kalibagor", "jumlah_siswa": 800},
    {"kecamatan": "Karanglewas", "jumlah_siswa": 1000},
    {"kecamatan": "Kebasen", "jumlah_siswa": 850},
    {"kecamatan": "Kedungbanteng", "jumlah_siswa": 950},
    {"kecamatan": "Kembaran", "jumlah_siswa": 1250},
]

def recursive_search(data, kecamatan, index=0):
    if index >= len(data):
        return None, index
    if data[index]["kecamatan"] == kecamatan:
        return data[index], index
    return recursive_search(data, kecamatan, index + 1)

def iterative_search(data, kecamatan):
    for i, entry in enumerate(data):
        if entry["kecamatan"] == kecamatan:
            return entry, i
    return None, -1

# Fungsi untuk input nama kecamatan dan melakukan pencarian
def search_kecamatan(data, kecamatan):
    print(f"Mencari data untuk kecamatan: {kecamatan}")

    # Pencarian rekursif
    start = time.time()
    recursive_result, recursive_index = recursive_search(data, kecamatan)
    recursive_time = time.time() - start

    if recursive_result:
        print(f"[Rekursif] Ditemukan: {recursive_result['kecamatan']} dengan jumlah siswa {recursive_result['jumlah_siswa']} (Index: {recursive_index})")
    else:
        print("[Rekursif] Data tidak ditemukan.")

    # Pencarian iteratif
    start = time.time()
    iterative_result, iterative_index = iterative_search(data, kecamatan)
    iterative_time = time.time() - start

    if iterative_result:
        print(f"[Iteratif] Ditemukan: {iterative_result['kecamatan']} dengan jumlah siswa {iterative_result['jumlah_siswa']} (Index: {iterative_index})")
    else:
        print("[Iteratif] Data tidak ditemukan.")

    # Tampilkan hasil dalam tabel
    results = pd.DataFrame({
        "Target": [kecamatan],
        "Recursive Time (s)": [recursive_time],
        "Iterative Time (s)": [iterative_time],
        "Recursive Index": [recursive_index],
        "Iterative Index": [iterative_index]
    })
    print("\nHasil Pencarian:")
    print(results.to_markdown(index=False))

# Ukur waktu eksekusi untuk rekursif dan iteratif
input_sizes = [5, 10, 20, 50, 100]  # Jumlah kecamatan untuk pengujian
recursive_times = []
iterative_times = []

# Perluas data dummy untuk pengujian skala besar
data_extended = data * 10

for n in input_sizes:
    test_data = data_extended[:n]
    kecamatan_target = "Kembaran"

    # Rekursif
    start = time.time()
    recursive_search(test_data, kecamatan_target)
    end = time.time()
    recursive_times.append(end - start)

    # Iteratif
    start = time.time()
    iterative_search(test_data, kecamatan_target)
    end = time.time()
    iterative_times.append(end - start)

# Tabel hasil dalam format DataFrame
results = pd.DataFrame({
    "Input Size (n)": input_sizes,
    "Recursive Time (s)": recursive_times,
    "Iterative Time (s)": iterative_times
})
print("\nHasil Perbandingan:")
print(results.to_markdown(index=False))

# Plot diagram garis
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, recursive_times, label="Recursive", marker="o", color="blue")
plt.plot(input_sizes, iterative_times, label="Iterative", marker="o", color="orange")
plt.title("Perbandingan Waktu Eksekusi Metode Pencarian")
plt.xlabel("Jumlah Data (n)")
plt.ylabel("Waktu Eksekusi (detik)")
plt.legend()
plt.grid(True)
plt.show()

# Input nama kecamatan untuk pencarian
kecamatan_input = input("Masukkan nama kecamatan yang ingin dicari: ")
search_kecamatan(data, kecamatan_input)
