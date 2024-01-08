# Definisikan fungsi vigenere_cipher dengan tiga parameter: text, key, dan mode.
def vigenere_cipher(text, key, mode):
    # Inisialisasi variabel result sebagai string kosong untuk menampung hasil enkripsi/dekripsi.
    result = ""
    
    # Konversi teks dan kunci menjadi huruf kapital agar kompatibel dengan alfabet.
    text = text.upper()
    key = key.upper()
    
    # Hitung panjang kunci.
    key_len = len(key)

    # Loop melalui setiap karakter dalam teks masukan.
    for i in range(len(text)):
        # Periksa apakah karakter saat ini adalah huruf alfabet.
        if text[i].isalpha():
            # Konversi karakter teks dan kunci menjadi bilangan bulat antara 0-25 (indeks alfabet).
            text_char = ord(text[i]) - ord('A')
            key_char = ord(key[i % key_len]) - ord('A')

            # Cek mode (enkripsi atau dekripsi) dan lakukan operasi yang sesuai.
            if mode == 'encrypt':
                encrypted_char = (text_char + key_char) % 26  # Enkripsi dengan modulus 26.
            elif mode == 'decrypt':
                encrypted_char = (text_char - key_char) % 26  # Dekripsi dengan modulus 26

            # Konversi karakter terenkripsi kembali menjadi huruf alfabet dan tambahkan ke hasil.
            result += chr(encrypted_char + ord('A'))
        else:
            # Jika karakter bukan huruf alfabet, tambahkan langsung ke hasil tanpa perubahan.
            result += text[i]

    # Mengembalikan teks hasil enkripsi/dekripsi.
    return result

# Meminta pengguna untuk memasukkan kalimat yang ingin dienkripsi/dekripsi.
plaintext = input("Masukkan kalimat : ")
key = input("Masukkan kunci : ")
mode = input("Pilih mode (encrypt/decrypt) : ")

# Memeriksa mode yang dimasukkan oleh pengguna dan mencetak hasilnya.
if mode == 'encrypt':
    ciphertext = vigenere_cipher(plaintext, key, 'encrypt')
    print("Hasil enkripsi :", ciphertext)
elif mode == 'decrypt':
    decrypted_text = vigenere_cipher(plaintext, key, 'decrypt')
    print("Hasil dekripsi : ", decrypted_text)
else:
    print("Mode yang dimasukkan tidak valid. Pilih 'encrypt' atau 'decrypt'.")
