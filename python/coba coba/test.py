def lanjutkan_rumus():
    print("Masukkan nilai a dan b:")
    a = int(input("a: "))
    b = int(input("b: "))
    
    print("\nProses:")
    print(f"a = {a}, b = {b}")
    
    while a > 0 and b > 0:
        n = a // b
        c = a - b * n
        print(f"{a} = {b} * {n} + {c}")
        
        a = b
        b = c
    
    print("\nHasil Akhir:")
    if b == 0:
        print(f"0 = {a} * 0 + 0")
    else:
        print(f"0 = {b} * 0 + 0")

# Jalankan fungsi
lanjutkan_rumus()