from time import time

from os.path import abspath, dirname, join

print("welcome")
print()
# namaFileUtama = "\\..\\test\\cryptarithmetic.txt"
# namaFile = os.path.dirname(__file__) + namaFileUtama



def split(word):
    return [char for char in word]

def pemecehCryptarithmetic(NamaFile):
    f = open(NamaFile, "r")
    content = f.read()
    listContent = content.split("\n")
    f.close()

    menghitungWaktu = time()
    listString = []
    jmlhBaris = 0
    for i in listContent:
        if i:
            listString.append(i.upper())  # ASUMSIKAN HURUF BESAR SEMUA
            jmlhBaris += 1

    # listString[jmlhBaris-3] = listString[jmlhBaris-3][:-1]
    listString[jmlhBaris - 3] = listString[jmlhBaris - 3].replace("+", "")  # Menghilangkan character '+'
    listString.pop(jmlhBaris - 2)  # Menghapus "-----"

    listHuruf = []
    contentLagi = []
    for i in range(jmlhBaris - 1):
        # listString[i].split()
        listString[i] = split(listString[i])
        listHuruf += listString[i]
        contentLagi.append(listString[i])

    listHuruf = list(set(listHuruf)) # MENGHILANGKAN DUPLIKASI
    tipeAngka = list(range(10))  # Angka yang bisa digunakan adalah 0 - 9
    coba = 0  # Menghitung jumlah percobaan

    for percobaan in solusiPermutasi(tipeAngka):
        kamusKata = dict(zip(listHuruf, percobaan[::-1]))  # {char:tipeAngka}

        nol = 0
        for i in range(len(contentLagi)):
            if (kamusKata[contentLagi[i][0]] == 0):
                nol += 1
        if nol != 0:
            continue

        else:
            hasil = 0
            jawaban = []

            for i in range(len(contentLagi) - 1):
                hasil += nilaiKata(contentLagi[i], kamusKata)
                jawaban.append(nilaiKata(contentLagi[i], kamusKata))

            if (hasil == nilaiKata(contentLagi[-1], kamusKata)):
                jawaban.append(nilaiKata(contentLagi[-1], kamusKata))
                end = time()
                print(content)
                print()
                n = len(jawaban)

                for i in range(n - 2):
                    print(jawaban[i])
                    print(f"{jawaban[n - 2]}")
                    print("------")
                    print(jawaban[n - 1])

                print()
                print("Jumlah percobaan :", coba)
                print("Waktu yang dibutuhkan :", end - menghitungWaktu, "detik")
                break
        coba += 1

# catatan ide: bruteforce: mencari cara untuk memnjumlahkan string dan
# mencocokkannya dari semua kemungkinan solusiPermutasi jmlh huruf yang ada
# kemungkinan terburuk = (10!)

# Menghitung nilai kata
def nilaiKata(word, dict):
    total = 0
    k = 1
    dibalik = word[::-1]
    for x in range(len(dibalik)):
        total += dict[dibalik[x]] * k
        k *= 10
    return total


def solusiPermutasi(array):
    if len(array) == 0:
        return []
    if len(array) == 1:
        return [array]
    temp = []
    for i in range(len(array)):
        m = array[i]
        remarr = array[:i] + array[i + 1:]
        for p in solusiPermutasi(remarr):
            temp.append([m] + p)
    return temp

print("Cryptarithmetic solver by JUAN LOUIS 13519075")
while(True):
    directory = dirname(dirname(abspath(__file__)))
    namafile = input("nama file: ")
    namaFile = join(directory, 'test\\' + namafile)
    print("silahkan tunggu...")
    print()
    pemecehCryptarithmetic(namaFile)
    print()
    call = input("apakah ingin melakukan percobaan lagi? y/n >> ").lower()
    if (call == "no" or call == "n"):
        break
