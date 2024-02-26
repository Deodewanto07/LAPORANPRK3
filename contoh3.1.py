 # Program input salah pada contoh 3.1
suhu = input("Masukan suhu tubuh anda")

try :
    suhu = int(suhu)
    if suhu >= 39:
        print("Kamu demam")
    else :
        print("Kamu tidak demam")

except :
    print("inputan kamu salah mohon masukan yang benar")
