import time
import random
import sys

# buat jaga jaga kalo datanya udah sampe 10k biar gak error pas pemanggilan rekursifnya makanya limitnya ditambahin
sys.setrecursionlimit(20000)

# ini fungsi buat linear search yang pake cara iteratif atau muter satu satu buat nyari barang di gudang | cara ini gak butuh data urut tapi bakal kerasa lambat banget kalo barang yang dicari ada di posisi paling ujung
# logikanya itu ngecek tiap index dari awal sampe ketemu makanya di matkul aka ini masuknya ke kelas efisiensi theta n | apet theta n karena operasinya dihitung pake sum i=1 sampe n (slide matkul aka)
# fungsi linear search - referensi materi minggu 9-10 tentang notasi sigma
def linear_search_iterative(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i  # kalo ketemu langsung stop di indexnya
    return -1  # balikin min satu kalo ternyata barangnya gak ada

# kalo yang ini buat nyari barang pake binary search tapi sistemnya rekursif manggil fungsinya sendiri | kinerjanya pake prinsip bagi dua atau divide and conquer jadinya jauh lebih cepet dibanding cara ngecek satu satu
# fungsi binary search - referensi minggu 9-10 (relasi rekurensi) & minggu 11-14 (peubah variabel)
# dapet theta log n setelah diselesaikan pake cara n = 2^k (slide matkul aka)
def binary_search_recursive(data, target, low, high):
    if low > high:
        return -1 # kondisi berenti kalo emang gak ketemu
    
    mid = (low + high) // 2
    if data[mid] == target:
        return mid # kondisi berenti kalo titik tengahnya pas di target
    elif data[mid] > target:
        return binary_search_recursive(data, target, low, mid - 1) # cari ke sebelah kiri
    else:
        return binary_search_recursive(data, target, mid + 1, high) # cari ke sebelah kanan

# fungsi ini buat jalanin tes atau eksperimen biar kita tau berapa detik waktu yang dibutuhin buat tiap algoritma
# n itu jumlah barangnya dari cuma satu sampe sepuluh rebu data buat diliat efek kenaikan running timenya
# datanya otomatis dibikin urut soalnya syarat buat jalanin binary search emang datanya kudu urut dulu
def run_experiment():
    input_sizes = [1, 10, 100, 500, 1000, 5000, 10000]
    
    print(f"{'n':<10} | {'linear (iteratif) [s]':<25} | {'binary (rekursif) [s]':<25}")
    print("-" * 65)

    for n in input_sizes:
        data_stok = list(range(1, n + 1))
        target = n # kita set targetnya di paling akhir biar dapet skenario terburuk atau worst case nya

        # nyatet waktu buat linear search pake perf counter biar hasilnya presisi banget sampe angka di belakang koma
        start_time = time.perf_counter()
        linear_search_iterative(data_stok, target)
        end_time = time.perf_counter()
        time_linear = end_time - start_time

        # nyatet waktu buat binary search
        start_time = time.perf_counter()
        binary_search_recursive(data_stok, target, 0, len(data_stok) - 1)
        end_time = time.perf_counter()
        time_binary = end_time - start_time

        print(f"{n:<10} | {time_linear:<25.10f} | {time_binary:<25.10f}")

if __name__ == "__main__":
    print("--- eksperimen analisis kompleksitas algoritma ---")
    print("studi kasus: pencarian stok barang inventaris gudang\n")
    run_experiment()