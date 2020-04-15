print('Tugas Modul 4 BAB V')
print('Kelompok 48')
print('Zulfa Fatah Akbar Ahmad/21120119130038 \nM. Richie Assariy/21120116130082')

KODE_MORSE_DICT = {' ':'/', 'A':'.-', 'B':'-...', 'C':'-.-.', 
                   'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 
                   'H':'....','I':'..', 'J':'.---', 'K':'-.-', 
                   'L':'.-..', 'M':'--', 'N':'-.','O':'---', 
                   'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 
                   'T':'-','U':'..-', 'V':'...-', 'W':'.--', 
                   'X':'-..-', 'Y':'-.--', 'Z':'--..',
                   '1':'.----', '2':'..---', '3':'...--', 
                   '4':'....-', '5':'.....', '6':'-....', 
                   '7':'--...', '8':'---..', 
                   '9':'----.','0':'-----', ', ':'--..--', 
                   '.':'.-.-.-','?':'..--..', '/':'-..-.', 
                   '-':'-....-', '(':'-.--.', ')':'-.--.-'}

def Morse_ke_Teks():
    teks = input('Masukkan kode morse: ')
    kode = [k for i in teks.split() for k,v in KODE_MORSE_DICT.items() if i==v]
    teksbaru = ''.join(kode)
    print('Pesan : '+ teksbaru)

print('''\n1 - Konversi Morse ke Teks\n2 - Quit\n ''')

while True:
    try:
        pilihan = int(input('Pilih: '))
        if pilihan == 1:
            print(Morse_ke_Teks())
            break
        elif pilihan == 2:
            print('Exiting')
            break
        else:
            print('Pilihan salah, masukkan lagi')
    except:
        print('Pilihan salah, masukkan lagi')
